<p align="center">
  <img src="https://user-images.githubusercontent.com/78009407/126273326-662b5aff-034f-4f48-a62a-69552195ff86.png" />
</p>

[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Purpose
This repository holds the code and the supporting files to convert SPARC data into NWB format using Python. The repository uses [PyNWB](https://pynwb.readthedocs.io/en/stable/) package. Instructions are provided below to run the code and convert datasets from sparc to NWB format.

## Usage
1. Create a folder named `data` and drop the sparc dataset in the data folder.
2. The dependencies required to run the python script are in `requirments.txt`. Install the dependencies.
```shell
python3 -m pip install requirements.txt
```
3. Change the `standard_path` and `filename` vairables in the main function to get the data and save the nwb files respectively.
4. Run the python script.
```shell
python3 sparc_to_nwb.py
```

## Conversion of SPARC Data to NWB Data
<ol>
<li>The above research paper was used as baseline for conversion of SPARC data to NWB format.</li>
<li>The NWB file was fed with the metadata information regarding the subject. The metadata information includes age, genotype, subject id, sex, weight, species, and description.
<ol>
  <li>The metadata information is extracted from sample and subject data files samples data and subject data respectivly.</li>
</ol>
</li>
<li>Additional metadata including session description, identifier, session start time, file creation data, institution, lab, experimenter, experiment description, related publications, and keywords were added to the NWB File.
<ol>
  <li>Institution and Lab records were left blank because of lack of information.</li>
  <li>The above information is manually retrieved from the experiment website.</li>
</ol>
</li>
<li>Finally the data about neural activity was included in addition to the electrodes data.
<ol>
  <li>The information about electrodes includes - x, y, and z co-ordinates, location, and group of the electrode.</li>
  <li>The information about time series includes - name, description, and the data itself.</li>
</ol>
</ol>

Below, we tabulated the information about containers and the data placed in them. Reamining data containers are left untouched for this dataset.

NWB Container | Data
------------- | ----
acquisition/events | Neural Activity Data
general_extracellular_ephys/electrodes | Electrodes Data
general_subject | Subject Metadata
intervals/trails | timestamp Metadata


## SPARC2NWB Team
[Marielle Darwin](https://github.com/mldarwin) | [Ananth Reddy](https://github.com/anbhimi) | [Derek Chang](https://github.com/DerekYJC) | [Patrick Chuang](https://github.com/lifestrugglee)

[contributors-shield]: https://img.shields.io/github/contributors/SPARC-FAIR-Codeathon/sparc2nwb.svg?style=flat-square
[contributors-url]: https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/SPARC-FAIR-Codeathon/sparc2nwb.svg?style=flat-square
[stars-url]: https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/stargazers
[issues-shield]: https://img.shields.io/github/issues/SPARC-FAIR-Codeathon/sparc2nwb.svg?style=flat-square
[issues-url]: https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/issues
