# Saves uploaded code in a temporary '.txt' file so that it not executable.
import os


# Reads content from the uploaded file, writes to local file, reads the content into memory and deletes the file.
def handle_uploaded_file(f):
    str_content = ''
    temp_txt = 'temp.txt'
    with open(temp_txt, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    file = open(temp_txt, 'r')
    if file.mode == 'r':
        str_content = file.read()
    file.close()
    os.remove('%s' % temp_txt)
    return str_content
