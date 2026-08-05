pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh '''
                    docker compose build
                '''
            }
        }

        stage('Tests') {
            steps {
                sh '''
                    source /opt/jenkins-venv/bin/activate
                    pytest
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    source /opt/jenkins-venv/bin/activate
                    flake8 .
                '''
            }
        }

    }
}
