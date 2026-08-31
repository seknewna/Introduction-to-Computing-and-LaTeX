#!/usr/bin/env bash
#
# Chapter 04 — Case Statements, Arrays & Substitution
# Real commands: case/esac, indexed & associative arrays, IFS,
# $(...) command substitution, $((...)) arithmetic, <(...) process sub.

for name in dave bill anyone; do
    case "$name" in
        d*)  echo "matched d*: $name" ;;
        b*)  echo "matched b*: $name" ;;
        *)   echo "matched *: $name"  ;;
    esac
done

echo
echo "Indexed array — note *the difference* between [*] and [@]:"
array=(foo bar baz)
echo "element 0: ${array[0]}"
echo "last element: ${array[-1]}"
echo "all (as one word): ${array[*]}"
echo "all (as separate words): ${array[@]}"

echo
echo "Associative array — string keys instead of positions:"
declare -A capitals=([France]=Paris [Japan]=Tokyo)
for key in "${!capitals[@]}"; do
    echo "$key is ${capitals[$key]}"
done

echo
echo "Command substitution — prefer \$(...) over legacy backticks:"
thing=$(whoami)
echo "thing is $thing"

echo
echo "Arithmetic expression:"
i=0
((i++))
echo "i is $i"
echo "2 + 2 = $((2 + 2))"

echo
echo "Process substitution treats a command's output like a file:"
diff <(printf 'a\nb\n') <(printf 'a\nc\n') || true
