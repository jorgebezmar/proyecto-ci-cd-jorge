pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "jorgebezmar/python-app:latest"
    }

    stages {

        stage('Clone') {
            steps {
                echo 'Clonando repositorio...'
                checkout scm
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas...'
                sh '''
                pip install flask pytest
                pytest
                '''
            }
        }

        stage('Build Image') {
            steps {
                echo 'Construyendo imagen Docker...'
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('DockerHub') {
            steps {
                echo 'Subiendo imagen a DockerHub...'
                sh '''
                docker login -u jorgeebzmar -p Jorge123@
                docker push $DOCKER_IMAGE
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Desplegando en Kubernetes...'
                sh '''
                kubectl apply -f deployment.yaml
                kubectl apply -f service.yaml
                '''
            }
        }

    }
}
