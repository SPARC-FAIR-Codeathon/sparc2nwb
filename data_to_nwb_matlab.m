clc
clear
%% Configure the path and run the python script
pe = pyenv; 
python_path = pe.Executable;
path = [pwd, '\'];
script = 'sparc2nwb_test.py';

% Run the script
[status, result] = system(strcat(python_path, {' '}, script));

