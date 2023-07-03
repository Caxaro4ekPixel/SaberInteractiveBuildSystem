from yaml_reader import builds, tasks


def get_sorted_tasks_by_build(build_name):
    try:
        tasks_temp_by_build = next((build['tasks'] for build in builds if build['name'] == build_name), [])
        res = [{tasks_name: search_dependency(tasks_name)} for tasks_name in tasks_temp_by_build]
        res = unpacker(sort_by_recursive_iterations(res))
        return res, tasks_temp_by_build, True
    except StopIteration:
        return [], [], False


def search_dependency(task_name):
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


def count_recursive_iterations(lst):
    count = 0
    for item in lst:
        if isinstance(item, list) or isinstance(item, dict):
            count = max(count, 1 + count_recursive_iterations(item))
        elif isinstance(lst[item], list) or isinstance(lst[item], dict):
            count = max(count, 1 + count_recursive_iterations(lst[item]))
    return count


def sort_by_recursive_iterations(lst):
    return sorted(lst, key=lambda x: count_recursive_iterations(x))


def unpacker(task):
    keys = []
    for item in task:
        for key in item:
            keys.append(key)
    return keys
