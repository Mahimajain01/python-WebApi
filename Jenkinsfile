pipeline {
    agent any
    environment {
        AZURE_CREDENTIALS = credentials('azure-service-principal')
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Mahimajain01/python-WebApi.git'
            }
        }
        stage('Build') {
            steps {
                bat 'echo Building on Windows'
            }
        }

        stage('Publish') {
            steps {
                bat 'zip -r app.zip .'
            }
        }
        stage('Deploy to Azure') {
            steps {
                withCredentials([azureServicePrincipal('azure-service-principal')]) {
                    bat 'az login --service-principal -u $AZURE_CREDENTIALS_USR -p $AZURE_CREDENTIALS_PSW --tenant $AZURE_CREDENTIALS_TEN'
                    bat 'az webapp up --name myPythonApp --resource-group myResourceGroup --runtime "PYTHON:3.9" --src-path .'
                }
            }
        }
    }
}
