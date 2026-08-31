#!/usr/bin/env bash
#
# Chapter 16 — Common Pitfalls
# Real commands: the classic `for f in $(ls)` bug, alias argument
# limitations, and ANSI codes inflating string length.

mkdir -p files
touch files/a files/b "files/d      e"

echo "The fragile way — breaks on filenames containing spaces:"
for f in $(ls files); do
    echo "  bad: $f"
done

echo
echo "The safe way — glob directly, no ls, no word-splitting:"
for f in files/*; do
    echo "  good: $f"
done

rm -rf files

echo
echo "Aliases can't take positional arguments the way functions can:"
shopt -s expand_aliases
alias greet-alias='echo hello \$1'   # \$1 never gets replaced
greet-alias world

greet-func() { echo "hello $1"; }
greet-func world

echo
echo "ANSI color codes count toward string length even though they're"
echo "invisible on screen:"
colored=$'\e[33mHello\e[0m'
echo "visible text is 5 characters, but \${#colored} reports: ${#colored}"
