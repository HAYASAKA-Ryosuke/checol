from typing import Optional

import git


class Git:
    def __init__(self, repo_path: str = "."):
        self.repo = git.Repo(repo_path)

    def head_diff(self, staged: bool = False):
        import pdb;pdb.set_trace()
        if staged:
            return self.repo.git.diff("HEAD", "--staged", '-W')
        else:
            return self.repo.git.diff("HEAD", '-W')

    def diff(self, branch_name: str, current_branch: Optional[str] = None):
        if current_branch is None:
            current_branch = self.repo.active_branch.name
        return self.repo.git.diff(branch_name, current_branch, '-W')
