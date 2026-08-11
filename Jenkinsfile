pipeline {
    agent any

    environment {
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
                sh '''
                    docker compose -f ${COMPOSE_FILE} build
                '''
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

        stage('Check Containers') {
            steps {
                sh '''
                    docker compose -f ${COMPOSE_FILE} ps

                    test "$(docker inspect -f '{{.State.Status}}' \
                        sim-synaptic-ci-api)" = "running"

                    test "$(docker inspect -f '{{.State.Status}}' \
                        sim-synaptic-ci-db)" = "running"
                '''
            }
        }

        stage('Wait Database') {
            steps {
                sh '''
                    echo "Attente de PostgreSQL..."

                    for i in $(seq 1 30); do
                        if docker compose -f ${COMPOSE_FILE} \
                            exec -T db pg_isready \
                            -U glory \
                            -d sim_synaptic; then
                            echo "PostgreSQL est prêt."
                            exit 0
                        fi

                        echo "PostgreSQL n'est pas encore prêt..."
                        sleep 2
                    done

                    echo "PostgreSQL n'est pas disponible."
                    exit 1
                '''
            }
        }

        stage('Tests') {
            steps {
                sh '''
                    docker compose -f ${COMPOSE_FILE} \
                        exec -T api pytest
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    docker compose -f ${COMPOSE_FILE} \
                        exec -T api flake8 app tests
                '''
            }
        }
    }

    post {
        always {
            sh '''
                docker compose -f ${COMPOSE_FILE} down -v || true
            '''
        }

        success {
            echo 'Pipeline exécuté avec succès.'
        }

        failure {
            echo 'Le pipeline a échoué.'
        }
    }
}
