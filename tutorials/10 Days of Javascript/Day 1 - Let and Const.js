
let currentLine = 0;
function readLine() {
	return input.split(/(?:\r\n|\r|\n)/g)[currentLine++]
}

function func() {
	const PI = Math.PI;
	let r = readLine();

	console.log(PI * r * r);
	console.log(2 * PI * r);
}

const input = '2.6';

func();