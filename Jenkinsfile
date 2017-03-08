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
          parallel (
            test: { sh 'pytest' },
            docs: { sh 'pycco src/*.py' },
            pep8: { sh 'pep8 src' }
          )
        }
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
