import os

pid = os.fork()

if pid < 0:
    print("Create process error")
elif pid == 0:
    print("New process")
else:
    print("The old process")

print("fork test end...")

