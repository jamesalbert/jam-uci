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
        dir('jam-uci') {
          git url: scm.getUserRemoteConfigs()[0].getUrl()
        }
        dir(project) {
          git url: "https://github.com/${project}.git"
        }
      }
    }
    stage('test') {
      steps {
        script {
          dir(project) {
            parallel (
              test: { sh 'pytest' },
              docs: { sh 'pycco src/*.py' },
              pep8: { sh 'pep8 src' }
            )
          }
        }
      }
    }
    stage('submit') {
      steps {
        script {
          def conf = parseJson(readFile('.eee'))
          sh "submit.py  --course=${conf.course} --assignment=${pwd()}/${conf.assignment} --name=\"${conf.name}\""
        }
      }
    }
  }
}
