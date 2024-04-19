import numpy as np
import torch
import torch.utils.data
import random
from PIL import Image
from glob import glob
import torchvision.transforms as transforms
import os
import cv2

batch_w = 600
batch_h = 400


class MemoryFriendlyLoader(torch.utils.data.Dataset):
    def __init__(self, img_dir, task):
        self.low_img_dir = img_dir
        self.task = task
        self.train_low_data_names = []

        for root, dirs, names in os.walk(self.low_img_dir):
            for name in names:
                self.train_low_data_names.append(os.path.join(root, name))

        self.train_low_data_names.sort()
        self.count = len(self.train_low_data_names)

        transform_list = []
        transform_list += [transforms.ToTensor()]
        self.transform = transforms.Compose(transform_list)

    def load_images_transform(self, file):
        # # Load the image using PIL and convert it to RGB
        # im = Image.open(file).convert('RGB')
        # # Convert the PIL image to a NumPy array
        # img_norm = np.array(im)
        # # Convert the RGB image to the HSV color space
        # hsv_image = cv2.cvtColor(img_norm, cv2.COLOR_RGB2HSV)
        # # Extract the V channel
        # v_channel = hsv_image[:, :, 2]
        # v_channel = np.expand_dims(v_channel, axis=-1)
        
        # Load the RGB image
        image = cv2.imread(file)
        
        # Convert the RGB image to the HSV color space
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        # Extract the V (value) channel
        intensity_channel = hsv_image[:,:,2]
        intensity_channel = self.transform(intensity_channel).numpy()
        # v_channel = np.expand_dims(intensity_channel, axis=1)
        return intensity_channel

    def __getitem__(self, index):

        low = self.load_images_transform(self.train_low_data_names[index])

        h = low.shape[0]
        w = low.shape[1]
        #
        h_offset = random.randint(0, max(0, h - batch_h - 1))
        w_offset = random.randint(0, max(0, w - batch_w - 1))
        #
        # if self.task != 'test':
        #     low = low[h_offset:h_offset + batch_h, w_offset:w_offset + batch_w]

        low = np.asarray(low, dtype=np.float32)
        # low = np.transpose(low[:, :, :], (2, 0, 1)) # HSV

        img_name = self.train_low_data_names[index].split('\\')[-1]
        # if self.task == 'test':
        #     # img_name = self.train_low_data_names[index].split('\\')[-1]
        #     return torch.from_numpy(low), img_name

        return torch.from_numpy(low), img_name

    def __len__(self):
        return self.count
