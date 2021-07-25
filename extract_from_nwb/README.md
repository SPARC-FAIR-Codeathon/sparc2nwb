<p align="center">
  <img src="https://user-images.githubusercontent.com/78009407/126273326-662b5aff-034f-4f48-a62a-69552195ff86.png" />
</p>

[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

## Purpose
This repository details how to extract data and metadata from a NWB file with either Matlab or Python.

## Extract NWB file data in Matlab using `EXTRACT_NWB.m` function
`EXTRACT_NWB.m` is a function that:
1. Loads the selected NWB file into Matlab
2. Extracts relevant data and metadata from NWB file as Matlab Workspace variables
3. Outputs a table with selected metadata values

### Add `matnwb` interface library to your path before using this function.
#### `matnwb` is a Matlab interface for reading and writing Neurodata Without Borders (NWB) 2.0 files. Follow the instructions found [here](https://neurodatawithoutborders.github.io/matnwb/#setup) for instructions on downloading and using the library.

### Usage
`EXTRACT_NWB.m` currently functions to extract optophysiological data and metadata from a file found in [this dataset](https://sparc.science/datasets/124?type=dataset&path=files%2Fprimary%2Fcompression%2Fsub-20180809_G5%2Fsam-20180809_G5).
* The function code can be altered to meet the needs of a different dataset or to extract more data/metdata than it currently provides.
* The command line code `util.nwbTree(nw);` creates a pop-up UI that allows the user to navigate through the contents and storage structure of the NWB file, here named `nw`. 
![image](https://user-images.githubusercontent.com/78009407/126884868-454d97df-3303-453c-9076-75ae9207b019.png)

The `NWB Tree` UI shows the user where to find certain data and metadata. For example here, to find data on the location of the electrodes, the user would first navigate to `general_extracellular_ephys_electrodes`, then to `vectordata`. In the function `EXTRACT_NWB.m`, the code to navigate to this data is `vectorData=nw.general_extracellular_ephys_electrodes.('vectordata');`. If the user wishes to navigate to a different container other than `general_extracellular_ephys_electrodes`, they would simply change the code within the function to navigate to the container of their choosing. More information pertaining to how to extract data from a NWB file can be found [here](https://neurodatawithoutborders.github.io/matnwb/tutorials/html/basicUsage.html).


## Extract NWB file data in Python 



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
