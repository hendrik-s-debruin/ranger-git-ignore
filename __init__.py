import ranger.container.directory
import subprocess
import os

ACCEPT_FILE_OLD = ranger.container.directory.accept_file


def is_git_ignored(file: str):
    abs_file_path = os.path.abspath(file)
    dirname = os.path.dirname(abs_file_path)
    return (
        subprocess.run(
            ["git", "check-ignore", file], capture_output=True, cwd=dirname
        ).returncode
        == 0
    )


def custom_accept_file(fobj, filters):
    if not fobj.fm.settings.show_hidden and is_git_ignored(fobj.path):
        return False
    return ACCEPT_FILE_OLD(fobj, filters)


ranger.container.directory.accept_file = custom_accept_file
