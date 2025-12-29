#!/bin/bash
echo "========================================"
echo " Crop Yield Prediction System"
echo " Starting Application..."
echo "========================================"

# Memastikan folder venv ada
if [ ! -d ".venv" ]; then
    echo "ERROR: Virtual environment not found. Please run ./install.sh first."
    exit 1
fi

# Mengaktifkan venv
source .venv/bin/activate

echo "Checking if packages are installed..."
python -c "import streamlit" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "ERROR: Streamlit is not installed!"
    exit 1
fi

echo "Starting Streamlit server..."
echo "URL: http://localhost:8501"
echo "Press Ctrl+C to stop."

# FIX: Menambahkan direktori saat ini ke PYTHONPATH agar folder 'models' terbaca
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Menjalankan aplikasi dari root directory
streamlit run src/app.py
