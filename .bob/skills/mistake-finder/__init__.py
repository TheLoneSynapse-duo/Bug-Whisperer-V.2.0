"""mistake-finder - find mistakes in your code and report them in a box.

Installable package that provides:

  * ``mistake-box``           - run a command and box its mistakes (CLI);
  * a pytest plugin           - box every failing test automatically.

The skill itself (workflow + checklist + report formats) lives next to this
module as markdown files.
"""

from . import box  # noqa: F401

__version__ = "1.0.0"
__all__ = ["box", "__version__"]
