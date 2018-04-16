
let currentLine = 0;
function readLine() {
	return input.split(/(?:\r\n|\r|\n)/g)[currentLine++]
}

function getLetter(s) {
	switch(s[0]) {
		case 'a':
		case 'e':
		case 'i':
		case 'o':
		case 'u':
			return 'A';
		case 'b':
		case 'c':
		case 'd':
		case 'f':
		case 'g':
			return 'B';
		case 'h':
		case 'j':
		case 'k':
		case 'l':
		case 'm':
			return 'C';
	}

	return 'D';
}

const input = 'adfgt\n';

const s = readLine()
console.log(getLetter(s));
