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
      steps {
        script {
          def workspace = pwd()
        }
        sh "submit.py  --course=${course} --assignment=${workspace}/${assignment} --name=\"${name}\""
      }
    }
  }
}
