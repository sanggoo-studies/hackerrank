
let currentLine = 0;
function readLine() {
	return input.split(/(?:\r\n|\r|\n)/g)[currentLine++]
}

function getSecondLargest(nums) {
	return nums.filter((v, i, s) => s.indexOf(v) === i).sort((a, b) => a - b).reverse()[1];
}

const input = '5\n' +
	'2 3 6 6 5\n' +
	'10\n' +
	'1 2 3 4 5 6 7 8 9 10\n';

let lines = input.split('\n').filter((v) => v.trim() !== '').length;
while(currentLine < lines) {
	const n = +(readLine());
	const nums = readLine().split(' ').map(Number);
	console.log(getSecondLargest(nums));
}

