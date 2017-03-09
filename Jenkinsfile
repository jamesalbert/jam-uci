import groovy.json.JsonSlurper

@NonCPS
def parseJson(filename) {
  println new JsonSlurper().parseText(filename)
  def jsonStr = readFile(filename)
  println jsonStr
  def json = writeObjectFromJson('{"test": "cat"}')
  echo "jsonStr=$jsonStr"
  echo "json=$json"
  return json
}

pipeline {
  agent any
  stages {
    stage('checkout') {
      steps {
        git url: "https://github.com/jamesalbert/${project}.git"
        script {
          def conf = parseJson(readFile('.eee'))
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
