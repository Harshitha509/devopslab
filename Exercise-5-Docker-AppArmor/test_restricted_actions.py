import docker

client = docker.from_env()

container = None

try:
    container = client.containers.run(
        "flask-apparmor",
        ports={"5000/tcp": 5001},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True,
        name="flask-apparmor-restriction-test"
    )

    print(f"Container started: {container.short_id}")

    # Test access to /etc/passwd
    exit_code, output = container.exec_run("cat /etc/passwd")
    print(f"Attempt to read /etc/passwd: Exit Code {exit_code}")
    print(output.decode(errors="replace"))

    # Test execution of /bin/bash
    exit_code, output = container.exec_run("/bin/bash")
    print(f"Attempt to execute /bin/bash: Exit Code {exit_code}")
    print(output.decode(errors="replace"))

finally:
    if container is not None:
        try:
            container.stop()
            container.remove()
            print("Container stopped and removed.")
        except docker.errors.APIError as error:
            print(f"Cleanup issue: {error}")
