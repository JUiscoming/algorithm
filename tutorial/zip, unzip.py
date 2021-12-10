# 예제 1. 2개의 리스트의 동일한 인덱스에 있는 원소들끼리 묶어서 하나의 원소(튜플)를 형성
# 두 리스트의 길이가 다르다면 더 짧은 길이의 리스트 길이에 맞춰서 zip
A = [1,2,3,4,5]
B = [2,4,6,8,10]

AB = list(zip(A, B))
print(f'AB: {AB}')

# 예제 2. 3(can be any natural number)개의 리스트 zip
X = [0] * 5
Y = [1] * 5
Z = [2] * 5

XYZ = list(zip(X, Y, Z))
print(f'XYZ: {XYZ}')

# 예제 3. N개의 원소가 있는 K개의 리스트를 zip한 리스트가 있을 때
# *(asterisk)을 통해 zipped list를 unpacking하면 N개의 튜플 존재 (각 튜플은 K개의 리스트를 묶어서 만들었기 때문에 K개의 원소 존재)
# 이 때 다시 zip을 수행하면 list(zip(*zipped_list)), 다시 N개의 원소가 있는 K개의 리스트 얻을 수 있음
A_r, B_r = zip(*AB)
print(A_r, B_r)