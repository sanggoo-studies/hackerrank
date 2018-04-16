
let currentLine = 0;
function readLine() {
	return input.split(/(?:\r\n|\r|\n)/g)[currentLine++];
}

const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
function getDayName(dateString) {
	return days[(new Date(dateString)).getDay()];
}

const input = '10/11/2009\n' +
	'11/10/2010';

let lines = input.split('\n').filter((v) => v.trim() !== '').length;
while(currentLine < lines) {
	const date = readLine();

	console.log(getDayName(date));
}
