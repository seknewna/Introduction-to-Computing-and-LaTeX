#!/usr/bin/env bash
#
# Chapter 02 — Man Pages, Variables & Permissions
# Real commands: man, help, compgen -b, which, type, file, $PATH,
# built-in variables, chmod, stat.

echo "man covers real programs on disk; bash builtins have their own help:"
echo "  man cp        # a real program"
echo "  help history  # history is a shell builtin, not a program"
echo "  compgen -b    # lists every builtin"

echo
echo "which finds programs on \$PATH; it fails on builtins — type works on both:"
which ls
type history

echo
echo "file tells you what kind of file something is:"
file /usr/bin/ls 2>/dev/null || file /bin/ls

echo
echo "\$PATH is a colon-separated list — split it onto separate lines:"
echo "$PATH" | tr ':' '\n' | head -5

echo
echo "A few variables bash sets for you:"
echo "PWD=$PWD"
echo "USER=$USER"
echo "SHELL=$SHELL"

echo
echo "Capture a command's output into a variable:"
now=$(date)
echo "now=$now"

echo
echo "Permissions — chmod +x is what makes a script directly runnable:"
touch demo-script.sh
stat demo-script.sh | head -4
chmod +x demo-script.sh
ls -lha demo-script.sh
rm demo-script.sh
