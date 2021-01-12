"""
str2d.py

a module that deals with strings in 2 dimensions


stencil.py

a module to produce Stencils and Masks that selectively conceal or reveal
elements of a sequence.
More of a discrete Jacquard than a continuous stencil, but, maybe, the noun
stencil is more universally understood.

# there is wonderful trivia and vocabulary to learn and maybe use here:
# https://en.wikipedia.org/wiki/Jacquard_loom#Principles_of_operation
"""

from Str2D.src.utils import apply_mask, chunk, shuffle


__all__ = [
    'apply_mask',
    'chunk',
    'Mask',
    'Perforation',
    'PUNCHED',
    'shuffle',
    'SOLID',
    'Stencil',
    'Str2D',
]
