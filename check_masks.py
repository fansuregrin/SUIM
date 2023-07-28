import os
from PIL import Image
import numpy as np
from shutil import copy

image_dir = '/DataA/pwz/workshop/Datasets/SUIM_orig/train_val/images'
masks_dir = '/DataA/pwz/workshop/Datasets/SUIM_orig/train_val/masks'
# need_reannot_dir = '/DataA/pwz/workshop/Datasets/SUIM_orig/train_val/need_re_annot'

# image_dir = '/DataA/pwz/workshop/Datasets/SUIM_orig/test/images'
# masks_dir = '/DataA/pwz/workshop/Datasets/SUIM_orig/test/masks'
# need_reannot_dir = '/DataA/pwz/workshop/Datasets/SUIM_orig/test/need_re_annot'

img_names = sorted(os.listdir(image_dir))
mask_names = sorted(os.listdir(masks_dir))
for img_name, mask_name in zip(img_names, mask_names):
    img = Image.open(os.path.join(image_dir, img_name))
    mask = Image.open(os.path.join(masks_dir, mask_name))
    img = np.asarray(img, dtype=np.uint8)
    mask = np.asarray(mask, dtype=np.uint8)
    r = np.all((mask==0)|(mask==255))
    if (not r) or (img.shape != mask.shape):
    # if (not r): # check masks files with improper color
    # if (img.shape != mask.shape): # check masks files with improper size
        # copy(os.path.join(image_dir, img_name), os.path.join(need_reannot_dir, 'images', img_name))
        # copy(os.path.join(masks_dir, mask_name), os.path.join(need_reannot_dir, 'improper_masks', mask_name))
        print(img_name, mask_name)