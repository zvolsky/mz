"""
base.py
local.py - specific to an installation (allowed to go into the repository)
secret.py - specific to an installation (should never go into repository)
"""

from .base import *  # noqa

# overrides from local settings
try:
    from .local import *  # noqa
except ImportError:
    pass

# overrides from local secret settings
try:
    # SECRET_KEY
    from .secret import *  # noqa
except ImportError:
    pass
