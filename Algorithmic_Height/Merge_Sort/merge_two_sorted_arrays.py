
'''first approach    
def merge_sorted_arrays(arr1,arr2):
    a,b=0,0
    merged_array=[]
    for c in range(n+m):
        if a==len(arr1):
            merged_array.extend(arr2[b:])
            break
        if b==len(arr2):
            merged_array.extend(arr1[a:])
            break        
        if arr1[a]<=arr2[b]:
            merged_array.append(arr1[a])
            a+=1
        else:
            merged_array.append(arr2[b]) 
            b+=1
    return merged_array
    '''
def merge_sorted_arrays(arr1,arr2):
    merged_array=[]
    while arr1 and arr2:
        if arr1[0]>=arr2[0]:
            merged_array += [arr2.pop(0)]
        else:
            merged_array += [arr1.pop(0)]
    merged_array+= arr1+arr2
    return merged_array


if __name__=="__main__":
    with open("rosalind_z.txt") as f:
        n=int(f.readline())
        arr1=[int(x) for x in f.readline().split(" ")]
        m=int(f.readline())
        arr2=[int(x) for x in f.readline().split(" ")]
    with open("output.txt","w") as f:
        f.write(" ".join([str(x) for x in merge_sorted_arrays(arr1,arr2)]))
        print(" ".join([str(x) for x in merge_sorted_arrays(arr1,arr2)]))