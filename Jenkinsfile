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

        stage('Tests') {
            steps {
                sh 'docker compose run --rm api pytest'
            }
        }

        stage('Lint') {
            steps {
                sh 'docker compose run --rm api flake8 .'
            }
        }

    }

    post {

        always {
            sh 'docker compose down || true'
        }

        success {
            echo '✅ Pipeline terminée avec succès.'
        }

        failure {
            echo '❌ Pipeline échouée.'
        }
    }
}
