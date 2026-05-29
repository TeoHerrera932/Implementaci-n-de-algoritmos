# 🏪 Sistema de Predicción de Ventas con Regresión Lineal

## 📋 Descripción

Sistema completo de **regresión lineal** para predecir ventas futuras basadas en el gasto en publicidad. Incluye análisis estadístico, visualización de datos, evaluación del modelo y predicciones personalizadas.

### Objetivo Principal
Predecir las ventas de un producto en función del gasto en publicidad mediante un modelo matemático de regresión lineal.

---

## 🎯 Características Principales

✅ **Creación de Datos**: Genera o carga datos realistas de publicidad vs ventas  
✅ **Modelo de Regresión Lineal**: Implementación con scikit-learn  
✅ **Validación Completa**: Entrada de usuario validada y manejo de errores  
✅ **Menú Interactivo**: Interfaz amigable con múltiples opciones  
✅ **Análisis Estadístico**: Media, desviación estándar, correlación  
✅ **Evaluación del Modelo**: MSE, RMSE, MAE, R²  
✅ **Visualización**: Gráficos de datos, modelo, residuos  
✅ **Predicciones**: Personalizadas y predicciones rápidas  
✅ **Análisis de Residuos**: Comprobación de supuestos del modelo  

---

## 📊 Requisitos Técnicos

### Dependencias Python
```
numpy>=1.21.0          # Computación numérica
pandas>=1.3.0          # Manipulación de datos
matplotlib>=3.4.0      # Visualización gráfica
seaborn>=0.11.0        # Gráficos estadísticos avanzados
scikit-learn>=0.24.0   # Machine Learning
```

### Sistema Operativo
- Windows, macOS o Linux
- Python 3.8 o superior

---

## 🚀 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/Implementaci-n-de-algoritmos
cd Implementaci-n-de-algoritmos
```

### 2. Instalar dependencias
```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

O con uv (recomendado):
```bash
uv pip install numpy pandas matplotlib seaborn scikit-learn
```

---

## 💻 Uso del Programa

### Ejecutar el programa
```bash
python Main.py
```

O con uv:
```bash
uv run Main.py
```

### Menú Principal
```
============================================================
🏪 SISTEMA DE PREDICCIÓN DE VENTAS - REGRESIÓN LINEAL
============================================================
1. 📊 Crear/Cargar datos
2. 📈 Entrenar modelo
3. 📉 Ver estadísticas y gráficos
4. 🔮 Hacer predicción personalizada
5. ⚡ Ver predicciones rápidas
6. 📋 Ver parámetros del modelo
7. 🎯 Evaluar modelo
8. 📊 Ver gráficos avanzados
9. ❌ Salir
```

---

## 📖 Guía de Opciones

### 1️⃣ Crear/Cargar Datos
- **Opción A**: Generar 10-10,000 registros simulados realistas
- **Opción B**: Cargar datos desde archivo CSV personalizado
- Mostrar primeras 5 filas y estadísticas descriptivas

### 2️⃣ Entrenar Modelo
- División automática: 80% entrenamiento, 20% prueba
- Entrenamiento del modelo de regresión lineal
- Muestra cantidad de registros para cada conjunto

### 3️⃣ Ver Estadísticas y Gráficos
- Tabla de estadísticas descriptivas (media, desv. est., cuartiles)
- Gráfico de dispersión de datos brutos

### 4️⃣ Hacer Predicción Personalizada
- Ingrese gasto en publicidad (validado)
- Reciba predicción de ventas estimadas
- Continúe con más predicciones o salga

### 5️⃣ Ver Predicciones Rápidas
- Predicciones preestablecidas: $5k, $10k, $15k, $20k, $25k, $30k
- Formato tabulado fácil de leer

### 6️⃣ Ver Parámetros del Modelo
- **Ecuación**: Ventas = β₀ + β₁ × Gasto_Publicidad
- **Intercepto (β₀)**: Punto de partida del modelo
- **Coeficiente (β₁)**: Cambio en ventas por cada $1k adicional
- Interpretación clara y didáctica

### 7️⃣ Evaluar Modelo
- **MSE** (Error Cuadrático Medio)
- **RMSE** (Raíz del Error Cuadrático Medio)
- **MAE** (Error Absoluto Medio)
- **R²** (Coeficiente de Determinación): 0 a 1
  - R² ≥ 0.9: ⭐⭐⭐⭐⭐ Excelente
  - 0.7 ≤ R² < 0.9: ⭐⭐⭐⭐ Muy Bueno
  - 0.5 ≤ R² < 0.7: ⭐⭐⭐ Bueno
  - 0.3 ≤ R² < 0.5: ⭐⭐ Regular
  - R² < 0.3: ⭐ Pobre

### 8️⃣ Ver Gráficos Avanzados
- **Gráfico 1**: Modelo vs Datos Reales - visualiza qué tan bien se ajusta
- **Gráfico 2**: Análisis de Residuos
  - Residuos vs Predicciones: comprobación de linealidad
  - Distribución de Residuos: histograma de errores

### 9️⃣ Salir
- Cierra el programa de forma ordenada

---

## 📐 Teoría del Modelo

### Ecuación de Regresión Lineal
$$y = \beta_0 + \beta_1 x + \varepsilon$$

Donde:
- **y**: Variable dependiente (Ventas)
- **x**: Variable independiente (Gasto en Publicidad)
- **β₀**: Intercepto (valor base)
- **β₁**: Coeficiente (pendiente)
- **ε**: Error residual

### Métricas de Evaluación

**R² (Coeficiente de Determinación)**
- Mide qué porcentaje de la variabilidad en ventas se explica por publicidad
- Rango: 0 a 1 (más cercano a 1 = mejor)

**RMSE (Raíz del Error Cuadrático Medio)**
- Error típico en unidades de la variable dependiente
- Menores valores = mejor precisión

**MAE (Error Absoluto Medio)**
- Error promedio en valor absoluto
- Más interpretable que RMSE

---

## 📂 Estructura de Archivos

```
Implementaci-n-de-algoritmos/
├── Main.py                    # Programa principal
├── README.md                  # Este archivo
├── test_input.txt            # Archivo de prueba (opcional)
└── datos.csv                 # Archivo de datos (si lo carga)
```

---

## 🔍 Ejemplos de Uso

### Ejemplo 1: Análisis Rápido
```
1. Crear datos (opción 1)
2. Entrenar modelo (opción 2)
3. Ver predicciones rápidas (opción 5)
4. Salir (opción 9)
```

### Ejemplo 2: Análisis Completo
```
1. Crear datos (opción 1)
2. Ver estadísticas (opción 3)
3. Entrenar modelo (opción 2)
4. Evaluar modelo (opción 7)
5. Ver gráficos avanzados (opción 8)
6. Hacer predicciones personalizadas (opción 4)
7. Salir (opción 9)
```

### Ejemplo 3: Usar Datos Propios
```
1. Cargar desde CSV (opción 1, subopción 2)
2. Entrenar modelo (opción 2)
3. Ver parámetros (opción 6)
4. Hacer predicciones (opción 4)
```

---

## 📊 Formato de Archivo CSV

Si desea cargar datos propios, use el siguiente formato:

```csv
Gasto_Publicidad,Ventas
5.2,28.5
10.8,41.2
15.3,54.8
```

**Columnas requeridas:**
- `Gasto_Publicidad`: Gasto en miles de USD (numérico)
- `Ventas`: Ventas en miles de unidades (numérico)

---

## ✅ Validaciones del Programa

✔️ Entrada numérica: Solo acepta números válidos  
✔️ Rango de valores: Validación de mínimos y máximos  
✔️ Existencia de modelo: Verifica que se haya entrenado antes de usar  
✔️ Existencia de datos: Verifica que se hayan cargado datos  
✔️ Manejo de excepciones: Captura y reporta errores de forma clara  
✔️ Entrada de usuario interrumpida: Detiene el programa gracefully  

---

## 🐛 Solución de Problemas

### Problema: "ModuleNotFoundError: No module named 'numpy'"
**Solución**: Instale las dependencias
```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

### Problema: Matplotlib no muestra gráficos
**Solución**: Los gráficos se mostrarán en una ventana separada. Si no aparece, verifique su entorno.

### Problema: El programa se congela
**Solución**: Si está cargando muchos datos, espere. Presione Ctrl+C para interrumpir.

### Problema: CSV no se carga
**Solución**: 
- Verifique que la ruta sea correcta
- Confirme que tenga columnas: `Gasto_Publicidad` y `Ventas`
- Use rutas absolutas o relativas correctas

---

## 📈 Casos de Uso Real

1. **Empresa de Marketing**: Optimizar presupuesto publicitario
2. **E-commerce**: Predecir ventas según gasto en ads
3. **Negocio Local**: Estimar ingresos por inversión en publicidad
4. **Análisis Académico**: Aprender regresión lineal de forma práctica
5. **Data Science**: Prototipo de predicción rápida

---

## 🎓 Conceptos Aprendidos

- ✅ Regresión lineal simple
- ✅ Ajuste de modelos con scikit-learn
- ✅ Dividir datos en train/test
- ✅ Evaluar modelos con múltiples métricas
- ✅ Analizar residuos
- ✅ Crear visualizaciones con matplotlib y seaborn
- ✅ Entrada/validación de usuario
- ✅ Manejo de excepciones
- ✅ Menús interactivos en Python

---

## 📝 Notas Importantes

⚠️ **Supuestos de Regresión Lineal**:
- Relación lineal entre variables
- Residuos distribuidos normalmente
- Varianza constante (homocedasticidad)
- Independencia de observaciones

⚠️ **Limitaciones**:
- Solo funciona para relaciones lineales
- Sensible a valores atípicos (outliers)
- Requiere datos de entrada de calidad

---

## 👨‍💻 Autor

Programa desarrollado como ejemplo práctico de implementación de algoritmos de Machine Learning.

---

## 📄 Licencia

Código libre para uso educativo y comercial.

---

## 🔗 Referencias

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [NumPy Documentation](https://numpy.org/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Matplotlib Documentation](https://matplotlib.org/)

---

**Versión**: 1.0  
**Última actualización**: 2026  
**Estado**: ✅ Completamente funcional