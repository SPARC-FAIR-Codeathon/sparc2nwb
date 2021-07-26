<p align="center">
  <img src="https://user-images.githubusercontent.com/78009407/126273326-662b5aff-034f-4f48-a62a-69552195ff86.png" />
</p>

[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

## Purpose

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

## Module Contains Description
The figure below indicates the structure design of the module. The lists in green circle are the contains based on the [dataset](https://sparc.science/datasets/124?type=dataset&path=files). The lists at the right bottom pink area are the default containers of the NWB format which refer to the [paper](https://www.nature.com/articles/s41597-020-0415-9#Fig2). Additionally, `NWB_SOURCE` also provides the access to the original NWB format of data.

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
