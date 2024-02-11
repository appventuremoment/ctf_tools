with open("Remove Unneeded Characters from File\Trollr.txt", 'r') as file:
	result = file.read()
	result = ''.join([i for i in result if not i.isdigit() and not i.isspace()])
	#result = ''.join([i for i in result if i.isalpha()])
	print(result)
