flag=true
pipeline {
    agent any
    parameters {
        //these are types of parameters
        string(name: 'VERSION',defaultValue: '', description: 'version to deploy on prod') 
        choice (name: 'VERSION', choices: ['1.1.0', '1.2.0', '1.3.0'], description: '')
        booleanParam(name: 'executeTests', defaultValue: true, description: '')

    }
    
    environment {
        NEW_VERSION = '1.3.0'

    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                // Here you can define commands for your build
                echo "BUliding version ${NEW_VERSION}"
                sh "nvm install"
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
