def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    s=len(data)
    return s
f=open('txt_file/data02.txt')
a=f.read()
print(main(a))
# Read data from file