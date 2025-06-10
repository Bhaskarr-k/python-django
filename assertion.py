def avg(marks):
    assert len(marks) !=0
    return sum(marks)/len(marks)

mark1=[11,12,14,15]
print("average of mark1:",avg(mark1))

mark1=[]
print("average of mark1:", avg(mark1))