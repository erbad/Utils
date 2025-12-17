# DIFFERENT SCRIPTS FOR EVERYDAY USE

# Remove all lines starting with # and empty lines from a file
# Then print the third column and sort it numerically
# Finally, print the first value of the sorted list, that is the minimum
minimum=$(sed '/^#/d;/^\s*$/d' file.dat | awk '{print $3}' | sort -n | head -n 1)

# Find how many times a value is under a cutoff and the minimum in a file.
# Then print them together
u=$(awk -v cutoff=0.5 '{if ($1<cutoff) under+=1} END {print under}' file) 
m=$(awk -v min=10 '{if ($1<min) min=$1} END {print min}' file) # min here at the beginning is a number extremely huge 
echo $u $m

# Function to call with a md.log file. 
# It returns the average of performance (checkpoint N/N-1) of the run in ns/day.

performance() {
        grep checkpoint $1 | awk '{print $4}' | awk 'BEGIN{prev=$1} {now=$1; dt=now-prev; perf+=dt*4*96/1000000; n++; prev=now} END {print perf/(n-1)}'
}



