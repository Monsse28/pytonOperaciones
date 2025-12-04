pipeline {
    agent { label 'python' } // agente que tenga Python

    environment {
        REPORTS_DIR = 'reports'
    }

    stages {
        stage('Entorno') {
            steps {
                sh 'python3 --version'
                sh 'pip install --upgrade pip'
                sh 'pip install pytest'
            }
        }

        stage('Descarga') {
            steps {
                git url: 'https://github.com/Monsse28/pytonOperaciones.git', branch: 'main'
            }
        }

        stage('Preparar') {
            steps {
                // Crear carpeta de reports si no existe
                sh 'mkdir -p $REPORTS_DIR'
            }
        }

        stage('Ejecutar') {
            steps {
                sh 'python3 hola.py || echo "hola.py terminó con error, continuando..."'
                sh 'python3 operaciones.py || echo "operaciones.py terminó con error, continuando..."'
            }
        }

        stage('Probar') {
            steps {
                sh "pytest --junitxml=$REPORTS_DIR/results.xml || echo 'Tests fallaron, pero seguimos'"
            }
        }
    }

    post {
        always {
            junit '$REPORTS_DIR/results.xml'
        }
    }
}

