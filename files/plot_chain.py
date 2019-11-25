import os
import glob
import sys
import types
import math
import torch
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import csv


def to_numpy(x):
    return x.detach().cpu().numpy()

def csv_to_tensor(f, m):
    a = []
    with open(f) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i, row in enumerate(csv_reader):
            if i == 0:
                continue  # skip first row
            n = int(row[-2])
            a.append(n)
        steps = a[-2]
    episodes = steps / (9.+m)
    print (episodes)
    return episodes

def plot(p):

    fig, ax = plt.subplots(1, 1, figsize=(12, 5))

    csv_files = glob.glob(p+'/*.csv') 
    csv_files = sorted(csv_files, key=lambda x: int(x.split('/')[1][1:-4]))
    if len(csv_files) > 50:
        r = list(range(4, 101))
    else:
        r = list(range(20, 101))[::2]
    print (csv_files)
    csv_data = [csv_to_tensor(f, idx) for (f, idx) in zip(csv_files, r)]
    samples = np.array(csv_data)
    

    ax.scatter(r, samples, color='b')
        
    ax.set_title('')
    sns.despine()
    plt.xlabel('Chain length', fontsize=18)
    plt.ylabel('Episodes to learn', fontsize=18)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('../figs/'+p+'.png')
    plt.show()

p = input('dirname: ')
plot(p)
