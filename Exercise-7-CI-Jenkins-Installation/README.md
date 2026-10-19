\# Exercise 7: Introduction to CI and Jenkins Installation



\## Objective

To understand the basics of Continuous Integration (CI) and install Jenkins using Docker.



\## Tools Used

\- Docker Desktop

\- Jenkins (`jenkins/jenkins:lts`)

\- Windows PowerShell

\- Web browser



\## Procedure



\### 1. Check Existing Jenkins Container

Checked whether a Jenkins container was already present using:



```powershell

docker ps -a --filter "name=^/jenkins$"

```



\### 2. Download and Run Jenkins

Pulled the Jenkins LTS Docker image and created a container with ports `8080` and `50000` mapped.



```powershell

docker run -d --name jenkins -p 8080:8080 -p 50000:50000 -v jenkins\_home:/var/jenkins\_home jenkins/jenkins:lts

```



\### 3. Verify the Container

Used the following command to check the running Jenkins container:



```powershell

docker ps --filter "name=^/jenkins$"

```



The container was running successfully, and port `8080` was mapped to the host machine.



\### 4. Retrieve the Initial Administrator Password

Retrieved the initial administrator password using:



```powershell

docker exec jenkins cat /var/jenkins\_home/secrets/initialAdminPassword

```



The password was used for Jenkins setup and is not included in this repository for security reasons.



\### 5. Access Jenkins

Opened the following URL in a web browser:



`http://localhost:8080`



The Jenkins dashboard loaded successfully.



\## Result

Jenkins was installed and run using Docker. The container status was verified, the initial administrator password was retrieved, and the Jenkins dashboard was accessed successfully.



\## Screenshots

The `screenshots` folder contains evidence of the Docker installation and container verification, along with the Jenkins dashboard.



