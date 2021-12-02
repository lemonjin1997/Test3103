pipeline {
	agent any{
		
	stages {
		stage('Build') {
			steps {
				sh 'docker compose up'
			}
		}
		stage('Test') {
			steps {
                sh ''
            }
		}
	}
	post{
		always{
			junit testResults: 'logs/unitreport.xml'
		}
	}
}
