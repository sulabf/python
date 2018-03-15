#import os
#tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])

import os
import sys
CPU_Pct=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))
#print results
print("CPU Usage = " '\n' + CPU_Pct)
sys.stdout = open('t2.txt', 'w')
print("CPU Usage = " '\n' + CPU_Pct)
