import sys


def get_project_path(name: str):
    """
    Get the full path of the project directory
    """
    list_paths = sys.path
    path0 = ""
    for path in list_paths:
        if path.rfind(name) != -1:
            if len(path0) == 0 or (len(path0) > len(path)):
                path0 = path
            else:
                continue
        else:
            continue
    if len(path0) == 0:
        raise NotADirectoryError("Project directory not found")
    else:
        return path0
