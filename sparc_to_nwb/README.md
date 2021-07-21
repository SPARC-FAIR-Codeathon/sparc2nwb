<p align="center">
  <img src="https://user-images.githubusercontent.com/78009407/126273326-662b5aff-034f-4f48-a62a-69552195ff86.png" />
</p>

[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Purpose
This repository holds the code and the supporting files to convert sparc data into NWB format using Python. The repository uses [PyNWB](https://pynwb.readthedocs.io/en/stable/) package. Instructions are provided below to run the code and convert datasets from sparc to NWB format.

## Usage
1. Create a folder named `data` and drop the sparc dataset in the data folder.
2. Create a folder named `nwb_files` to hold all the nwb files created by the python script.
3. Install the required python dependencies to run the script.
```shell
python3 -m pip install requirements.txt
```
4. Change the `standard_path` and `filename` vairables in the main function to get the data and save the nwb files respectivly.
5. Run the python script.
```shell
python3 sparc_to_nwb.py
```

## SPARC2NWB Team
[Marielle Darwin](https://github.com/mldarwin) | [Ananth Reddy](https://github.com/anbhimi) | [Derek Chang](https://github.com/DerekYJC) | [Patrick Chuang](https://github.com/lifestrugglee)

[contributors-shield]: https://img.shields.io/github/contributors/SPARC-FAIR-Codeathon/sparc2nwb.svg?style=flat-square
[contributors-url]: https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/SPARC-FAIR-Codeathon/sparc2nwb.svg?style=flat-square
[stars-url]: https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/stargazers
[issues-shield]: https://img.shields.io/github/issues/SPARC-FAIR-Codeathon/sparc2nwb.svg?style=flat-square
[issues-url]: https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/issues
