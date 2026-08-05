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
                sh 'docker compose -f ${COMPOSE_FILE} build'
            }
        }

        stage('Start Containers') {
            steps {
                sh '''
                docker compose -f ${COMPOSE_FILE} down -v || true
                docker compose -f ${COMPOSE_FILE} up -d
                '''
            }
        }

        stage('Wait Database') {
            steps {
                sh 'sleep 10'
            }
        }

        stage('Tests') {
            steps {
                sh 'docker compose -f ${COMPOSE_FILE} exec -T api pytest'
            }
        }

        stage('Lint') {
            steps {
                sh 'docker compose -f ${COMPOSE_FILE} exec -T api flake8 app tests'
            }
        }
    }

    post {
        always {
            sh 'docker compose -f ${COMPOSE_FILE} down -v'
        }

        success {
            echo 'Pipeline exécuté avec succès.'
        }

        failure {
            echo 'Le pipeline a échoué.'
        }
    }
}
