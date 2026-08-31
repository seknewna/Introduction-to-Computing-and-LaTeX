#!/usr/bin/env bash
#
# Chapter 01 — Terminal & File Basics
# Real commands from this lesson: cd, mkdir, touch, cat, echo, rm, pwd,
# cp, alias, man, ls -a, ls -l, grep -A/-B/-C/-i/-o/-v, less/more.

mkdir -p foo && cd foo

pwd                          # confirm where you are (CWD)
touch lesson-1.txt
echo hi > lesson-1.txt
cat lesson-1.txt
cp lesson-1.txt lesson-2.txt
rm lesson-1.txt lesson-2.txt

echo
echo "Hidden files start with a dot and are skipped by plain ls:"
touch .lesson.txt
ls                           # .lesson.txt is not listed
ls -a                        # now it shows up
ls -l .lesson.txt
rm .lesson.txt

echo
echo "grep context flags — build a small file to search:"
printf 'a\nb\nc\n' > file.txt
grep -A1 b file.txt          # 1 line of context After the match
grep -i B file.txt           # case-Insensitive
grep -o b file.txt           # Only print the matched text
grep -v b file.txt           # Invert — show non-matching lines
rm file.txt

echo
echo "man rm shows -i (confirm before delete) — worth aliasing:"
echo "  alias rm='rm -i'"

cd .. && rm -rf foo
