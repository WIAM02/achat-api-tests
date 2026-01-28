pipeline {
    agent any

    environment {
        BASE_URL   = 'https://dev.consult-it.com'
        API_PREFIX = '/api/v1'
        API_TOKEN  = 'eb6f13b384b420af5d3c72c753a20745'
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
