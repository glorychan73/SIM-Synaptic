pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "sim-synaptic-ci"
        COMPOSE_FILE = "docker-compose.ci.yml"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Create .env') {
            steps {
                writeFile file: '.env', text: '''
POSTGRES_USER=glory
POSTGRES_PASSWORD=1234
POSTGRES_DB=sim_synaptic
DATABASE_URL=postgresql://glory:1234@db:5432/sim_synaptic
'''
            }
        }

        stage('Build') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Start Containers') {
            steps {
                sh 'docker compose down -v --remove-orphans || true'
                sh 'docker compose up -d'
            }
        }

        stage('Check Containers') {
            steps {
                sh 'docker compose ps'
                sh 'docker compose ps --status running'
            }
        }

        stage('Wait Database') {
            steps {
                sh 'sleep 10'
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
            sh 'docker compose down -v --remove-orphans || true'
            sh 'rm -f .env || true'
        }

        success {
            echo 'Pipeline exécuté avec succès.'
        }

        failure {
            echo 'Le pipeline a échoué.'
        }
    }
}
