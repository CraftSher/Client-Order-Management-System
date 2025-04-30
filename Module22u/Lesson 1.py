#import os
# folder_name = 'Project'
# file_name = 'my_file.txt'
#
# path = 'docs/{folder}/{file}'.format(
#     folder = folder_name,
#     file = file_name
# )
#
# print(path)
#
# rel_path = os.path.join('docs', folder_name, file_name)
# print(rel_path)
# abs_path = os.path.abspath(file_name)
# print(abs_path)

import os

def print_dirs(project):
    print('n\Содержимое директории', project)
    for i_elem in os.listdir(project):
        path = os.path.join(project, i_elem)
        print('    ', path)
projects_list = ['PythonProject', 'Python_Basic']
for i_project in projects_list:
    path_to_project = os.path.abspath(os.path.join('..', '..', i_project))
    print_dirs(path_to_project)