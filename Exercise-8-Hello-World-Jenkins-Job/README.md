\# Exercise 8: Creating a Hello World Jenkins Job



\## Objective

To create a Jenkins Freestyle job that retrieves a shell script from GitHub and executes it.



\## Tools Used

\- Git and GitHub

\- Jenkins

\- Docker

\- Bash shell script



\## Procedure



1\. Created a public GitHub repository named `devops-sample-code`.

2\. Created a shell script named `hello-world.sh` containing:



&#x20;  ```bash

&#x20;  #!/bin/bash

&#x20;  echo "Hello, Jenkins!"

&#x20;  ```



3\. Initialized a local Git repository, committed the script, and pushed it to the `main` branch on GitHub.

4\. Opened Jenkins at `http://localhost:8080` and created a Freestyle project named `HelloWorld`.

5\. Configured Source Code Management to use the GitHub repository:



&#x20;  `https://github.com/Harshitha509/devops-sample-code.git`



6\. Configured the build step to execute:



&#x20;  ```bash

&#x20;  sh hello-world.sh

&#x20;  ```



7\. Saved the job, selected \*\*Build Now\*\*, and checked the Console Output.



\## Result

The Jenkins job executed successfully and printed `Hello, Jenkins!` in the Console Output. The build finished with status `SUCCESS`.



\## Screenshots

The `screenshots` folder contains the Jenkins Console Output showing the successful build.

