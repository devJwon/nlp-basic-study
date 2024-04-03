'''
Deep Thought
“All right,” said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable.
“You’re really not going to like it,” observed Deep Thought.
“Tell us!”
“All right,” said Deep Thought. “The Answer to the Great Question…”
“Yes…!”
“Of Life, the Universe and Everything…” said Deep Thought.
“Yes…!”
“Is…” said Deep Thought, and paused.
“Yes…!”
“Is…”
“Yes…!!!…?”
“Forty-two,” said Deep Thought, with infinite majesty and calm.”

— The Hitchhiker’s Guide to the Galaxy, Douglas Adams

In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
'''

prompts = input("The answer to the Great Question of Life, the Universe and Everything is...: ")
prompts = prompts.lower()
if prompts == '42' or prompts == 'forty-two' or prompts == 'forty two':
	print("Yes")
else:
	print("No")


# main 함수 사용
'''
def main():
    inputs = input("The answer to the Great Question of Life, the Universe and Everything is...: ")
    inputs = inputs.lower()
    print(deep_thought(inputs))

def deep_thought(prompts):
	if prompts == '42' or prompts == 'forty-two' or prompts == 'forty two':
		return "Yes"
	else:
		return "No"

main()
'''
