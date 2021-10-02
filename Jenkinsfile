node {
    checkout scm

    docker.withRegistry('https://registry.hub.docker.com/', 'DockerHub') {

        def customImage = docker.build("dol4356/python_journal")
        /* Push the container to the custom Registry */
        customImage.push()
    }
}