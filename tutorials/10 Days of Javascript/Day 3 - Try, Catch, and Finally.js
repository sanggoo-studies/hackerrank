
let currentLine = 0;
function readLine() {
	return input.split(/(?:\r\n|\r|\n)/g)[currentLine++]
}

function reverseString (s) {
	try {
		console.log(s.split('').reverse().join(''));
	} catch(e) {
		console.log(e.message);
		console.log(s);
	}
}

const input = '"1234"\n' +
	'Number(1234)';

let lines = input.split('\n').filter((v) => v.trim() !== '').length;
while(currentLine < lines) {
	const s = eval(readLine());
	reverseString (s);
}
