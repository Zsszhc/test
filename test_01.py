#题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

#程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
# 1
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if i != k and i != j and j != k:
#                 print(i, j, k)

# #使用列表方式并计算总结
# # 2
# l = []
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if i != k and i != j and j != k:
#                 l.append([i, j, k])
# print("总数: " + str(len(l)))
# for o in l:
#     print(o)

# #将for循环和list和成一句并打印结果
# # 3
# list_num = list(range(1, 5))
# print(list_num)
#
# list_test = [i*100 + j*10 + k for i in list_num for j in list_num for k in list_num if (j != i and k != j and k != i)]
# print(list_test)

# #设置最大值，最小值
# # 4
# line = []
# for i in range(123, 433):
#     a = i % 10
#     b = (i % 100) // 10
#     c = (i % 1000) // 100
#     if a != b and b != c and a != c and 0 < a < 5 and 0 < b < 5 and 0 < c < 5:
#         print(i)
#         line.append(i)
# print("The total is %d" % len(line))

# # 利用集合去除重复元素
# # 5
# import pprint
#
# list_num = ['1', '2', '3', '4']
# list_result = []
#
# for i in list_num:
#     for k in list_num:
#         for j in list_num:
#             if len(set(i + j + k)) == 3:
#                 list_result += [int(i + j + k)]
# print("能组成%d个互不相同的三位数。" % len(list_result))
# pprint.pprint(list_result)
