from typing import Optional

import git


class Git:
    def __init__(self, repo_path: str = "."):
        self.repo = git.Repo(repo_path)

    def head_diff(self, staged: bool = False):
        if staged:
            return self.repo.git.diff("HEAD", "--staged")
        else:
            return self.repo.git.diff("HEAD")

    def diff(self, branch_name: str, current_branch: Optional[str] = None):
        if current_branch is None:
            current_branch = self.repo.active_branch.name
        return self.repo.git.diff(branch_name, current_branch)
