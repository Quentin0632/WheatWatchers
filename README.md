<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Quentin/WheatWatchers">
    <img src="logo/wheatWatchersLogo.png" alt="Logo" width="364" height="205">
  </a>

<h3 align="center">Wheat Watchers</h3>

  <p align="center">
    Innovating methods for agricultural ground data collection and crop assessments using street level images and satellite data: <br />
    A prototype in Alsace
 
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<div align="justify">
  
The project is part of a project to monitor crops using satellite data, undertaken by Nasa's food security and agriculture program: Nasa Harvest. The objective of this program is to provide information that will allow, for example, to anticipate crop failures and therefore agricultural production deficits, or to identify the most efficient practices.   

Commissioned by members of the TRIO research team of the ICube laboratory, our project concerns more specifically the field collection of data (crop images collected by a camera) that should allow the interpretation of satellite images (by training machine learning models).  

The first challenge is to develop a method to evaluate the distance between the photographed object (a fragment of field/crop) and the go-pro camera mounted on a car from which the picture is taken. This step aims at assigning to the collected data an exact location (and not the road where the picture was taken).  

The next step consists in automating the identification of the types of crops and the agricultural practices implemented on these crops from the plantation images.  

The final objective is to obtain a detailed mapping of the crops, based on surveys conducted throughout the year. 
</div>

### Software requirements

* [Python version 3.6+](https://www.python.org/downloads/)
* [exiftool](https://exiftool.org/)
* [ffmpeg](https://www.ffmpeg.org/download.html)

### Some Python libraries you will need to include (and to install if it is not already done)

* glob
* torch
* cv2
* os
* shutil
* math
* numpy
* exif
* copy
* csv
* sys
* argparse
* pandas
* datetime
* pathlib
* subprocess
* json
* re
* traceback
* gpxpy


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


<pre> 
WheatWatchers
│   arrayToCSV.py                                                         
│   boundingBoxesMatching.py              
│   Calc_coordonnéesGPS.py                
│   distanceCarToCrop.py                  
│   exiftool.exe                          
│   ffmpeg.exe                       
│   gf2gv.py                         
│   log.gpx                          
│   main.py                     
│   ML.py                          
│   videosToFrames.py                               
├───CSV                            
├───FRAMES                          
│   ├───LEFT                         
│   │       README.txt                          
│   └───RIGHT
│           README.txt
├───RESULTATS
│       README.txt
├───VIDEO
│   ├───LEFT
│   │       README.txt
│   └───RIGHT
│           README.txt
└───yolov5
    │   0.8.1'
    │   CONTRIBUTING.md
    │   dataset.yaml
    │   detect.py
    │   Dockerfile
    │   export.py
    │   hubconf.py
    │   LICENSE
    │   README.md
    │   requirements.txt
    │   setup.cfg
    │   train.py
    │   tutorial.ipynb
    │   val.py
    │   yolov5l.pt
    │   yolov5m.pt
    │   yolov5s.pt
    ├───.git
    │   ├───objects
    │   └───refs
    ├───.github
    │   └───workflows
    ├───data
    │   ├───hyps
    │   ├───images
    │   └───scripts
    ├───models
    │   └───hub
    ├───runs
    │   └───train
    └───utils
</pre>

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation


<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
