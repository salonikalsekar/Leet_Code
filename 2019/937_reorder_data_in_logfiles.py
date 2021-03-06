# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         digList = []
#         alphList = []
#         finalList = []
#         for i in logs:
#             log = i.split()
#             if log[1].isdigit():
#                 digList.append(i)
#             else:
#                 alphList.append(i)
#
#         alphList = sorted(alphList, key=lambda x: x.split()[1:] + [x.split()[0]])
#         return (alphList + digList)


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digList = []
        alphList = []
        finalList = []
        for i in logs:
            log = i.split()
            if log[1].isdigit():
                digList.append(i)
            else:
                alphList.append(i)

        alphList = sorted(alphList, key=lambda x: (x.split()[1:], x.split()[0]))
        return (alphList + digList)




    # for k,v in sorted(d.items(), key = lambda x:(-x[0] ,  x[1]))
    # minus only works on integer and reverses it