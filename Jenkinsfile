pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                bat 'python --version'
                bat 'pip --version'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }
    }
}
