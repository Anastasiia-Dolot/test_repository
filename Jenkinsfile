node {
    checkout scm

    docker.withRegistry('https://registry.hub.docker.com/', 'DockerHub') {

        docker.build("dol4356/python_journal")
        docker.up("dol4356/python_journal")
    }
}