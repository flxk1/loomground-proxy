# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 flxk1
"""loomground-proxy — Does this measurement still stand for what it claims?

One narrow problem. See :mod:`loomground_proxy.proxy` for the reasoning;
this module only re-exports it and the version.
"""

from ._version import __version__
from .proxy import (
    Movement,
    Proxy,
    Substitution,
    KINDS,
    check_proxies,
    chain,
    fold_substitutions,
    ProxyCycle,
)

__all__ = [
    "__version__",
    "Movement",
    "Proxy",
    "Substitution",
    "KINDS",
    "check_proxies",
    "chain",
    "fold_substitutions",
    "ProxyCycle",
]
