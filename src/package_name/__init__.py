"""package_name."""

from pathlib import Path

from package_name.utils.logger import set_logger


logger = set_logger(__name__, "INFO")
package_dir = Path(__file__).parents[2].absolute()
