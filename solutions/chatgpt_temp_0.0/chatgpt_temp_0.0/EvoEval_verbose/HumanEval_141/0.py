
def file_name_check(file_name):
    if sum((char.isdigit() for char in file_name)) > 3:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    (name, extension) = file_name.split('.')
    if not name or not name[0].isalpha():
        return 'No'
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'