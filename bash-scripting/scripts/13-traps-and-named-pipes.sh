#!/usr/bin/env bash
#
# Chapter 13 — Trap Signals & Named Pipes
# Real commands: trap ... exit, mkfifo, reading/writing a FIFO path.

cleanup() {
    echo "cleanup function running"
}
trap cleanup exit

echo "script starting"
echo "..."
echo "script done"
# 'cleanup' fires here automatically because of the trap on exit

echo
echo "Named pipes let two processes talk through a path on disk:"
pipe="/tmp/course-pipe-$$"
mkfifo "$pipe"

echo "[client] hello" > "$pipe" &
read -r line < "$pipe"
echo "[reader] got: $line"

rm -f "$pipe"
