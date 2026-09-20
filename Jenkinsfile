pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'taskly-api',
                url: 'https://github.com/AvinCarvalho/taskly-api.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t eesho/taskly-api:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'USERNAME',
                    passwordVariable: 'PASSWORD'
                )]) {
                    sh 'echo $PASSWORD | docker login -u $USERNAME --password-stdin'
                    sh 'docker push eesho/taskly-api:latest'
                }
            }
        }

        stage('Deploy to k3s') {
            steps {
                sh 'sudo kubectl rollout restart deployment taskly-api'
            }
        }

        stage('Trigger K8s Deploy') {
            steps {
                build job: 'taskly-k8s'
            }
        }
    }

    post {
        success {
            echo 'taskly-api Deployed!'
        }

        failure {
            echo 'Deployment Failed!'
        }
    }
}
