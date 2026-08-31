#!/usr/bin/env bash
#
# Chapter 03 — Finally Scripting
# Real commands: read -p, positional args ($1, $@), functions with
# local, if/[[ ]], for loops (list, range, C-style), I/O redirection.

echo "Take input from the user, or fall back to it if no argument was given:"
if [[ -n $1 ]]; then
    name=$1
else
    name='course-student'   # in place of an interactive read -p prompt
fi
echo "hello $name!"

echo
echo "A function using 'local' so it doesn't leak into the caller's scope:"
my-func() {
    local arg1=$1
    echo "hello from my function, arg1 is $arg1"
}
my-func "$@"

echo
echo "Return codes are separate from printed output:"
check-even() {
    (( $1 % 2 == 0 ))
}
check-even 4 && echo "4 is even (exit code: $?)"

echo
echo "The three for-loop shapes covered in this lesson:"
for name in foo bar baz; do echo "name is $name"; done
for c in {a..c}; do echo "c is $c"; done
for ((i = 0; i < 3; i++)); do echo "i is $i"; done

echo
echo "Reading lines piped in from another command:"
printf 'one\ntwo\n' | while read -r line; do
    echo "got line: $line"
done
