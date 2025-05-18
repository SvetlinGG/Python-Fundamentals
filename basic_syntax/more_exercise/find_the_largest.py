num = int(input())
new_num = [int(d) for d in str(num)]
new_num.sort(reverse = True)
final_num = "".join(str(i) for i in new_num)
print(final_num)

