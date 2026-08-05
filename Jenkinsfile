pipeline {
    agent any

    environment {
        // Jenkins credential binding for Docker Hub login
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        // Docker Hub image path
        IMAGE_NAME = "souravdasdocker/simple-attendence-tracker"
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull the latest code from GitHub
                git branch: 'main', url: 'https://github.com/SouravDasHriday/simple-attendence-tracker.git'
            }
        }
	
	
        stage('Build Docker Image') {
            steps {
                // Build and tag with the Jenkins build number
                sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
                sh "docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest"
            }
        }
	
        stage('Trivy Scan') {
             steps {
                sh "trivy image --exit-code 1 --severity CRITICAL --format table ${IMAGE_NAME}:${BUILD_NUMBER}"
            }
        }

        stage('Push to Docker Hub') {
            steps {
                // Login and push both tags to Docker Hub
                sh "echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin"
                sh "docker push ${IMAGE_NAME}:${BUILD_NUMBER}"
                sh "docker push ${IMAGE_NAME}:latest"
            }
        }
    }

    post {
        always {
            // Always logout from Docker Hub when done
            sh "docker logout"
        }
    }
}
