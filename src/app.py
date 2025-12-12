import streamlit as st
import pandas as pd
import numpy as np
import joblib
import xgboost as xgb
import lightgbm as lgb
import shap
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, mean_absolute_percentage_error
import os

st.set_page_config(
    page_title="Crop Yield Prediction",
    page_icon="🌾",
    layout="wide"
)

@st.cache_resource
def load_models():
    models = {}
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_dir = os.path.join(current_dir, '..', 'models')
    
    if os.path.exists(f'{model_dir}/decision_tree.pkl'):
        models['Decision Tree'] = joblib.load(f'{model_dir}/decision_tree.pkl')
    
    if os.path.exists(f'{model_dir}/random_forest.pkl'):
        models['Random Forest'] = joblib.load(f'{model_dir}/random_forest.pkl')
    
    if os.path.exists(f'{model_dir}/xgboost_model.json'):
        xgb_model = xgb.XGBRegressor()
        xgb_model.load_model(f'{model_dir}/xgboost_model.json')
        models['XGBoost'] = xgb_model
    
    if os.path.exists(f'{model_dir}/lightgbm_model.txt'):
        lgb_model = lgb.Booster(model_file=f'{model_dir}/lightgbm_model.txt')
        models['LightGBM'] = lgb_model
    
    return models

@st.cache_data
def load_metrics():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    metrics_path = os.path.join(current_dir, '..', 'models', 'model_comparison.csv')
    if os.path.exists(metrics_path):
        return pd.read_csv(metrics_path)
    return None

def main():
    st.title("🌾 Crop Yield Prediction System")
    st.markdown("---")
    
    menu = st.sidebar.selectbox(
        "Navigation",
        ["🏠 Home", "📊 Upload & Preview", "🤖 Run Model", "🔍 Explainability", "💾 Download"]
    )
    
    if menu == "🏠 Home":
        show_home()
    elif menu == "📊 Upload & Preview":
        show_upload_preview()
    elif menu == "🤖 Run Model":
        show_run_model()
    elif menu == "🔍 Explainability":
        show_explainability()
    elif menu == "💾 Download":
        show_download()

def show_home():
    st.header("🏠 Project Description")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Prediksi Hasil Panen Pertanian
        
        Sistem Machine Learning untuk memprediksi hasil panen (Yield) berdasarkan berbagai faktor:
        
        **📌 Features:**
        - 🌱 Crop (Jenis Tanaman)
        - 🌍 Soil Type (Jenis Tanah)
        - ☁️ Weather Condition (Kondisi Cuaca)
        - 💧 Irrigation Used (Penggunaan Irigasi)
        - 🧪 Fertilizer Used (Penggunaan Pupuk)
        - 📊 Numerical Features (Suhu, Kelembaban, pH, dll)
        
        **🎯 Target:** Yield (Ton/Hektar)
        """)
    
    with col2:
        st.info("""
        **Dataset Info:**
        - 📁 800 samples
        - 📊 9 features
        - 🎯 1 target variable
        - ✅ Train/Test: 80/20
        """)
    
    st.markdown("---")
    
    st.subheader("📊 Dataset Information")
    
    # Get absolute path relative to this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(current_dir, '..', 'data', 'dataset_800.csv')
    
    if os.path.exists(dataset_path):
        df = pd.read_csv(dataset_path, sep=';', decimal=',')
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Samples", df.shape[0])
        col2.metric("Features", df.shape[1] - 1)
        col3.metric("Mean Yield", f"{df['Yield_tons_per_hectare'].mean():.2f}")
        col4.metric("Std Yield", f"{df['Yield_tons_per_hectare'].std():.2f}")
        
        st.dataframe(df.head(10), use_container_width=True)
    else:
        st.warning("Dataset tidak ditemukan!")
    
    st.markdown("---")
    
    st.subheader("🤖 Model Comparison")
    metrics_df = load_metrics()
    if metrics_df is not None:
        st.dataframe(metrics_df, use_container_width=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.barplot(data=metrics_df, x='R²', y='Model', palette='viridis', ax=ax)
            ax.set_title('Model Comparison: R² Score')
            st.pyplot(fig)
        
        with col2:
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.barplot(data=metrics_df, x='MAE', y='Model', palette='coolwarm', ax=ax)
            ax.set_title('Model Comparison: MAE')
            st.pyplot(fig)

def show_upload_preview():
    st.header("📊 Upload & Preview Data")
    
    uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file, sep=';', decimal=',')
            
            st.success(f"✅ Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")
            
            st.subheader("📋 Data Preview")
            st.dataframe(df.head(20), use_container_width=True)
            
            st.subheader("📊 Statistical Summary")
            st.dataframe(df.describe(), use_container_width=True)
            
            st.session_state['uploaded_data'] = df
            
        except Exception as e:
            st.error(f"Error loading file: {e}")
    else:
        st.info("Please upload a CSV file to preview")

def show_run_model():
    st.header("🤖 Run Model Prediction")
    
    models = load_models()
    
    if not models:
        st.error("No models found! Please train models first.")
        return
    
    model_name = st.selectbox("Select Model", list(models.keys()))
    
    if st.button("🚀 Run Prediction", type="primary"):
        with st.spinner("Running prediction..."):
            current_dir = os.path.dirname(os.path.abspath(__file__))
            test_data_path = os.path.join(current_dir, '..', 'data', 'X_test.csv')
            test_target_path = os.path.join(current_dir, '..', 'data', 'y_test.csv')
            
            if os.path.exists(test_data_path) and os.path.exists(test_target_path):
                X_test = pd.read_csv(test_data_path)
                y_test = pd.read_csv(test_target_path).values.ravel()
                
                model = models[model_name]
                
                if model_name == 'LightGBM':
                    y_pred = model.predict(X_test)
                else:
                    y_pred = model.predict(X_test)
                
                r2 = r2_score(y_test, y_pred)
                mae = mean_absolute_error(y_test, y_pred)
                rmse = np.sqrt(mean_squared_error(y_test, y_pred))
                mape = mean_absolute_percentage_error(y_test, y_pred) * 100
                
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("R² Score", f"{r2:.4f}")
                col2.metric("MAE", f"{mae:.4f}")
                col3.metric("RMSE", f"{rmse:.4f}")
                col4.metric("MAPE", f"{mape:.2f}%")
                
                st.subheader("📊 Actual vs Predicted")
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.scatter(y_test, y_pred, alpha=0.6)
                ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
                ax.set_xlabel('Actual Yield')
                ax.set_ylabel('Predicted Yield')
                ax.set_title(f'{model_name} - Actual vs Predicted')
                ax.grid(True, alpha=0.3)
                st.pyplot(fig)
                
                st.session_state['predictions'] = y_pred
                st.session_state['actual'] = y_test
                
            else:
                st.error("Test data not found!")

def show_explainability():
    st.header("🔍 Model Explainability (SHAP)")
    
    models = load_models()
    
    if not models:
        st.error("No models found!")
        return
    
    model_name = st.selectbox("Select Model for SHAP Analysis", list(models.keys()))
    
    if st.button("🔬 Generate SHAP Analysis", type="primary"):
        with st.spinner("Computing SHAP values..."):
            current_dir = os.path.dirname(os.path.abspath(__file__))
            train_data_path = os.path.join(current_dir, '..', 'data', 'X_train.csv')
            test_data_path = os.path.join(current_dir, '..', 'data', 'X_test.csv')
            
            if os.path.exists(train_data_path) and os.path.exists(test_data_path):
                X_train = pd.read_csv(train_data_path).astype(float)
                X_test = pd.read_csv(test_data_path).astype(float)
                
                model = models[model_name]
                
                explainer = shap.Explainer(model, X_train)
                shap_values = explainer(X_test)
                
                st.success("✅ SHAP values computed!")
                
                st.subheader("📊 SHAP Summary Plot")
                fig, ax = plt.subplots(figsize=(12, 8))
                shap.summary_plot(shap_values, X_test, show=False)
                plt.title(f'SHAP Summary Plot - {model_name}', fontsize=16, pad=20)
                st.pyplot(fig)
                
                st.subheader("📈 Feature Importance")
                feature_importance = pd.DataFrame({
                    'feature': X_train.columns,
                    'importance': np.abs(shap_values.values).mean(axis=0)
                }).sort_values('importance', ascending=False)
                
                fig, ax = plt.subplots(figsize=(10, 6))
                top_10 = feature_importance.head(10)
                sns.barplot(data=top_10, x='importance', y='feature', palette='viridis', ax=ax)
                ax.set_title(f'Top 10 Feature Importance - {model_name}')
                ax.set_xlabel('Mean |SHAP value|')
                st.pyplot(fig)
                
                st.dataframe(feature_importance.head(10), use_container_width=True)
                
            else:
                st.error("Training/Test data not found!")

def show_download():
    st.header("💾 Download Predictions")
    
    if 'predictions' in st.session_state and 'actual' in st.session_state:
        results_df = pd.DataFrame({
            'Actual': st.session_state['actual'],
            'Predicted': st.session_state['predictions'],
            'Error': st.session_state['actual'] - st.session_state['predictions']
        })
        
        st.dataframe(results_df, use_container_width=True)
        
        csv = results_df.to_csv(index=False)
        st.download_button(
            label="📥 Download Predictions CSV",
            data=csv,
            file_name="predictions.csv",
            mime="text/csv"
        )
    else:
        st.info("No predictions available. Please run a model first!")
    
    st.markdown("---")
    
    st.subheader("📦 Download Trained Models")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_files = {
        'Decision Tree': os.path.join(current_dir, '..', 'models', 'decision_tree.pkl'),
        'Random Forest': os.path.join(current_dir, '..', 'models', 'random_forest.pkl'),
        'XGBoost': os.path.join(current_dir, '..', 'models', 'xgboost_model.json'),
        'LightGBM': os.path.join(current_dir, '..', 'models', 'lightgbm_model.txt')
    }
    
    for name, path in model_files.items():
        if os.path.exists(path):
            with open(path, 'rb') as f:
                st.download_button(
                    label=f"📥 Download {name} Model",
                    data=f,
                    file_name=os.path.basename(path),
                    mime="application/octet-stream"
                )

if __name__ == "__main__":
    main()
