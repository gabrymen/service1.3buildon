# Usa una immagine base di Python
FROM python:3.10-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia il file requirements.txt nella directory di lavoro
COPY requirements.txt .

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto dell'applicazione nella directory di lavoro
COPY . .

# Imposta le variabili d'ambiente
ENV FLASK_APP=run.py
ENV FLASK_ENV=development

# Espone la porta che Flask utilizza
EXPOSE 5000

# Comando per eseguire l'applicazione
CMD ["flask", "run", "--host=0.0.0.0"]
