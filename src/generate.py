import io
from data import Data
from typing import List, Callable

def replaceFileNameShell(bad:str, good:str) -> str:
    return (
        f"\nfor file in *; do"
        f"\n    if [[ \"$file\" == *\"{bad}\"* ]]; then"
        f"\n        new=$(echo \"$file\" | sed 's/{bad}/{good}/g')"
        f"\n        mv \"$file\" \"$new\""
        f"\n    fi"
        f"\ndone\n"
    )

def makeShell(name:str, fns:List[Callable]) -> None:
    with open(f"{Data.ProjectDirectory}/build/{Data.Version}/{name}-{Data.Version}.sh", "w") as file:
        file.write("#!/bin/bash\n\n")

        for fn in fns:
            fn(file)

        file.write(replaceFileNameShell("%2B", "+"))
        file.write(replaceFileNameShell("%20", " "))

        file.write("\nrm -- \"$0\"")
    return

def generateScripts() -> None:
    server:Callable = lambda file: [file.write(f"curl -L -O {link}\n") for link in Data.Server]
    client:Callable = lambda file: [file.write(f"curl -L -O {link}\n") for link in Data.Client]
    both:Callable = lambda file: [file.write(f"curl -L -O {link}\n") for link in Data.Both]

    makeShell("Server", [server, both])
    makeShell("Client",[client, both])
    makeShell("Full", [server, client, both])

    return