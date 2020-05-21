# Proyecto Final
### Sistema de predicción de riesgos de enfermedades cardiovasculares. 

Las enfermedades cardiovasculares (ECV) son un conjunto de trastornos del corazón y de los vasos sanguíneos. De acuerdo con la Organización Mundial de la Salud (OMS) son la principal causa de muerte en el mundo, las cifras de defunciones tanto en hombres como en mujeres abarcan más del 40% de las enfermedades crónicas. 

![](Images/F_oms.jpg)

![](Images/H_oms.jpg)

A pesar de que los factores de riesgo son conocidos, es muy habitual que los síntomas se confundan y que las enfermedades se reconozcan únicamente cuando el estado de salud se ha deteriorado. Debido a que no existe una fórmula ni una manera para predecir manualmente cómo es que esos factores son responsables de una ECV, una herramienta que puede ser implementada para la prevención y detección temprana de este tipo de enfermedades es la ciencia de datos, particularmente aplicando técnicas de Machine Learning. 

### Datos utilizados

###### Visualización de datos

Para la realización de gráficas para la comprensión del problema, así como para tener una idea general del problema, se utilizaron bases de datos obtenidas de la página oficial de la OMS, así como datos obtenidos de la Secretaría de Salud. (Carpeta Datos)

###### Entrenamiento del modelo y análisis exploratorio de datos.

Para el entrenamiento del modelo, se utilizó una base de datos de 70,000 pacientes, perteneciente a una base de datos de kaggle.com Esta base contaba con 12 tipos de datos de pacientes, como son: 

* ID: para identificar al paciente

* Edad del paciente

* Género del paciente (1= hombre, 2= mujer)

* Peso del paciente (en kg)

* Estatura del paciente (en cm)

* Presión sistólica

* Presión diastólica

* Nivel de glucosa

  Considerando [1: Bajo (<110 mg/dl) 2: Medio (110 - 130 mg/dl) 3: Alto (>130 mg/dl)]

* Nivel de colesterol

  Considerando [1: Bajo (<200 mg/dl) 2: Medio (200 - 240 mg/dl) 3: Alto (>240 mg/dl)]

También incluye tres factores de riesgo, clasificados con (1 y 0) :

* Consumo de tabaco
* Consumo de alcohol
* Realización de actividad física

### Entrenamiento del modelo

Se probaron diferentes modelos de Machine Learning, pertenecientes a la librería de scikit-learn. Con base en múltiples pruebas y en los resultados obtenidos de r2 score, mean square error y la obtención de la matriz de correlación, se seleccionó una máquina de soporte vectorial (SVC) para realizar la clasificación. 

Para el target de la base de datos, se empleó una columna llamada 'cardio', que tenía como parámetros 1 y 0, indicando si el paciente tenía o no una enfermedad cardiovascular. 

Una vez entrenado el modelo y después de realizar las pruebas correspondientes, se exportó a un archivo tipo pickle (Carpeta datos) para utilizarlo en el programa principal. 

### Programa principal

El programa para el usuario incluye las funciones necesarias para que los datos ingresados sean validados de manera que puedan ser ingresados al modelo y así se realice una predicción. 

Una vez que se muestra el resultado de dicha predicción en forma de porcentaje, al usuario se le proporciona un pequeño resumen de los datos que ha ingresado comparados con los valores ideales recomendados por la Organización Mundial de la Salud (OMS).

##### Carpetas y contenido

###### Datos

* Cardio_train.csv: Base de datos obtenida de kaggle.com
* Clean_data.csv: Datos procesados y analizados, empleados para el modelo de ML
* data(1).csv: Datos utilizados para la visualización, obtenidos de la OMS
* GHE.xlsx: Datos utilizados para la visualización, obtenidos de la OMS
* modelo_fin: Modelo de machine learning para el programa principal
* mortalidad_2019.xlsx: Datos utilizados para la visualización, obtenidos del Instituo Mexicano de Cardiología
* Tasa_Mortalidad_Cardiovascular: Datos utilizados para la visualización, obtenidos de la Secretaría de Salud.

###### Principal

* GráficaSS_MX.ipynb: Creación de gráfica animada con datos de la Secretaría de Salud
* Gráficas_trimestre.ipynb: Visualización de datos, creación de gráficas con matplotlib.
* EDA.ipynb: Análisis exploratorio de datos y limpieza de datos. Creación de base para el modelo de ML.
* Prueba_modelosML.ipynb: Ejemplo de aplicación de machine learning al dataset.
* final.py: Programa principal. 





