cat > .gitignore <<'EOF'
# Data folders (do NOT upload)
dataset/
dataset/*.csv
datasets/
Deep_Learning_Projects/datasets/
Digit_Recognition_using_ANN/datasets/

# Virtual envs
venv/
DLenv/

# Jupyter / caches / OS
.ipynb_checkpoints/
__pycache__/
.DS_Store

# Large model files
*.keras
*.h5
*.pb
EOF