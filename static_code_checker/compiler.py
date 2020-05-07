import os
import sys
import webbrowser

try:
    from code_file import  File
except :
    from static_code_checker.code_file import File
        

def get_and_clean_files():
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

    files = []
    io_files = sys.argv
    for i in range(io_files):
        if i > 1:
            break
        io_files[i] = file_parser(io_files[i])


    for r, d, f in os.walk(os.getcwd()):
        for file in f:
            files.append(os.path.join(r, file), *io_files)

    for i in range(files):
        if not files[i].cleared:
            del files[i]
        if io_files[2]:
            if 'driver' not in file[i].file_loc:
                del files[i]

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



with open('static_code_checker.html', 'w+') as f:
    f.write(startHTML + endHTML)

webbrowser.open_new_tab('static_code_checker.html')
