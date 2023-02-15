pipeline {
    agent any

    stages {
        stage('version') {
            steps {
              sh 'python3 --version'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 server.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing....'
            }
        }
    }
}
