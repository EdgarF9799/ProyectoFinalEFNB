# -*- coding: utf-8 -*-
"""Pruebaunitaria01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FgOQeuJm2Z_hjLDAR4FPInto6Pm-3eAM
"""

import os
import pytest

def test_training_data_existence():
    # Path of the dataset in the system
    data_folder = 'C:\Users\Edgar F\Desktop\000MLOPS\02AmbientesVirtuales\my_project\data'

    data_path = os.path.join(data_folder, 'heart.csv')

    assert os.path.exists(data_path), "Training data file does not exist."