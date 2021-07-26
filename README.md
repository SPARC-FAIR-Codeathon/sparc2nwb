<p align="center">
  <img src="https://user-images.githubusercontent.com/78009407/126273326-662b5aff-034f-4f48-a62a-69552195ff86.png" />
</p>

[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

## Purpose
This is the repository for Team 1 of the [2021 SPARC FAIR Codeathon](https://sparc.science/help/2021-sparc-fair-codeathon). Supported by the [NIH Common Fund](https://commonfund.nih.gov/), [SPARC](https://sparc.science/) is an open access data sharing resource with high-value datasets, maps, tools, and computational studies in the field of bioelectronic medicine that ultimately aims to improve targeting for more specifically designed neuromodulation therapies.

## Project Goals

### Identifying the Problem
A major problem our team has identified is that data within the [SPARC Portal](https://sparc.science/) is stored in a variety of different file formats and is not standardized. This heterogeneity limits data sharing as well as interoperability between programming languages, which slows progress in the field. Our team sought methods that would overcome this challenge and improve the [FAIRness](https://www.fosteropenscience.eu/learning/assessing-the-fairness-of-data/#/id/5c52e8cf0d3def29462d8cb5) of SPARC data.

![image](https://user-images.githubusercontent.com/78009407/126266615-45145c58-d560-4ffb-a855-67334e6530e8.png)

### Creating a Solution
Our project goal was to improve the readability and accessibility of SPARC data by standardizing the format in which the data is stored. We achieved this goal by first converting raw data stored on the [SPARC Portal](https://sparc.science/) into NWB format. Once the data was in NWB format, we then created APIs to extract the data out of the NWB files so that researchers can manipulate the data for analyses in multiple programming languages. 

![image](https://user-images.githubusercontent.com/78009407/126270243-286a0091-967a-4d71-8031-e33939a435ef.png)

### What is Neurodata Without Borders (NWB)?
[Neurodata Without Borders (NWB)](https://www.nwb.org/nwb-neurophysiology/) is a NIH-based initiative to create a cross-platform standard for neurophysiology data storage and sharing. 

![image](https://user-images.githubusercontent.com/78009407/126270802-c69bea33-3f2a-4739-83ae-80c1acf7d817.png)

The NWB file format allows users to store raw and processed data and associated metadata in a single, standardized format. Common file formats used in experimentation (e.g., .csv, .xlsx, .json, .m, .py) can be converted into .nwb format and the stored file information can then be extracted into the programming language of choice (i.e., Matlab, Python, C++) for processing and analyses. NWB is a dynamic format and does not have a stable folder structure for storing data across domains. Instead, the folder structure heavily depends on the study experimentation process and the type of data that was collected. The figure below illustrates the data storage structure for electrophysiological data, as an example ([Source](https://www.nature.com/articles/s41597-020-0415-9#Fig2)).
![image](https://user-images.githubusercontent.com/78009407/126580017-5fe43593-0bd0-419c-b3c1-bfc652f1b6c5.png)

### Description of data used to develop the pipeline
Our team created the tools and the code to convert data and metadata from an [optophysiological study dataset](https://sparc.science/datasets/124?type=dataset&path=files) within the [SPARC Portal](https://sparc.science/) into NWB format. The study [(protocol here](https://www.protocols.io/view/mechanosensitive-enteric-neurons-incidence-and-abu-bpcamise), [manuscript here)](https://www.nature.com/articles/s41598-020-70216-6) aimed to characterize porcine and human neuronal responses to mechanical compression and tension using immunohisochemical techniques.

#### Rationale for choosing [this dataset](https://sparc.science/datasets/124?type=dataset&path=files) to illustrate the use of our tools
We chose this dataset to illustrate the use of our tools for multiple reasons. First, optophysiological research methods are common within the [SPARC Portal](https://sparc.science/). By providing a template to convert this type of data to NWB, our project outcomes have a high impact in that more users can utilize our tools with minimal changes needed. We document the process of how we built the NWB file structure so that users can tailor our tools for different types of data as well.

Second, when choosing this dataset, we considered the impact potential and what would be helpful for the field. We ultimately chose to work with optophysiological data from a study that tested the neuronal response to mechanical stimulation in the porcine colon. This research contributed to investigating the underlying factors of inflammatory bowel disease (IBD), a condition which is a steeply growing public health crisis. 

The research community has recognized the critical nature of this crisis and has committed large amounts of resources to investigate the underlying factors of IBD. There has been consistently large amounts of publications regarding colon disease over recent years and the field is in need of comparative studies of neuronal mechanisms across species. These factors highlight the importance of open communication and data sharing in this subfield. Colon disease research is desperately needed, but the data is hard to access. We therefore chose an optophysiological dataset as this type of data would be highly relevant for SPARC users, and we chose to convert data from the field of colon disease research as this is a consistently rising area of study within the field. 

### User guide

#### Step 1: Find dataset you wish to convert to NWB format from the [SPARC Portal](https://sparc.science/)

#### Step 2: View template to determine if the chosen dataset complies with the structure of our tools

##### Template dataset structure
The current conversion APIs in the following step require the user to organize the dataset in the format of the template dataset structure below.
![image](https://github.com/DerekYJC/sparc2nwb/blob/d4407d9b98d01077c8ac3e827b5a3ab2137be5de/images/template_datastructure.jpg)

In the *manifest.xlsx*, ```filename``` represents the dataset filename **including the path**, and ```timestamp``` represents the time of the experiment to be acquired.
![image](https://github.com/DerekYJC/sparc2nwb/blob/d4407d9b98d01077c8ac3e827b5a3ab2137be5de/images/template_manifest.jpg)

In the *samples.xlsx*, the following data columns are required, including ```subject_id```, ```age```, ```specimen type```, ```sex```, ```species```, ```protocol title```, ```specimen```, and ```anatomical location```.

In the *subjects.xlsx*, the following data columns are required, including ```subject_id```, and ```Weight_kg```.
![image](https://github.com/DerekYJC/sparc2nwb/blob/d4407d9b98d01077c8ac3e827b5a3ab2137be5de/images/template_samples_subjects.jpg)

If the dataset is in the same raw storage format, use the [GUI](https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/tree/main/gui) in the following step to enter the dataset file path and convert to NWB file. If it is in a different format, you can either manipulate the format of the raw dataset or alter the [conversion script](https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/tree/main/sparc_to_nwb) in the following step to convert to NWB according to your specific needs. 

#### Step 3: Convert the raw data files to NWB format
You have three options for converting your data to NWB format. Documentation and further instruction regarding these tools can be found in the respective folders within this repository.
* Option 1: [Use Python-based GUI](https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/tree/main/gui) 
* Option 2: [Use conversion script script in Python](https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/tree/main/sparc_to_nwb)
* Option 3: [Use conversion script in Matlab](https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/tree/main/sparc_to_nwb_matlab)

##### In this example, converted data within the NWB file includes: 
1. Timeframe (i.e., timestamp in frame number)
2. Neuronal response (i.e., changes in fluorescence in response to stimulus)

##### And converted metadata within the NWB file ncludes: 
1. Subject Metadata (Age, Genotype, Subject ID, Sex, Weight, Species, and Description)
2. Session Metadata (Session Description, Identifier, Session start time, File creation date, Institution, Lab, Experimenter, Experiment Description, Related Publications, and Keywords)
3. Mechanical stimulus type (i.e., stretch or compression)
4. Specific neuron within a group that responded to stimulus

##### Further documentation regarding where the raw data is stored within the NWB file during the conversion process is located [here](https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/tree/main/sparc_to_nwb).

#### Step 4: Extract (meta)data out of NWB file 
You can extract the desired (meta)data out of the NWB file using either Matlab- or Python-based APIs located [here](https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/tree/main/extract_from_nwb). Further documentation regarding how to navigate the contents of the NWB file are included within the folder contents.

#### Step 5: Process and analyze (meta)data 
You are now able to view and manipulate the contents of the dataset in either Python or Matlab.

## Additional References
1. https://discover.pennsieve.io/datasets/99
2. https://github.com/SteinmetzLab/dataToNWB/tree/master/visualDiscriminationNeuropixels
3. https://pynwb.readthedocs.io/en/stable/

## Manuscipt
A manuscript that details the process of creating these tools, including open source code and data used in our project, is currently in progress. Check back soon!

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
