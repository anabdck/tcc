"""
Separação do dataset para treinamento e teste
"""
import os
import cv2
import numpy as np
import fileinput
from random import seed
from random import random
import math

test_fraction = 0.2
train_fraction = 1 - test_fraction

seed()

ROOT_DIR = os.getcwd()
dir = ROOT_DIR + '/data'
os.chdir(dir)

dataset_size = int(len(os.listdir(dir))/2)

list = []
test_list = []
train_list = []

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".txt"):
        file = str.split(filename, ".")[0]
        list.append(file)


#Colocando aleatoriamente itens dentro da pasta de validacao
for x in range(int(test_fraction*dataset_size)):
    filename = list.pop(int(random()*(dataset_size-x)))
    os.rename(filename + ".txt", "../valid/" + filename + ".txt")
    os.rename(filename + ".jpg", "../valid/" + filename + ".jpg")
    test_list.append(filename)

#Colocando o restante dos itens dentro da pasta de treinamento
for filename in list:
    os.rename(filename + ".txt", "../obj/" + filename + ".txt")
    os.rename(filename + ".jpg", "../obj/" + filename + ".jpg")
    train_list.append(filename)

# salvando arquivo txt com a lista de teste e treinamento
dir = ROOT_DIR + "/../yolov4_train"
os.chdir(dir)
with open("test.txt", "w") as outfile:
    for line in test_list:
        outfile.write('data/valid/' + line + '.jpg')
        outfile.write("\n")
    outfile.close()

with open("train.txt", "w") as outfile:
    for line in train_list:
        outfile.write('data/obj/' + line + '.jpg')
        outfile.write("\n")
    outfile.close()
