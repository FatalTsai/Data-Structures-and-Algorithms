OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRIORITY = {'+':1, '-':1, '*':2, '/':2}


def infixtopostfix(form):
	stack = []
	output = ''

	for op in form:
		if op not in OPERATORS:
			output += op
		elif op == '(':
			stack.append('(')
		elif op == ')':
			while stack and stack[-1] != '(':
				output += stack.pop()
			stack.pop()
		else:
			while stack and stack[-1] != '(' and PRIORITY[op] <= PRIORITY[stack[-1]]:
				output += stack.pop()
			stack.append(op)
	while stack: 
		output+= stack.pop()
	print(output)
	return output

infixtopostfix("10 + 3 * 5 / (16 - 4)")
infixtopostfix("(A + B) * (C + D + E)")
 
