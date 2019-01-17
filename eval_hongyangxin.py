import os
import h5py
import numpy as np
import argparse
import torch
import copy
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable
from models_pretrained import *
import torch.nn.functional as F
import torchvision
from torchvision import transforms
from utils import load_data, majority_vote
import bird_or_bicycle
from itertools import chain
from unrestricted_advex import eval_kit

# os.environ['CUDA_VISIBLE_DEVICES'] = "0"
weight_path = 'res50_28_best.pt'
net = ResNet50Pre()


def eval_adv_rotate_KLloss_fn(x_np):
	x_np = x_np.transpose((0, 3, 1, 2))  # from NHWC to NCHW
	x_t = torch.from_numpy(x_np).cuda()
	net.eval()
	with torch.no_grad():
		return net(x_t).cpu().numpy()


# --- MAIN ---
if __name__ == "__main__":
	net.load_state_dict(torch.load(weight_path))
	
	device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
	net = nn.DataParallel(net)
	net.to(device)
	# net.cuda()
	# net.cpu()
	eval_kit.evaluate_bird_or_bicycle_model(
		eval_adv_rotate_KLloss_fn,
		model_name='hongyang_xin')
	