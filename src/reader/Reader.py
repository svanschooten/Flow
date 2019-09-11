import yaml
import logging
from steps import types as step_types

logger = logging.getLogger(__name__)


class Reader(object):
    def __init__(self, path: str = None, verbose: bool = False):
        """
        Constructor
        :param path: The config path, is nullable
        :param verbose: Print what you read
        """
        self.path = path
        self.verbose = verbose
        self.__read__()

    def set_path(self, path: str) -> None:
        """
        Set the path and read the contents
        :param path:
        :return:
        """
        self.path = path
        self.__read__()

    def __read__(self) -> None:
        """
        Read the contents (private)
        :return:
        """
        if self.path is not None:
            with open(self.path, 'r') as stream:
                try:
                    self.content = yaml.safe_load(stream)
                    if self.verbose:
                        logger.debug(self.content)
                except yaml.YAMLError as exc:
                    logger.error(exc)

    def process(self) -> dict:
        """
        Process the content into a library
        :return:
        """
        if self.content is None:
            logger.warning("Content is empty! Needs to be initialised properly first")
            return {}

        step_library = {}

        for element in self.content['elements']:
            step_type = step_types.get(element.get('type'), "Invalid type!")
            step_library[element.get('name')] = step_type(element)

        return step_library
