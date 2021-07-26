<p align="center">
  <img src="https://user-images.githubusercontent.com/78009407/126273326-662b5aff-034f-4f48-a62a-69552195ff86.png" />
</p>

[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

## Purpose
This repository details how to extract data and metadata from a NWB file with either Matlab or Python APIs.

## Extract NWB file data with Matlab-based API
`EXTRACT_NWB.m` is a function that:
1. Loads the selected NWB file into Matlab
2. Extracts relevant data and metadata from NWB file 
3. Outputs a table with selected metadata values

### Requirements
Add `matnwb` interface library to your path before using this function.
`matnwb` is a Matlab interface for reading and writing Neurodata Without Borders (NWB) 2.0 files. Follow the instructions found [here](https://neurodatawithoutborders.github.io/matnwb/#setup) for instructions on downloading and using the library.

### Usage
`EXTRACT_NWB.m` currently functions to extract optophysiological data and metadata from a file found in [this dataset](https://sparc.science/datasets/124?type=dataset&path=files%2Fprimary%2Fcompression%2Fsub-20180809_G5%2Fsam-20180809_G5).
* The function code can be altered to meet the needs of a different dataset or to extract more data/metdata than it currently provides.
* The command line code `util.nwbTree(nw);` creates a pop-up UI that allows the user to navigate through the contents and storage structure of the NWB file, here named `nw`. 
![image](https://user-images.githubusercontent.com/78009407/126884868-454d97df-3303-453c-9076-75ae9207b019.png)

The `NWB Tree` UI shows the user where to find certain data and metadata. 

* For example here, to find data on the location of the electrodes, the user would first navigate to `general_extracellular_ephys_electrodes`, then to `vectordata`. 
* As written within the function, the code to navigate to this data is `vectorData=nw.general_extracellular_ephys_electrodes.('vectordata');`. 
* If the user wishes to navigate to and extract (meta)data from a different container other than `general_extracellular_ephys_electrodes`, they would simply change the code to navigate to the container with the (meta)data of their choosing. 
* For instance, if the user wanted to extract data from `general_experimenter`, they would index into this container like so: `generalExp=nw.general_experimenter.('general_experimenter');`. The user would now have a Workspace variable containing this information.

More information pertaining to how to extract data from a NWB file in Matlab can be found [here](https://neurodatawithoutborders.github.io/matnwb/tutorials/html/basicUsage.html).

## Extract NWB file data with Python-based API 
1. The dependencies required to run the python script are in [`requirments.txt`](https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/blob/main/sparc_to_nwb/requirements.txt) in [sparc_to_nwb](https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/tree/main/sparc_to_nwb). They will need to be installed prior to continuing.
```shell
python3 -m pip install requirements.txt
```
2. Download the [`extract_nwb.py`](https://github.com/lifestrugglee/sparc2nwb/blob/main/extract_from_nwb/extract_nwb.py) to your local folder.
3. Utilize the script like the followings:
```shell
import extract_nwb

fpath = r'SPARC\nwb_files\compression_ISP_20180813_G5.nwb'
nwb_data = extract_nwb.EXTRACT_NWB(fpath)
```
3. Once the data is loaded, the data can easily be grabbed by using its functions
```shell
# EXAMPLE
nwb_data.get_subject() # get experiment subject information
nwb_data.get_electrodes() # get electrode data
```

### Module containing the description
The figure below indicates the structure design of the module. The lists in green circle are the contents based on the [dataset](https://sparc.science/datasets/124?type=dataset&path=files). The lists in the right, bottom pink area are common containers within the NWB format, references from this [manuscript](https://www.nature.com/articles/s41597-020-0415-9#Fig2). Additionally, `NWB_SOURCE` provides the access to the original NWB format of the data.

<p align="center">
  <img src="https://github.com/lifestrugglee/sparc2nwb/blob/main/extract_from_nwb/source_vs_nwb.png" />
</p>


## SPARC2NWB Team
[Marielle Darwin](https://github.com/mldarwin) | [Ananth Reddy](https://github.com/anbhimi) | [Derek Chang](https://github.com/DerekYJC) | [Patrick Chuang](https://github.com/lifestrugglee)

[contributors-shield]: https://img.shields.io/github/contributors/SPARC-FAIR-Codeathon/sparc2nwb.svg?style=flat-square
[contributors-url]: https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/SPARC-FAIR-Codeathon/sparc2nwb.svg?style=flat-square
[stars-url]: https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/stargazers
[issues-shield]: https://img.shields.io/github/issues/SPARC-FAIR-Codeathon/sparc2nwb.svg?style=flat-square
[issues-url]: https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/issues
[license-shield]: https://img.shields.io/github/license/SPARC-FAIR-Codeathon/sparc2nwb.svg?style=flat-square
[license-url]: https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/blob/main/LICENSE
