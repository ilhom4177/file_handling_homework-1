def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    x=9
    for i in range(len(data)):
        if data[i].isdigit():
            if x>=int(data[i]):
                x=int(data[i])
    return x
f=open('txt_file/data09.txt')
a=f.read()
print(main(a))
# Read data from file