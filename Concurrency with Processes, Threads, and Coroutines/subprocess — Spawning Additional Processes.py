


"""
Subprocess provides an API for creating and communicating with secondary processes. 
It is especially good for running programs that produce or consume text, 
since the API supports passing data back and forth through the standard input and output channels of the new process.
"""



import subprocess


# Running External Command

completed = subprocess.run(['ls', '-lh'])

print("ReturnCode :", completed.returncode)



# Capturing Output

print()
print("*" * 40)

completed = subprocess.run(['ls', '-lh'], stdout=subprocess.PIPE,)

print("ReturnCode :", completed.returncode)
print()
print("Have {} bytes in stdout:\n{}".format(len(completed.stdout),
                                            completed.stdout.decode('utf-8')))



# Connecting Segments of a Pipe

print()
print("*" * 40)


cat = subprocess.Popen(
    ['cat', 'index.rst'],
    stdout=subprocess.PIPE,
)

grep = subprocess.Popen(
    ['grep', '..literalinclude::'],
    stdin=cat.stdout,
    stdout=subprocess.PIPE,
)


cut = subprocess.Popen(
    ['cut', '-f', '3', '-d:'],
    stdin=grep.stdout,
    stdout=subprocess.PIPE,
)


end_of_pipe = cut.stdout


print("Included Files :")

for line in end_of_pipe:
    print(line.decode('utf-8').strip())


"""
The above code reproduces the following:

    cat index.rst | grep ".. literalinclude" | cut -f 3 -d:
"""




