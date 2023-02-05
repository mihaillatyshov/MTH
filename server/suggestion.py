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


def test():
    return "hello"


def suggestion(data):
    nodes = session.query(Node).all()
    vals = [node.value for node in nodes]
    vals.append(data)
    vectors = vectorize(vals)
    B = vectors[-1]
    results = {}
    similar = []
    for i in range(len(vectors)):
        A = vectors[i]
        cosine = similarity(A, B)
        similar.append(cosine)
        results[cosine] = i
    similar.sort(reverse=True)
    res = similar[:5]
    reccomedations = []
    for name in range(len(res)):
        reccomedations.append(vals[name])
    return reccomedations

