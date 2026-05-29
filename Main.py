"""
Sistema de Predicción de Ventas con Regresión Lineal
Objetivo: Predecir ventas basadas en gasto en publicidad
Autor: Sistema de IA
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import sys
import os

# Configuración de estilo
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Variables globales
df = None
model = None
X_train = None
X_test = None
y_train = None
y_test = None
y_pred = None


def validar_entrada_numerica(mensaje, minimo=None, maximo=None):
    """
    Valida entrada numérica del usuario
    
    Args:
        mensaje: Mensaje a mostrar
        minimo: Valor mínimo permitido
        maximo: Valor máximo permitido
    
    Returns:
        float: Número validado
    """
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"❌ El valor debe ser mayor o igual a {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"❌ El valor debe ser menor o igual a {maximo}")
                continue
            return valor
        except ValueError:
            print("❌ Error: Ingrese un número válido")


def crear_datos_simulados(n=200):
    """
    Crea datos simulados realistas de publicidad vs ventas
    
    Args:
        n: Número de registros a generar
    
    Returns:
        DataFrame: Datos generados
    """
    try:
        np.random.seed(42)
        
        # Gasto en publicidad (entre 1 y 30 mil dólares)
        advertising = np.random.uniform(1, 30, n)
        
        # Ventas = 2.5 * advertising + ruido + tendencia base
        sales = 2.5 * advertising + np.random.normal(0, 4, n) + 15
        
        df_temp = pd.DataFrame({
            'Gasto_Publicidad': advertising,
            'Ventas': sales
        })
        
        print(f"\n✅ Dataset creado con {n} registros")
        return df_temp
    except Exception as e:
        print(f"❌ Error al crear datos: {e}")
        return None


def mostrar_estadisticas_datos(data):
    """Muestra estadísticas descriptivas del dataset"""
    try:
        print("\n" + "="*60)
        print("📊 ESTADÍSTICAS DESCRIPTIVAS DEL DATASET")
        print("="*60)
        print(data.describe())
        print("\nPrimeras 5 filas del dataset:")
        print(data.head())
    except Exception as e:
        print(f"❌ Error al mostrar estadísticas: {e}")


def visualizar_datos_brutos(data):
    """Visualiza la relación entre publicidad y ventas"""
    try:
        plt.figure(figsize=(12, 6))
        sns.scatterplot(x='Gasto_Publicidad', y='Ventas', data=data, 
                       alpha=0.6, s=80, color='steelblue')
        plt.title('Relación entre Gasto en Publicidad y Ventas', fontsize=14, fontweight='bold')
        plt.xlabel('Gasto en Publicidad (miles de USD)', fontsize=12)
        plt.ylabel('Ventas (miles de unidades)', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
        print("✅ Gráfico de datos brutos mostrado")
    except Exception as e:
        print(f"❌ Error al visualizar datos: {e}")


def entrenar_modelo(data):
    """
    Entrena el modelo de regresión lineal
    
    Args:
        data: DataFrame con los datos
    
    Returns:
        tuple: Modelo entrenado y datos de entrenamiento/prueba
    """
    try:
        global X_train, X_test, y_train, y_test
        
        X = data[['Gasto_Publicidad']]
        y = data['Ventas']
        
        # División de datos (80% entrenamiento, 20% prueba)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Crear y entrenar modelo
        modelo = LinearRegression()
        modelo.fit(X_train, y_train)
        
        print("\n✅ Modelo entrenado exitosamente")
        print(f"   Datos de entrenamiento: {len(X_train)}")
        print(f"   Datos de prueba: {len(X_test)}")
        
        return modelo
    except Exception as e:
        print(f"❌ Error al entrenar modelo: {e}")
        return None


def mostrar_parametros_modelo(modelo):
    """Muestra los parámetros del modelo entrenado"""
    try:
        print("\n" + "="*60)
        print("📐 PARÁMETROS DEL MODELO DE REGRESIÓN LINEAL")
        print("="*60)
        print(f"Ecuación: Ventas = {modelo.intercept_:.4f} + {modelo.coef_[0]:.4f} × Gasto_Publicidad")
        print(f"\nIntercepto (β₀) = {modelo.intercept_:.4f}")
        print(f"Coeficiente (β₁) = {modelo.coef_[0]:.4f}")
        print(f"\nInterpretación: Por cada mil dólares adicionales en publicidad,")
        print(f"se espera un aumento de {modelo.coef_[0]:.2f} mil unidades en ventas")
    except Exception as e:
        print(f"❌ Error al mostrar parámetros: {e}")


def evaluar_modelo(modelo):
    """
    Evalúa el desempeño del modelo
    
    Args:
        modelo: Modelo entrenado
    """
    try:
        global y_pred
        
        y_pred = modelo.predict(X_test)
        
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        print("\n" + "="*60)
        print("📈 EVALUACIÓN DEL MODELO")
        print("="*60)
        print(f"Error Cuadrático Medio (MSE): {mse:.4f}")
        print(f"Raíz del Error Cuadrático Medio (RMSE): {rmse:.4f}")
        print(f"Error Absoluto Medio (MAE): {mae:.4f}")
        print(f"Coeficiente de Determinación (R²): {r2:.4f}")
        print(f"\nCalidad del modelo:")
        if r2 >= 0.9:
            print("   ⭐⭐⭐⭐⭐ Excelente (R² >= 0.9)")
        elif r2 >= 0.7:
            print("   ⭐⭐⭐⭐ Muy Bueno (0.7 <= R² < 0.9)")
        elif r2 >= 0.5:
            print("   ⭐⭐⭐ Bueno (0.5 <= R² < 0.7)")
        elif r2 >= 0.3:
            print("   ⭐⭐ Regular (0.3 <= R² < 0.5)")
        else:
            print("   ⭐ Pobre (R² < 0.3)")
    except Exception as e:
        print(f"❌ Error al evaluar modelo: {e}")


def visualizar_modelo(modelo):
    """Visualiza el modelo y las predicciones"""
    try:
        plt.figure(figsize=(12, 6))
        plt.scatter(X_test, y_test, color='blue', alpha=0.6, s=80, label='Datos reales (Test)')
        plt.plot(X_test.sort_values('Gasto_Publicidad'), 
                modelo.predict(X_test.sort_values('Gasto_Publicidad')), 
                color='red', linewidth=3, label='Línea de regresión')
        plt.title('Predicción de Ventas vs Datos Reales', fontsize=14, fontweight='bold')
        plt.xlabel('Gasto en Publicidad (miles de USD)', fontsize=12)
        plt.ylabel('Ventas (miles de unidades)', fontsize=12)
        plt.legend(fontsize=11)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
        print("✅ Gráfico de modelo mostrado")
    except Exception as e:
        print(f"❌ Error al visualizar modelo: {e}")


def visualizar_residuos(modelo):
    """Visualiza los residuos del modelo"""
    try:
        residuos = y_test - y_pred
        
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Gráfico de residuos vs predicciones
        axes[0].scatter(y_pred, residuos, color='green', alpha=0.6, s=80)
        axes[0].axhline(y=0, color='red', linestyle='--', linewidth=2)
        axes[0].set_xlabel('Predicciones', fontsize=11)
        axes[0].set_ylabel('Residuos', fontsize=11)
        axes[0].set_title('Residuos vs Predicciones', fontsize=12, fontweight='bold')
        axes[0].grid(True, alpha=0.3)
        
        # Histograma de residuos
        axes[1].hist(residuos, bins=20, color='orange', alpha=0.7, edgecolor='black')
        axes[1].set_xlabel('Residuos', fontsize=11)
        axes[1].set_ylabel('Frecuencia', fontsize=11)
        axes[1].set_title('Distribución de Residuos', fontsize=12, fontweight='bold')
        axes[1].grid(True, alpha=0.3, axis='y')
        
        plt.tight_layout()
        plt.show()
        print("✅ Análisis de residuos mostrado")
    except Exception as e:
        print(f"❌ Error al visualizar residuos: {e}")


def hacer_predicciones(modelo):
    """Realiza predicciones personalizadas"""
    try:
        print("\n" + "="*60)
        print("🔮 PREDICCIÓN DE VENTAS PERSONALIZADA")
        print("="*60)
        
        while True:
            try:
                gasto = validar_entrada_numerica(
                    "\nIngrese gasto en publicidad (miles USD) [0 para salir]: ",
                    minimo=0
                )
                
                if gasto == 0:
                    break
                
                prediccion = modelo.predict([[gasto]])[0]
                print(f"\n💰 Gasto: ${gasto:.2f}k → 📊 Ventas estimadas: {prediccion:.2f}k unidades")
                
            except ValueError:
                print("❌ Error: Ingrese un número válido")
                
    except Exception as e:
        print(f"❌ Error al hacer predicciones: {e}")


def predicciones_rapidas(modelo):
    """Muestra predicciones rápidas para valores preestablecidos"""
    try:
        valores_test = np.array([[5], [10], [15], [20], [25], [30]])
        predicciones = modelo.predict(valores_test)
        
        print("\n" + "="*60)
        print("⚡ PREDICCIONES RÁPIDAS")
        print("="*60)
        print(f"{'Gasto (miles USD)':<20} {'Ventas Predichas (miles)':<25}")
        print("-"*45)
        
        for gasto, pred in zip(valores_test.flatten(), predicciones):
            print(f"${gasto:>6.1f}k{'':<11} {pred:>20.2f}k unidades")
    except Exception as e:
        print(f"❌ Error al generar predicciones rápidas: {e}")


def menu_principal():
    """Menú principal interactivo"""
    global df, model
    
    while True:
        print("\n" + "="*60)
        print("🏪 SISTEMA DE PREDICCIÓN DE VENTAS - REGRESIÓN LINEAL")
        print("="*60)
        print("1. 📊 Crear/Cargar datos")
        print("2. 📈 Entrenar modelo")
        print("3. 📉 Ver estadísticas y gráficos")
        print("4. 🔮 Hacer predicción personalizada")
        print("5. ⚡ Ver predicciones rápidas")
        print("6. 📋 Ver parámetros del modelo")
        print("7. 🎯 Evaluar modelo")
        print("8. 📊 Ver gráficos avanzados")
        print("9. ❌ Salir")
        print("="*60)
        
        opcion = input("Seleccione una opción (1-9): ").strip()
        
        if opcion == '1':
            print("\n1. Crear datos simulados")
            print("2. Cargar desde archivo CSV")
            subopcion = input("Seleccione (1-2): ").strip()
            
            if subopcion == '1':
                n = int(validar_entrada_numerica(
                    "Cantidad de registros (default 200): ",
                    minimo=10, maximo=10000
                ) or 200)
                df = crear_datos_simulados(n)
            elif subopcion == '2':
                ruta = input("Ingrese ruta del archivo CSV: ").strip()
                try:
                    df = pd.read_csv(ruta)
                    print("✅ Archivo cargado exitosamente")
                except FileNotFoundError:
                    print("❌ Archivo no encontrado")
            
            if df is not None:
                mostrar_estadisticas_datos(df)
                
        elif opcion == '2':
            if df is None:
                print("❌ Primero debe cargar datos")
            else:
                model = entrenar_modelo(df)
                
        elif opcion == '3':
            if df is None:
                print("❌ Primero debe cargar datos")
            else:
                mostrar_estadisticas_datos(df)
                visualizar_datos_brutos(df)
                
        elif opcion == '4':
            if model is None:
                print("❌ Primero debe entrenar el modelo")
            else:
                hacer_predicciones(model)
                
        elif opcion == '5':
            if model is None:
                print("❌ Primero debe entrenar el modelo")
            else:
                predicciones_rapidas(model)
                
        elif opcion == '6':
            if model is None:
                print("❌ Primero debe entrenar el modelo")
            else:
                mostrar_parametros_modelo(model)
                
        elif opcion == '7':
            if model is None:
                print("❌ Primero debe entrenar el modelo")
            else:
                evaluar_modelo(model)
                
        elif opcion == '8':
            if model is None:
                print("❌ Primero debe entrenar el modelo")
            else:
                print("\n1. Visualizar modelo")
                print("2. Analizar residuos")
                subopcion = input("Seleccione (1-2): ").strip()
                if subopcion == '1':
                    visualizar_modelo(model)
                elif subopcion == '2':
                    visualizar_residuos(model)
                    
        elif opcion == '9':
            print("\n👋 ¡Gracias por usar el sistema! Hasta luego.")
            break
        else:
            print("❌ Opción no válida")


if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrumpido por el usuario")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error fatal: {e}")
        sys.exit(1) 