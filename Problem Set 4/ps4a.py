# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx    ~ 1 hour

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return [sequence]
    elif len(sequence) == 2:
        return [sequence, sequence[::-1]]
    else:
        seq_copy = sequence[:]
        perm_list = []
        for char in sequence:
            perm_list +=  [char + x for x in get_permutations(seq_copy.replace(char, ''))]
        return perm_list

if __name__ == '__main__':
    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    example_input = 'a b'
    print('Input:', example_input)
    print('Expected Output:', ['a b', 'ab ', ' ab', ' ba', 'ba ', 'b a'])
    print('Actual Output:', get_permutations(example_input))
    
    example_input = 'dog'
    print('Input:', example_input)
    print('Expected Output:', ['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god'])
    print('Actual Output:', get_permutations(example_input))
    
    example_input = 'man'
    print('Input:', example_input)
    print('Expected Output:', ['man', 'mna', 'amn', 'anm', 'nma', 'nam'])
    print('Actual Output:', get_permutations(example_input))

