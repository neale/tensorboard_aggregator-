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

    if p2 == '': iters = 1
    for _ in range(iters):
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
        
        colors = ['b' if item < 1990 else 'r' for item in samples]
        ax.scatter(r, samples, s=5., color=colors)
        
    ax.set_facecolor('whitesmoke')       
    major_xticks = np.arange(0, 101, 25)
    minor_xticks = np.arange(0, 101, 12.5)
    major_yticks = np.arange(0, 2001, 500)
    minor_yticks = np.arange(0, 2001, 250)
    
    # Wild
    ax.set_xticks(major_xticks)
    ax.set_xticks(minor_xticks, minor=True)
    ax.set_yticks(major_yticks)
    ax.set_yticks(minor_yticks, minor=True)
    plt.xticks([25, 50, 75, 100])
    plt.yticks([])

    ax.set_title('')
    plt.grid(which='both')
    sns.despine()
    #plt.xlabel('Chain length', fontsize=18)
    #plt.ylabel('Episodes to learn', fontsize=18)
    #plt.tight_layout()
    plt.savefig('../figs/'+p+'.png')
    plt.show()

p = input('dirname: ')
p2 = input('dirname2: ')

plot(p)
