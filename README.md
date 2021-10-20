# test_repository
Deploying website on Django with AWS, Docker and Jenkins from repository on GitHub

I created two EC2 instances, bounded to them Elastic IPs with Terraform and configured instances. 
After it when a developer makes changes and commits the changes to GitHub, Jenkins (on the first AWS EC2 instance) pulls changes from 
GitHub automatically and builds the project in a docker container and if build is successful, Jenkins sends the changes on the node server 
(on the second AWS EC2 instance) and the project deploys in a docker container on this instance and the container works in the background.
