import datetime
import json
import random
import time
from datetime import datetime
import GitHubController


class scheduler:
    config: dict[str, dict[datetime.date, dict]]

    def __init__(self):
        self.Git = GitHubController.Controller()

        with open("config/cfg.json") as file:
            self.config = json.load(file)
        if self.config == {}:
            self.CreateNewConfig()

    def CreateNewConfig(self):
        self.config = {"Date": datetime.now().strftime("%d-%m-%Y"), "Upload": 0}
        self.SaveCFG()

    def SaveCFG(self):
        with open("config/cfg.json", "w") as file:
            json.dump(self.config, file)

    def _Handler(self):
        day, month, year = map(int, self.config.get("Date").split('-'))
        if datetime.now().hour >= 10 and datetime.now().hour <= 21:
            if month == datetime.now().month and day == datetime.now().day:
                if self.config.get("Upload") < 3:
                    if self.Git.Storage.GetAllProjectName() != []:
                        self.Git.UploadProject(random.choice(self.Git.Storage.GetAllProjectName()))
                        self.config["Upload"] += 1
                        self.SaveCFG()
                    else:
                        print("FileNotFounde")
                time.sleep(1 * 60 * 60)
            else:
                self.CreateNewConfig()
        else:
            print("Skiping...")

    def loop(self):
        while True:
            self._Handler()
            time.sleep(1)
