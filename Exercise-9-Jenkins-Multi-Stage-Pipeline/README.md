\# Exercise 9: Jenkins Multi-Stage Pipeline for a Python Flask Application



\## Objective

To create and execute a Jenkins Pipeline that builds, tests, and deploys a sample Python Flask application.



\## Tools Used

\- Jenkins

\- Docker

\- Python

\- Flask

\- Git and GitHub



\## Application Files

The Python application is maintained in the GitHub repository `devops-sample-code`, inside the `python-flask-app` directory.



\- `app.py` — Flask application that returns a greeting.

\- `requirements.txt` — Lists Flask and compatible Werkzeug dependencies.

\- `test\_app.py` — Unit test for the application endpoint.

\- `Jenkinsfile` — Defines the multi-stage pipeline.



\## Pipeline Stages



\### 1. Build

Created a Python virtual environment and installed the dependencies listed in `requirements.txt`.



\### 2. Test

Executed the unit tests using Python's `unittest` framework to verify that the Flask application's home endpoint returns the expected response.



\### 3. Deploy

Copied `app.py` and `requirements.txt` into the `python-app-deploy` directory in the Jenkins workspace.



\## Execution

Configured the Jenkins job `Python-MultiStage-Pipeline` using Pipeline script from SCM. Jenkins retrieved the `Jenkinsfile` from the GitHub repository and executed the pipeline.



\## Result

The Build, Test, and Deploy stages completed successfully. The Jenkins pipeline finished with status `SUCCESS`.



\## Screenshots

The `screenshots` folder contains the Jenkins Console Output showing the successful pipeline execution.

