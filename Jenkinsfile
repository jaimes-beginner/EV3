pipeline {
    agent any
    
    stages {
        stage('Construcción (Build)') {
            steps {
                echo 'Iniciando fase de Construcción...'
                echo 'Creando entorno virtual e instalando dependencias...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Pruebas (Test)') {
            steps {
                echo 'Ejecutando pruebas automatizadas...'
                echo 'Verificando que la aplicación responda "Hola Mundo"...'
                sh '''
                    . venv/bin/activate
                    pytest test-app.py
                '''
            }
        }
        
        stage('Despliegue (Deploy)') {
            steps {
                echo 'Iniciando despliegue de la aplicación...'
                sh 'echo "¡Despliegue exitoso! La aplicación segura está en producción."'
            }
        }
    }
}