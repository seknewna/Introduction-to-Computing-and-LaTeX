#!/usr/bin/env bash
#
# Chapter 15 — PS1 & Customizing Bash
# Real commands: PS1 escape sequences, shopt -s cdspell/autocd,
# conditional aliases for ~/.bashrc.

echo "Current PS1:"
echo "$PS1"

echo
echo "A custom prompt using \u \h \w — user, host, working directory:"
echo '  PS1="\u@\h:\w\$ "'

echo
echo "Two interactive-only shell options worth turning on in .bashrc:"
echo '  shopt -s cdspell   # forgives small typos in cd targets'
echo '  shopt -s autocd    # typing a directory name alone cd'"'"'s into it'

echo
echo "A conditional alias — only defined if the feature is supported:"
echo '  ls --color=auto &>/dev/null && alias ls="ls --color=auto"'

echo
echo "Readline shortcuts worth practicing at the prompt (not scriptable):"
echo "  Ctrl+W   delete one word back"
echo "  Ctrl+U   delete to start of line"
echo "  Ctrl+R   reverse search through history"
