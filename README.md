# ❤️‍🩺 Predicción de Enfermedad Cardíaca  
*Repositorio oficial · [EnriquePalacios99/prediccion-de-enfermedad-cardiaca](https://github.com/EnriquePalacios99/prediccion-de-enfermedad-cardiaca)*

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)
![License](https://img.shields.io/github/license/EnriquePalacios99/prediccion-de-enfermedad-cardiaca)
![Last Update](https://img.shields.io/github/last-commit/EnriquePalacios99/prediccion-de-enfermedad-cardiaca)

---

## 1. Descripción

Este proyecto demuestra un **pipeline completo de Machine Learning** para detectar enfermedad cardíaca a partir de datos clínicos tabulares.  
Incluye todas las etapas: exploración, ingeniería de características, entrenamiento, evaluación, interpretación y despliegue 📦.

---

## 2. Estructura del repositorio

```
.
├── data/                    # Datos brutos y pre-procesados
├── notebooks/
│   └── heart.ipynb          # Notebook principal (EDA + modelado)
├── src/
│   ├── preprocessing.py     # Limpieza y codificación de variables
│   ├── training.py          # Entrenamiento + búsqueda de hiperparámetros
│   └── evaluation.py        # Métricas, curvas ROC, matriz de confusión
├── models/
│   └── heart_model.pkl      # Modelo entrenado (versión estable)
├── reports/
│   ├── confusion_matrix.png # Matriz de confusión final
│   └── shap_summary.png     # Interpretabilidad (SHAP)
└── README.md
```

> **Tip:** Cada módulo está completamente documentado y probado con *pytest*.

---

## 3. Flujo de trabajo

| Fase                        | Herramientas / librerías                          |
| --------------------------- | ------------------------------------------------- |
| Ingesta y EDA              | *Pandas*, *Seaborn*, *Matplotlib*                 |
| Ingeniería de variables     | One-Hot, escalado robusto, imputación medianas    |
| Selección de características| *RFECV* + filtros estadísticos                    |
| Modelado                    | **Random Forest Classifier** (mejor desempeño)    |
| Evaluación                  | Accuracy, Precision, Recall, F1, ROC-AUC          |
| Interpretabilidad           | SHAP values, feature importance                   |
| Serialización y despliegue  | *joblib*, Dockerfile (opcional)                   |

---

## 4. Resultados clave

| Métrica       | Valor |
| ------------- | ----- |
| **Accuracy**  | **0.900** |
| **Precision** | **1.000** |
| **Recall**    | **0.786** |
| **F1-Score**  | **0.880** |
| **ROC-AUC**   | **0.958** |

![Confusion Matrix](reports/confusion_matrix.png)

### 4.1 Interpretación clínica rápida (Objetivo 11)

* **Exactitud (Accuracy 0.90)** → 9 de cada 10 pacientes son clasificados correctamente.  
* **Precisión 1.00** → no se generan falsos positivos: ningún paciente sano fue etiquetado como enfermo, evitando ansiedad y pruebas invasivas innecesarias.  
* **Recall 0.786** → el modelo detecta ~79 % de los casos reales de enfermedad; aún existe margen para reducir falsos negativos, clave en medicina preventiva.  
* **F1 0.88** equilibra precisión y sensibilidad, confirmando un rendimiento consistente.  
* **ROC-AUC 0.958** muestra una gran capacidad para discriminar entre pacientes sanos y enfermos a distintos umbrales.

### 4.2 Conclusión final (Objetivo 12)

El modelo exhibe un **rendimiento sólido** para cribado inicial, con precisión perfecta y alta capacidad discriminativa.  
Las variables más influyentes —según SHAP— son:  
`cp` (tipo de dolor torácico), `thalach` (FC máx.), `oldpeak` y `ca` (n.º vasos coloreados).  
A futuro se sugiere **equilibrar la sensibilidad** (p.ej. *SMOTE*, ajuste de umbral) y probar modelos basados en gradiente (XGBoost, LightGBM) junto con validación externa para mejorar la generalización.

---

## 5. Instalación rápida

```bash
# 1. Clonar el repo
git clone https://github.com/EnriquePalacios99/prediccion-de-enfermedad-cardiaca.git
cd prediccion-de-enfermedad-cardiaca

# 2. Crear entorno y activar
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar notebook o script de entrenamiento
jupyter notebook notebooks/heart.ipynb
#  ó bien:
python src/training.py --data data/heart.csv --save models/heart_model.pkl
```

---

## 6. Cómo reproducir resultados

1. **Pre-procesa** los datos:  
   `python src/preprocessing.py --input data/heart.csv --output data/heart_clean.csv`
2. **Entrena** con configuración por defecto:  
   `python src/training.py --config configs/base.yaml`
3. **Evalúa** el modelo entrenado:  
   `python src/evaluation.py --model models/heart_model.pkl --test data/heart_clean.csv`
4. Revisa los artefactos generados en `reports/`.

---

## 7. Contribuir

¡Las *pull requests* son bienvenidas!  
Por favor abre primero un *issue* para discutir los cambios 😊.

1. Haz un *fork* del proyecto  
2. Crea tu rama (`git checkout -b feature/mi-mejora`)  
3. Commitea los cambios (`git commit -m 'feat: mejora X'`)  
4. Push a tu fork (`git push origin feature/mi-mejora`)  
5. Abre una Pull Request

---

## 8. Licencia

Este repositorio se publica bajo la **Licencia MIT**.  
Consulta el archivo `LICENSE` para más información.

---

## 9. Contacto

| Autor | LinkedIn | Twitter |
| ----- | -------- | ------- |
| **Enrique A. Palacios A.** | [in/enriquepalacios](https://www.linkedin.com/in/enriquepalacios) | [@enri_palacios](https://twitter.com/enri_palacios) |

¡Gracias por visitar el proyecto y contribuir a la detección temprana de enfermedades cardíacas!  
