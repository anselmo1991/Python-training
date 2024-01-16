import logging
import argparse
from importlib1 import get_package_path

def log_package_info(package_name, logger):
    result = get_package_path(package_name)

    if result != "Package not found":
        package = importlib.import_module(package_name)
        logger.warning("Package name: %s" % package_name)
        logger.warning("Package description: %s" % package.__doc__)
        logger.info("Package path: %s" % result)
        try:
            logger.debug("Package version: %s" % package.__version__)
        except AttributeError:
            logger.error("Package version not found")
    else:
        logger.error(result)

if __name__ == "__main__":
    # Configure command-line arguments
    parser = argparse.ArgumentParser(description="Log information about a Python package.")
    parser.add_argument("package_path", type=str, help="Path to the Python package.")
    parser.add_argument("--console_log_level", type=str, default="WARNING", help="Console log level (default: WARNING).")
    parser.add_argument("--file_log_level", type=str, default="DEBUG", help="File log level (default: DEBUG).")
    parser.add_argument("--log_file", type=str, default="package_info.log", help="Log file name (default: package_info.log).")

    args = parser.parse_args()

    # Configure logging
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
    logger = logging.getLogger()

    # Configure console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, args.console_log_level))
    logger.addHandler(console_handler)

    # Configure file handler
    file_handler = logging.FileHandler(args.log_file)
    file_handler.setLevel(getattr(logging, args.file_log_level))
    logger.addHandler(file_handler)

    # Log package information
    log_package_info(args.package_path, logger)
