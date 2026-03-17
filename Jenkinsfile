pipeline {
    agent any

    environment {
        // Corregido: jorgebezmar (según tus otros archivos) en lugar de jorgeebzmar
        DOCKER_IMAGE = "jorgebezmar/python-app:latest"
    }

    stages {
        // Eliminamos la etapa 'Clone' porque Jenkins hace el checkout automático al inicio [cite: 2, 3]

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas...'
                // Usamos el flag --break-system-packages para evitar el error de PEP 668 
                sh '''
                pip install --break-system-packages flask pytest
                pytest test_app.py
                '''
            }
        }

        stage('Build Image') {
            steps {
                echo 'Construyendo imagen Docker...'
                sh 'docker build -t $DOCKER_IMAGE .' [cite: 5]
            }
        }

        stage('DockerHub') {
            steps {
                echo 'Subiendo imagen a DockerHub...'
                // Nota: Por seguridad, lo ideal es usar Credentials de Jenkins, 
                // pero he mantenido tu lógica corrigiendo el usuario 
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
                ''' [cite: 7]
            }
        }
    }
}
