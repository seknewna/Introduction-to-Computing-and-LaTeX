#!/usr/bin/env bash
#
# Chapter 07 — Sourcing Code, Subshells & Return vs. Output
# Real commands: source, { } vs ( ), capturing stdout vs stderr
# separately when calling a function.

cat > lib.sh << 'INNER_EOF'
greet() {
    local name=$1
    echo "hello $name!"
}
INNER_EOF

source lib.sh      # loads greet() into THIS shell
greet dave
rm lib.sh

echo
echo "{ } runs in the current shell; ( ) runs in an isolated subshell:"
{ set_in_brace="yes"; }
echo "set_in_brace=$set_in_brace"
( set_in_paren="yes" )
echo "set_in_paren='${set_in_paren:-unset}'"

echo
echo "A function's stdout and stderr can be redirected independently:"
my-func() {
    echo "this goes to stdout" >&1
    echo "this goes to stderr" >&2
}
output=$(my-func 2>/dev/null)   # keep stdout, throw away stderr
echo "captured: $output"
