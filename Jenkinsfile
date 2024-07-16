pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Вилучення коду з репозиторію
                git 'https://your-repository-url.git'
            }
        }

                stage('Install Dependencies') {

        steps {
            // Перевірка
            sh 'python --version'
        }
    }

        stage('Install Dependencies') {
            steps {
                // Встановлення залежностей проекту
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Запуск автотестів
                sh 'pytest --junitxml=results.xml'
            }
        }

        stage('Publish Test Results') {
            steps {
                // Збір результатів тестування та їх публікація у Jenkins
                junit 'results.xml'
            }
        }
    }

    post {
        always {
            // Архівування результатів тестування незалежно від результату
            archiveArtifacts artifacts: 'results.xml', allowEmptyArchive: true
        }
    }
}