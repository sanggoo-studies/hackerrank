let btns = '';
for(let i = 1; i < 10; i++) {
	btns += '<button id="btn' + i +'">' + i + '</button>';
}
document.getElementById('btns').innerHTML = btns;

btns = [];
for(let i = 1; i < 10; i++) {
	btns.push(document.getElementById('btn' + i));
}

document.getElementById('btn5').addEventListener('click', function() {
	let first = btns[0].innerHTML;
	btns[0].innerHTML = btns[3].innerHTML;
	btns[3].innerHTML = btns[6].innerHTML;
	btns[6].innerHTML = btns[7].innerHTML;
	btns[7].innerHTML = btns[8].innerHTML;
	btns[8].innerHTML = btns[5].innerHTML;
	btns[5].innerHTML = btns[2].innerHTML;
	btns[2].innerHTML = btns[1].innerHTML;
	btns[1].innerHTML = first;
})