from typing import Optional

import git


class Git:
    def __init__(self, repo_path: str = "."):
        self.repo = git.Repo(repo_path)

    def diff(self, spec: str):
        return self.repo.git.diff(*spec.strip().split(' '), "-U10000")
