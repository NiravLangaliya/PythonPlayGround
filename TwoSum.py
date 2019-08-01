"""
Given nums = [2, 7, 11, 15], target = 9
"""
def twoSum(given_num,target):
    dict_map=dict()
    for i in range(len(given_num)):
            if given_num[i] not in dict_map:
                dict_map[target-given_num[i]] = i
            else:
                return given_num[dict_map[given_num[i]]],given_num[i]

if __name__ == "__main__":
    given_num=[2,7,11,15]
    target = 22
    result = list(twoSum(given_num,target))
    print (result)