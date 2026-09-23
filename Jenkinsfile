pipeline {
    agent any

    stages {

        stage('Run Python') {
            steps {
                bat 'python factorial.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t factorial-app:latest .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run --rm factorial-app:latest'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}