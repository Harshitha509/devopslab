import docker

client = docker.from_env()

# Build the Docker image
client.images.build(path=".", tag="flask-apparmor")

print("Image built successfully.")

# Run the container with the requested AppArmor profile
try:
    container = client.containers.run(
        "flask-apparmor",
        ports={"5000/tcp": 5001},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True,
        name="flask-apparmor-sdk-test"
    )

    print(f"Container started: {container.short_id}")

    # Inspect the requested security options
    container_info = client.api.inspect_container(container.id)
    security_options = container_info["HostConfig"]["SecurityOpt"]

    print(f"Configured security options: {security_options}")

finally:
    # Clean up the test container if it was created
    try:
        container.stop()
        container.remove()
        print("Container stopped and removed.")
    except (NameError, docker.errors.NotFound):
        pass
    except docker.errors.APIError as error:
        print(f"Container cleanup issue: {error}")

