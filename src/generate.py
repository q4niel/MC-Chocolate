import io
from data import Data
from typing import List, Callable

def makeShell(name:str, fns:List[Callable]) -> None:
    with open(f"{Data.ProjectDirectory}/build/{Data.Version}/{name}-{Data.Version}.sh", "w") as file:
        file.write("#!/bin/bash\n\n")
        for fn in fns:
            fn(file)
        file.write("\nrm -- \"$0\"")
    return

def generateScripts() -> None:
    serverCurls:Callable = lambda file: [file.write(f"curl -L -O {link}\n") for link in Data.Server]
    clientCurls:Callable = lambda file: [file.write(f"curl -L -O {link}\n") for link in Data.Client]
    bothCurls:Callable = lambda file: [file.write(f"curl -L -O {link}\n") for link in Data.Both]

    makeShell("Server", [serverCurls, bothCurls])
    makeShell("Client",[clientCurls, bothCurls])
    makeShell("Full", [serverCurls, clientCurls, bothCurls])

    return