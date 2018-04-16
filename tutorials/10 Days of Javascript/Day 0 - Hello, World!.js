
let currentLine = 0;
function readLine() {
	return input.split(/(?:\r\n|\r|\n)/g)[currentLine++]
}

function greeting(parameterVariable) {
	// This line prints 'Hello, World!' to the console:
	console.log('Hello, World!');

	console.log(parameterVariable);
}

const input = 'Welcome to 10 Days of JavaScript!\n' +
	'Welcome to 20 Days of JavaScript!';

const parameterVariable = readLine()
greeting(parameterVariable);
