pipeline {
    agent { label 'python' }

    environment {
        REPORTS_DIR = 'reports'
    }

    stages {

        stage('Preparar Entorno') {
            steps {
                echo 'Instalando dependencias...'
                sh 'python3 --version'
                sh 'pip install --upgrade pip'
                sh 'pip install pytest'
            }
        }

        stage('Descargar Código') {
            steps {
                git url: 'https://github.com/Monsse28/pytonOperaciones.git', branch: 'main'
            }
        }

        stage('Preparar Reportes') {
            steps {
                echo "Creando carpeta de reportes si no existe..."
                sh "mkdir -p $REPORTS_DIR"
            }
        }

        stage('Verificar Tests') {
            steps {
                script {
                    def testFiles = sh(script: "ls test_*.py 2>/dev/null || true", returnStdout: true).trim()
                    if (testFiles == '') {
                        echo "No se encontraron tests en el repositorio."
                        currentBuild.result = 'UNSTABLE'
                    } else {
                        echo "Se encontraron tests: ${testFiles}"
                    }
                }
            }
        }

        stage('Ejecutar Tests') {
            steps {
                echo 'Ejecutando tests con pytest...'
                // Ejecuta pytest y genera reporte JUnit
                sh "pytest --junitxml=$REPORTS_DIR/results.xml || echo 'Algunos tests fallaron, revisa logs'"
                // Lista archivos en reports para debug
                sh "ls -l $REPORTS_DIR || echo 'Carpeta de reports vacía o no existe'"
            }
        }
    }

    post {
        always {
            echo 'Publicando resultados de tests en Jenkins...'
            // Solo publica si existe el archivo
            script {
                if (fileExists("$REPORTS_DIR/results.xml")) {
                    junit "$REPORTS_DIR/results.xml"
                } else {
                    echo "No se encontró el archivo de reporte JUnit."
                }
            }
        }
    }
}


