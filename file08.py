def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    m=0
    for i in range(len(data)):
        if data[i].isdigit():
            if m<int(data[i]):
                m=int(data[i])
    return m
f=open('txt_file/data08.txt')
a=f.read()
print(main(a))
# Read data from file