def deepCopyBinaryTree(originalTree):
    copyList = []
    for i in originalTree:
        if type(i) == tuple:
           copyList.append(tuple(deepCopyBinaryTree(i)))
        else:
            copyList.append(i)
    return copyList


if __name__ == "__main__":
    originalTree = (1, (2, (4, (7, None, None), None), None), (3, (5, None, None), (6, None, None)))
    deepCopiedTuple = (tuple(deepCopyBinaryTree(originalTree)))
    print(deepCopiedTuple)

