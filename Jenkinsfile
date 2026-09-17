pipeline {
    agent any
    
    parameters {
        choice(name: 'EXAM_MODULE', choices: ['student-portal', 'examiner-dashboard', 'evaluation-engine'], description: 'Select the module of the Online Examination System to build')
        choice(name: 'ENVIRONMENT', choices: ['dev', 'staging', 'prod'], description: 'Select the target deployment environment')
    }
    
    stages {
        stage('Checkout Source Code') {
            steps {
                // Replace with your actual GitHub username and repository name
                git branch: 'main', url: 'https://github.com/saquib-18/assessment-7.git'
            }
        }
        
        stage('Show Selected Parameters') {
            steps {
                echo "Selected Examination Module: ${params.EXAM_MODULE}"
                echo "Selected Target Environment: ${params.ENVIRONMENT}"
            }
        }
        
        stage('Build Module for Environment') {
            steps {
                echo "Compiling and packaging the ${params.EXAM_MODULE} for the ${params.ENVIRONMENT} environment..."
                echo "Build process completed successfully!"
            }
        }
    }
}
