"""Duration parser helper.

from __future__ import annotations

import re

# Seconds per unit. Supported: weeks, days, hours, minutes, seconds.
_UNITS = {
    "w": 604800,
    "d": 86400,
    "h": 3600,
    "m": 60,
    "s": 1,
}

def parse_duration(spec: str) -> int:
    """Convert a duration string like '1h30m' into total seconds."""
    total = 0
    for amount, unit in re.findall(r"(\d+)([wdhms])", spec):
        if unit in _UNITS:
            total += int(amount) * _UNITS[unit]
    return total
