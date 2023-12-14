def get_subsets(input: str) -> [str]:
    def helper(temp, j):
        output.append(temp)

        for i in range(j, len(input)):
            temp += input[i]
            helper(temp, i + 1)
            temp = temp[:len(temp) - 1]


    output = []
    helper("", 0)
    return output    

print(get_subsets("123"))