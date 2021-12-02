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
                sh 'docker exec -it test3103-team-1 python3 -m pytest src/test.py'
            }
		}
		stage('TestUI') {
			steps {
                sh 'docker exec -it test3103-team-1 python3 -m pytest src/testUI.py'
            }
		}
		stage('Code Quality Check via SonarQube') { 
           steps { 
               script { 
                def scannerHome = tool 'SonarQube'; 
                   withSonarQubeEnv('SonarQube') { 
                   sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=OWASP -Dsonar.sources=." 
                   } 
               } 
           } 
        } 
	}
	post{
		always{
			junit testResults: 'logs/unitreport.xml'
		}
	}
}
