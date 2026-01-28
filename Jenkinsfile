pipeline {
    agent any

    environment {
        BASE_URL   = 'https://dev.consult-it.com'
        API_PREFIX = '/api/v1'
    }

    stages {
        stage('Setup') {
            steps {
                bat 'py --version'
                bat 'py -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'py -m pytest'
            }
        }
    }
}
