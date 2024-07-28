import torch
import torch.nn as nn
from torch.nn import functional as F

# hyperparameters
batch_size = 3072 # how many independent sequences will we process in parallel?
block_size = 1024 # what is the maximum context length for predictions?
max_iters = 10000
eval_interval = 1000
learning_rate = 1e-5
device = 'cuda' if torch.cuda.is_available() else 'cpu'
eval_iters = 200
n_embd = 256
n_head = 8
n_layer = 6
dropout = 0.0
# ------------

torch.manual_seed(1337)

with open('dataset.txt', 'r', encoding='utf-8') as f:
    text = f.read()
