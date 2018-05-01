let res = document.getElementById('res');
let strRes = '';

document.getElementById('btn0').addEventListener('click', function() {
	strRes += '0';
	res.innerHTML = strRes;
});

document.getElementById('btn1').addEventListener('click', function() {
	strRes += '1';
	res.innerHTML = strRes;
});

document.getElementById('btnClr').addEventListener('click', function() {
	strRes = '';
	res.innerHTML = strRes;
});

document.getElementById('btnEql').addEventListener('click', function() {
	let exp = res.innerHTML.match(/([01]+)([\+=\/\*])([01]+)/);

	let num1 = parseInt(exp[1], 2)
	let num2 = parseInt(exp[3], 2);
	let result = 0;

	console.log(num1, num2);

	switch(exp[2]) {
		case '+':
			result = num1 + num2;
			break;
		case '-':
			result = num1 - num2;
			break;
		case '*':
			result = num1 * num2;
			break;
		case '/':
			result = Math.round(num1 / num2);
			break;
	}

	strRes = (result).toString(2);
	res.innerHTML = strRes;
});

document.getElementById('btnSum').addEventListener('click', function() {
	strRes += '+';
	res.innerHTML = strRes;
});

document.getElementById('btnSub').addEventListener('click', function() {
	strRes += '-';
	res.innerHTML = strRes;
});

document.getElementById('btnMul').addEventListener('click', function() {
	strRes += '*';
	res.innerHTML = strRes;
});

document.getElementById('btnDiv').addEventListener('click', function() {
	strRes += '/';
	res.innerHTML = strRes;
});