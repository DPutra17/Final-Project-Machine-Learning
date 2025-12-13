"""
Sidebar component
"""
import streamlit as st
from datetime import datetime
from models.model_loader import load_models
from models.data_loader import get_best_model
from config.settings import PAGES


def render_sidebar():
    """Render the enhanced sidebar with navigation"""
    
    # Logo and branding
    st.sidebar.markdown("""
    <div style='text-align: center; padding: 1.4rem 0; border: 1px solid rgba(255,255,255,0.06);
                border-radius: 16px; background: rgba(255,255,255,0.04);
                backdrop-filter: blur(12px); box-shadow: 0 16px 40px rgba(0,0,0,0.25);'>
        <h1 style='color: #93c5fd; margin: 0; font-size: 2.4rem;'>🌾</h1>
        <h2 style='background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 100%);
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                   margin: 0.35rem 0; font-size: 1.4rem; font-weight: 800;'>CropYield AI</h2>
        <p style='color: #cbd5e1; font-size: 0.92rem; margin: 0;'>Production ML Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.sidebar.markdown("---")
    
    # Navigation
    page_list = list(PAGES.values())
    
    # Check if navigation button was clicked from home page
    if 'selected_page' in st.session_state:
        default_page = st.session_state['selected_page']
    else:
        default_page = PAGES['home']
    
    default_index = page_list.index(default_page) if default_page in page_list else 0
    
    selected_page = st.sidebar.radio(
        "Select Page:",
        page_list,
        index=default_index,
        label_visibility="collapsed",
        key="sidebar_navigation"
    )
    
    # Update selected page in session state
    st.session_state['selected_page'] = selected_page
    
    # System status
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 System Status")
    
    models = load_models()
    
    if models:
        st.sidebar.markdown(f"""
        <div style='background: linear-gradient(135deg, rgba(16,185,129,0.18) 0%, rgba(16,185,129,0.08) 100%);
                padding: 1rem; border-radius: 14px; margin: 0.5rem 0;
                border: 1px solid rgba(16,185,129,0.35); backdrop-filter: blur(10px);
                color: #ecfdf3; box-shadow: 0 12px 32px rgba(16,185,129,0.18);'>
            <div style='font-size: 1.4rem; text-align: center;'>✓</div>
            <div style='text-align: center; font-weight: 700;'>System Ready</div>
            <div style='text-align: center; font-size: 0.92rem;'>{len(models)} Models Active</div>
        </div>
        """, unsafe_allow_html=True)
        
        best_model = get_best_model()
        if best_model:
            st.sidebar.markdown(f"""
            <div style='background: linear-gradient(135deg, rgba(245,158,11,0.2) 0%, rgba(245,158,11,0.08) 100%);
                        padding: 0.85rem; border-radius: 14px; margin: 0.5rem 0;
                        border: 1px solid rgba(245,158,11,0.35); backdrop-filter: blur(10px);
                        color: #fef3c7;'>
                <div style='font-size: 0.85rem;'>Best Model</div>
                <div style='font-weight: 700; font-size: 1.05rem;'>🏆 {best_model}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.sidebar.markdown("""
        <div style='background: linear-gradient(135deg, rgba(239,68,68,0.18) 0%, rgba(239,68,68,0.08) 100%);
                    padding: 1rem; border-radius: 14px; margin: 0.5rem 0;
                    border: 1px solid rgba(239,68,68,0.35); backdrop-filter: blur(10px);
                    color: #fee2e2;'>
            <div style='font-size: 1.4rem; text-align: center;'>⚠</div>
            <div style='text-align: center; font-weight: 700;'>No Models Loaded</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.sidebar.markdown("---")
    
    # Footer
    st.sidebar.markdown(f"""
    <div style='text-align: center; padding: 1rem 0; color: #cbd5e1;'>
        <div style='font-size: 0.9rem; margin-bottom: 0.5rem; color: #e5e7eb;'>👥 <strong>ML Team</strong></div>
        <div style='font-size: 0.82rem;'>📅 Updated: {datetime.now().strftime('%Y-%m-%d')}</div>
        <div style='margin-top: 1rem;'>
            <a href='https://github.com' target='_blank' style='color: #a5b4fc; text-decoration: none; margin: 0 0.5rem; font-weight: 600;'>📚 Docs</a>
            <a href='https://github.com' target='_blank' style='color: #a5b4fc; text-decoration: none; margin: 0 0.5rem; font-weight: 600;'>💻 GitHub</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    return selected_page
