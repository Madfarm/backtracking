def get_subsets_string(input: str) -> [str]:
    def helper(temp, j):
        output.append(temp)

        for i in range(j, len(input)):
            temp += input[i]
            helper(temp, i + 1)
            temp = temp[:len(temp) - 1]


    output = []
    helper("", 0)
    return output    

# print(get_subsets_string("123"))

def get_subsets_list(input: [int]):
    def list_helper(temp, index):
        output.append(temp[:])

        for i in range(index, len(input)):
            temp.append(input[i])
            list_helper(temp, i + 1)
            temp.pop()
    
    output = []
    list_helper([], 0)
    return output

# print(get_subsets_list([1,2,3]))
