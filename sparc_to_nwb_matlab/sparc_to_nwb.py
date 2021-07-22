import os
import pandas as pd
import numpy as np
from datetime import datetime
import logging
import pickle
import pynwb
import sys
from dateutil.tz import tzlocal
from pynwb.device import Device
from pynwb.ecephys import ElectrodeGroup
from pynwb import NWBFile

def convert_to_nwb(data, nwb_file, standard_path, d):

    file_path = standard_path+d
    electrode_groups = list()
    for i in range(len(data)):
        probe_device = Device(name=str(i+1))
        probe_electrode_group = ElectrodeGroup(
            name = 'probe_'+str(i+1),
            description = '',
            device = probe_device,
            location = ''
        )
        
        electrode_groups.append(probe_electrode_group)
        
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
            data_name = file_path.split('/')[4] +'_'+d.split('/')[-1].split('.')[0]+'_'+col+'_data'

            data_array = np.array(data[col].values)

            nwb_file.add_electrode_column(
                name = data_name,
                description = '1.25 kHz',
                data = data_array
            )
                
    return (nwb_file)

def main(standard_path, manifest_data):
    
    experimenter = 'Gemma Mazzuoli-Weber'
    experiment_description = 'In this study, we investigated the sensitivity of enteric neurons to mechanical stimuli comparing tissue samples from porcine proximal and distal colon.'
    related_publications = 'https://doi.org/10.26275/0khe-2os4'
    keywords = ['mechanosensitivity', 'voltage sensitive dye', 
                'ultrafast neuroimaging technique', 'immunohistochemistry', 
                'enteric nervous system ']
    
    for d in manifest_data['filename']:
        file_path = standard_path+d
        data = pd.read_excel(file_path, sheet_name='responses')
        file_name = file_path.split('/')[4] +'_'+ file_path.split('/')[-1].split('.')[0]
        filename = './nwb_files/'+file_name+'.nwb'
        
        session_start_time = manifest_data[manifest_data['filename'] == d]['timestamp'].values[0]
        session_timestamp = datetime.strptime(session_start_time[:-1], '%Y-%m-%dT%H:%M:%S.%f')
        
        nwb_file = NWBFile(session_description = 'Sample NWB File',
                        identifier = file_name,
                        session_start_time = session_timestamp,
                        file_create_date = datetime.now(tzlocal()),
                        institution = '',
                        lab = '',
                        experimenter = experimenter,
                        experiment_description = experiment_description,
                        related_publications = related_publications,
                        keywords = keywords
                        )

        nwb_file = convert_to_nwb(data, nwb_file, standard_path, d)
        pickle.dump(nwb_file, open(filename, 'wb'))

if __name__ == '__main__':
    log_format = '%(levelname)s %(asctime)s - %(message)s'
    logging.basicConfig(filename='',
                        level=logging.INFO,
                        format=log_format,
                        filemode='w')
    logger = logging.getLogger()

    standard_path = './Pennsieve-dataset-124-version-2/files/primary/'
    manifest_data = pd.read_excel(standard_path+'manifest.xlsx')

    # If there is no nwb_folders filder, then create it.    
    if not os.path.exists('./nwb_files/'):
        os.makedirs('./nwb_files/')
        
    main(standard_path, manifest_data)    