const dpadButtons = document.querySelectorAll('#dpad button');

handleInteractionStart = (event) => {
	event.preventDefault()
	console.log(`${event.currentTarget.id} has started ${event.type}`);
	fetch('/control', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			direction: event.currentTarget.id,
			event: 'start',
		})
	})
};

handleInteraction = (event) => {
	event.preventDefault()
	console.log(`${event.currentTarget.id} was ${event.type}ed`);
};

handleInteractionEnd = (event) => {
	event.preventDefault()
	console.log(`${event.currentTarget.id} has stopped ${event.type}`);
	fetch('/control', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			direction: event.currentTarget.id,
			event: 'end',
		})
	})
};

for (const btn of dpadButtons) {
	btn.addEventListener('mousedown', handleInteractionStart);
	btn.addEventListener('touchstart', handleInteractionStart);

	btn.addEventListener('click', handleInteraction);
	btn.addEventListener('touch', handleInteraction);

	btn.addEventListener('mouseup', handleInteractionEnd);
	btn.addEventListener('touchend', handleInteractionEnd);
}
