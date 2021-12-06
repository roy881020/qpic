import json

test_path = 'data/hico_20160224_det/annotations/test_hico.json'
train_path = 'data/hico_20160224_det/annotations/trainval_hico.json'

with open(test_path, 'r') as json_file:
    test_data = json.load(json_file)

with open(train_path, 'r') as json_file:
    train_data = json.load(json_file)

import pdb; pdb.set_trace()

for i in range(len(test_data['annotation'])):
    if 23 in test_data['annotation'][i]['hoi']:
        print(i)



