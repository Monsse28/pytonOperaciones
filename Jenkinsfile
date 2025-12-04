pipeline {
    agent any

    stages {
        stage('Entorno') {
            steps {
                sh 'python3 --version'
                sh 'pip install pytest'
                // Si realmente necesitas 'pigs', asegúrate que esté instalado
                sh 'pigs --version || echo "pigs no está instalado"'
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
                sh 'python3 -m pytest --junitxml=results.xml'
            }
        }
    }
}



