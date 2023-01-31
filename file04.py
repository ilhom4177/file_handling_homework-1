def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    l=[]
    for i in range(len(data)):
        if not data[i].isdigit():
            l.append(data[i])
    return l
f=open('txt_file/data04.txt')
a=f.read()
print(main(a))    
# Read data from file