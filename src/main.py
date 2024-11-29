import os
import shutil
from links import Links
from shell import makeShell

def main() -> None:
    projDir:str = os.path.abspath(__file__)[:-12]

    if os.path.exists(f"{projDir}/build"):
        shutil.rmtree(f"{projDir}/build")
    os.makedirs(f"{projDir}/build")

    Links.init(projDir)
    makeShell(projDir)
    return

if __name__ == "__main__": main()