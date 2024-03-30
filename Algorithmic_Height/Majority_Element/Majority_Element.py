# With Sorting 


# Divied AND Conquer
def count(arr,k,l,r):
    c=0
    for i in range(l,r+1):

        if arr[i]==k:
            c+=1
    return c
def majority_element(arr,l,r):
    
    if l==r:
        return arr[l]
    mid = l+ ((r-l)//2)
    # print(mid)
    # print(l,r)
    left_majority_element = majority_element(arr,l,mid)
    right_majority_element= majority_element(arr,mid+1,r)
    #print(f"l,r,leftmaj,rightmaj:{l,r,left_majority_element,right_majority_element}")

    if left_majority_element==right_majority_element:
        return left_majority_element
    if count(arr,left_majority_element,l,r) > (r-l+1)//2:
        return left_majority_element
    elif count(arr,right_majority_element,l,r) > (r-l+1)//2:
        return right_majority_element
    else: 
        return -1
    
array=[8, 7, 7 ,7, 1, 7, 3, 7]
print(majority_element(array,l=0,r=len(array)-1))

with open("rosalind_maj (2).txt") as f_in:
    n,k=[int(i) for i in f_in.readline().rstrip().split(" ")]
    for _ in range(k):
        array=[str(x) for x in f_in.readline().split(" ")]
        with open("output.txt","a") as f_out:
            #f_out.write(" FGG")
            f_out.write(str(majority_element(array,l=0,r=len(array)-1))+" ")
            print(str(majority_element(array,l=0,r=len(array)-1)),end=" ")


   
