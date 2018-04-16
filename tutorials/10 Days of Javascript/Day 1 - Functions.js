
let currentLine = 0;
function readLine() {
	return input.split(/(?:\r\n|\r|\n)/g)[currentLine++]
}

function factorial(n) {
	return n > 1 ? n * factorial(n - 1) : 1;
}

const input = '4';

const n = +(readLine());

console.log(factorial(n));
