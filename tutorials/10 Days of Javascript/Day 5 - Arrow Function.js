
let currentLine = 0;
function readLine() {
	return input.split(/(?:\r\n|\r|\n)/g)[currentLine++];
}

function modifyArray(nums) {
	return nums.map((n) => n * (n % 2 === 0 ? 2 : 3));
}

const input = '5\n' +
	'1 2 3 4 5';

let lines = input.split('\n').filter((v) => v.trim() !== '').length;
while(currentLine < lines) {
	const n = +(readLine());
	const a = readLine().split(' ').map(Number);

	console.log(modifyArray(a).toString().split(',').join(' '));
}
