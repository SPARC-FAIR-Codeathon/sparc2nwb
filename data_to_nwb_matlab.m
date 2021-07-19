clc
clear
%% Configure the path and run the python script
pe = pyenv; 
python_path = pe.Executable;
path = [pwd, '\'];
script = 'data_to_nwb.py';

% Run the script
[status, result] = system(strcat(python_path, {' '}, script));

