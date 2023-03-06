from PIL import Image
import numpy as np
from .utils import *
import torch
import einops
import random
from pytorch_lightning import seed_everything




def pre_img(img_path):
    c_img = np.array(Image.open(img_path))
    c_img = resize_image(HWC3(c_img), 512)
    H, W, C = c_img.shape
    detected_map = np.zeros_like(c_img, dtype=np.uint8)
    detected_map[np.min(c_img, axis=2) < 127] = 255
    control = torch.from_numpy(detected_map.copy()).float() / 255.0
    control = control.unsqueeze(0)
    control = einops.rearrange(control, 'b h w c -> b c h w').clone() # 1 3 512 512
    return control

def clip(text_a, text_b):
    pass





if __name__ == '__main__':
    c_img_path = '../src/test_imgs/user_3.png'
    prompt = "hot air balloon, best quality, extremely detailed, sunset, beach"
    neg_prompt = "longbody, lowres, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality"
    c_img = pre_img(c_img_path)
    seed = 9
    if seed == -1:
        seed = random.randint(0, 65535)
    seed_everything(seed)

    clip(prompt, neg_prompt)
