from typing import List
import os
import json

class Links:
    Client:List[str] = []
    Server:List[str] = []
    Both:List[str] = []

    @staticmethod
    def init(projDir:str) -> None:
        with open(f"{projDir}/src/links.json", "r") as file:
            data = json.load(file)
            Links.Client = data["client"]
            Links.Server = data["server"]
            Links.Both = data["both"]
        return