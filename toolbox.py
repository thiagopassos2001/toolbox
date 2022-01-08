# -*- coding: utf-8 -*-

def CreateMatrix(m,n,value):
    '''
    
    Parameters
    ----------
    m : int
        Número de Linhas.
    n : int
        Número de colunas.
    value : float
        Valor a preencher a matriz.

    Returns
    -------
    M : list
        Lista com m linhas, n colunas preenchida com value.

    '''
    M = []
    
    for i in range(m):
        M_line = []
        for j in range(n):
            M_line.append(value)
        M.append(M_line)
        
    return M

def DimMatrix(M):
    '''

    Parameters
    ----------
    M : list
        Matriz binimensional.

    Returns
    -------
    Dim : tuple
        Tupla contendo as dimenões m (linhas) e n (colunas) da matriz M.

    '''
    Dim = []
    
    while type(M) == list:
        Dim.append(len(M))
        M = M[0]
        
    Dim = tuple(Dim)
    
    return Dim

def SameDimensions(A,B):
    '''

    Parameters
    ----------
    A : list
        Matriz a ser comparada.
    B : list
        Matriz a ser comparada.

    Returns
    -------
    bool, True or False
        Verdadeiro se A e B possuirem a mesma dimensão e 
        falso se o contrário ocorrer.
    tuple, (m,n)
        Dimensão m (linhas) e n (colunas) das matrizes; se não
        possuirem a mesma dimensão, retorna (0,0).

    '''
    dimA = DimMatrix(A)
    dimB = DimMatrix(B)
    
    if dimA == dimB:
        return True, dimA
    else:
        raise ValueError('As matrizes não tem a mesma dimensão')
    
def SumMatrix(A,B):
    '''

    Parameters
    ----------
    A : list
        Matriz a ser somada.
    B : list
        Matriz a ser somada.

    Returns
    -------
    C : list
        Matriz resultante da soma A + B.

    '''
    
    have_same_dim, dim = SameDimensions(A,B)
    
    if have_same_dim:
        m, n = dim
        C = CreateMatrix(m,n,0)
    
        for i in range(m):
            for j in range(n):
                C[i][j] = A[i][j] + B[i][j]
            
        return C

def SubMatrix(A,B):
    '''

    Parameters
    ----------
    A : list
        Matriz a ser subtraída.
    B : list
        Matriz a ser subtraída.

    Returns
    -------
    C : list
        Matriz resultante da subtração A - B.

    '''
    
    have_same_dim, dim = SameDimensions(A,B)
    
    if have_same_dim:
        m, n = dim
        C = CreateMatrix(m,n,0)
    
        for i in range(m):
            for j in range(n):
                C[i][j] = A[i][j] - B[i][j]
            
        return C
        