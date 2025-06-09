Examen de Minería de Datos: Predicción de Enfermedad Cardíaca
Duración total: 1 hora y 30 minutos
Base de datos: Disponible en el Campus Virutal
Descripción General
Este dataset contiene información clínica de pacientes con el objetivo de diagnosticar
enfermedades cardíacas. Es una versión corregida del conjunto de datos original de
UCI Machine Learning Repository, con errores revisados y descripciones ajustadas.
Atributos
Incluye 13 variables independientes (edad, tipo de dolor en el pecho, frecuencia
cardíaca, colesterol, etc.) y una variable objetivo:
condition: 0 indica que no hay enfermedad cardíaca, 1 indica que sí la hay.
Instrucciones generales
◆ Desarrolla el examen en un entorno Jupyter Notebook o Google Colab.
◆ Responde cada sección de forma clara. Justifica tus respuestas teóricas con
tus propias palabras.
◆ Comenta tu código para explicar cada paso brevemente.
◆ Se evaluará: comprensión de objetivos, aplicación técnica, y claridad del
análisis.
Parte 1: Análisis Conceptual (Tiempo estimado: 25 minutos)
Responde brevemente las siguientes preguntas:
1. Objetivo comercial: Explica con tus palabras cuál es el objetivo comercial de utilizar
este dataset en un contexto hospitalario.
2. Objetivo de minería de datos: Plantea el objetivo de minería de datos que se debe
cumplir con este conjunto de datos.
3. Tipo de problema: ¿Se trata de un problema de clasificación, regresión u otro?
Justifica brevemente.
4. Tipo de variables: Identifica y clasifica al menos 4 variables en tipos: numérica,
categórica, binaria u ordinal.
5. Significado de cp (chest pain): Describe qué representa la variable cp y por qué
podría ser relevante para predecir una enfermedad cardíaca.
Parte 2: Implementación Técnica en Python (Tiempo estimado: 65 minutos)
Requisitos técnicos: Python 3, Pandas, Scikit-learn, Matplotlib/Seaborn
6. Carga del dataset: Carga el archivo heart.csv en un DataFrame y muestra las
primeras 5 filas.
7. Análisis exploratorio (EDA):
◆ Describe brevemente la distribución de datos: usa histogramas y
df.describe().
◆ Verifica valores nulos.
◆ Genera y comenta una matriz de correlación.
8. Preparación de datos (10 min)
◆ Codifica variables categóricas si es necesario (cp, thal, slope).
◆ Verifica el balance de clases (condition).
9. Separación de datos: Divide el conjunto de datos en entrenamiento y prueba (80/20).
10. Entrenamiento de modelo: Entrena un modelo y Justifica tu elección en una
línea.
11. Evaluación del modelo: Comenta brevemente qué significan estas métricas en el
contexto médico.
12. Conclusión final: Redacta en 3-4 líneas:
◆ ¿Cómo fue el rendimiento del modelo?
◆ ¿Qué variables parecen ser las más influyentes?
◆ ¿Qué mejorarías en un futuro trabajo?

