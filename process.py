import sys
import datetime
now = datetime.datetime.now()
title = "Data on killed and injured Palestinians in Gaza since 07/10/23"
subtitle = f"Data captured on {now}"

print(f"<h1>{title}</h1>")
print(f"<h2>{subtitle}</h2")

print("<pre>")
for line in sys.stdin:
  print(line)
print("</pre>")
