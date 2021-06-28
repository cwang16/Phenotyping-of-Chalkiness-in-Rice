# Deep Learning based High-Throughput Phenotyping of Chalkiness in Rice Exposed to High Night Temperature
<!--Web-based application will be available as soon as the paper is published <br />
Mobile friendly, no installation required, no coding skills required <br />-->
Dataset of original images is available <a href="https://ksuemailprod-my.sharepoint.com/:f:/g/personal/cwang16_ksu_edu/EuW4snBXRwhFizUUhDymxM8BSwG7PQmdX64yHqHak_GhSg?e=HufGdh">here.</a>  <br />
Models for polished and unpolished rice are available <a href="https://ksuemailprod-my.sharepoint.com/:f:/g/personal/cwang16_ksu_edu/EuWYz0GHek5EsJoWOXyQMFcB-i47HwHYnv9tAUipJuB3Hw?e=mGRFep">here.</a>The models are used in main.py file.
 <br />
<!-- Datasets of individual polished and unpolished seed images are available <a href="">here.</a>  <br />-->

##
The repository contains data and models for detecting chalkiness in rice grains. The models are based on a weakly supervised segementation approach, Grad-CAM (Selvaraju et al., 2017). The Pytorch implementation of Grad-CAM (WonKwang Lee, 2018), available at https://github.com/1Konny/gradcam_plus_plus-pytorch, was used to segment chaliness area from rice grains. We experiment with models that are trained with both polished and unpolished rice seeds.  The dataset, model, and code are available in this repository to enable reproducibility, reuse and transfer of knowledge to chalkiness detection tasks for other types of rice seeds.
<br />

<br>
<p align="center">
<img src=assets/Screenshot.png>
</p>

## Content of the Repository
__main.py__ is the code for segementing the rice chalkiness area from rice seeds <br />

## segement rice chalkiness area from rice seeds:
See below the command to segement the rice chalkiness area from rice seeds <br />

python main.py






