
def correct_bracketing_advanced(brackets: str):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    for bracket in brackets:
        if bracket in bracket_pairs.values():
            stack.append(bracket)
        elif bracket in bracket_pairs.keys():
            if stack == [] or bracket_pairs[bracket] != stack.pop():
                return False
    return stack == []

if __name__ == '__main__':
    inputs = [['('], ['()'], ['(()())'], [')(()'], ['[{()}]'], ['[{()}'], ['{[()]}'], ['{[(])}'], ['{(([{()}]))}'], ['(((([]{()}))))'], ['{()}[]{[()]()}'], ['[({})]({[()]})[{}]'], ['{[([{()}])]}'], ['{}{}{}[][][][]()()()'], ['{()}'], ['{[()]}[()]{()}[{}]'], ['{[()]}(([])){}{}{[[]]}'], ['{()}{[()]({{}})[{}]}'], ['{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}'], ['{[]{()}}[(([]))]'], ['{[({[{[()]}])]}]'], ['{[(((([])){}))]}'], ['{[()]({[(())]})}'], ['{[(((())))]}'], ['{[(((((((((((()))))))))))))]}'], ['{[()]({[{[]}]})}'], ['{[(()(()))]}'], ['{[((((()))))]}'], ['{[((()))]}[()]{()}'], ['{[((()))(()())()]}'], ['(({{[[()]]}}))'], ['{[((()))]}'], ['[({{[()]}})]'], ['({[()]})[{[()]}]'], ['{[()][()]{}([])}'], [''], ['(((((((((())))))))))'], ['{((())[][])}[{}]({})'], ['()[]{}{[()]()}'], ['()()()()(((((([]))))){{{{{{}}}}}}'], ['(((((({{{{{{[[[[[[]]]]]]}}}}}}))))))'], ['{[()]}{[()]}{[()]}'], ['{[()]}(){}[][]'], ['{[()]}{[((()))]}{[({{}})]}'], ['(((((((((({{{[[[()]]]}}})))))))))))'], ['({[()]}{[()]}[()]{[()]})'], ['({[()]})({[()]})[()]({[()]})'], ['({[()]})({[()]}[()]({[()]}))'], ['({[()]})({[()]})[()]({[()]}))'], ['[({[()]})({[()]})[()]({[()]})]'], ['[[[[[[[[[[[]]]]]]]]]]]'], ['{(((((((((((())))))))))))}'], ['{[()]}{[()]}{[()]}{[()]}{[()]}{[()]}{[()]}{[()]}{[()]}{[()]}'], ['({[()]}{}[()][]{[()]})'], ['({[()]}{}[()][]{[()]}){[()]}{[()]}'], ['({[()]}{[()]}[()]({[()]}))'], ['{[()]}{[()]}{[()]}{[()]}{[()]}{[()]}{[()]}{[()]}{[()]}{[()]}{[()]}'], ['({[()]}{[()]}[()]({[()]}))'], ['{{[[(())]]}}'], ['[]{}()[]{}()'], ['(([([])]))'], ['{[}()]'], ['({[({({})})]})'], ['((([]))){}[]'], ['(())({{[[]]}}){}'], ['{[()]}()[][]{}'], ['(]{}'], [')(((([])))[]{}[]{{}}'], ['[[[]]]({{}})'], ['((((((()))))))'], ['{({({({({})})})})}'], [''], ['([{'], [')]}'], ['({[]})'], ['{[()]}{[()]}'], ['(((((((((('], ['}}}}}}}}'], ['[[[[[[[[[['], ['()[]{}'], ['{(})'], ['{()}[]'], ['{()}[{()}]'], ['({[({[({[})]})]})]'], ['({[({[({[})]})]})'], ['({[({[({[})]})]})]']]
    number_of_executions = 10000
    inputs_len = len(inputs)

    execution_counter = 0
    inputs_counter = 0

    while execution_counter != number_of_executions:
        a = correct_bracketing_advanced(*inputs[inputs_counter])
        inputs_counter += 1

        if inputs_counter == inputs_len:
            inputs_counter = 0
            execution_counter += 1

