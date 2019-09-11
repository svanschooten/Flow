import logging
from reader import Reader


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
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
    logger.info(log_str)


if __name__ == '__main__':
    main()
