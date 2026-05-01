# DeployMLModel
an end-to-end ML deployment project

# Criar ambiente
python -m venv venv
# Ativar (Windows)
venv\Scripts\activate
# Ativar (Linux/Mac)
source venv/bin/activate
# Depois instalar as dependências
pip install -r requirements.txt

# Criar imagem no Docker:
docker build -t imagem_nome .
# Verificar:
docker images
# Run Docker Container:
docker run -p 8000:8000 imagem_nome

# Run Streamlit:
streamlit run client.py
