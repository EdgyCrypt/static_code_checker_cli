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
        value = "<div>"
        for i in range(self.inputs):
            # file, args: list = None
            value += compare(self.languageType.run_file(self.file_loc, self.inputs[i]), self.outputs[i])
            value += "</div>"
            
def compare(original_text: str, generated_text: str):
    """
    Compares 2 strings and returns html to be served to the models
    original_text - The text from the example
    generated_text - The text from the
    """
    def prep_html(text: str, expression: bool):
        """
        Returns the match or miss for each character while already moving it to html
        text: the actual character
        expression: matching status
        """
        if expression:
            return f'<div class="__g__"> {text} </div>'
        else:
            return f'<div class="__r__"> {text} </div>'

    comparison = ""
    
    # we will assume that this is the actual text
    for i in range(len(generated_text)):
        try:
            comparison += prep_html(generated_text[i], generated_text[i] == original_text[i])
        except IndexError:
            comparison += prep_html(generated_text[i], False)

    if len(original_text) > len(generated_text):
        comparison += prep_html(original_text[len(generated_text):len(original_text)], False)

    percent_match = comparison.count("__g__") / (comparison.count("__g__") + comparison.count("__r__"))

    return comparison, percent_match
