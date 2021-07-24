import os
import pandas as pd
from pynwb import NWBHDF5IO

class EXTRACT_NWB():
    def __init__(self, file_path):
        
        nwbfile = NWBHDF5IO(file_path, 'r').read()
        self.__nwbfile = nwbfile
        
        data_dict = {}
#         data_dict['id'] = list(self.__nwbfile.electrodes.id)
        for col in nwbfile.electrodes.colnames:
            exec(f'data_dict["{col}"] = list(nwbfile.electrodes.{col}.data)')
        #     print(nwbfile.electrodes.(col))
        self.__data_df = pd.DataFrame.from_dict(data_dict)
        
        defaultColLs = ['acquisition','general_device','subject','intervals','stimulus','units']
        dataColLs = ['electrodes_description', 'electrodes', 'file_date', 'experiment_description', 'identifier']
        tmpAll = dataColLs + defaultColLs
        
        nwbColls = list(nwbfile.fields.keys())
#         nwbColls

    def get_nwb_source(self):
        return self.__nwbfile
    
    # Based on the paper
    def get_acquisition(self):
        return self.__nwbfile.acquisition
        
    def get_general_device(self):
        return self.__nwbfile.general
        
    def get_intervals(self):
        return self.__nwbfile.intervals
        
    def get_stimulus(self):
        return self.__nwbfile.stimulus
        
    def get_units(self):
        return self.__nwbfile.units
    
    # ------------ for this dataset
    def get_electrodes_description(self):
        return self.__nwbfile.electrodes.description
    
    def get_electrodes(self):
        return self.__data_df
    
    def get_experiment_description(self):
        return self.__nwbfile.experiment_description
    
    def get_identifier(self):
        return self.__nwbfile.identifier
    
    def get_subject(self):
        return dict(self.__nwbfile.fields['subject'].fields)   
    
    def get_session_description(self):
    	return self.__nwbfile.session_description
    
    def get_session_start_time(self):
        return self.__nwbfile.session_start_time
    
    def get_timestamps_reference_time(self):
        return self.__nwbfile.timestamps_reference_time
    
    def get_file_create_date(self):
        return self.__nwbfile.file_create_date[0]
    
    def get_keywords(self):
        return self.__nwbfile.keywords
    
    def get_epoch_tags(self):
        return self.__nwbfile.epoch_tags
    
    def get_lab(self):
        return self.__nwbfile.lab
    
    def get_institution(self):
        return self.__nwbfile.institution
    
    def get_experimenter(self):
        return self.__nwbfile.experimenter
    
    def get_related_publications(self):
        return self.__nwbfile.related_publications

# testNWB = EXTRACT_NWB(fpath)
# print('done')
