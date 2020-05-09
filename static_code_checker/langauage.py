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
        try:
            if self.compiled:
                run([self.compiler_command, file])
                file = file.replace(self.file_type, self.compiled_type)
                if args != None:
                    return run([self.execute_command, file, *args])
                else:
                    return run([self.execute_command, file])
            else:
                if args != None:
                    return run([self.compiler_command, file, *args])
                else:
                    return run([self.compiler_command, file])
        except :
            return("is broken")


compiled_langauges = ['Java', 'Kotlin', 'Scala']


def run(line):
    return subprocess.Popen(line, stdout=subprocess.PIPE).communicate()[0].decode("utf-8")


def findPythonCommand():
    possible_commands = ['python3', 'python', 'py3', 'py']
    for command in possible_commands:
        line = [command, '--version']

        try:
            output = run(line)
        except:
            continue

        if '3' in output:
            return command


langauges = [
    ProgramingLanguage('Java', '.java', 'javac', 'java', ''),
    ProgramingLanguage('JavaScript (NODE)', '.js', 'node', None, None),
    ProgramingLanguage('Kotlin', '.kt', 'javac', 'java', ''),
    ProgramingLanguage('Perl', '.pl', "perl", None, None),
    ProgramingLanguage('Python', '.py', findPythonCommand(), None, None),
    ProgramingLanguage('Ruby', '.rb', "ruby", None, None),
    ProgramingLanguage('Scala', '.scala', "scalac", 'scala', '')
]

if __name__ == "__main__":
    for language in langauges:
        print(language)
