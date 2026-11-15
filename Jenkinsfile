
pipeline {
    agent any

    stages {
        stage('Check Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv .venv'
                sh '.venv/bin/python -m pip install -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                sh '.venv/bin/python -m pytest -v'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                sh '.venv/bin/python monitor.py'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'evidently_report.html',
                             allowEmptyArchive: true
        }
    }
}