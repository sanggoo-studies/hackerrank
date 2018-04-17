
let currentLine = 0;
function readLine() {
	return input.split(/(?:\r\n|\r|\n)/g)[currentLine++];
}

function regexVar() {
	return /^(Mr?s|[MDE]r)\.[A-Z][A-Za-z]*$/g;
}

const input = 'Mr.X\n' +
	'Mrs.Y\n' +
	'Dr#Joseph\n' +
	'Er .Abc\n' +
	'Dr.abc';

let lines = input.split('\n').filter((v) => v.trim() !== '').length;
while(currentLine < lines) {
	const re = regexVar();
	const s = readLine();

	console.log(re.test(s));
}
