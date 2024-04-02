import os
from typing import Optional

import fire
from halo import Halo
from prompt_toolkit import prompt

from checol.gpt import Claude
from checol.vcs import Git

spinner = Halo(text="Loading", spinner="dots")


def get_user_input() -> str:
    """
    Read user input until empty line.
    """
    result = ""
    while True:
        line = input()
        if line == "":
            break
        result += f"{line}\n"
    return result


def generate_response_from_claude(git_diff: str) -> None:
    model = os.environ.get("ANTHROPIC_API_MODEL", "claude-3-haiku-20240307")
    claude = Claude(api_key=os.environ.get("ANTHROPIC_API_KEY"), model=model)

    description = prompt("Description > ", multiline=True)

    sending_message = f"{description}\n\n{git_diff}" if description else git_diff

    spinner.start()
    message = claude.send(sending_message)
    spinner.stop()

    while True:
        print("AI > ", end="")
        for line in message.content[0].text.split("\n"):
            print(line)
        user_message = prompt("You > ", multiline=True)
        spinner.start()
        message = claude.send(user_message)
        spinner.stop()


def uncommitted(staged: bool = False):
    git_path = os.getcwd()
    git = Git(git_path)
    uncommitted_diff = git.head_diff(staged=staged)
    generate_response_from_claude(uncommitted_diff)


def diff(branch: Optional[str] = None):
    git_path = os.getcwd()
    git = Git(git_path)
    diff = git.diff(branch)
    generate_response_from_claude(diff)


def main():
    if os.environ.get("ANTHROPIC_API_KEY") is None:
        print("Please set ANTHROPIC_API_KEY environment variable.")
        return
    print("CTRL+C to exit.")
    print("To confirm, type Enter with an empty space.")
    fire.Fire({"uncommitted": uncommitted, "diff": diff})


if __name__ == "__main__":
    main()
