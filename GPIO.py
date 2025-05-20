import RPi.GPIO as GPIO

mode = GPIO.getmode()
print(f"Mode is {mode}\n")

channel_one= 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel_one, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

with open("results.txt", "w") as logfile:
    try:
        while True:
            edge_channel = GPIO.wait_for_edge(channel_one, GPIO.BOTH)
            logfile.write(f"GPIO value: {edge_channel}")
            logfile.flush()
    except KeyboardInterrupt:
        print("Concluded")
    finally:
        GPIO.cleanup()
