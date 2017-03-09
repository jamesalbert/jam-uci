import groovy.json.JsonSlurper

@NonCPS
def parseJson(filename) {
  def ret = new JsonSlurper().parseText(readFile(filename))
  echo ret
  return ret
}

pipeline {
  agent any
  stages {
    stage('checkout') {
      steps {
        git url: "https://github.com/jamesalbert/${project}.git"
        script {
          def conf = parseJson('.eee')
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
