#!/usr/bin/env bash
#
# Chapter 17 — Forkbombs & Course Wrap-up
#
# This chapter covers the classic bash forkbomb: a function that
# recursively spawns two copies of itself in the background, forever,
# exhausting process slots or memory. It's a well-known piece of shell
# trivia (search "bash fork bomb" for the one-liner), included here
# for recognition only — this file deliberately does not include or
# execute one.
#
# If you ever want to see the effect safely, do it only in a disposable
# VM or container, and cap your process count first:
#   ulimit -u 100

echo "A forkbomb defines a function that calls itself twice, piped"
echo "together and backgrounded, doubling the process count on every"
echo "generation until the system runs out of room."

echo
echo "That wraps up Part 1 — Bash Scripting."
echo "Next up: Part 2 — R Programming."
