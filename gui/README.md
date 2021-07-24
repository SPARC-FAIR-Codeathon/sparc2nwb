<p align="center">
  <img src="https://user-images.githubusercontent.com/78009407/126273326-662b5aff-034f-4f48-a62a-69552195ff86.png" />
</p>

[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Purpose
This repository holds the code and the supporting files to convert SPARC data into NWB format using **MATLAB**. The repository runs Python script, *sparc_to_nwb.py*, in MATLAB. Instructions are provided below to run the code and convert datasets from sparc to NWB format.

## Prerequisite
1. MATLAB
2. Python
3. [PyNWB](https://pynwb.readthedocs.io/en/stable/) package

## Getting started
Before starting, install the required python dependencies mentioned [here](https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/tree/main/sparc_to_nwb#usage).

In MATLAB, **configure Your System to Use Python**. Detailed instructions are provided on [MATLAB documentation](https://www.mathworks.com/help/matlab/matlab_external/install-supported-python-implementation.html).

## Define customized values in *sparc_to_nwb.py*
In *sparc_to_nwb.py*, change the values (e.g., ```standard_path```, ```experimenter```, ```experiment_descriptioni```, ```related_publications```, ```keywords```, etc.) for personalized usage.

## Convert SPARC data to NWB format
Open *sparc_to_nwb.m* in MATLAB and run the script.

## SPARC2NWB Team
[Marielle Darwin](https://github.com/mldarwin) | [Ananth Reddy](https://github.com/anbhimi) | [Derek Chang](https://github.com/DerekYJC) | [Patrick Chuang](https://github.com/lifestrugglee)

[contributors-shield]: https://img.shields.io/github/contributors/SPARC-FAIR-Codeathon/sparc2nwb.svg?style=flat-square
[contributors-url]: https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/SPARC-FAIR-Codeathon/sparc2nwb.svg?style=flat-square
[stars-url]: https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/stargazers
[issues-shield]: https://img.shields.io/github/issues/SPARC-FAIR-Codeathon/sparc2nwb.svg?style=flat-square
[issues-url]: https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/issues
