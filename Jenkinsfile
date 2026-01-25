



pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/divyanshsharma31/Mini-project-Amazon.com-clone-.git'
            }
        }
options { skipDefaultCheckout(true) }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t amazon-frontend:latest .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker rm -f amazon-site || true
                docker run -d --name amazon-site -p 8090:80 amazon-frontend:latest
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh 'curl -s http://localhost/health.html | head -n 1'
            }
        }
    }
}







