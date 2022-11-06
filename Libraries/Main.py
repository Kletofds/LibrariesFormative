################################################
# Kelton Figurski
# Main Code
################################################

import time


from Modules import Simple

print(f"Currently running: {Simple.file_name}")

time.sleep(1)

Simple.spell_numbers(5)

time.sleep(2)


from Modules import Return

print("\nNow running:", {Return.file_name})
time.sleep(1)

returned_list = Return.numbers(1, 25)
print(returned_list)

time.sleep(2)



