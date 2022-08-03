from datetime import datetime

while True:
    t = datetime.now().strftime('%H: %M: %S.%f')[:-3]
    print(t)