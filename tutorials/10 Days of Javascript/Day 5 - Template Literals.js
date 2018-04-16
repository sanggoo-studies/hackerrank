
let currentLine = 0;
function readLine() {
	return input.split(/(?:\r\n|\r|\n)/g)[currentLine++];
}

function sides(literals, ...expressions) {
	const P = expressions[1];
	const A = expressions[0];

	return [
		(P + Math.sqrt(P * P - 16 * A)) / 4,
		(P - Math.sqrt(P * P - 16 * A)) / 4
	].sort()
}

const input = '10\n' +
	'14';

let lines = input.split('\n').filter((v) => v.trim() !== '').length;
while(currentLine < lines) {
	let s1 = +(readLine());
	let s2 = +(readLine());

	[s1, s2] = [s1, s2].sort();

	const [x, y] = sides`The area is: ${s1 * s2}.\nThe perimeter is: ${2 * (s1 + s2)}.`;

	console.log((s1 === x) ? s1 : -1);
	console.log((s2 === y) ? s2 : -1);
}
