**Service 1.3 BuildOn**

Questo progetto è un servizio di clustering di machine learning basato su Flask. Fornisce API per preprocessare i dati e eseguire clustering sui dati preprocessati.

**Struttura del Progetto**

La struttura del progetto è organizzata come segue:
```
service1.3/
│
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── main_routes.py
│   │   ├── api_routes.py
│   ├── preprocess.py
│   ├── clustering.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── cluster_model.pkl
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── helpers.py
│   ├── logging.py
│   ├── static/
│   │   ├── swagger.yaml
│
├── tests/
│   ├── __init__.py
│   ├── test_routes.py
│   ├── test_apis.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── example_input.json
│
├── notebooks/
│   ├── exploratory_analysis.ipynb
│   ├── model_training.ipynb
│
├── .gitignore
├── README.md
├── requirements.txt
├── config.py
├── run.py
├── setup.py
├── start.sh
├── Dockerfile
├── docker-compose.yml

```


**Descrizione delle directory e dei file**

- `app/`: Contiene il codice principale dell'applicazione Flask.
  - `__init__.py`: Inizializza l'app Flask e carica la configurazione.
  - `routes/`: Contiene i file di routing per definire le API.
    - `__init__.py`: Inizializza il modulo `routes`.
    - `main_routes.py`: Definisce le principali route dell'API.
    - `api_routes.py`: File placeholder per eventuali API aggiuntive.
  - `static/`: Cartella contenente file di configurazione di Swagger.
    - `swagger.yaml`: Configurazione per la documentazione delle API con Swagger.
  - `preprocess.py`: Contiene la logica per preprocessare i dati.
  - `clustering.py`: Contiene la logica per il clustering dei dati.
  - `models/`: Contiene i modelli di machine learning.
    - `__init__.py`: Inizializza il modulo `models`.
    - `cluster_model.pkl`: Modello di clustering pre-addestrato.
  - `utils/`: Contiene funzioni di utilità.
    - `__init__.py`: Inizializza il modulo `utils`.
    - `helpers.py`: Contiene funzioni di aiuto generiche.
  - `logging.py`: Configurazione e inizializzazione del logging.

- `tests/`: Contiene i test unitari per l'applicazione.
  - `__init__.py`: Inizializza il modulo `tests`.
  - `test_routes.py`: Test per le route dell'API.
  - `test_apis.py`: Test per le API principali.

- `data/`: Contiene i dati utilizzati dall'applicazione.
  - `raw/`: Dati grezzi.
  - `processed/`: Dati preprocessati.
  - `example_input.json`: Esempio di input JSON per l'API.

- `notebooks/`: Contiene i notebook Jupyter per l'analisi e l'addestramento del modello.
  - `exploratory_analysis.ipynb`: Analisi esplorativa dei dati.
  - `model_training.ipynb`: Addestramento del modello di clustering.

- `.gitignore`: File per escludere file e directory dal controllo di versione.
- `README.md`: Questo file. Contiene la descrizione del progetto e la struttura.
- `requirements.txt`: Elenco delle dipendenze del progetto.
- `config.py`: File di configurazione per l'applicazione Flask.
- `run.py`: Script per eseguire l'app Flask.
- `setup.py`: Script di setup per il progetto.
- `start.sh`: Script di avvio per configurare l'ambiente e avviare l'applicazione.
- `Dockerfile`: Definizione dell'immagine Docker per il progetto.
- `docker-compose.yml`: Definizione dei servizi Docker per il progetto.

**Configurazione dell'Ambiente**

Prerequisiti

Assicurati di avere Python 3.6+ e pip installati.

Creazione di un Ambiente Virtuale

Crea e attiva un ambiente virtuale:
```
python3 -m venv venv
source venv/bin/activate  # Su Windows: venv\Scripts\activate
```
Installazione delle Dipendenze

Installa le dipendenze utilizzando pip e il file setup.py:
```
pip install .
```
**Configurazione delle Variabili d'Ambiente**

Crea un file .env nella directory principale del progetto e aggiungi le seguenti variabili d'ambiente:

```
SECRET_KEY=mysecretkey
FLASK_ENV=development
PYTHONPATH=/path/to/your/project/service1.3
DATABASE_URL=sqlite:///app.db
```
**Esecuzione dell'Applicazione**

Avvia l'applicazione Flask:
```
python run.py
```
L'applicazione sarà disponibile su http://127.0.0.1:5000/.

**Utilizzo di Docker**
Costruzione e Avvio dei Contenitori Docker
Costruisci l'immagine Docker e avvia il contenitore in modalità detached (in background):
```
docker-compose build
```
```
docker-compose up -d
```
Verifica lo stato dei servizi:

```
docker-compose ps
```
Visualizza i log del contenitore in esecuzione:

```
docker-compose logs -f
```
Accedi alla shell del contenitore (se necessario):

```
docker-compose exec web /bin/bash
```

Ferma e rimuovi i contenitori, le reti e i volumi creati da docker-compose:

```
docker-compose down

```
Accedi a Docker Hub

```
docker login

```
Costruisci l'immagine Docker (se non lo hai già fatto)

```
docker-compose build
```
Tagga l'immagine Docker

```
docker tag service1.3_app:latest myusername/myapp:latest
```
Pusha l'immagine Docker su Docker Hub

```
docker push myusername/myapp:latest
```
**API**

Documentazione Swagger

La documentazione delle API è disponibile su http://127.0.0.1:5000/swagger.

Endpoint

- GET /: Endpoint principale per verificare che l'applicazione sia in esecuzione.
- POST /api/preprocess: Preprocessa i dati di input.
- POST /api/cluster: Esegue il clustering sui dati preprocessati.

Testing

Esegui i test utilizzando unittest:
```
./start.sh

```
oppure
```
python3 tests/test_routes.py

```
**Contribuire**

Contribuisci al progetto aprendo issue o inviando pull request. Ogni contributo è benvenuto!

**Licenza**

Questo progetto è rilasciato sotto la licenza MIT. Vedi il file LICENSE per maggiori dettagli.
