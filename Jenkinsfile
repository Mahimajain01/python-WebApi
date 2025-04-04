pipeline {
    agent any
    environment {
        AZURE_CREDENTIALS = credentials('azure-service-principal')
        SHELL = 'C:\Program Files\Git\usr\bin\sh.exe'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Mahimajain01/python-WebApi.git'
            }
        }
        stage('Build') {
            steps {
                sh 'echo Building on Windows'
            }
        }

        stage('Publish') {
            steps {
                sh 'zip -r app.zip .'
            }
        }
        stage('Deploy to Azure') {
            steps {
                withCredentials([azureServicePrincipal('azure-service-principal')]) {
                    sh 'az login --service-principal -u $AZURE_CREDENTIALS_USR -p $AZURE_CREDENTIALS_PSW --tenant $AZURE_CREDENTIALS_TEN'
                    sh 'az webapp up --name myPythonApp --resource-group myResourceGroup --runtime "PYTHON:3.9" --src-path .'
                }
            }
        }
    }
}
