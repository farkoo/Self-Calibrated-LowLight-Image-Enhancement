import os
import sys
import numpy as np
import torch
import argparse
import torch.utils
import torch.backends.cudnn as cudnn
from PIL import Image
from torch.autograd import Variable
from model import Finetunemodel

from multi_read_data import MemoryFriendlyLoader

parser = argparse.ArgumentParser("SCI")
parser.add_argument('--data_path', type=str, default="C:\\Seminar\\Dataset\\LOLdataset\\eval15\\low\\",
                    help='location of the data corpus')
parser.add_argument('--save_path', type=str, default="C:\\Seminar\\15-Session\\SCI-HSV-LOL\\gray-images\\", help='location of the data corpus')
parser.add_argument('--model', type=str, default="C:\\Seminar\\15-Session\\SCI-HSV-LOL\\weights_499.pt", help='location of the data corpus')
parser.add_argument('--gpu', type=int, default=0, help='gpu device id')
parser.add_argument('--seed', type=int, default=2, help='random seed')

args = parser.parse_args()
save_path = args.save_path
os.makedirs(save_path, exist_ok=True)

TestDataset = MemoryFriendlyLoader(img_dir=args.data_path, task='test')

test_queue = torch.utils.data.DataLoader(
    TestDataset, batch_size=1,
    pin_memory=True, num_workers=0)


def save_images(tensor, path):
    # Ensure the tensor is on the CPU
    tensor = tensor.cpu()
    # Squeeze the dimensions if they are of size 1
    tensor = tensor.squeeze(0).squeeze(0)
    # Convert to a numpy array
    image_numpy = tensor.numpy()
    # Convert to a grayscale image
    image_numpy = np.transpose(image_numpy, (0, 1))
    # Scale the values to [0, 255] and convert to uint8
    image_numpy = np.clip(image_numpy * 255.0, 0, 255.0).astype('uint8')
    # Create a PIL Image and save it as PNG
    im = Image.fromarray(image_numpy)
    im.save(path, 'png')


def main():
    if not torch.cuda.is_available():
        print('no gpu device available')
        sys.exit(1)

    model = Finetunemodel(args.model)
    model = model.cuda()

    model.eval()
    with torch.no_grad():
        for _, (input, image_name) in enumerate(test_queue):
            input = Variable(input, volatile=True).cuda()
            image_name = image_name[0].split('\\')[-1].split('.')[0]
            i, r = model(input)
            u_name = '%s.png' % (image_name)
            print('processing {}'.format(u_name))
            u_path = save_path + '/' + u_name
            save_images(r, u_path)



if __name__ == '__main__':
    main()
