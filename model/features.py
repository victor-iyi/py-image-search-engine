"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 02 January, 2018 @ 1:25 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
import glob
import os
import pickle

import cv2

from model.descriptor import Histogram


def extract(dataset):
    features = {}
    descriptor = Histogram(bins=[8, 8, 8])

    for filename in glob.glob(os.path.join(dataset, '*.jpg|png$')):
        # e.g. places/eiffel_tower.jpg => eiffel_tower
        img_name = os.path.basename(filename).split('.')[0]

        image = cv2.imread(filename)
        feature = descriptor.describe(image)
        # key - image name, value - feature vector
        features[img_name] = feature
    return features


# Writing the index to disk
def save(obj, path):
    if not os.path.isfile(path):
        os.makedirs(os.path.dirname(path))
    with open(path, 'w') as f:
        pickle.dump(obj, f)
