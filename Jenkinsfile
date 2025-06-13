flag=true
pipeline {
    agent any
    environment {
        NEW_VERSION = '1.3.0'

    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                // Here you can define commands for your build
                echo "BUliding version ${NEW_VERSION}"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                // Here you can define commands for your tests
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                // Here you can define commands for your deployment
            }
        }
    }

    post {
        always {
            // this action will happen always regardless of the result of the build 
            echo 'Post build condition running'
        }
        failure {
            // this action will happen only if the build has failed 
            echo 'Post Action if Build Failed'
        }
    }
}
