#!/usr/bin/env bash
#
# Chapter 08 — Parameter & Array Expansion
# Real commands: case conversion (^ , ,), default/required values
# (:-  ?), replacements (# ## % // ), substrings, array slicing.

s='dave eddy'
echo "uppercase first letter: ${s^}"
echo "uppercase everything:   ${s^^}"

echo
name=${1:-dave}
echo "default if unset: $name"

path=/home/dave/data.txt
echo "strip shortest prefix:  ${path#*/}"
echo "strip longest prefix:   ${path##*/}"
echo "strip shortest suffix:  ${path%/*}"
echo "replace first match:    ${path/a/o}"
echo "replace all matches:    ${path//a/o}"

echo
echo "Substrings by offset and length:"
echo "${s:0:4}"
echo "${s: -4}"

echo
echo "Loop a string one character at a time using substring expansion:"
len=${#s}
for ((i = 0; i < len; i++)); do
    printf '%s' "${s:i:1}"
done
echo

echo
echo "Array expansion works the same way, applied to every element:"
arr=(foo bar baz)
printf '<%s>\n' "${arr[@]/a/1}"
