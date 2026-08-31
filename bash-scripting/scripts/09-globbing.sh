#!/usr/bin/env bash
#
# Chapter 09 — Globbing
# Real commands: *, ?, [..] character classes, extglob's !( ) +( ) @( ),
# and the nullglob/dotglob/globstar shell options.

mkdir -p files
touch files/foo.txt files/foo.jpg files/bar.txt files/baz.jpg

echo "Basic wildcard — every .txt file:"
printf '%s\n' files/*.txt

echo
echo "? matches exactly one character:"
printf '%s\n' files/ba?.txt

echo
echo "[..] matches one character from a set:"
printf '%s\n' files/ba[rz].txt

echo
echo "Extended globbing (needs extglob enabled) — everything except .txt:"
shopt -s extglob
printf '%s\n' files/!(*.txt)
shopt -u extglob

echo
echo "nullglob — a non-matching glob expands to nothing instead of the"
echo "literal pattern string:"
shopt -s nullglob
printf '<%s>\n' files/*.md
shopt -u nullglob

rm -rf files
