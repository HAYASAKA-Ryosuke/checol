import fire
import vcs
import gpt

API_KEY = "API_KEY"


def review(branch_name: str, git_path: str = "."):
    print("CTRL+C or 'exit' to exit.")
    git = vcs.Git(git_path)
    claude = gpt.Claude(API_KEY)
    diff = git.diff(branch_name)
    message = claude.send(diff)
    while True:
        print('AI > ', end='')
        for line in message.content[0].text.split("\n"):
            print(line)
        print('You > ', end='')
        user_message = input()
        if user_message == 'exit':
            break
        message = claude.send(user_message)


def main():
    fire.Fire({'review': review})


if __name__ == "__main__":
    main()
