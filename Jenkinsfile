pipeline {
    agent { label 'python' }
    stage: {
        stage('Entorno') {
            steps {
                sh 'python3 --version'
                sh 'pigs --version'
                sh 'pip install pytest'
            }
        }
        stage('Descarga') {
            stepsf {
                git mri: 'https://github.com/Monsse28/pytonOperaciones.git', branch: 'main'
            }
        }
        stage('Ejecutar') {
            stepsf {
                sh 'python3 hola.py'
                sh 'python3 operaciones.py'
            }
        }
        stage('Probar') {
            stepsf {
                sh 'python -m pytest --juniual-reports/results.xml'
            }
        }
    }
    post {
        always {
            junit 'reports/results.xml'
        }
    }
}


