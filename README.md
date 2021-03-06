

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/hamza-mughees/Microsoft-Detecting-COVID-19/tree/Readm">
    <img src="machineLearninglogo.PNG" alt="Logo" width="2000" height="300">
  </a>

  <h3 align="center">Machine Learning in Medicine </h3>

  <p align="center">
    Github repository for Software Engineering Group 23 (2021)
    <br />
    <a href="https://github.com/hamza-mughees/Microsoft-Detecting-COVID-19/tree/Readm"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</p>





<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
Github repository for Software Engineering Group 23 (2021)

COVID-19 has brought the world into a deep financial and health crisis. With the number of cases rising daily, it becomes increasingly difficult to test and diagnose the virus efficiently and effectively. The purpose of this system is to make the diagnosis of COVID-19 a lot quicker and easier. This can be achieved with the help of modern technologies such as machine learning and deep learning. A number of datasets have been made public over the duration of this pandemic. These datasets consist of various X-rays, some of which test positive for COVID-19 and others negative. This project uses a concatenation of some of these datasets to train a Convolutional Neural Networks model. Once trained, this model has the potential to predict the presence of COVID-19 on X-ray scans.

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->


### Built With

* Microsoft Azure
* Python
* TensorFlow
* Keras
* sciKit Learn
<!-- * scope to add more in future
* []() -->



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

You need to have access to Microsoft Azure.
Install the following packages: 
 ```
 pip install tensorflow
 ```
 ```
 pip install sklearn
 ```
 ```
 pip install azure-storage-blob
 ```
 ```
 pip install requests
 ```
 ```
 pip install python-dotenv
 ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/hamza-mughees/Microsoft-Detecting-COVID-19.git
   ```



<!-- USAGE EXAMPLES -->
## Usage 

The intention of this project is to detect the presence of COVID-19 in X-Ray images of lungs.
It works by passing an X-Ray image of lungs through our trained convolutional neural network, them the CNN will output a percentage with the probability of the diagnosis being positive. To run a diagnosis on your image, download the `api-call.py` file and insert the path to the image you wish to diagnose. Then run the script and the API will call the model and return a diagnosis of the image





<!-- CONTRIBUTING -->
## Contributing

<!-- Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**. -->

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. 




<!-- CONTACT -->
## Contact - Email :

Hamza    - `mugheesh@tcd.ie`</br>
Jason    - `mullenj7@tcd.ie`</br>
Masanari - `doim@tcd.ie`</br>
Sarah  - `Dolans1@tcd.ie`</br>
Sean - `slangan@tcd.ie`</br>




<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements 
* [COVID-chestxray-dataset](https://github.com/ieee8023/COVID-chestxray-dataset)
* [Figure1-COVID-chestxray-dataset](https://github.com/agchung/Figure1-COVID-chestxray-dataset)
* [COVID-NET](https://github.com/lindawangg/COVID-Net)

* [COVID19-radiography-database ](https://www.kaggle.com/tawsifurrahman/COVID19-radiography-database)
* [rsna-pneumonia-detection-challenge](https://www.kaggle.com/c/rsna-pneumonia-detection-challenge)
* [Actualmed-COVID-chestxray-dataset](https://github.com/agchung/Actualmed-COVID-chestxray-dataset
)










<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
