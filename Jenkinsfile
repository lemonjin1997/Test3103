pipeline {
	agent any
		
	stages {
		stage ('Checkout') { 
            steps { 
                git branch:'main', url: 'https://github.com/lemonjin1997/Test3103.git' 
		    } 
		} 
		stage('Build') {
			steps {
				sh 'python3 -m /home/student95/src/app.py'
				//sh 'docker compose up'
			}
		}
		stage('Test') {
			steps {
               		 sh 'python3 -m pytest src/test.py'
            		}
		}
		stage('TestUI') {
			steps {
                	sh 'test3103-team-1 python3 -m pytest src/testUI.py'
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
