import os


def app_version(request):
    project_root = os.path.abspath(os.path.dirname(__file__))

    with open(os.path.join(project_root, 'version')) as f:
        _version = f.read()

    return {'app_version': _version}

