def get_permutations(string: str):
    def helper(temp):
        if len(temp) == len(string):
            output.append(temp)
            return
        

        for i in range(len(string)):
            if (not string[i] in temp):  
                temp += string[i]
                helper(temp)
                temp = temp[:len(temp)-1]

    
    output = []
    helper("")

    return output


    

print(get_permutations("qwbr"))


