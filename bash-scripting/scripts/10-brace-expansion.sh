#!/usr/bin/env bash
#
# Chapter 10 — Brace Expansion
# Real commands: {a,b,c} comma lists, {1..N} numeric ranges, and
# combining braces with a shared filename prefix.

echo "Comma list:"
echo {hello,world}

echo
filename='my-file'
echo "Prefix + comma list, useful for generating related filenames:"
echo "$filename."{txt,jpg,mov}

echo
echo "Numeric range with a step:"
echo {1..20..5}

echo
echo "Combined with globbing — braces don't require the files to exist,"
echo "unlike a glob pattern:"
mkdir -p files
touch files/{foo,bar}.txt
printf '<%s>\n' files/{foo,bar}.txt
rm -rf files
