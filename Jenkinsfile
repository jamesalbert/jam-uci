import groovy.json.JsonSlurper

@NonCPS
def parseJson(text) {
  return (new JsonSlurper()).parseText(text)
}

pipeline {
  agent any
  stages {
    stage('checkout') {
      steps {
        git url: "https://github.com/jamesalbert/${project}.git"
        script {
          def InputJson = parseJson(readFile('.eee'))
          InputJson.each { k, v ->
            println k
          }
        }
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
        // sh "submit.py  --course=${course} --assignment=${workspace}/${assignment} --name=\"${name}\""
      }
    }
  }
}
