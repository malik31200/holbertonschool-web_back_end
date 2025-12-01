#!/usr/bin/env python3
"""
0-simple_helper_function
a function named index_range that takes
two integer arguments page and page_size.
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Return a tuple containing a start and an end index for pagination.

    Args:
        page (int): The current page number (1-indexed)
        page_size (int): The number of items per page.

    Returns:
        Tuple [int, int]: A tuple (start_index, end_index).
    """
    start_index: int = (page - 1) * page_size
    end_index: int = page * page_size

    return (start_index, end_index)
