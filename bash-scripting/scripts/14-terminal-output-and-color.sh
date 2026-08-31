#!/usr/bin/env bash
#
# Chapter 14 — Terminal Output & Color
# Real commands: \e[...m ANSI escapes, tput setaf/sgr0, cursor
# save/restore with \e7 and \e8, and the [ -t 1 ] TTY check.

echo -e '\e[1mbold text\e[0m'
echo $'\e[31mred text\e[0m'

echo
echo "tput is a more portable way to reach the same codes:"
tput setaf 2; echo "green via tput"; tput sgr0

echo
echo "Save cursor position, print elsewhere, then restore it:"
printf '\e7'
printf '\e[5;10Hoverwritten text'
printf '\e8'
echo

echo
echo "Only use color if stdout is an actual terminal:"
if [[ -t 1 ]]; then
    echo "stdout is a TTY — color is safe here"
else
    echo "stdout is redirected — skip the escape codes"
fi
