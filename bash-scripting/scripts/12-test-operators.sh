#!/usr/bin/env bash
#
# Chapter 12 — Test Operators
# Real commands: help '[[', help '[', help test, and quoted
# ANSI-C ($'...') strings.

touch demo.txt

[ -f demo.txt ]; echo "[ -f ] exit code: $?"
[[ -f demo.txt && -r demo.txt ]] && echo "[[ ]]: demo.txt exists and is readable"
test -f demo.txt && echo "test: demo.txt exists"

rm demo.txt

echo
echo "Plain echo doesn't interpret backslash escapes by default:"
echo 'line1\nline2'

echo
echo "\$'...' (ANSI-C quoting) does interpret them:"
echo $'line1\nline2'
