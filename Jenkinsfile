pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Fetching latest code from GitHub...'
                git branch: 'main', url: 'https://github.com/divyanshsharma31/Mini-project-Amazon.com-clone-.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image amazon-frontend:latest...'
                sh 'docker build -t amazon-frontend:latest .'
            }
        }

        stage('Deploy Container') {
            steps {
                echo 'Removing old container if it exists...'
                echo 'Starting new container on port 8090...'
                sh '''
                docker rm -f amazon-site || true
                docker run -d --name amazon-site -p 8090:80 amazon-frontend:latest
                '''
            }
        }

        stage('Health Check') {
            steps {
                echo 'Running health check on deployed application...'
                sh 'curl -s http://localhost:8090/health.html | head -n 1'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully. Application is live.'
        }
        failure {
            echo 'Pipeline failed. Please check Console Output for details.'
        }
    }
}
