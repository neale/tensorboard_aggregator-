from tensorboard.backend.event_processing import event_accumulator

import os
import sys
import pandas as pd

paths = []
tfp = input('tf log dirname: ')
path = '/home/ubuntu/repos/hyperdeeprl/tf_log/'+tfp
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".ubuntu-MS-7B48"):
             p = os.path.join(root, file)
             paths.append(p)

filepath = 'files/'+tfp
if not os.path.exists(filepath):
    os.makedirs(filepath)
else:
    print ('folder exists, will not overwrite, please delete and rerun')
    sys.exit(0)

paths = sorted(paths, key=lambda x: int(x.split('N')[-1].split('-')[0]))
for i, path in enumerate(paths):
    ea = event_accumulator.EventAccumulator(path,
        size_guidance={ # see below regarding this argument
            event_accumulator.COMPRESSED_HISTOGRAMS: 500,
            event_accumulator.IMAGES: 4,
            event_accumulator.AUDIO: 4,
            event_accumulator.SCALARS: 0,
            event_accumulator.HISTOGRAMS: 1,
    })

    ea.Reload() # loads events from file
    n = path.split('N')[1].split('-')[0]
    print (path)
    df = pd.DataFrame(ea.Scalars('episodic_return_train')).to_csv(filepath+'/N{}.csv'.format(n)) 
