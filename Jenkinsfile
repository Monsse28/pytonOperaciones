pipeline {
    agent { label 'python' }

    stages {
        stage('Entorno') {
            steps {
                sh 'python3 --version'
                sh 'pigs --version'
                sh 'pip install pytest'
            }
        }

        stage('Descarga') {
            steps {
                git url: 'https://github.com/Monsse28/pytonOperaciones.git', branch: 'main'
            }
        }

        stage('Ejecutar') {
            steps {
                sh 'python3 hola.py'
                sh 'python3 operaciones.py'
            }
        }

        stage('Probar') {
            steps {
                sh 'python -m pytest --junitxml=reports/results.xml'
            }
        }
    }

    post {
        always {
            junit 'reports/results.xml'
        }
    }
}
