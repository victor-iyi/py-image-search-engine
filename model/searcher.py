"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 31 December, 2017 @ 8:50 AM.
  
  Copyright © 2017. Victor. All rights reserved.
"""
from scipy.spatial.distance import euclidean


class Searcher:

    def __init__(self, features):
        self.features = features

    def search(self, query):
        results = {}

        for name, feature in self.features.items():
            dist = euclidean(query, feature)
            results[name] = dist

        results = sorted([(d, n) for n, d in results.items()])
        return results
