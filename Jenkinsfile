pipeline {
    agent {
        label 'python'
    }

    stages {
        stage('Entorno') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version'
                sh 'pip install pytest'
                sh 'pip install pandas'
            }
        }

        stage('Descarga') {
            steps {
                git url: 'https://github.com/Monsse28/pytonOperaciones.git', branch: 'main'
            }
        }

        stage('Ejecutar') {
            steps {
                sh 'python3 operaciones.py'
            }
        }

        stage('Probar') {
            steps {
                sh 'pip install pandas'
                sh 'python3 -m pytest --junitxml=reports/results.xml'
            }
            post {
                always {
                    junit 'reports/results.xml'
                }
            }
        }
    }
}



