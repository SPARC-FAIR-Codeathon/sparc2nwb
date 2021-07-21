%% Configure the path and run the python script
pe = pyenv; 
python_path = pe.Executable;   % Get the path of Python executable
path = [pwd, '\'];
script = 'sparc_to_nwb.py';    % Filename of Python script to make conversion

% Parameters for data conversion
standard_path = "./Pennsieve-dataset-124-version-2/files/primary/";

% Run the script
[status, result] = system(strcat(python_path, {' '}, ...
                                 script, {' '}, ...
                                 standard_path, {' '} ...
                                 ));

