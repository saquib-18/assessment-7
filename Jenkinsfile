pipeline {
    agent any
    
    stages {
        stage('Checkout Source') {
            steps {
                // Replace with your repository URL
                git branch: 'main', url: 'https://github.com/saquib-18/assessment-7.git'
            }
        }
        
        stage('Generate Exam Report') {
            steps {
                // Use 'sh' if running on a Linux Jenkins agent
                bat 'python generate_exam_report.py'
            }
        }
        
        stage('Archive Exam Artifacts') {
            steps {
                // Saves the report so it can be downloaded directly from Jenkins UI
                archiveArtifacts artifacts: 'exam_report.txt', fingerprint: true
            }
        }
    }
}
