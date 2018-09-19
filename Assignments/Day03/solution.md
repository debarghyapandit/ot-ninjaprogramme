
# Assignment 3

# Task 1: Read about the below topics

#- sed (stream editor)
  SED command in UNIX is stands for stream editor and it can perform lot’s of function on file like, searching, find and replace,   insertion or deletion. Though most common use of SED command in UNIX is for substitution or for find and replace. By using SED you can edit files even without opening it, which is much quicker way to find and replace something in file, than first opening that file in VI Editor and then changing it.

The basic usage is:

sed [options] commands [file-to-edit]

General syntax for sed −

/pattern/action

Some important Blogs:
https://www.digitalocean.com/community/tutorials/the-basics-of-using-the-sed-stream-editor-to-manipulate-text-in-linux
https://www.computerhope.com/unix/used.htm
https://www.tutorialspoint.com/unix/unix-regular-expressions.htm
https://www.tecmint.com/linux-sed-command-tips-tricks/
https://www.linuxtechi.com/20-sed-command-examples-linux-users/


-awk
  Awk is a programming language which allows easy manipulation of structured data and the generation of formatted reports. Awk stands for the names of its authors “Aho, Weinberger, and Kernighan”
The Awk is mostly used for pattern scanning and processing. It searches one or more files to see if they contain lines that matches with the specified patterns and then perform associated actions.

Some of the key features of Awk are:

  - Awk views a text file as records and fields.
  - Like common programming language, Awk has variables, conditionals and loops
  - Awk has arithmetic and string operators.
  - Awk can generate formatted reports
  - Awk reads from a file or from its standard input, and outputs to its standard output. Awk does not get along with non-text files.

Awk Blog:
https://www.thegeekstuff.com/2010/01/awk-introduction-tutorial-7-awk-print-examples
https://www.cse.iitb.ac.in/~br/courses/cs699-autumn2013/refs/awk-tutorial.html
https://likegeeks.com/awk-command/

- shebang
  The shebang is a special character sequence "#!" located at the top of many script file that specifies which program should be called to run the script. The shebang is always on the first line of the file, and is composed of the characters #! followed by the path to the interpreter program. 
 For example, in a shell script, the complete line may look similar to the following:
 #!/bin/bash

The #! syntax used in scripts to indicate an interpreter for execution of script under UNIX / Linux operating systems.

- exit status
  Each Linux command returns a status when it terminates normally or abnormally. You can use command exit status in the shell script to display an error message or take some sort of action.

Exit codes are a number between 0 and 255, which is returned by any Unix command when it returns control to its parent process.
Other numbers can be used, but these are treated modulo 256, so exit -10 is equivalent to exit 246, and exit 257 is equivalent to exit 1.
These can be used within a shell script to change the flow of execution depending on the success or failure of commands executed.
Success is traditionally represented with exit 0; failure is normally indicated with a non-zero exit-code.

check exit status of command using echo $?

