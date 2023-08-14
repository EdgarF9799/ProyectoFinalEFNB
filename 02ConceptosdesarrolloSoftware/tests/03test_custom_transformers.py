# -*- coding: utf-8 -*-
"""test_custom_transformers02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FgOQeuJm2Z_hjLDAR4FPInto6Pm-3eAM

CustomScaler
Verifies that the CustomEncoder transformer correctly performs label encoding.
"""

import numpy as np
from sklearn.datasets import load_iris
from transformers.custom_transformers import CustomScaler, CustomEncoder


def test_custom_scaler():

      # Ruta ficticia a la carpeta "data" en el sistema
    data_folder = 'C:\Users\Edgar F\Desktop\000MLOPS\02AmbientesVirtuales\my_project\data'

    # Load the data
    data = os.path.join(data_folder, 'heart.csv')

     Y = data.data

     # Create an instance of the CustomScaler
     encoder = CustomEncoder()

    # Paso 3: Ajustar el transformador a los datos
    encoder.fit(y)

    # Paso 4: Transformar los datos utilizando el CustomEncoder
    y_encoded = encoder.transform(y)

    # Paso 5: Realizar afirmaciones para verificar la codificación
    assert np.array_equal(np.unique(y_encoded), np.array([0, 1, 2])), "Encoding not performed correctly"