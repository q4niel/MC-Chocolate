import os
import shutil
from data import Data
from script import generateScripts

def main() -> None:
    Data.init(os.path.abspath(__file__)[:-12])

    if os.path.exists(f"{Data.ProjectDirectory}/build"):
        shutil.rmtree(f"{Data.ProjectDirectory}/build")
    os.makedirs(f"{Data.ProjectDirectory}/build")

    generateScripts()

    return

if __name__ == "__main__": main()