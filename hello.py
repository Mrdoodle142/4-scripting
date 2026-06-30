#!/usr/bin/env python3
import sys
from datetime import datetime

user_name = sys.argv[1]
current_time = datetime.now().astimezone().strftime("%c")

print (f"Hello {user_name},right now the time is {current_time}" )

