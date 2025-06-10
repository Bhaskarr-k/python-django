list1=[12,2,3,4,5]
list2=[5,6,7,8,9]
print("list1 -> ",list1)
print("list2 -> ",list2)
print("id of list1 -> ",id(list1))
print("id of list2 -> ",id(list2))
list1.append(['basu','bhaskar'])
print(list1)

# crete a copy using shallow copy
import copy
old_list=[[1,2,3],[4,5,6],[7,8,9]]
new_list=copy.copy(old_list)
print("lod list:",old_list)
print("new_list:", new_list)

# adding elements to the old_list using shallow copy
old_list.append([5,5,5])
print("old_list:",old_list)
print("new_list:",new_list)

# copying a list using deep copy
import copy
old_list=[[1,1,1],[22,2,2],[3,3,3]]
new_list=copy.deepcopy(old_list)
print("old_list:", old_list)
print("new_list:",new_list)
print("id of old_list - > ",id (old_list))
print("id of new_list - > ",id (new_list))