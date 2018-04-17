
let currentLine = 0;
function readLine() {
	return input.split(/(?:\r\n|\r|\n)/g)[currentLine++];
}

function regexVar() {
	return /^([aeiou]).+\1$/gi;
}

const input = 'bcd\n' +
	'abcd\n' +
	'abcda\n' +
	'abcdo';

let lines = input.split('\n').filter((v) => v.trim() !== '').length;
while(currentLine < lines) {
	const re = regexVar();
	const s = readLine();

	console.log(re.test(s));
}
