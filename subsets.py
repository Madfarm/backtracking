def get_subsets(input: str) -> [str]:
    def helper(temp: str, index: int, ogString: str):
        output.append(temp)

        for i in range(index, len(ogString)):
            temp += ogString[i]
            helper(temp, index + 1, ogString)
            temp = temp[:len(temp) - 1]


    output = []
    helper("", 0, input)


    return output


print(get_subsets("Tia"))