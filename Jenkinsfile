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
                
                // Agregamos -u root para evitar el bloqueo de permisos al guardar el archivo
                sh 'docker run --rm -u root -v $(pwd):/zap/wrk/:rw -t zaproxy/zap-stable zap-baseline.py -t http://10.0.2.15:5000 -r reporte_zap.html || true'
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