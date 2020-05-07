import subprocess

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

    def run_file(self, file, args: list = None):
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

compiled_langauges = ['Java']

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


langauges = []
langauges.append(ProgramingLanguage(
    'Java', '.java', 'javac', 'java', '.class'))
langauges.append(ProgramingLanguage(
    'Python', '.py', findPythonCommand(), None, None))
