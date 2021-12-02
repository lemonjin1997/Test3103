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
				//sh 'curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose'
				//sh 'chmod +x /usr/local/bin/docker-compose'
				//sh 'docker network create selenium_network'
				sh 'bash tmp.sh'
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
		stage('Test') {
			steps {
				sh 'docker ps'
               		 sh 'docker-compose exec -T test_team_1 sh -c "python3 -m pytest src/test.py"'
            		}
		}
		stage('TestUI') {
			steps {
                	sh 'docker-compose exec -T test_team_1 sh -c "python3 -m unittest src/testUI.py'
            		}
		}
		
	}
	post{
		always{
			junit testResults: 'logs/unitreport.xml'
		}
	}
	
}
