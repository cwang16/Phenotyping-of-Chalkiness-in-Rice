# Deep Learning based High-Throughput Phenotyping of Chalkiness in Rice Exposed to High Night Temperature
Web-based application will be available as soon as the paper is published <br />
Mobile friendly, no installation required, no coding skills required <br />
Dataset is available at <a href="https://ksuemailprod-my.sharepoint.com/:f:/g/personal/cwang16_ksu_edu/EuW4snBXRwhFizUUhDymxM8BSwG7PQmdX64yHqHak_GhSg?e=HufGdh">Download</a>
Models for polished and unpolished rice are available at <a href="https://ksuemailprod-my.sharepoint.com/:f:/g/personal/cwang16_ksu_edu/EuWYz0GHek5EsJoWOXyQMFcB-i47HwHYnv9tAUipJuB3Hw?e=mGRFep">Download</a>
 <br />

##
The repository introduced a tool segementing rice chalkiness from rice seeds using Grad-CAM (Selvaraju et al, ICCV, 2017). The Pytorch implementation of Grad-CAM (WonKwang Lee, 2018), available at https://github.com/1Konny/gradcam_plus_plus-pytorch, was used to segment chaliness area from rice seed. Models are trained with polished rice (1000+ seeds) and unpolished rice (10000+ seeds), respectively.  The dataset, model, and code where the layers are modified according to the rice chlakiness segmentation is made available here to enable easy training or fine-tuning of models for other sets of seeds chalkiness segmentation. 
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






