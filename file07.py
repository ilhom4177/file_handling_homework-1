def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    s=0
    for i in range(len(data)):
        if data[i].isdigit():
            s+=int(data[i])
    return s
f=open('txt_file/data07.txt')
a=f.read()
print(main(a))    
# Read data from file