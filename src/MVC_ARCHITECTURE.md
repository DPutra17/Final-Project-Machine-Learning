# MVC Architecture - Crop Yield Prediction System

## 📁 Project Structure

```
src/
├── app.py                          # Original monolithic app (legacy)
├── app_mvc.py                      # New MVC-based entry point
│
├── config/                         # Configuration
│   └── settings.py                 # App settings and constants
│
├── models/                         # Model Layer (Data & Business Logic)
│   ├── model_loader.py             # ML model loading utilities
│   └── data_loader.py              # Dataset loading utilities
│
├── views/                          # View Layer (UI Pages)
│   ├── __init__.py
│   ├── home.py                     # Home page view
│   ├── single_prediction.py        # Single prediction view (TODO)
│   ├── model_performance.py        # Model performance view (TODO)
│   ├── shap_analysis.py            # SHAP analysis view (TODO)
│   ├── data_visualization.py       # Data visualization view (TODO)
│   ├── batch_prediction.py         # Batch prediction view (TODO)
│   └── model_comparison.py         # Model comparison view (TODO)
│
├── components/                     # Reusable UI Components
│   ├── sidebar.py                  # Sidebar component
│   └── cards.py                    # Card components
│
└── utils/                          # Helper Utilities
    ├── styling.py                  # CSS styling utilities
    └── helpers.py                  # Helper functions
```

## 🏗️ Architecture Overview

### Model Layer (`models/`)
**Responsibility:** Data access and business logic
- Load ML models (Decision Tree, Random Forest, XGBoost, LightGBM)
- Load datasets (training, testing, original)
- Load encoders for categorical features
- Handle predictions
- Calculate metrics

### View Layer (`views/`)
**Responsibility:** User interface and presentation
- Render pages and UI components
- Display data visualizations
- Handle user interactions
- Call model layer for data
- Use components for reusable UI elements

### Components (`components/`)
**Responsibility:** Reusable UI elements
- Sidebar navigation
- Card components
- Buttons and badges
- Info boxes
- Loading indicators

### Configuration (`config/`)
**Responsibility:** Application settings
- Paths configuration
- Color schemes
- Feature names
- Page definitions
- App constants

### Utilities (`utils/`)
**Responsibility:** Helper functions
- CSS styling
- Data formatting
- Validation
- Metric calculations
- Feature encoding

## 🚀 Usage

### Run the MVC version:
```bash
streamlit run src/app_mvc.py
```

### Run the original version:
```bash
streamlit run src/app.py
```

## 🔄 Migration Status

✅ **Completed:**
- Core architecture setup
- Configuration management
- Model layer (model_loader, data_loader)
- Component layer (sidebar, cards)
- Utilities (styling, helpers)
- Home view (fully functional)

🚧 **In Progress:**
- Single Prediction view
- Model Performance view
- SHAP Analysis view
- Data Visualization view
- Batch Prediction view
- Model Comparison view

## 📝 How to Add a New Page

1. **Create a view file** in `views/` folder:
```python
# views/my_page.py
import streamlit as st

def render():
    """Render my page"""
    st.header("My New Page")
    # Your page content here
```

2. **Import the view** in `views/__init__.py`:
```python
from . import home, my_page

__all__ = ['home', 'my_page']
```

3. **Add route** in `app_mvc.py`:
```python
from views import home, my_page

# In main() function:
elif selected_page == "My Page":
    my_page.render()
```

4. **Add page config** in `config/settings.py`:
```python
PAGES = {
    'home': '🏠 Home',
    'my_page': '📄 My Page',
    # ...
}
```

## 🎨 Component Usage Examples

### Using Card Component:
```python
from components.cards import gradient_card, feature_card

# Gradient card
gradient_card("Title", "Description", "🎯", ['#667eea', '#764ba2'])

# Feature card with button
if feature_card("🔮", "Title", "Description", "Click Me", "btn_key"):
    st.success("Button clicked!")
```

### Using Model Loader:
```python
from models.model_loader import load_models, predict

models = load_models()
model = models['XGBoost']
prediction = predict(model, 'XGBoost', features_df)
```

### Using Data Loader:
```python
from models.data_loader import load_dataset, load_metrics

df = load_dataset()
metrics = load_metrics()
```

## 🎯 Benefits of MVC Architecture

1. **Separation of Concerns:** Clear separation between data, logic, and presentation
2. **Reusability:** Components can be reused across different pages
3. **Maintainability:** Easier to maintain and debug
4. **Scalability:** Easy to add new features and pages
5. **Testing:** Easier to write unit tests for individual components
6. **Collaboration:** Multiple developers can work on different parts
7. **Code Organization:** Cleaner and more organized codebase

## 📚 Best Practices

1. **Keep views simple:** Views should only handle presentation
2. **Business logic in models:** All data processing should be in model layer
3. **Reuse components:** Create components for repeated UI elements
4. **Configuration centralized:** All settings in config/settings.py
5. **Error handling:** Always use try-except blocks
6. **Documentation:** Add docstrings to all functions
7. **Type hints:** Use type hints for better code clarity

## 🔗 Related Files

- Original app: `src/app.py`
- New MVC app: `src/app_mvc.py`
- Configuration: `src/config/settings.py`
- Models: `src/models/`
- Views: `src/views/`
- Components: `src/components/`
- Utils: `src/utils/`
