import yaml
import os.path

builds_path = "builds/builds.yaml"
tasks_path = "builds/tasks.yaml"

if not os.path.isfile(builds_path):
    raise FileNotFoundError("builds.yaml not found")

if not os.path.isfile(tasks_path):
    raise FileNotFoundError("tasks.yaml not found")

with open(builds_path, 'r') as f:
    builds = yaml.safe_load(f)['builds']

with open(tasks_path, 'r') as f:
    tasks = yaml.safe_load(f)['tasks']
