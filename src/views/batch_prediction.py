"""
Batch Prediction View
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from models.model_loader import load_models
from models.data_loader import load_train_test_data


def render():
    """Render batch prediction page"""
    st.header("🤖 Batch Prediction")
    st.markdown("Upload a CSV file to predict yields for multiple samples")
    st.markdown("---")
    
    models = load_models()
    
    if not models:
        st.error("⚠️ No models found!")
        return
    
    st.info("📋 **Required columns:** Soil_Type, Crop, Rainfall_mm, Temperature_Celsius, Fertilizer_Used, Irrigation_Used, Weather_Condition, Days_to_Harvest")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        uploaded_file = st.file_uploader("📁 Upload CSV File", type=['csv'])
    
    with col2:
        selected_model = st.selectbox("🤖 Select Model", list(models.keys()))
    
    if uploaded_file is not None:
        _process_uploaded_file(uploaded_file, selected_model, models)
    else:
        _show_sample_format()


def _process_uploaded_file(uploaded_file, selected_model, models):
    """Process uploaded CSV file"""
    try:
        # Try different separators
        try:
            df_input = pd.read_csv(uploaded_file, sep=';', decimal=',')
        except:
            df_input = pd.read_csv(uploaded_file)
        
        st.success(f"✅ File loaded: {df_input.shape[0]} rows, {df_input.shape[1]} columns")
        
        st.subheader("📋 Preview Uploaded Data")
        st.dataframe(df_input.head(10), use_container_width=True)
        
        if st.button("🚀 Run Batch Prediction", type="primary"):
            with st.spinner("🔄 Processing predictions..."):
                try:
                    # Load training columns template for one-hot alignment
                    train_data = load_train_test_data()
                    train_columns = train_data['X_train'].columns.tolist()
                    
                    # Prepare features with one-hot encoding
                    df_processed = df_input.copy()
                    
                    # Convert boolean columns to int first
                    if 'Fertilizer_Used' in df_processed.columns:
                        df_processed['Fertilizer_Used'] = df_processed['Fertilizer_Used'].astype(int)
                    if 'Irrigation_Used' in df_processed.columns:
                        df_processed['Irrigation_Used'] = df_processed['Irrigation_Used'].astype(int)
                    
                    # One-hot encode categorical columns
                    categorical_cols = [col for col in ['Soil_Type', 'Crop', 'Weather_Condition'] 
                                      if col in df_processed.columns]
                    
                    if categorical_cols:
                        df_processed = pd.get_dummies(df_processed, columns=categorical_cols, drop_first=True)
                    
                    # Align to training columns
                    for col in train_columns:
                        if col not in df_processed.columns:
                            df_processed[col] = 0
                    
                    # Keep only training columns in correct order
                    df_processed = df_processed[train_columns]
                    
                    # Make predictions
                    model = models[selected_model]
                    predictions = model.predict(df_processed)
                    
                    # Add predictions to original dataframe
                    df_results = df_input.copy()
                    df_results['Predicted_Yield'] = predictions
                    
                    st.success("✅ Predictions completed!")
                    
                    # Display results
                    st.subheader("📊 Prediction Results")
                    st.dataframe(df_results, use_container_width=True)
                    
                    # Statistics
                    col1, col2, col3, col4 = st.columns(4)
                    col1.metric("Total Predictions", len(predictions))
                    col2.metric("Avg Predicted Yield", f"{predictions.mean():.2f}")
                    col3.metric("Max Predicted Yield", f"{predictions.max():.2f}")
                    col4.metric("Min Predicted Yield", f"{predictions.min():.2f}")
                    
                    # Visualization
                    fig = go.Figure()
                    fig.add_trace(go.Histogram(
                        x=predictions,
                        nbinsx=30,
                        marker_color='#667eea',
                        marker_line=dict(color='#764ba2', width=1)
                    ))
                    fig.update_layout(
                        title='Distribution of Predicted Yields',
                        xaxis_title='Predicted Yield (tons/ha)',
                        yaxis_title='Frequency',
                        height=400,
                        plot_bgcolor='#0f172a',
                        paper_bgcolor='#0f172a',
                        font=dict(color='#e5e7eb', family='Inter'),
                        xaxis=dict(gridcolor='#1f2937'),
                        yaxis=dict(gridcolor='#1f2937')
                    )
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Download results
                    csv = df_results.to_csv(index=False)
                    st.download_button(
                        label="📥 Download Predictions",
                        data=csv,
                        file_name=f"batch_predictions_{selected_model}.csv",
                        mime="text/csv",
                        type="primary"
                    )
                    
                except Exception as e:
                    st.error(f"❌ Prediction error: {str(e)}")
                    st.exception(e)
    
    except Exception as e:
        st.error(f"❌ Error loading file: {str(e)}")
        st.exception(e)


def _show_sample_format():
    """Show sample file format"""
    st.markdown("### 📄 Sample File Format")
    sample_data = {
        'Soil_Type': ['Sandy', 'Clay', 'Loam'],
        'Crop': ['Rice', 'Wheat', 'Cotton'],
        'Rainfall_mm': [1000.0, 850.5, 920.3],
        'Temperature_Celsius': [25.5, 22.0, 28.3],
        'Fertilizer_Used': [True, False, True],
        'Irrigation_Used': [True, True, False],
        'Weather_Condition': ['Rainy', 'Sunny', 'Cloudy'],
        'Days_to_Harvest': [120, 110, 130]
    }
    sample_df = pd.DataFrame(sample_data)
    st.dataframe(sample_df, use_container_width=True)
    
    csv_sample = sample_df.to_csv(index=False)
    st.download_button(
        label="📥 Download Sample Template",
        data=csv_sample,
        file_name="sample_batch_input.csv",
        mime="text/csv"
    )
