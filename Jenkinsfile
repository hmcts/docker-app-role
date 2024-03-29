#!groovy

properties(
  [[$class: 'GithubProjectProperty', displayName: 'Role: docker-app', projectUrlStr: 'https://github.com/hmcts/docker-app-role/'],
   pipelineTriggers([[$class: 'GitHubPushTrigger']])]
)

node {
  ws('docker-app-role') { // This must be the name of the role otherwise ansible won't find the role
    try {
      wrap([$class: 'AnsiColorBuildWrapper', colorMapName: 'xterm']) {
        stage('Checkout') {
          checkout scm
        }

        stage('Start containers') {
          sh '''
            molecule create
          '''
        }

        stage('Run role') {
          sh '''
            molecule converge
          '''
        }

        stage('Check idempotent') {
          sh '''
            molecule idempotence
          '''
        }

        stage('Run tests') {
          sh '''
            molecule syntax
            molecule verify
          '''
        }
      }

    } catch (err) {
      slackSend(
        channel: '#devops-builds',
        color: 'danger',
        message: "${env.JOB_NAME}: <${env.BUILD_URL}console|Build ${env.BUILD_DISPLAY_NAME}> has FAILED")
      throw err
    } finally {
      stage('Cleanup') {
        sh '''
          molecule destroy
        '''
      }
      deleteDir()
    }
  }
}
