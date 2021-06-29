import os
import PIL
import numpy as np
import torch
import torch.nn.functional as F
import torchvision.models as models
from torchvision.utils import make_grid, save_image

from utils import visualize_cam, Normalize
from gradcam import GradCAM, GradCAMpp

# load image
img_dir = "./datasets/test"
model_dir = "./models"
img_name = "18P31686_MG_HC003_ROI_30.jpg" # add image name here
img_path = os.path.join(img_dir, img_name)
pil_img = PIL.Image.open(img_path)

# preprocess image
normalizer = Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
torch_img = torch.from_numpy(np.asarray(pil_img)).permute(2, 0, 1).unsqueeze(0).float().div(255).cuda()
torch_img = F.upsample(torch_img, size=(224, 224), mode='bilinear', align_corners=False)
normed_torch_img = normalizer(torch_img)

#Load torchvision models and make model dictionaries
resnet = torch.load(os.path.join(model_dir, "resnet101_28.pkl")) #add model file name here
resnet.eval(), resnet.cuda();

cam_dict = dict()

resnet_model_dict = dict(type='resnet', arch=resnet, layer_name= 'layer2_0_conv2', input_size=(224, 224))
resnet_gradcam = GradCAM(resnet_model_dict, True)
resnet_gradcampp = GradCAMpp(resnet_model_dict, True)
cam_dict['resnet'] = [resnet_gradcam, resnet_gradcampp]

images = []
for gradcam, gradcam_pp in cam_dict.values():
    mask, _ = gradcam(normed_torch_img, class_idx=1)
    heatmap, result = visualize_cam(mask.cpu(), torch_img)
    images.append(torch.stack([torch_img.squeeze().cpu(), heatmap, result], 0))

images = make_grid(torch.cat(images, 0), nrow=3)

#Save and show results
output_dir = 'outputs'
os.makedirs(output_dir, exist_ok=True)
output_name = img_name
output_path = os.path.join(output_dir, output_name)

save_image(images, output_path)
PIL.Image.open(output_path)
