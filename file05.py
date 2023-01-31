def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    l=[]
    a=0
    b=0
    for i in range(len(data)):
        if data[i].isdigit():
            a+=1
        else:
            b+=1
    l.append(a)
    l.append(b)
    return l
f=open('txt_file/data05.txt')
c=f.read()
print(main(c)) 
# Read data from file