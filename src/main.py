import os
import shutil
from data import Data
from generate import generateScripts

def makeBuildDir() -> None:
    if not os.path.exists(f"{Data.ProjectDirectory}/build"):
        os.makedirs(f"{Data.ProjectDirectory}/build")

    if os.path.exists(f"{Data.ProjectDirectory}/build/{Data.Version}"):
        shutil.rmtree(f"{Data.ProjectDirectory}/build/{Data.Version}")

    os.makedirs(f"{Data.ProjectDirectory}/build/{Data.Version}")
    return

def main() -> None:
    Data.init(os.path.abspath(__file__)[:-12])
    makeBuildDir()
    generateScripts()
    return

if __name__ == "__main__": main()