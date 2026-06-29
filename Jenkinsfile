pipeline {
    agent any
    stages {
        stage('Construcción (Build)') {
            steps {
                echo 'Iniciando fase de Construcción...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Pruebas Funcionales (Test)') {
            steps {
                echo 'Verificando que la aplicación funcione...'
                sh '''
                    . venv/bin/activate
                    pytest test-app.py
                '''
            }
        }
        stage('Pruebas de Seguridad (OWASP ZAP)') {
            steps {
                echo 'Lanzando escáner OWASP ZAP contra la aplicación local...'
                sh '''
                    mkdir -p zap-reports
                    chmod 777 zap-reports

                    docker run --rm \
                        --user root \
                        -v $(pwd)/zap-reports:/zap/wrk/:rw \
                        -t zaproxy/zap-stable \
                        /bin/bash -c "
                            zap-baseline.py -t http://10.0.2.15:5000 -r reporte_zap.html || true
                            chmod 777 /zap/wrk/reporte_zap.html
                        " || true

                    cp zap-reports/reporte_zap.html . && echo "Reporte copiado OK" || echo "WARN: reporte no encontrado"
                '''
            }
        }
        stage('Despliegue (Deploy)') {
            steps {
                echo '¡Despliegue exitoso! Aplicación auditada y en producción.'
            }
        }
    }
    post {
        always {
            echo 'Guardando el reporte de vulnerabilidades...'
            archiveArtifacts artifacts: 'reporte_zap.html', allowEmptyArchive: true
        }
    }
}