 * Run below command
```
:(){ :|: & };:
```
 
# This is Fork Bomb.
It is a program which harms a system by making it run out of memory. It forks processes infinitely to fill memory. The fork bomb is a form of denial-of-service (DoS) attack against a Linux based system.

The fork bomb is a form of denial-of-service (DoS) attack against a Linux based system. It makes use of the fork operation.
Once a successful fork bomb has been activated in a system it may not be possible to resume normal operation without rebooting the system as the only solution to a fork bomb is to destroy all instances of it

# Explaination:-
```
:(){ :|:& };: is nothing but a bash function.
```

This function get executed recursively. It is often used by sys admin to test user process limitations. Linux process limits can be configured via /etc/security/limits.conf and PAM.

Once a successful fork bomb has been activated in a system it may not be possible to resume normal operation without rebooting the system as the only solution to a fork bomb is to destroy all instances of it.

Step by Step Explanation of the script:

fork() bomb is defined as follows:
```
:(){
 :|:&
};:

```
       
:() means you are defining a function named :
{:|: &} means run the function : and send its output to the : function again and run that in the background.

:|: – it will call itself using programming technique called recursion and pipes the output to another call of the function ‘:’
       Therefore, ‘:|:’ simply gets two copies of ‘:’ loaded whenever ‘:’ is called
& – Puts the function call in the background,  disown the functions, if the first ‘:’ is killed, all of the functions that it has started should NOT be auto-killed(child cannot die) and start eating system resources.
; – Terminate the function definition
: – Call (run) the function aka set the fork() bomb.

Here is more human readable code:
```
bomb() {
 bomb | bomb &
}; bomb

```

Essentially we are creating a function that calls itself twice every call and doesn’t have any way to terminate itself. It will keep doubling up until you run out of system resources.


# How it Works

Fork bombs operate both by consuming CPU time in the process of forking, and by saturating the operating system’s process table. A basic implementation of a fork bomb is an infinite loop that repeatedly launches new copies of itself.
To incapacitate a system, they rely on the assumption that the number of programs and processes which may execute simultaneously on a computer. fork() will generate new process but if you put this process in while true loop, then it will create many processes and when the limit is crossed, your system will crash.

# Way to prevent the fork() Bomb

*   Avoid use of fork in any statement which might end up into an infinite loop.
*   Limit the process of fork as below :-
      Login as root, and edit the file( /etc/security/limits.conf ), to add users and configure, their limit.
      Edit the file as:
```
         your_user_name hard nproc 10
```
      now your_user_name can create 10 process

# Some Blogs

  * https://www.geeksforgeeks.org/fork-bomb/
  * https://www.cyberciti.biz/faq/understanding-bash-fork-bomb/
