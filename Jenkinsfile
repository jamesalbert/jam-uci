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
        sh 'pytest'
      }
    }
    stage('submit') {
      def workspace = pwd()
      steps {
        sh "echo ${workspace}"
        // sh "submit.py  --course=${course} --assignment=${workspace}$ --name=\"${name}\""
      }
    }
  }
}
