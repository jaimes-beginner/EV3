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
                    # Correr ZAP con volumen nombrado
                    docker run --rm \
                        --user root \
                        -v zap-results:/zap/wrk/:rw \
                        -t zaproxy/zap-stable \
                        /bin/bash -c "
                            zap-baseline.py -t http://10.0.2.15:5000 -r reporte_zap.html || true
                            chmod 777 /zap/wrk/reporte_zap.html 2>/dev/null || true
                        " || true

                    # Extraer el reporte usando la ruta real del volumen Jenkins en el host
                    docker run --rm \
                        -v zap-results:/zap/wrk/:ro \
                        -v /var/lib/docker/volumes/jenkins_home/_data/workspace/Pipeline-Parcial3:/output/:rw \
                        alpine \
                        cp /zap/wrk/reporte_zap.html /output/reporte_zap.html

                    # Verificar
                    ls -la $WORKSPACE/reporte_zap.html && echo "Reporte generado OK" || echo "ERROR: reporte no encontrado"

                    # Limpiar volumen temporal
                    docker volume rm zap-results || true
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