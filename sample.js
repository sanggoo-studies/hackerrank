
let currentLine = 0;
function readLine() {
	return input.split(/(?:\r\n|\r|\n)/g)[currentLine++];
}

function func(n) {
	return 0;
}

const input = 'Welcome to 10 Days of JavaScript!\n' +
	'Welcome to 20 Days of JavaScript!';

let lines = input.split('\n').filter((v) => v.trim() !== '').length;
while(currentLine < lines) {
	const n = readLine();
	func(n);
}
