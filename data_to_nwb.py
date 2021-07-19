import os
import pandas as pd
import numpy as np
import datetime import datetime
import pynwb
import logging
import pickle
from pynwb.device import Device
from pynwb.ecephys import ElectrodeGroup
from pynwb import NWBFile, NWBHDF5IO

def convert_to_nwb(data, nwb_file):
    
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

def main():
    
    curr_dir = os.getcwd()
    manifest_filepath = curr_dir+'files/primary/manifest.xlsx'
    manifest_data = pd.read_excel(manifest_filepath)
    for d in manifest_data['filename']:
        nwb_file = NWBFile(session_description = 'NWB File Format - In Vitro Imaging of Mechanosensitive Submucous Neurons in the Porcine Colon.', 
                   identifier = 'nwbfile_1',
                   session_start_time = datetime.now())

        standard_path = ''
        file_path = standard_path+d
        data = pd.read_excel(file_path, sheet_name='responses')
        nwb_file = convert_to_nwb(data, nwb_file)
        filename = file_path.split('/')[4] +'_'+ file_path.split('/')[-1].split('.')[0]
        nwb_filename = ''+filename+'.nwb'

        pickle.dump(nwb_file, open(filename, 'wb'))

if __name__ == '__main__':
    log_format = '%(levelname)s %(asctime)s - %(message)s'
    logging.basicConfig(filename='',
                        level=logging.INFO,
                        format=log_format,
                        filemode='w')
    logger = logging.getLogger()
    main()
    