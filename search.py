#linear search
def lin_search(arr,key):
  for i in arr:
    if i == key:
      a=arr.index(i)
      return a
  return False


#binary search
def bin_search(arr,key):
  low=0
  high=len(arr)-1
  while high>=low:
    mid=(low+high)//2
    if key==mid:
      print(key,arr.index(key))
      return True
    if (key<mid):
      high=mid-1
    else:
      low=mid+1
  return False