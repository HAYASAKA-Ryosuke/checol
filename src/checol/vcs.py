from typing import Optional

import git


class Git:
    def __init__(self, repo_path: str = "."):
        self.repo = git.Repo(repo_path)

    def head_diff(self, staged: bool = False):
        if staged:
            return self.repo.git.diff("HEAD", "--staged", "-U10000")
        else:
            return self.repo.git.diff("HEAD", "-U10000")

    def diff(
        self,
        branch_name: Optional[str] = None,
        base_branch: Optional[str] = None,
    ):
        if base_branch is None:
            base_branch = self.repo.active_branch.name
        return self.repo.git.diff(branch_name, base_branch, "-U10000")
