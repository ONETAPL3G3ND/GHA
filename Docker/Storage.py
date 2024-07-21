import os
import shutil

class Storage:
    def __init__(self, MainFolder: str = "Project"):
        self.MainFolder = MainFolder

        if not os.path.exists(MainFolder):
            os.makedirs(MainFolder)
            print(f"A project folder ({MainFolder}) has been created!")

    def GetAllFileInProject(self, ProjectName: str) -> dict:
        files = {}

        for i in os.listdir(f"{self.MainFolder}/{ProjectName}"):
            files[i] = open(f"{self.MainFolder}/{ProjectName}/{i}")
        return files

    def GetAllProjectName(self):
        return os.listdir(f"{self.MainFolder}/")

    def DeleteProject(self, ProjectName: str):
        shutil.rmtree(f"{self.MainFolder}/{ProjectName}")

