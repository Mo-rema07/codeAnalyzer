# Saves uploaded code in a temporary '.txt' file so that it not executable.


def handle_uploaded_file(f):
    str_content = ''
    with open('file.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    file = open('file.txt', 'r')
    if file.mode == 'r':
        str_content = file.read()
    file.close()
    return str_content
