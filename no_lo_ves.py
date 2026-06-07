import random

def ponerlos_juntos(nums: list):
  if not nums:
    return []
  nums.sort()
  lo_visto = {nums[0]}
  grupito = list(lo_visto)
  grupos = []
  for i in range(1, len(nums)):
    if nums[i] not in lo_visto:
      if nums[i]-1 == nums[i-1]:
        grupito.append(nums[i])
      else:
        grupos.append(grupito)
        grupito = [nums[i]]
    lo_visto.add(nums[i])
  grupos.append(grupito)
  return grupos


if __name__ == '__main__':
  res = ponerlos_juntos([random.randint(0, 24) for _ in range(10)])
  print(res)
  
