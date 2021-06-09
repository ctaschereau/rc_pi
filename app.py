from flask import Flask, render_template, request
from gpiozero import Motor
from time import sleep

motor = Motor(17, 18, None, True)

app = Flask(__name__)

speed = 1.0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
	global speed

	if request.json['event'] == 'click':
		if request.json['direction'] == 'right':
			if speed < 1.0:
				speed = speed + 0.1
		
		if request.json['direction'] == 'left':
			if speed > 0.0:
				speed = speed - 0.1
		print('Speed is now : ' + str(speed))

	if request.json['event'] == 'start':
		if request.json['direction'] == 'up':
			motor.forward(speed)
		
		if request.json['direction'] == 'down':
			motor.backward(speed)

	if request.json['event'] == 'end':
		motor.stop()
		
			
	
	return ('', 204)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
