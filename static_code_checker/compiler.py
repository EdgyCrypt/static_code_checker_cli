import os
import subprocess
import webbrowser

compiled_langauges = ['Java']

class ProgramingLanguage():
    def __init__(self, name: str, file_type: str, compiler_command: str, execute_command: str = None, compiled_type: str = None):
        self.name = name

        if self.name in compiled_langauges:
            self.compiled = True
        else:
            self.compiled = False

        self.file_type = file_type
        self.compiled_type = compiled_type
        self.compiler_command = compiler_command
        self.execute_command = execute_command

    def __repr__(self):
        return f"""
        {self.name} 
            COMPILED?:      {self.compiled}
            FILE_TYPE:      {self.file_type}
            COMPILED_TYPE:  {self.compiled_type}
            COMPILER_CM:    {self.compiler_command}
            EXECUTE_CM:     {self.execute_command}

        """

    def run_file(self, file, args:list = None):
        if self.compiled:
            run([self.compiler_command, file])
            file = file.replace(self.file_type, self.compiled_type)
            if args is None:
                return run([self.execute_command, file, *args])
            else:
                return run([self.execute_command, file])
        else:
            if args is None:
                return run([self.execute_command, file, *args])
            else:
                return run([self.execute_command, file])

def run(line):
    return subprocess.Popen(line, stdout=subprocess.PIPE).communicate()[0]

def findPythonCommand():
    possible_commands = ['python', 'python3', 'py', 'py3']
    for command in possible_commands:
        line = [command, '--version']

        try:
            output = run(line)
        except:
            continue

        if '3' in output.decode("utf-8"):
            return command

startHTML= """
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
<body>
"""

langauges = []
langauges.append(ProgramingLanguage(
    'Java', '.java', 'javac', 'java', '.class'))
langauges.append(ProgramingLanguage(
    'Python', '.py', findPythonCommand(), None, None))

all_files = []
for r, d, f in os.walk(os.getcwd()):
    for file in f:
        file = os.path.join(r, file)

        for langauge in langauges:
            if langauge.file_type in file:
                print(langauge.run_file(file))

with open('static_code_checker.html', 'w+') as f:
    f.write(startHTML + endHTML)

# webbrowser.open_new_tab('static_code_checker.html')
