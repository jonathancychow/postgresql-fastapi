import yaml
from pathlib import Path

def get_credentials():
    current_file_dir = Path(__file__).resolve()
    repo_dir = current_file_dir.parent.parent.parent
    cred_path = Path(repo_dir, 'cred.yaml')
    with open(cred_path) as f:
        configurations = yaml.safe_load(f.read())
        credentials = configurations['CREDENTIALS']
        user = credentials['USER']
        db = credentials['DB']
        password = credentials['PASSWORD']
        host = credentials['HOST']
        port = credentials['PORT']

    return user, db, password, host, port