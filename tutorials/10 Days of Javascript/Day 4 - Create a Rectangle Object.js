
let currentLine = 0;
function readLine() {
	return input.split(/(?:\r\n|\r|\n)/g)[currentLine++];
}

function Rectangle(a, b) {
	this.length = a;
	this.width = b;
	this.perimeter = a * 2 + b * 2;
	this.area = a * b;
}

const input = '4\n' +
	'5';

let lines = input.split('\n').filter((v) => v.trim() !== '').length;
while(currentLine < lines) {
	const a = +(readLine());
	const b = +(readLine());

	const rec = new Rectangle(a, b);

	console.log(rec.length);
	console.log(rec.width);
	console.log(rec.perimeter);
	console.log(rec.area);
}
