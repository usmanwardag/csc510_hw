# CSC510 Homework

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/usmanwardag/csc510_hw)

[![Build Status](https://app.travis-ci.com/usmanwardag/csc510_hw.svg?branch=main)](https://app.travis-ci.com/usmanwardag/csc510_hw)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5393344.svg)](https://doi.org/10.5281/zenodo.5393344)


[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub license](https://img.shields.io/github/license/usmanwardag/csc510_hw)](https://github.com/usmanwardag/csc510_hw/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/usmanwardag/csc510_hw)](https://github.com/usmanwardag/csc510_hw/issues)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/usmanwardag/csc510_hw)](https://github.com/usmanwardag/csc510_hw/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub stars](https://img.shields.io/github/stars/usmanwardag/csc510_hw)](https://github.com/usmanwardag/csc510_hw/stargazers)

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
         <li><a href="#example">Example</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This is our take on a "good" Github Repo. We picked a [Kaggle](https://www.kaggle.com/starbucks/starbucks-menu) dataset of Starbucks nutrition drinks for this Repo and we show the drinks that fall into the following three categories:
* Lowest Calorie Drink
* Highest Carb Drink
* Highest Protein Drink

<!-- GETTING STARTED -->
## Getting Started

The repo contains a simple python script which reads our dataset and based on it we perform basic functions to find specific drinks.

### Prerequisites

We require Python (Version 3 and above) to be installed locally. Click [here](https://www.python.org/downloads/) to install depending on your Operating System. 

### Installation
First, install the Python packages listed in [requirements.txt](https://github.com/usmanwardag/csc510_hw/blob/main/requirements.txt)
  ```sh
  pip install -r requirements.txt
  ```
  
Next, install the `hwcsc510` package, and you are good to go.
  ```sh
  pip install -e .
  ```

### Example 
To find the lowest calorie drink in the Starbucks menu:
  ```sh
  from hwcsc510.code import find_low_calorie_drink
  print(find_low_calorie_drink())
  ```

<!-- CONTRIBUTING -->
## Contributing

We would be happy to receive contributions! If you'd like to, please go through our [CONTRIBUTING.md](https://github.com/usmanwardag/csc510_hw/blob/main/CONTRIBUTING.md)

<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE](https://github.com/usmanwardag/csc510_hw/blob/main/LICENSE) for more information.

<!-- CONTACT -->
## Contact

* [Kriti Khullar](https://github.com/kriti0207)
* [Muskan Gupta](https://github.com/muskan7828)
* [Suneha Bose](https://github.com/sbosenc)
* [Urvashi Kar](https://github.com/Urvashi74)
* [Usman Mahmood Khan](https://github.com/usmanwardag)

## Acknowledgments

We thank our Professor of course CSC510 - Professor Dr. [Timothy Menzies](http://menzies.us/) for giving us this exciting way of exploring how we can go about building a good repository.
