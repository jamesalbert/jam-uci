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
        dir(project) {
          git url: "https://github.com/${project}.git"
        }
        dir('jamesalbert/jam-uci') {
          git url: scm.getUserRemoteConfigs()[0].getUrl()
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
          def conf = parseJson(readFile("${project}/.eee"))
          sh "jamesalbert/jam-uci/src/submit.py  \
              --course=${conf.course} \
              --assignment=${pwd()}/${conf.assignment} \
              --name=\"${conf.name}\""
        }
      }
    }
  }
}
