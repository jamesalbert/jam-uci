pipeline {
  agent any
  stages {
    stage('checkout') {
      steps {
        git url: "https://github.com/jamesalbert/${project}.git"
      }
    }
    stage('test') {
      steps {
        script {
          def workspace = pwd()
        }
        sh "echo ${workspace}"
        sh 'pytest'
      }
    }
    stage('submit') {
      steps {
        script {
          def workspace = pwd()
        }
        sh "echo ${workspace}"
        // sh "submit.py  --course=${course} --assignment=${workspace}$ --name=\"${name}\""
      }
    }
  }
}
