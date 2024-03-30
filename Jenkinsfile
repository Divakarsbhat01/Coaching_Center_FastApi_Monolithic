pipeline {
    agent any

    stages 
    {
        stage('Hello') 
        {
            steps {
                echo 'Hello World'
            }
        }
        stage("Git Checkout") 
        {
            steps 
            {
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Divakarsbhat01/Coaching_Center_FastApi_Monolithic']])
            }
        }
        stage('Docker Build') 
        {
            steps 
            {
                sh "docker build -t coacenmonofastapi ."
                    
            }
        }
        stage("Pushing image to Docker Hub") 
        {
            steps 
            {
                withCredentials([string(credentialsId: 'dockerhubpwd', variable: 'dockerhubpwd'), string(credentialsId: 'dockerhubuser', variable: 'dockerhubuser')])
                {
                    sh "docker login -u divakarsbhat1 -p ${dockerhubpwd}"
                    sh "docker tag coacenmonofastapi divakarsbhat1/coacenmonofastapi:latest"
                    sh "docker push divakarsbhat1/coacenmonofastapi:latest"
                }
            }
        }
    }
}

