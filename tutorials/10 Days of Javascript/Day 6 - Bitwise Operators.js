
let currentLine = 0;
function readLine() {
	return input.split(/(?:\r\n|\r|\n)/g)[currentLine++];
}

function getMaxLessThanK(n, k) {
	let max = 0
	for(let i = 0; i < n; i++) {
		for(let j = i + 1; j <= n; j++) {
			let v = i & j;
			if(v < k && v > max) {
				max = v
			}
		}
	}
	return max;
}

const input = '3\n' +
	'5 2\n' +
	'8 5\n' +
	'2 2';

let lines = input.split('\n').filter((v) => v.trim() !== '').length;
while(currentLine < lines) {
	const q = +(readLine());

	for (let i = 0; i < q; i++) {
		const [n, k] = readLine().split(' ').map(Number);

		console.log(getMaxLessThanK(n, k));
	}
}
