import os
import sys
import webbrowser

try:
    from static_code_checker.code_file import File
except ImportError:
    from code_file import  File

def file_parser(line):
    # is a file
    if os._exists(line):
        contents = ''
        with open(line, 'r') as reader:
            for i in reader.readlines():
                contents += i
        contents.split('^^^')
        return contents
    else:
        return line


def get_and_clean_files():
    
    files = []
    io_files = sys.argv 
    del io_files[0]
    
    for i in range(len(io_files)):
        if i > 1:
            break
        io_files[i] = file_parser(io_files[i])

    

    for r, d, f in os.walk(os.getcwd()):
            for file in f:
                try:
                    files.append(File(file, io_files[0], io_files[1]))

                except :
                    try:
                        files.append(File(file, io_files[0]))

                    except :
                        files.append(File(file))
    
    for i in range(len(files)):
        try:
            if not files[i].languageType:
                del files[i]
        except :
            break
        try:
            if io_files[2]:
                if 'driver' not in file[i].file_loc:
                    del files[i]
        except :
            None

    return files

startHTML = """
<head>
    <meta charset="utf-8">
    <title>Static Code Checker</title>
    <style> #mainHeader{text-align:center;color:whitesmoke;}.center{text-align:center;width:100%;display:inline-block;}.topBar{text-align:center;width:100%;display:inline-block;background-color:#AA0D36;height:80px;border-bottom:solid 2px black;}.homeBody{margin-top:2%;}body{background-color:#badce6;}</style>
</head>
<body>
    <div>
        <div class="center">
            <div class="topBar">
                <h1 id="mainHeader">Static Code Checker</h1>
            </div>
        </div>
"""

endHTML = """
    </div>
</body>
"""

files = get_and_clean_files()
middle = ""

for file in files:
    if file.tests:
        middle += file.tests 
  
with open('static_code_checker.html', 'w+') as f:
    f.write(startHTML + middle + endHTML)

webbrowser.open_new_tab('static_code_checker.html')
