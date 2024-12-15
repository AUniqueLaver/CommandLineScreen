
# [ Use key ]
# def matMuitplication(m1 = None, m2 = None):
#     if m1 == None:
#         m1 = [[1,2],[1,9]]
#     if m2 == None:
#         m2 = [[1,2],[1,9]]
#
#     if len(m1[0]) != len(m2):
#         print("Matrix columns and rows do not match, cannot multiply")
#
#     m1 = mat1;
#     m2 = mat2;
#
#     matTransposed = []
#     
#     for rowNum in range(0, len(m2[0])):
#         matTransposed.append([])
#
#     # [ Maybe slow transposation method ]
#     for rowIdx in m2:
#         idx = 0;
#         for num in range(0, len(rowIdx)):
#             matTransposed[idx].append(rowIdx[num])
#             idx += 1
#
#     resultMat = []
#
#     for rowN in m1:
#         newRow = []
#         for numMatIdx in range(0, len(matTransposed)):
#             result = 0;
#             for num in range(0, len(rowN)):
#                 result += rowN[num] * matTransposed[numMatIdx][num]
#             newRow.append(result)
#         resultMat.append(newRow)
#
#     # print(len(m1))
#     print(resultMat)


# def geometricSequence(n = None):
#     if n == None:
#         n = 0
#
#     init = 1
#     for i in range(0, n):
#         init *= 4
#         print(init)

def initRPS():
    dieChange = 1
    print("Welcome to RPS, chose rock, paper or scissor")
    while True:
        s = ""
        dieChange += 1
        dieChange %= 3
        s = input(s)
        if s == "rock":
            if dieChange == 0:
                print("win")
            if dieChange != 0:
                print("loss")
        if s == "scissor":
            if dieChange == 1:
                print("win")
            if dieChange != 1:
                print("loss")
        if s == "paper":
            if dieChange == 2:
                print("win")
            if dieChange != 2:
                print("loss")

