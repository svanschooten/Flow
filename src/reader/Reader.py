import yaml
from steps import types as step_types


class Reader(object):
    def __init__(self, path, verbose=False):
        self.path = path
        self.verbose = verbose

        with open(path, 'r') as stream:
            try:
                self.content = yaml.safe_load(stream)
                if self.verbose:
                    print(self.content)
            except yaml.YAMLError as exc:
                print(exc)

    def process(self):
        if self.content is None:
            print("Content is empty! Needs to be initialised properly first")
            return

        step_library = {}

        for element in self.content['elements']:
            step_type = step_types.get(element.get('type'), "Invalid type!")
            step_library[element.get('name')] = step_type(element)

        return step_library
