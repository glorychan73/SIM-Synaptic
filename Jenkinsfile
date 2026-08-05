pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "sim-synaptic-pipeline"
    }

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

        stage('Start Containers') {
            steps {
                sh 'docker compose up -d'
            }
        }

        stage('Tests') {
            steps {
                sh 'docker compose exec -T api pytest'
            }
        }

        stage('Lint') {
            steps {
                sh 'docker compose exec -T api flake8 app tests'
            }
        }
    }

    post {

        always {
            sh 'docker compose down'
        }

        success {
            echo 'Pipeline exécuté avec succès.'
        }

        failure {
            echo 'Le pipeline a échoué.'
        }
    }
}
