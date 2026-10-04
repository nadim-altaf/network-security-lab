Network Security Lab - All programs
Nadim Altaf | Roll No. 2324CUKmr24 | B.Tech 7th Sem

File numbers match the experiment numbers in the report.

Python programs:   python3 <file>.py
  (07 and 08 need PyCryptodome:  pip install pycryptodome)

Experiment 6 - Buffer Overflow Vulnerability (C program):
  gcc -O0 -fno-stack-protector -D_FORTIFY_SOURCE=0 06_buffer_overflow.c -o bof
  ./bof
