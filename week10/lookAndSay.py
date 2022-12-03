def lookandsay(input):
    if input == "0":
        return 
    print(input)
    newInput = int(input / 10)
    return (lookandsay(newInput))
    """ TODO: Write a function that applies the look and say sequence 3 times, 
        using the previous result as the input for the next sequence.
    @param: input [string] --> The initial input.
    @return [string result] - The result of applying the look and say sequence 3 times.
    """

def sum(input):
    sum = 0
    for s in input:
        sum += int(s)
    return sum

def main():
    cases = int(input())
    for _ in range(cases):
        print(sum(lookandsay(str(input()))))

main()