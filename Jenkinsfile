pipeline {
    agent any

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
