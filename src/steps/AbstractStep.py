from abc import ABCMeta, abstractmethod


class AbstractStep:
    __metaclass__ = ABCMeta
    type = 'Step'

    def __init__(self, config: dict):
        self.name = config.get('name', "Name required!")
        self.inputs = config.get('inputs', "Inputs required!")
        self.input_data = {}
        self.outputs = config.get('outputs', "Outputs required!")
        self.output_data = {}
        self.method = config.get('method', "Method required!")

        assert isinstance(self.name, str)
        assert isinstance(self.inputs, list)
        assert isinstance(self.outputs, list)
        assert isinstance(self.method, str)

    def __str__(self) -> str:
        return f"{self.type}{{name:{self.name}, inputs:{self.inputs}, outputs:{self.outputs}, method:{self.method}}}"

    def __repr__(self) -> str:
        return self.__str__()

    @abstractmethod
    def read_inputs(self, signal_library: dict) -> None:
        """
        Based on the inputs given from the library, select the correct one based on the configuration in 'inputs'.
        These are then placed in the correct place in 'input_data'.
        """
        pass

    @abstractmethod
    def process(self, method: callable) -> None:
        """
        Call the configured method in the correct way and place the results in 'output_data'
        """
        pass

    @abstractmethod
    def write_outputs(self, signal_library: dict) -> dict:
        """
        Select and manipulate the output data before writing it to the signal library.
        WARN: please return 'signal_library'
        """
        pass
