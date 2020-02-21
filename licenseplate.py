from itertools import product
from string import ascii_uppercase

filepath = 'licenseplates.txt'
outFile = open(filepath, 'w')

for nums in range(0, 10000):
  nums = str(nums)
  nums = nums.zfill(4)
  for letters in product(ascii_uppercase, repeat=3):
    license_plate = ((''.join(letters)) + nums)
    print(license_plate)
  outFile.write(license_plate)
