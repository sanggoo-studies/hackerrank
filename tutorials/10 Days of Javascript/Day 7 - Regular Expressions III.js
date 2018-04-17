
let currentLine = 0;
function readLine() {
	return input.split(/(?:\r\n|\r|\n)/g)[currentLine++];
}

function regexVar() {
	return /[0-9]+/g;
}

const input = '102, 1948948 and 1.3 and 4.5\n' +
	'1 2 3';

let lines = input.split('\n').filter((v) => v.trim() !== '').length;
while(currentLine < lines) {
	const re = regexVar();
	const s = readLine();

	const r = s.match(re);

	for (const e of r) {
		console.log(e);
	}
}
