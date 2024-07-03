**Service 1.3 BuildOn**

This project is a machine learning clustering service based on Flask. It provides APIs to preprocess data and perform clustering on the preprocessed data.

**Project Structure**

The project structure is organized as follows:


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


**Directory and File Descriptio**
    • app/: Contains the main Flask application code.
        ◦ __init__.py: Initializes the Flask app and loads the configuration.
        ◦ routes/: Contains routing files to define the APIs.
            ▪ __init__.py: Initializes the routes module.
            ▪ main_routes.py: Defines the main API routes.
            ▪ api_routes.py: Placeholder file for additional APIs.
        ◦ static/: Folder containing Swagger configuration files.
            ▪ swagger.yaml: Configuration for API documentation with Swagger.
        ◦ preprocess.py: Contains the logic for data preprocessing.
        ◦ clustering.py: Contains the logic for data clustering.
        ◦ models/: Contains machine learning models.
            ▪ __init__.py: Initializes the models module.
            ▪ cluster_model.pkl: Pre-trained clustering model.
        ◦ utils/: Contains utility functions.
            ▪ __init__.py: Initializes the utils module.
            ▪ helpers.py: Contains generic helper functions.
        ◦ logging.py: Logging configuration and initialization.
    • tests/: Contains unit tests for the application.
        ◦ __init__.py: Initializes the tests module.
        ◦ test_routes.py: Tests for the API routes.
        ◦ test_apis.py: Tests for the main APIs.
    • data/: Contains data used by the application.
        ◦ raw/: Raw data.
        ◦ processed/: Preprocessed data.
        ◦ example_input.json: Example JSON input for the API.
    • notebooks/: Contains Jupyter notebooks for analysis and model training.
        ◦ exploratory_analysis.ipynb: Data exploratory analysis.
        ◦ model_training.ipynb: Clustering model training.
    • .gitignore: File to exclude files and directories from version control.
    • README.md: This file. Contains the project description and structure.
    • requirements.txt: List of project dependencies.
    • config.py: Configuration file for the Flask application.
    • run.py: Script to run the Flask app.
    • setup.py: Setup script for the project.
    • start.sh: Startup script to set up the environment and start the application.
    • Dockerfile: Docker image definition for the project.
    • docker-compose.yml: Docker services definition for the project.

**Environment Setup**

Prerequisites

Make sure you have Python 3.6+ and pip installed.

Creating a Virtual Environment

Create and activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate  # Su Windows: venv\Scripts\activate
```
Installing Dependencies

Install dependencies using pip and the setup.py file:

```
pip install .
```
**Configuring Environment Variables**

Create a .env file in the main project directory and add the following environment variables:

```
SECRET_KEY=mysecretkey
FLASK_ENV=development
PYTHONPATH=/path/to/your/project/service1.3
DATABASE_URL=sqlite:///app.db
```
**Running the Application**

Start the Flask application:

```
python run.py
```
The application will be available at http://127.0.0.1:5000/.


**Using Docker**
Building and Starting Docker Containers

Build the Docker image and start the container in detached mode (in the background):

```
docker-compose up -d
```
Check the status of the services:

```
docker-compose ps
```
View the logs of the running container:

```
docker-compose logs -f
```
Access the container shell (if necessary):

```
docker-compose exec web /bin/bash
```

Stop and remove the containers, networks, and volumes created by docker-compose:
```
docker-compose down
```
**API**

Swagger Documentation

The API documentation is available at http://127.0.0.1:5000/swagger.

Endpoints

GET /: Main endpoint to check if the application is running.
POST /api/preprocess: Preprocesses the input data.
POST /api/cluster: Performs clustering on the preprocessed data.
Testing

Run tests using unittest:

```
./start.sh

```
or

```
python3 tests/test_routes.py

```
**Contributing**

Contribute to the project by opening issues or submitting pull requests. All contributions are welcome!


**License**

This project is released under the MIT license. See the LICENSE file for more details.