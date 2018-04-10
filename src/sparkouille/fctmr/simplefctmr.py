#-*- coding: utf-8 -*-
"""
@file
@brief Simple *mapper* and *reducer* implemented in :epkg:`Python`
"""
from itertools import groupby


def mapper(fct, gen):
    """
    Applies function *fct* to a generator.

    @param      fct     function
    @param      gen     generator
    @return             generator
    """
    return map(fct, gen)


def reducer(fctkey, gen, asiter=True, sort=True):
    """
    Implements a reducer.

    @param      key     function which returns the key
    @param      gen     generator
    @param      asiter  returns an iterator on each element of the group
                        of the group itself
    @param      sort    sort elements by key before grouping
    @return             generator
    """
    if sort:
        new_gen = map(lambda x: x[1], sorted(
            map(lambda el: (fctkey(el), el), gen)))
        gr = groupby(new_gen, fctkey)
    else:
        gr = groupby(gen, fctkey)
    if asiter:
        # Cannot return gr. Python is confused when yield and return
        # are used in the same function.
        for _ in gr:
            yield _
    else:
        for key, it in gr:
            yield key, list(it)
