"""
Conversão das anotações de "HRIPCB dataset" em xml para as anotações em txt utilizadas no YOLO
Referências:
https://stackoverflow.com/questions/19772288/python-parse-xml-and-save-as-txt
"""
import os
import cv2
import numpy as np
from tqdm import tqdm
import argparse
import fileinput
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET


obj_names = ["open_circuit", "short", "mouse_bite", "spur", "spurious_copper", "missing_hole"]

def convert(splited_filename, coords, group):
    img_dir = "/home/ana/github/PCB_DATASET/images/" + group + "/" + splited_filename + ".jpg"
    imagem = cv2.imread(img_dir)
    coords[2] -= coords[0]         # diferença largura (x_fim - x_inicio)
    coords[3] -= coords[1]         # diferença altura (y_fim - y_inicio)
    x_dif = int(coords[2] / 2)     # converte diferença_largura pra int
    y_dif = int(coords[3] / 2)     # converte diferença_altura pra int
    coords[0] = coords[0] + x_dif  # x_inicio + diferença largura
    coords[1] = coords[1] + y_dif  # y_inicio + diferença altura
    largura = int(imagem.shape[1]) # = largura da imagem
    altura = int(imagem.shape[0])  # = altura da imagem
    coords[0] /= largura
    coords[1] /= altura
    coords[2] /= largura
    coords[3] /= altura
    return coords

if __name__ == "__main__":
    annotations_folder = 'Annotations'
    os.chdir('/home/ana/github/PCB_DATASET')
    for folder in os.listdir(annotations_folder):
        if (folder.endswith(".JPG") or folder.endswith(".jpg") or folder.endswith(".TXT") or folder.endswith(".txt")) :
            pass
        else:
            print(' - - - ' + folder + ' - - - ')
            for filename in tqdm(os.listdir(annotations_folder + '/' + folder)):
                if (filename.endswith(".XML") or filename.endswith(".xml")) :
                    splited_filename = str.split(filename, ".")[0]
                    annotations = []
                    tree = ET.parse(annotations_folder+'/'+folder+"/"+filename)
                    root = tree.getroot()
                    annotations = []
                    for object in root.findall('object'):
                        coords = []
                        name = object.find('name').text
                        coords.append(int(object.find('bndbox').find('xmin').text))
                        coords.append(int(object.find('bndbox').find('ymin').text))
                        coords.append(int(object.find('bndbox').find('xmax').text))
                        coords.append(int(object.find('bndbox').find('ymax').text))
                        coords = convert(splited_filename, coords, folder)
                        newline = str(obj_names.index(name)) + " " + str(coords[0]) + " " + str(coords[1]) + " " + str(coords[2]) + " " + str(coords[3])
                        annotations.append(newline)

                    os.chdir("/home/ana/github/pcb-fabrication-fault-detection/pcb_data/data")
                    with open(splited_filename + ".txt", "w") as outfile:
                        for line in annotations:
                            outfile.write(line)
                            outfile.write("\n")
                        outfile.close()
                    os.chdir('/home/ana/github/PCB_DATASET')
