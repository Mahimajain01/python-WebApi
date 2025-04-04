pipeline {
    agent any

    environment {
        AZURE_CREDENTIALS_ID = 'azure-credentials' // Jenkins Azure credentials ID
        RESOURCE_GROUP = 'rg-py-jenkins'
        APP_SERVICE_PLAN = 'app-service-py'
        WEB_APP_NAME = 'webApp-py'
        LOCATION = 'eastus'
        RUNTIME_STACK = 'PYTHON|3.9'
    }

    stages {
        stage('Login to Azure') {
            steps {
                withAzure(credentialsId: AZURE_CREDENTIALS_ID) {
                    bat 'az login --service-principal -u %AZURE_CLIENT_ID% -p %AZURE_CLIENT_SECRET% --tenant %AZURE_TENANT_ID%'
                }
            }
        }

        stage('Create Resource Group') {
            steps {
                bat 'az group create --name %RESOURCE_GROUP% --location %LOCATION%'
            }
        }

        stage('Create App Service Plan') {
            steps {
                bat 'az appservice plan create --name %APP_SERVICE_PLAN% --resource-group %RESOURCE_GROUP% --sku F1 --is-linux'
            }
        }

        stage('Create Web App') {
            steps {
                bat 'az webapp create --resource-group %RESOURCE_GROUP% --plan %APP_SERVICE_PLAN% --name %WEB_APP_NAME% --runtime "%RUNTIME_STACK%"'
            }
        }

        stage('Deploy App to Azure') {
            steps {
                bat 'az webapp deployment source config-zip --resource-group %RESOURCE_GROUP% --name %WEB_APP_NAME% --src my-app.zip'
            }
        }
    }
}
