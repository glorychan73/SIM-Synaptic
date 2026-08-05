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
                sh 'docker compose build'
            }
        }

        stage('Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Lint') {
            steps {
                sh 'flake8 .'
            }
        }
    }
}
