
let currentLine = 0;
function readLine() {
	return input.split(/(?:\r\n|\r|\n)/g)[currentLine++];
}

function getCount(objects) {
	let count = 0;
	for(let i in objects) {
		if(objects[i].x === objects[i].y) {
			count++;
		}
	}
	return count;
}

const input = '5\n' +
	'1 1\n' +
	'2 3\n' +
	'3 3\n' +
	'3 4\n' +
	'4 5';

let lines = input.split('\n').filter((v) => v.trim() !== '').length;
while(currentLine < lines) {
	const n = +(readLine());
	let objects = [];

	for (let i = 0; i < n; i++) {
		const [a, b] = readLine().split(' ');

		objects.push({x: +(a), y: +(b)});
	}

	console.log(getCount(objects));
}
