import os
import subprocess

application_dir = "application"
pf_libraries_dir = "pf-libraries"


def get_git():
    git = "git"
    exported_git_path = os.environ.get('git_path')
    if exported_git_path:
        git = "\"" + exported_git_path + "\""
    return git


def git_command(command):
    return get_git() + " " + command


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def create_directories(directory_list: list):
    for directory in directory_list:
        create_directory(directory)


def execute_command(home, command):
    subprocess.run(command, shell=True, cwd=home)


def pull_project(home):
    git_directory = home + "/.git"
    if os.path.exists(git_directory):
        execute_command(home, git_command("pull"))


def clone_project(root, project, url):
    if url != "":
        command = git_command("clone ") + url + " " + project
        execute_command(root, command)


def setup_project(home):
    module_directory = home + "/setup.py"
    if os.path.exists(module_directory):
        execute_command(home, "python setup.py develop")


def clone_and_setup(root, project, url, path):
    if not os.path.exists(path):
        clone_project(root, project, url)
        setup_project(path)


def pull_setup_project(home):
    pull_project(home)
    setup_project(home)


def clone_pull_setup(projects: dict):
    root = projects['dir']
    create_directory(root)
    repositories: dict = projects['repositories']
    repository_names = repositories.keys()
    for name in repository_names:
        print("\n\n\n\n-------------------------------------------------------------------------------------")
        print("Working with repository: " + name + ", source: " + root)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        path = os.path.join(root, name)
        repository = repositories.get(name)
        clone_and_setup(root, name, repository, path)
        pull_setup_project(path)
        print("-------------------------------------------------------------------------------------")


source_projects = {
    "dir": pf_libraries_dir,
    "repositories": {
        "flask-pf-common": "https://github.com/problemfighter/flask-pf-common.git",
        "flask-pf-sqlalchemy": "https://github.com/problemfighter/flask-pf-sqlalchemy.git",
        "flask-pf-marshmallow-swagger": "https://github.com/problemfighter/flask-pf-marshmallow-swagger.git",
        "pf-python-io": "https://github.com/problemfighter/pf-python-io.git",
        "pf-flask-communication": "https://github.com/problemfighter/pf-flask-communication.git",
        "pf-py-object-man": "https://github.com/problemfighter/pf-py-object-man.git",
    }
}


def pull_and_setup_application_modules():
    print("\n\n\n\n-------------------------------------------------------------------------------------")
    print("Taking Application Module Pull")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    if os.path.exists(application_dir):
        pull_project(application_dir)
        for directory in os.listdir(application_dir):
            path = os.path.join(application_dir, directory)
            if os.path.isdir(path):
                print("\n\n\n\n################################################################################")
                print("Taking pull and setup of " + directory)
                print("################################################################################")
                pull_setup_project(path)


def start():
    clone_pull_setup(source_projects)
    pull_project("./")
    pull_and_setup_application_modules()


if __name__ == '__main__':
    start()
