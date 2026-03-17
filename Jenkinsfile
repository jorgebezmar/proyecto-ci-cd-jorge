pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "jorgebezmar/python-app:latest"
    }

    stages {
        stage('Test') {
            steps {
                echo 'Ejecutando pruebas...'
                sh '''
                pip install --break-system-packages flask pytest
                pytest test_app.py
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
                echo "Jorge123@" | docker login -u jorgebezmar --password-stdin
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
