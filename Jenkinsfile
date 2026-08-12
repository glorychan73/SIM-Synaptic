pipeline {

    agent any

    environment {
        COMPOSE_PROJECT_NAME = "sim-ci-${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Generate .env') {
            steps {
                sh '''
                    echo "Génération du fichier .env"

                    cat > .env <<EOF
POSTGRES_USER=glory
POSTGRES_PASSWORD=1234
POSTGRES_DB=sim_synaptic
DATABASE_URL=postgresql://glory:1234@db:5432/sim_synaptic
EOF
                '''
            }
        }

        stage('Build Docker') {
            steps {
                sh '''
                    docker compose \
                      -p ${COMPOSE_PROJECT_NAME} \
                      -f docker-compose.ci.yml \
                      build
                '''
            }
        }

        stage('Start CI') {
            steps {
                sh '''
                    docker compose \
                      -p ${COMPOSE_PROJECT_NAME} \
                      -f docker-compose.ci.yml \
                      up -d
                '''
            }
        }

        stage('Wait for services') {
            steps {
                sh '''
                    echo "Attente du démarrage des services..."

                    sleep 5

                    docker compose \
                      -p ${COMPOSE_PROJECT_NAME} \
                      -f docker-compose.ci.yml \
                      ps
                '''
            }
        }

        stage('Tests') {
            steps {
                sh '''
                    docker compose \
                      -p ${COMPOSE_PROJECT_NAME} \
                      -f docker-compose.ci.yml \
                      exec -T api pytest
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    docker compose \
                      -p ${COMPOSE_PROJECT_NAME} \
                      -f docker-compose.ci.yml \
                      exec -T api flake8 app tests
                '''
            }
        }
    }

    post {

        always {
            sh '''
                docker compose \
                  -p ${COMPOSE_PROJECT_NAME} \
                  -f docker-compose.ci.yml \
                  down -v --remove-orphans || true

                rm -f .env || true
            '''
        }

        success {
            echo 'CI SUCCESS : Tests et lint OK'
        }

        failure {
            echo 'CI FAILURE : consulter les logs Jenkins'
        }
    }
}
