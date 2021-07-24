import os
from time import time
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import logging
import pickle
import pynwb
from dateutil.tz import tzlocal
from pynwb.device import Device
from pynwb.ecephys import ElectrodeGroup
from pynwb import NWBFile, TimeSeries, NWBHDF5IO

# def get_timeseries(n, start_time, frequency):
#     start_time = datetime.strptime(start_time[:-1], '%Y-%m-%dT%H:%M:%S.%f')
#     delta_time = 1/1250
#     added_seconds = timedelta(0, delta_time)
#     time_series = []
#     while(n):
#         n = n-1
#         start_time = start_time+added_seconds
#         time_series.append(str(start_time))

#     return (time_series)


def convert_to_nwb(data, nwb_file):

    electrode_groups = list()
    for i in range(len(data)):
        probe_device = Device(name=str(i+1))
        probe_electrode_group = ElectrodeGroup(
            name = 'Probe'+str(i+1),
            description = '',
            device = probe_device,
            location = ''
        )
        nwb_file.add_device(probe_device)
        electrode_groups.append(probe_electrode_group)
        nwb_file.add_electrode_group(probe_electrode_group)
        
    del_cols = []
    for col in data.columns:
        if ('frame' not in col) and ('neuron' not in col):
            del_cols.append(col)
    data = data.drop(del_cols, axis=1)
        
    locations_array = ['']*len(data)
    locations = np.array(locations_array)
    groups_array = [electrode_groups[i] for i in range(len(data))]
    groups = np.asarray(groups_array)
        
    for i in range(len(groups)):
        nwb_file.add_electrode(
                id=i,
                x=float('NaN'),
                y=float('NaN'),
                z=float('NaN'),
                imp=float('NaN'),
                location=str(locations[i]),
                group=groups[i],
                filtering='none'
        )

    for i, col in enumerate(data.columns):
        if col != 'frame':
            data_name = col+'_data'

            data_array = np.array(data[col].values)

            nwb_file.add_electrode_column(
                name = data_name,
                description = '1.25 kHz',
                data = data_array
            )
                
    return (nwb_file)

def main(standard_path, manifest_data, logger):

    for d in manifest_data['filename']:
        file_path = standard_path+d
        samples_path = '/'.join(standard_path.split('/')[0:-2])+'/samples.xlsx'
        subjects_path = '/'.join(standard_path.split('/')[0:-2])+'/subjects.xlsx'

        data = pd.read_excel(file_path, sheet_name='responses')
        start_timestamp = manifest_data[manifest_data['filename'] == d]['timestamp'].values[0]
        # time_series = get_timeseries(n=len(data), start_time=start_timestamp, frequency = 1250)

        file_name = file_path.split('/')[5] +'_'+ file_path.split('/')[-1].split('.')[0]
        if not os.path.exists('./nwb_files/'+standard_path.split('/')[-2]+'/'):
            os.makedirs('./nwb_files/'+standard_path.split('/')[-2]+'/')
        filename = './nwb_files/'+standard_path.split('/')[-2]+'/'+file_name+'.nwb'
        
        subject_id = d.split('/')[1]
        session_start_time = manifest_data[manifest_data['filename'] == d]['timestamp'].values[0]
        session_timestamp = datetime.strptime(session_start_time[:-1], '%Y-%m-%dT%H:%M:%S.%f')
        samples_data = pd.read_excel(samples_path)
        subjects_data = pd.read_excel(subjects_path)

        subject = pynwb.file.Subject(
            age = samples_data[samples_data['subject_id'] == subject_id]['age'].values[0],
            genotype = str(samples_data[samples_data['subject_id'] == subject_id]['specimen type'].values[0])+' '+str(samples_data[samples_data['subject_id'] == subject_id]['specimen anatomical location'].values[0]),
            subject_id = subject_id,
            sex = samples_data[samples_data['subject_id'] == subject_id]['sex'].values[0],
            weight = str(subjects_data[subjects_data['subject_id'] == subject_id]['Weight_kg'].values[0])+' kgs',
            species = samples_data[samples_data['subject_id'] == subject_id]['species'].values[0],
            description = samples_data[samples_data['subject_id'] == subject_id]['protocol title'].values[0]
        )
        
        nwb_file = NWBFile(session_description = 'Sample NWB File',
                        identifier = file_name,
                        session_start_time = session_timestamp,
                        file_create_date = datetime.now(tzlocal()),
                        institution = '',
                        lab = '',
                        subject = subject,
                        experimenter = 'Gemma Mazzuoli-Weber',
                        experiment_description = 'In this study, we investigated the sensitivity of enteric neurons to mechanical '
                                                    'stimuli comparing tissue samples from porcine proximal and distal colon.',
                        related_publications = 'https://doi.org/10.26275/0khe-2os4',
                        keywords = ['mechanosensitivity', 'voltage sensitive dye', 
                                    'ultrafast neuroimaging technique', 'immunohistochemistry', 
                                    'enteric nervous system ']
                        )
        # nwb_ts = TimeSeries(name='nwb_testseries', timestamps=time_series)
        # nwb_file.add_acquisition(nwb_ts)

        nwb_file = convert_to_nwb(data, nwb_file)
        
        io = NWBHDF5IO(filename, 'w')
        io.write(nwb_file)
        io.close()

        logger.info('Saved'+str(filename))

if __name__ == '__main__':
    log_format = '%(levelname)s %(asctime)s - %(message)s'
    logging.basicConfig(filename='conversion.logs',
                        level=logging.INFO,
                        format=log_format,
                        filemode='w')
    logger = logging.getLogger()

    standard_path = './Pennsieve-dataset-124-version-2/files/primary/'
    manifest_data = pd.read_excel(standard_path+'manifest.xlsx')

    # If there is no nwb_folders filder, then create it.    
    if not os.path.exists('./nwb_files/'):
        os.makedirs('./nwb_files/')
        
    main(standard_path, manifest_data, logger)    