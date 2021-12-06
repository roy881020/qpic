import numpy as np
import pdb
import argparse
from datasets import build_dataset, get_coco_api_from_dataset

path = 'data/hico_20160224_det/annotations/corre_hico.npy'

test = np.load(path)

parser = argparse.ArgumentParser()
parser.add_argument('--dataset_file', default='hico')
parser.add_argument('--hoi_path', default='data/hico_20160224_det', type=str)
dataset_train = build_dataset(image_set='train', args= parser.parse_args())