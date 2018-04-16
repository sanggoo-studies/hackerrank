
let currentLine = 0;
function readLine() {
	return input.split(/(?:\r\n|\r|\n)/g)[currentLine++]
}

function vowelsAndConsonants(s) {
	let i = 0;
	let vowel = ''
	let consonant = ''

	for(i = 0; i < s.length; i++){
		switch(s[i]) {
			case 'a':
			case 'e':
			case 'i':
			case 'o':
			case 'u':
				vowel += s[i];
				break;

			default:
				consonant += s[i];
		}
	}

	vowel += consonant;
	for(i = 0; i < vowel.length; i++) {
		console.log(vowel[i]);
	}
}

const input = 'javascriptloops\n';

const s = readLine()
vowelsAndConsonants(s);
