#ShellScript
This is the official ShellScript runner.
#About
ShellScript is a bash/shell command runner written in Python.
#Syntax
Basic ShellScript works like this.

`<shellscript>` - A open ShellScript tag signals that we are going to run ShellScript commands.

`run git init;` - Using the run command will signal that you are going to run a command, in this case, `git init`. Of course you end with a semi-colon to signal that it is the end of the command.

`return git init;` - Using the return command will signal that you wish to return the results of `git init`. Then end with a semi-colon.

`</shellscript>` - Signals we are done running ShellScript commands.