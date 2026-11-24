"""Duration parser helper.

Supported units:
* w – weeks (7 days)
* d – days
* h – hours
* m – minutes
* s – seconds
"""

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
    """Convert a duration string like '1h30m' into total seconds.

    The function parses the *spec* using a regular expression that extracts
    consecutive `<number><unit>` pairs. Supported units are defined in the
    `_UNITS` mapping above. Any unknown unit is ignored.
    """
    total = 0
    for amount, unit in re.findall(r"(\d+)([wdhms])", spec):
        if unit in _UNITS:
            total += int(amount) * _UNITS[unit]
    return total
