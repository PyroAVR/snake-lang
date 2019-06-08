"""
Whenever delegates of any kind are imported, ensure that the delegate system
is loaded and initialized.
module var __delegate_int__ is used to store this object.
"""
from typing import Callable
__delegate_int__ = dict()

__all__ = ['delegate']
