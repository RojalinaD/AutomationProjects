# Find if a substr is present in a string


def findsubstr(s1,sub1):
    if len(sub1) > len(s1):
        return False
    else:
         if s1.find(sub1) == -1:
             print("substring not found")

         else:
             print("substring found")



str1 = "Programming"
substr = "gram"

findsubstr(str1,substr)