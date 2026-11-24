"""Duration parser helper."""

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

# A single component cannot repeat a unit (e.g. "1h2h"), and components must be
# written from the largest unit to the smallest ("1h30m", not "30m1h").
_UNIT_ORDER = {unit: rank for rank, unit in enumerate(_UNITS)}

_SPEC_RE = re.compile(r"^(?:\d+[wdhms])+$")
_PART_RE = re.compile(r"(\d+)([wdhms])")


def parse_duration(spec: str) -> int:
    """Convert a duration string like '1h30m' or '2d4h' into total seconds.

    Supported units are weeks (``w``), days (``d``), hours (``h``), minutes
    (``m``) and seconds (``s``). A spec is a concatenation of ``<amount><unit>``
    components, optionally separated by whitespace, written from the largest
    unit to the smallest, with each unit used at most once.

    Raises:
        ValueError: if ``spec`` is empty, contains an unsupported unit, repeats a
            unit, or lists units out of order. Previously an unknown or missing
            unit was silently dropped, which turned ``'1d'`` into ``0``.
    """
    if not isinstance(spec, str):
        raise ValueError(f"duration spec must be a string, got {type(spec).__name__}")

    stripped = spec.strip()
    if not stripped:
        return 0

    compact = re.sub(r"\s+", "", stripped)
    if not _SPEC_RE.fullmatch(compact):
        raise ValueError(f"invalid duration spec: {spec!r}")

    total = 0
    previous_rank = -1
    for amount, unit in _PART_RE.findall(compact):
        rank = _UNIT_ORDER[unit]
        if rank <= previous_rank:
            raise ValueError(
                f"units must be unique and ordered from largest to smallest: {spec!r}"
            )
        previous_rank = rank
        total += int(amount) * _UNITS[unit]
    return total
