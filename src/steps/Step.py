from steps.AbstractStep import AbstractStep


class Step(AbstractStep):

    def read_inputs(self, signal_library):
        for signal in self.inputs:
            self.input_data[signal] = signal_library.get(signal)

    def process(self, method):
        self.output_data = method.apply(self.input_data)

    def write_outputs(self, signal_library):
        for signal in self.outputs:
            signal_library[signal] = self.output_data.get(signal)
        return signal_library
