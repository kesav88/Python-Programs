#Python Program to Check if the Substring is Present in the Given String

def check_substring(string,substring):
    if substring in string:
        return "substring is present in the string"
    else:
        return "substring is not present in the string"


string="kesava raju"
substring="raju"
print(check_substring(string,substring))