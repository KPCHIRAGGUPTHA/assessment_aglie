pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/YOUR_USERNAME/factorial-app.git'
            }
        }

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