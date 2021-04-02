from __future__ import annotations

import typing

from monty.design_patterns import singleton

if typing.TYPE_CHECKING:
    from typing import Optional
    from uuid import UUID

    from maggma.stores import Store

__all__ = ["CURRENT_JOB"]


@singleton
class State:
    uuid: Optional[UUID] = None
    store: Optional[Store] = None

    def reset(self):
        self.uuid = None
        self.store = None


CURRENT_JOB = State()
