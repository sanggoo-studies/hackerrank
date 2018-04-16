
let currentLine = 0;
function readLine() {
	return input.split(/(?:\r\n|\r|\n)/g)[currentLine++];
}

function isPositive(a) {
	if(a > 0) {
		return 'YES';
	} else {
		if(a === 0) {
			throw Error('Zero Error');
		} else {
			throw Error('Negative Error');
		}
	}
}

const input = '3\n' +
	'1\n' +
	'2\n' +
	'3\n' +
	'3\n' +
	'2\n' +
	'0\n' +
	'6\n' +
	'2\n' +
	'-1\n' +
	'20';

let lines = input.split('\n').filter((v) => v.trim() !== '').length;
while(currentLine < lines) {
	const n = +(readLine());

	for (let i = 0; i < n; i++) {
		const a = +(readLine());

		try {
			console.log(isPositive(a));
		} catch (e) {
			console.log(e.message);
		}
	}
}
