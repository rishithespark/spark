pipeline {
    agent any
    
    stages {
        stage('Init Env') {
            steps {
                
                checkout scm
                
                sh 'echo test setup star'
                sh 'docker docker pull pypi/bandit '
                sh 'docker ps -a'
                
            }
        }
        stage('Test for security issues') {
            steps {
                sh 'bandit -r /var/lib/jenkins/workspace/bandit '
            }
        }
    }
}
