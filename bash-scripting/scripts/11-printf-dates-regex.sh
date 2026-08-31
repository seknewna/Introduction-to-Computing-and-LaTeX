#!/usr/bin/env bash
#
# Chapter 11 — printf, Date Formatting & Regular Expressions
# Real commands: printf format specifiers (%s %d %5s %-5s %05d),
# date +FORMAT, printf '%(FORMAT)T', regex with [[ =~ ]], mapfile.

echo "printf needs a format string — passing data directly is a bug:"
s='hello world'
printf '%s\n' "$s"

echo
echo "Width and padding:"
printf '%5s|%-5s|\n' hi hi
printf '%05d\n' 55

echo
echo "Date formatting, two ways:"
datefmt='%Y-%m-%d %H:%M:%S'
date "+$datefmt"
printf "%($datefmt)T\n" -1

echo
echo "Matching a pattern with a regex:"
email='user@example.com'
if [[ "$email" =~ ^[^@]+@[^@]+\.[a-z]+$ ]]; then
    echo "'$email' looks like an email"
fi

echo
echo "mapfile reads lines straight into an array:"
printf 'one\ntwo\nthree\n' > lines.txt
mapfile -t lines < lines.txt
echo "line 2: ${lines[1]}"
rm lines.txt
