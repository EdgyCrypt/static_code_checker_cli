try:
    from langauage import langauges
except :
    from static_code_checker.langauage import langauges

class File():
    def __init__(self, file_loc: str, inputs: list, outputs: list):
        self.file_loc = file_loc

        self.languageType = None

        self.cleared = True

        for i in langauges:
            if i.file_type in file_loc:
                self.languageType = i
                break

        if self.languageType == None:
            self.cleared = False

        self.inputs = inputs
        self.outputs = outputs

    def run_tests(self):
        if not self.cleared:
            return False

        full_text = ""
        reusable = "<div><p>ChangeThis<\p></div>"

        for i in range(inputs):
            full_text += reusable.replace(
                "ChangeThis",  self.languageType.run_file(self.file_loc, self.inputs[i]))
        
        return full_text        