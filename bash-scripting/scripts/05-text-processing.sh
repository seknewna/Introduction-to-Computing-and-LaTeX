#!/usr/bin/env bash
#
# Chapter 05 — Text Processing
# Real commands: cut, tr, sed, awk -F, grep -c, find -type/-name/-exec.

echo "name,age,city" > people.csv
echo "Alice,30,Boston" >> people.csv
echo "Bob,25,Denver" >> people.csv

echo "cut -d',' -f2 — pull just the age column:"
cut -d',' -f2 people.csv

echo
echo "sed — swap Boston for a placeholder:"
sed 's/Boston/[city]/' people.csv

echo
echo "awk -F',' — print field 1 and field 3, skipping the header:"
awk -F',' 'NR > 1 { print $1, $3 }' people.csv

echo
echo "grep -c — count matching lines instead of printing them:"
grep -c 'Alice' people.csv

rm people.csv

echo
echo "find — locate files by type and name, then act on each match:"
find . -maxdepth 1 -type f -name "*.sh"
find . -maxdepth 1 -type f -name "*.sh" -exec echo "found: {}" \;
