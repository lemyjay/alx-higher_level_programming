#!/usr/bin/python3
'''
Matrix Multiplication
'''


def matrix_mul(m_a, m_b):
    """
    A function that multiplies 2 matrices
    
    Prototype:
        def matrix_mul(m_a, m_b):
    
    Args:
        m_a (list): a list of lists of integers or floats
        m_b (list): a list of lists of integers or floats
    
    Returns:
        A new matrix as the result of the multiplication
    
    Raises:
        TypeError: - if m_a or m_b is not a list
                   - if m_a or m_b is not a list of lists
                   - if m_a or m_b is not a rectangle (all rows should be of the same size)
                   - if one element of those list of lists is not an integer or float
        
        ValueError: - if m_a or m_b is empty
                    - if m_a and m_b can't be multiplied
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if any(not isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(not isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_a or any(not row for row in m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or any(not row for row in m_b):
        raise ValueError("m_b can't be empty")
    if any(not isinstance(j, (int, float)) for i in m_a for j in i):
        raise TypeError("m_a should contain only integers or floats")
    if any(not isinstance(j, (int, float)) for i in m_b for j in i):
        raise TypeError("m_b should contain only integers or floats")
    
    row_a = len(m_a[0])
    row_b = len(m_b[0])
    if any(len(i) != row_a for i in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(i) != row_b for i in m_b):
        raise TypeError("each row of m_b must be of the same size")
    
    # For the multiplication of two matrices to be possible, the number of
    # columns of matrix A should be equal to the number of rows in matrix B
    num_of_colums_matA = len(m_a[0])
    num_of_rows_matB = len(m_b)
    if num_of_colums_matA != num_of_rows_matB:
        raise ValueError("m_a and m_b can't be multiplied")
    new_matrix = []
    k = 0
    for i in m_a:
        t = []
        h = []
        for k in range(len(m_b[0])):
            for a in m_b:
                t.append(a[k])
            result = 0
            for c in range(len(t)):
                result += (t[c] * i[c])
        h.append(result)
        new_matrix.append(h)
        k += 1
    return new_matrix