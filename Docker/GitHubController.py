import github
import TOKEN
from github import Github
import Storage
from progress.bar import ShadyBar
from datetime import datetime

class Controller:
    def __init__(self):
        self.GitHub = Github(TOKEN.TOKEN)
        self.User = self.GitHub.get_user()
        self.Storage = Storage.Storage()

    def _CreateNewRepo(self, RepoName: str) -> github.Repository.Repository:
        return self.User.create_repo(RepoName)

    def _UploadFile(self, ProjectName: str, Repo: github.Repository.Repository):
        files = self.Storage.GetAllFileInProject(ProjectName)
        bar = ShadyBar('Uploading files', max=len(files.keys()))
        bar.start()
        for file in files.keys():
            bar.next()
            Repo.create_file(path=file, message="New Project", content=files.get(file).read())
        bar.finish()

    def _GetNowTimeStamp(self):
        return f"[{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}]"

    def UploadProject(self, ProjectName: str):
        print(f"{self._GetNowTimeStamp()} The project upload process has started!")
        print(f"{self._GetNowTimeStamp()} Creating Repository...")
        repo = self._CreateNewRepo(ProjectName)
        self._UploadFile(ProjectName, repo)
        print(f"{self._GetNowTimeStamp()} Deleting Project Folder...")
        self.Storage.DeleteProject(ProjectName)
        print(f"{self._GetNowTimeStamp()} The project upload process is complete!")




