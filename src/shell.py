from links import Links

def makeShell(projDir:str) -> None:
    with open(f"{projDir}/build/server.sh", "w") as file:
        file.write("#!/bin/bash\n\n")

        for link in Links.Server:
            file.write(f"curl -O {link}\n")

        for link in Links.Both:
            file.write(f"curl -O {link}\n")

        file.write("\nrm -- \"$0\"")

    with open(f"{projDir}/build/client.sh", "w") as file:
        file.write("#!/bin/bash\n\n")

        for link in Links.Client:
            file.write(f"curl -O {link}\n")

        for link in Links.Both:
            file.write(f"curl -O {link}\n")

        file.write("\nrm -- \"$0\"")
    return