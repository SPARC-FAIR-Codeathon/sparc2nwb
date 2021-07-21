%% Configure the path and run the python script
pe = pyenv; 
python_path = pe.Executable;   % Get the path of Python executable
path = [pwd, '\'];
script = 'sparc_to_nwb.py';    % Filename of Python script to make conversion

% Run the script
[status, result] = system(strcat(python_path, {' '}, script));
