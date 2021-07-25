<p align="center">
  <img src="https://user-images.githubusercontent.com/78009407/126273326-662b5aff-034f-4f48-a62a-69552195ff86.png" />
</p>

[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

## Purpose
This repository holds the code and the supporting files to convert SPARC data into NWB format using a **GUI**. The GUI runs *sparc2nwb_gui.py*. Instructions are provided below to run the code and convert datasets from sparc to NWB format.

![image](https://github.com/DerekYJC/sparc2nwb/blob/0f81b210adfc5008ed74f74dd162aa2bde1b5d8d/gui/images/image.png)

## Prerequisite
1. Python
2. [PyNWB](https://pynwb.readthedocs.io/en/stable/) package
3. [tkinter](https://docs.python.org/3/library/tkinter.html) package

## Getting started
Before starting, install the required python dependencies mentioned [here](https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/tree/main/sparc_to_nwb#usage), as well as the **tkinter** package.

## Open the GUI
Open *sparc2nwb_gui.py* and run the script. The GUI will appear.

## Select the folders of the dataset
Click ```Browse``` button and select the folder. When the folder is selected, the folder path should show up in the *Standard Path* textbox.

## Provide the dataset description
Type the dataset description in the corresponding entry box. Note that you can provide more than one keyword separated commas.

## Covert the data into NWB format
Click ```Convert``` button to start the conversion. The *Logging information* will display where the converted files are saved.

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
