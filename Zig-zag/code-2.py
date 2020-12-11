def printSubSequences(STR, subSTR=""):
    """
    function:
        To print all subsequences of string
        concept:
            Pick and Don’t Pick
        variables:
            STR = string
            subSTR = to store subsequence
    """
    if len(STR) == 0:
        print(subSTR, end=" ")
        return
    printSubSequences(STR[:-1], subSTR + STR[-1])
    printSubSequences(STR[:-1], subSTR)
    return


S = "bcade"
K = 3

printSubSequences(S)