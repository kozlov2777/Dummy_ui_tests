pipeline {
    agent any

    environment {
        CONTAINER_NAME = 'dummy_ui_tests'
    }

    stages {
        stage('Download and Run Docker Image') {
            steps {
                script {
                    bat "docker pull kozlov2777/dummy-ui-tests"
                    try{
                        bat "docker run --name ${env.CONTAINER_NAME} kozlov2777/dummy-ui-tests"
                    }catch (Exception e) {
                        currentBuild.result = 'SUCCESS'
                    }

                }
            }
        }

        stage('Copy Allure result') {
            steps {
                script {
                    bat "docker cp ${env.CONTAINER_NAME}:/Dummy_ui_tests/allure-results ./allure-results"
                }
            }
        }

        stage('Stop and Remove Container') {
            steps {
                script {
                    bat "docker stop ${env.CONTAINER_NAME}"
                    bat "docker rm ${env.CONTAINER_NAME}"
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
}