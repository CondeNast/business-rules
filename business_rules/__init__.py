# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
__version__ = '1.0'

from .engine import run_all, run_all_with_results
from .utils import export_rule_data

# Appease pyflakes by "using" these exports
assert run_all
assert export_rule_data
assert run_all_with_results
