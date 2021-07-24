import os
import itertools
import tkinter as tk
import numpy   as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import logging
import pickle
import pynwb
import sys
from tkinter import *  
from PIL import ImageTk,Image
from tkinter.ttk import Combobox, Progressbar
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
from tkinter import scrolledtext
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from skimage import io
from datetime import datetime, timedelta
from dateutil.tz import tzlocal
from pynwb.device import Device
from pynwb.ecephys import ElectrodeGroup
from pynwb import NWBFile, TimeSeries, NWBHDF5IO

import time

# Define the function for data conversion
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

def main_(standard_path, manifest_data, logger):
    
    experimenter = experimenter_ent.get()
    experiment_description = experimenter_desc_ent.get()
    related_publications = publication_ent.get()
    keywords = keywords_ent.get().split(',')
    
    n_files = len(manifest_data['filename'])
    prog = np.linspace(0, 100, n_files+1, dtype=int)
    progress['value'] = prog[0]
    
    for it, d in enumerate(manifest_data['filename']):
        file_path = standard_path+d
        samples_path = '/'.join(standard_path.split('/')[0:-2])+'/samples.xlsx'
        subjects_path = '/'.join(standard_path.split('/')[0:-2])+'/subjects.xlsx'    
        
        data = pd.read_excel(file_path, sheet_name='responses')
        start_timestamp = manifest_data[manifest_data['filename'] == d]['timestamp'].values[0]
        # time_series = get_timeseries(n=len(data), start_time=start_timestamp, frequency = 1250)
             
        file_name = file_path.split('/')[-4] +'_'+ file_path.split('/')[-1].split('.')[0]
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
                        experimenter = experimenter,
                        experiment_description = experiment_description,
                        related_publications = related_publications,
                        keywords = keywords
                        )

        nwb_file = convert_to_nwb(data, nwb_file)
        
        io = NWBHDF5IO(filename, 'w')
        io.write(nwb_file)
        io.close()

        logger.info('Saved '+str(filename))
        # pickle.dump(nwb_file, open(filename, 'wb'))
        
        logger_text.insert(tk.INSERT, 'Saved '+str(filename)+'\n')
        
        progress['value'] = prog[it+1]
        prog_frame.update_idletasks()
        
        title_ = "sparc2nwb (" + str(it+1) + "/" + str(n_files) + ") converted!"
        window.title(title_)
        
        
# Define the function for the command
def get_path():
    global folder_selected
    folder_selected = askdirectory()
    txt_standardPath.insert(tk.END, folder_selected)

    
# Have a simple application
window = tk.Tk()
window.title("sparc2nwb")
window.geometry('1050x500')

# Create the main containers (Frame)
main_frame = tk.Frame(window, width=800, height=450, pady=20, padx=30)
side_frame = tk.Frame(window, width=200, height=450, pady=20)
prog_frame = tk.Frame(window, width=1000, height=50, pady=10)

experimenter_ent = tk.StringVar()
experimenter_desc_ent = tk.StringVar()
publication_ent = tk.StringVar()
keywords_ent = tk.StringVar()

def convert():        
    log_format = '%(levelname)s %(asctime)s - %(message)s'
    logging.basicConfig(filename='conversion.logs',
                        level=logging.INFO,
                        format=log_format,
                        filemode='w')
    logger = logging.getLogger()

    #standard_path = './Pennsieve-dataset-124-version-2/files/primary/'
    standard_path = folder_selected + '/'
    manifest_data = pd.read_excel(standard_path+'manifest.xlsx')

    # If there is no nwb_folders filder, then create it.    
    if not os.path.exists('./nwb_files/'):
        os.makedirs('./nwb_files/')
        
    main_(standard_path, manifest_data, logger)

xscrollbar = Scrollbar(main_frame, orient=HORIZONTAL)
xscrollbar.grid(row=5, columnspan=2, sticky="e", padx=5, ipadx=188)
xscrollbar_2 = Scrollbar(main_frame, orient=HORIZONTAL)
xscrollbar_2.grid(row=8, columnspan=2, sticky="e", padx=5, ipadx=188)

# Left frame
label_standardPath = tk.Label(main_frame, text="Standard Path", fg="black", font=('Arial', 10))
txt_standardPath = tk.Text(main_frame, width=70, height=1, font=('Arial', 10))
empt1 = tk.Label(main_frame, text=" ", fg="black", height=1)
btn_standardPath = tk.Button(main_frame, text="Browse", bg="gold", fg="black", font=('Arial', 10), command=get_path)
empt3 = tk.Label(main_frame, text=" ", fg="black", height=2)
label_datasetDesc = tk.Label(main_frame, text="Dataset description", fg="black", font=('Arial', 12, 'bold'))
label_experimeter = tk.Label(main_frame, text="Experimenter", fg="black", font=('Arial', 10))
experimenter_entry = tk.Entry(main_frame, textvariable=experimenter_ent, font=('Arial',10,'italic'), width=60)
label_experimeter_desc = tk.Label(main_frame, text="Experiment description", fg="black", font=('Arial', 10))
experimenter_desc_entry = tk.Entry(main_frame, textvariable=experimenter_desc_ent, font=('Arial',10,'italic'), width=60,
                                   xscrollcommand=xscrollbar.set)
label_publication = tk.Label(main_frame, text="Related publication", fg="black", font=('Arial', 10))
publication_entry = tk.Entry(main_frame, textvariable=publication_ent, font=('Arial',10,'italic'), width=60)
label_keywords = tk.Label(main_frame, text="Keywords (comma separated)", fg="black", font=('Arial', 10))
keywords_entry = tk.Entry(main_frame, textvariable=keywords_ent, font=('Arial',10,'italic'), width=60,
                                   xscrollcommand=xscrollbar_2.set)
label_keywords = tk.Label(main_frame, text="Keywords (comma separated)", fg="black", font=('Arial', 10))
keywords_entry = tk.Entry(main_frame, textvariable=keywords_ent, font=('Arial',10,'italic'), width=60,
                                   xscrollcommand=xscrollbar_2.set)
label_logger = tk.Label(main_frame, text="Logging information", fg="grey", font=('Arial', 10))
logger_text = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, font=('Arial',10,'italic'), width=57,
                                   height=7)

label_standardPath.grid(row=0, column=0, sticky="ns", padx=2)
txt_standardPath.grid(row=0, column=1, sticky="ns", padx=2)
empt1.grid(row=0, column=2, sticky="ns", padx=2)
btn_standardPath.grid(row=0, column=3, sticky="ns", padx=2)
empt3.grid(row=1, columnspan=3, sticky="ns", padx=2)
label_datasetDesc.grid(row=2, columnspan=2, sticky="w")
label_experimeter.grid(row=3, column=0, sticky="ew", padx=2, pady=5)
experimenter_entry.grid(row=3, columnspan=2, sticky="e", padx=5, pady=5)
label_experimeter_desc.grid(row=4, column=0, sticky="ew", padx=2, pady=5)
experimenter_desc_entry.grid(row=4, columnspan=2, sticky="e", padx=5, pady=5, ipady=5)

xscrollbar.config(command=experimenter_desc_entry.xview)

label_publication.grid(row=6, column=0, sticky="ew", padx=2, pady=5)
publication_entry.grid(row=6, columnspan=2, sticky="e", padx=5, pady=5)
label_keywords.grid(row=7, column=0, sticky="ew", padx=2, pady=5)
keywords_entry.grid(row=7, columnspan=2, sticky="e", padx=5, pady=5, ipady=5)

xscrollbar_2.config(command=keywords_entry.xview)

label_logger.grid(row=9, column=0, sticky="ew", padx=2, pady=5)
logger_text.grid(row=9, columnspan=2, sticky="e", padx=5, pady=5)

# Right frame
image = Image.open("image.jpg")
image = image.resize((200, 200), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)
panel = tk.Label(side_frame, image=image)
empt2 = tk.Label(side_frame, text=" ", fg="black", height=10)
btn_convert = tk.Button(side_frame, text="  Convert  ", bg="lightgreen", fg="black", font=('Arial', 12), command=convert)

panel.grid(row=0, column=0)
empt2.grid(row=1, column=0)
btn_convert.grid(row=2, column=0)

# Bottom frame
label_progress = tk.Label(prog_frame, text="Conversion progress", fg="black", font=('Arial', 10))
progress = Progressbar(prog_frame, orient=tk.HORIZONTAL, length=770, mode='determinate')

label_progress.grid(row=0, column=0, sticky="ew", padx=50)
progress.grid(row=0, column=1, sticky="ew")

# Organization for frames
main_frame.grid(row=0, column=0, sticky="ns")
side_frame.grid(row=0, column=1, sticky="ns")
prog_frame.grid(row=1, columnspan = 2, sticky="ew")

tk.mainloop()
