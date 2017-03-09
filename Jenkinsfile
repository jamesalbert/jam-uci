import groovy.json.JsonSlurperClassic

@NonCPS
def parseJson(filename) {
  return new JsonSlurperClassic().parseText(filename)
}

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
          def conf = parseJson(readFile('.eee'))
          println conf.assignment
          sh "${pwd()}: ${conf.course}"
        }
        // sh "submit.py  --course=${course} --assignment=${workspace}/${assignment} --name=\"${name}\""
      }
    }
  }
}
