<p align="center">
  <img src="https://user-images.githubusercontent.com/78009407/126273326-662b5aff-034f-4f48-a62a-69552195ff86.png" />
</p>

[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Purpose
This is the repository for Team 1 of the [2021 SPARC FAIR Codeathon](https://sparc.science/help/2021-sparc-fair-codeathon). Supported by the [NIH Common Fund](https://commonfund.nih.gov/), [SPARC](https://sparc.science/) is an open access data sharing resource with high-value datasets, maps, tools, and computational studies in the field of bioelectronic medicine that ultimately aims to improve targeting for more specifically designed neuromodulation therapies.

## Project Goals

### Identifying the Problem
A major problem our team has identified is that data within the [SPARC Portal](https://sparc.science/) is stored in a variety of different file formats and is not standardized. This heterogeneity limits data sharing as well as interoperability between programming languages, which slows progress in the field. Our team sought methods that would overcome this challenge and improve the [FAIRness](https://www.fosteropenscience.eu/learning/assessing-the-fairness-of-data/#/id/5c52e8cf0d3def29462d8cb5) of SPARC data.

![image](https://user-images.githubusercontent.com/78009407/126266615-45145c58-d560-4ffb-a855-67334e6530e8.png)

### Creating a Solution
Our project goal is to improve the readability and accessibility of SPARC data by standardizing the format in which the data is stored. We will achieve this goal by first converting raw data stored on the SPARC portal into NWB format. Once the data is in NWB format, we will then create APIs to extract the data out of the NWB files so that researchers can manipulate the data for analyses in multiple programming languages. 

![image](https://user-images.githubusercontent.com/78009407/126270243-286a0091-967a-4d71-8031-e33939a435ef.png)

### What is Neurodata Without Borders (NWB)?
[Neurodata Without Borders (NWB)](https://www.nwb.org/nwb-neurophysiology/) is a NIH-based initiative to create a cross-platform standard for neurophysiology data storage and sharing. 

![image](https://user-images.githubusercontent.com/78009407/126270802-c69bea33-3f2a-4739-83ae-80c1acf7d817.png)

The NWB file format allows users to store raw and processed data and associated metadata in a single, standardized format. Common file formats used in experimentation (e.g., .csv, .xlsx, .json, .m, .py) can be converted into .nwb format and the stored file information can then be extracted into the programming language of choice (i.e., Matlab, Python, C++) for processing and analyses. NWB is a dynamic format and does not have a stable folder structure for storing data across domains. Instead, the folder structure heavily depends on the study experimentation process and the type of data that was collected. 

## Conversion of SPARC data to NWB format

[under construction]

### Description of data used to develop the pipeline
Our team created the tools and the code to convert data and metadata from an [optophysiological study dataset](https://sparc.science/datasets/124?type=dataset&path=files) within the SPARC portal into NWB format. The study [(protocol here](https://www.protocols.io/view/mechanosensitive-enteric-neurons-incidence-and-abu-bpcamise), [manuscript here)](https://www.nature.com/articles/s41598-020-70216-6) aimed to characterize porcine and human neuronal responses to mechanical compression and tension using immunohisochemical techniques.

### Step 1: Convert raw data in SPARC Portal into NWB format using Python
#### Converted data includes: 
1. Timeframe (i.e., timestamp in frame number)
2. Neuronal response (i.e., changes in fluorescence in response to stimulus)

#### Converted metadata includes: 
1. Study subject ID
2. Mechanical stimulus type (i.e., stretch or compression)
3. Specific neuron within a group that responded to stimulus
More descriptors can be added as metadata as needed.

### Step 2: Extract data from NWB file with Matlab- and Python-based APIs for analyses


## Additional References
1. https://discover.pennsieve.io/datasets/99
2. https://github.com/SteinmetzLab/dataToNWB/tree/master/visualDiscriminationNeuropixels
3. https://pynwb.readthedocs.io/en/stable/

## SPARC2NWB Team
[Marielle Darwin](https://github.com/mldarwin) | [Ananth Reddy](https://github.com/anbhimi) | [Derek Chang](https://github.com/DerekYJC) | [Patrick Chuang](https://github.com/lifestrugglee)

[contributors-shield]: https://img.shields.io/github/contributors/SPARC-FAIR-Codeathon/sparc2nwb.svg?style=flat-square
[contributors-url]: https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/SPARC-FAIR-Codeathon/sparc2nwb.svg?style=flat-square
[stars-url]: https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/stargazers
[issues-shield]: https://img.shields.io/github/issues/SPARC-FAIR-Codeathon/sparc2nwb.svg?style=flat-square
[issues-url]: https://github.com/SPARC-FAIR-Codeathon/sparc2nwb/issues

