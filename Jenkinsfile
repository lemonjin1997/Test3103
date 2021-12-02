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
				sh 'curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose'
				sh 'chmod +x /usr/local/bin/docker-compose'
				sh 'bash tmp.sh'
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
