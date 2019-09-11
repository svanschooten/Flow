import logging
from reader import Reader
from methods import methods

# Logging level can be put on ERROR, WARN, INFO and DEBUG which will show more and more of the log statements
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fun(step_library: dict) -> None:
    for step_name in step_library:
        step = step_library.get(step_name)
        # Lets see it process an addition, first the empty step
        logger.debug(step)
        # Then set the inputs
        input_data = {'x': 3, 'y': 4}
        step.set_input_data(input_data)
        logger.debug(step)
        # Process it and show the result
        step.process(methods.get(step.get_method()))
        logger.debug(step)
        logger.info(f"{input_data} == {step.get_method()} ==> {step.get_output_data()}")


def main():
    # Print some information
    logger.info("Initializing Flow framework, reading configuration")

    # The path to the configuration file
    path = 'conf/example.yaml'

    # Create a reader
    reader = Reader()
    # Set the path (can also be done with the Reader construction)
    reader.set_path(path)
    # Process the configuration file
    step_library = reader.process()

    # This can also be done in one line:
    # step_library = Reader(path).process()

    # Print the content of the library
    log_str = "Printing library:\n"
    for name in step_library:
        log_str += f"\t{name}: {step_library[name]}\n"
    logger.debug(log_str)

    # Some more fun
    fun(step_library)


if __name__ == '__main__':
    main()
