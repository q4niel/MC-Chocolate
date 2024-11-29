from typing import List
import os
import json

class Data:
    ProjectDirectory:str = ""
    Version:str = ""
    Client:List[str] = []
    Server:List[str] = []
    Both:List[str] = []

    @staticmethod
    def init(projDir:str) -> None:
        with open(f"{projDir}/src/data.json", "r") as file:
            data = json.load(file)
            Data.ProjectDirectory = projDir
            Data.Version = data["version"]
            Data.Client = data["client"]
            Data.Server = data["server"]
            Data.Both = data["both"]
        return