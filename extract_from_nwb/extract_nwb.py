import os
import pandas as pd
from pynwb import NWBHDF5IO
from types import MethodType

class EXTRACT_NWB():
    def __init__(self, file_path):
        
        nwbfile = NWBHDF5IO(file_path, 'r').read()
        self.__nwbfile = nwbfile
        
        data_dict = {}
        data_dict_desc = {}
        data_dict['id'] = list(nwbfile.electrodes.id.data)
        for col in nwbfile.electrodes.colnames:
            exec(f'data_dict["{col}"] = list(nwbfile.electrodes.{col}.data)')
            exec(f'data_dict_desc["{col}"] = nwbfile.electrodes.{col}.description')
        #     print(nwbfile.electrodes.(col))
        self.__data_df = pd.DataFrame.from_dict(data_dict)
        self.__data_dict_desc = data_dict_desc
        
        defaultColLs = ['acquisition', 'devices', 'intervals', 'stimulus', 'units', 'subject']
        dataColLs = ['electrodes_description', 'electrodes', 'experiment_description', 'identifier',
                'session_description', 'session_start_time', 'lab', 'institution', 'epoch_tags',
                'timestamps_reference_time','file_create_date', 'keywords', 'experimenter', 'related_publications']
        tmpAll = dataColLs + defaultColLs

        nwbColls = list(nwbfile.fields.keys())

        str_fun = '''
def get_%s(self):
    print("it is in %s!")
self.get_%s = MethodType(get_%s, self)'''

        for i in nwbColls:
            if i not in tmpAll: 
                exec(str_fun%(i, i, i, i))
        
    def get_nwb_source(self):
        return self.__nwbfile
    
    # Based on the paper
    def get_acquisition(self):
        return self.__nwbfile.acquisition
        
    def get_devices(self):
        return self.__nwbfile.devices
        
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
        return [self.__data_df, self.__data_dict_desc]
    
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
        return list(self.__nwbfile.keywords)
    
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
        
