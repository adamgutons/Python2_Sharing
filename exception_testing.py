import sys
from subprocess import call


def foo():
	python_file = sys.argv[0]
	while True:
		try:
			foo2()
		except:
			#print('shit...')
			call(["python", python_file])
		else: break

def foo2():
	#print(sys.argv[0])
	x = int(input('>> '))



def main():
	foo()

main()