def StringReverse(str, start, end):
    sub_string = str[start:end+1]
    
    if len(sub_string) == 0:
        return sub_string
    else:
        return sub_string[-1] + StringReverse(sub_string[:-1], 0, len(sub_string) - 2)

str = "University of Engineering and Technology Lahore"
start = 20  
end = 40    

print(StringReverse(str, start, end))