#!/usr/bin/env bash
#
# Chapter 06 — Bash Arguments, Pipe Status & Timing
# Real commands: bash -x (trace), bash -n (syntax check), bash -u
# (error on unset vars), PIPESTATUS, time.

cat > sample.sh << 'INNER_EOF'
#!/usr/bin/env bash
first_name='john'
last_name='eddy'
echo "Hello $first_name $last_name!"
INNER_EOF

echo "bash -n only checks syntax, it does not run the script:"
bash -n sample.sh && echo "syntax OK"

echo
echo "bash -x traces every command as it executes:"
bash -x sample.sh

rm sample.sh

echo
echo "PIPESTATUS holds the exit code of every stage in a pipeline, not"
echo "just the last one that \$? would give you:"
true | false | true
echo "PIPESTATUS: ${PIPESTATUS[@]}"

echo
echo "time reports real/user/sys time for a command:"
time sleep 0.2
