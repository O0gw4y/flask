pipeline {
    agent any

    parameters {
        // Use either string or choice, not both for VERSION
        choice(name: 'VERSION', choices: ['1.1.0', '1.2.0', '1.3.0'], description: 'Version to deploy on prod')
        booleanParam(name: 'executeTests', defaultValue: true, description: 'Run tests before deploying')
    }

    environment {
        NEW_VERSION = '1.3.0'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                echo "Building version ${env.NEW_VERSION}"
            }
        }
        stage('Test') {
            when {
                expression { params.executeTests }
            }
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying version ${params.VERSION}..."
            }
        }
    }

    post {
        always {
            echo 'Post build condition running'
        }
        failure {
            echo 'Post Action if Build Failed'
        }
    }
}
