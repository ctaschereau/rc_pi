from flask import Flask, render_template, request
import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
	print(request.json['direction'])
	print(request.json['event'])
	GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
	GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
	GPIO.output(8, GPIO.HIGH) # Turn on
	sleep(1)                  # Sleep for 1 second
	GPIO.output(8, GPIO.LOW)  # Turn off
	GPIO.cleanup()
	return ('', 204)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')