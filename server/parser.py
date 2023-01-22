from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from numpy.linalg import norm

from db import *
from GraphParser import *
session = Session()


def vectorize(data):
    return TfidfVectorizer().fit_transform(data).toarray()


def similarity(A, B):
    return np.dot(A,B)/(norm(A)*norm(B))


if __name__ == "__main__":
    vals = GP.GetNodes()
    vectors = vectorize(vals)
    B = np.random.rand(6342)
    results = {}
    similar = []
    for i in range(len(vectors)):
        A = vectors[i]
        cosine = similarity(A, B)
        # print("Cosine Similarity:", cosine)
        similar.append(cosine)
        results[cosine] = i
    similar.sort(reverse=True)
    # print(similar)
    res = similar[:5]
    print(res)
    for j in res:
        print(results.get(j))
    for name in range(len(res)):
        print(vals[name], end="|||")