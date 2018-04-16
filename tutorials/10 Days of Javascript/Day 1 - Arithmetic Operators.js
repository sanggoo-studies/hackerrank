
let currentLine = 0;
function readLine() {
	return input.split(/(?:\r\n|\r|\n)/g)[currentLine++]
}

function getArea(length, width) {
	return length * width
}

function getPerimeter(length, width) {
	return length * 2 + width * 2;
}

const input = '3\n' +
	'4.5\n';

const length = +(readLine());
const width = +(readLine());

console.log(getArea(length, width));
console.log(getPerimeter(length, width));
