from yaml_reader import builds, tasks


# This method is used to get the sorted tasks by build
def get_sorted_tasks_by_build(build_name: str) -> tuple:
    try:
        tasks_temp_by_build = next((build['tasks'] for build in builds if build['name'] == build_name), [])
        res = [{tasks_name: search_dependency(tasks_name)} for tasks_name in tasks_temp_by_build]
        res = unpacker(sort_by_recursive_iterations(res))
        return res, tasks_temp_by_build, True
    except StopIteration:
        return [], [], False


# This method recursively searches for dependencies and returns a list of these dependencies
def search_dependency(task_name: str) -> list:
    task_temp = []
    for task in tasks:
        if task['name'] == task_name:
            if task['dependencies']:
                for dependency in task['dependencies']:
                    res = search_dependency(dependency)
                    task_temp.append(res)
            else:
                task_temp.append(task)
    return task_temp


# This method recursively counts the number of attachments
def count_recursive_iterations(lst) -> int:
    count = 0
    for item in lst:
        if isinstance(item, list) or isinstance(item, dict):
            count = max(count, 1 + count_recursive_iterations(item))
        elif isinstance(lst[item], list) or isinstance(lst[item], dict):
            count = max(count, 1 + count_recursive_iterations(lst[item]))
    return count


# This method sorts the tasks by the number of recursive iterations
def sort_by_recursive_iterations(lst: list) -> list:
    return sorted(lst, key=lambda x: count_recursive_iterations(x))


# This method unpacks the keys of the dictionary
def unpacker(task: list) -> list:
    keys = []
    for item in task:
        for key in item:
            keys.append(key)
    return keys
