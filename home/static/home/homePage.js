var arr = [
	'Java',
	'Python',
	'C++',
	'Django',
	'React',
	'CSS',
	'HTML',
	'JS',
	'Maths',
	'Physics',
	'Chemistry',
	'Biology',
	'Humanities',
	'Law'
];
var el = document.getElementsByClassName('circles')[0];
el = el.children;
let sheet = document.styleSheets[3].cssRules;
console.log(sheet);
for (var i = 0; i < el.length; i++) {
	setText(el[i]);
	let rule = findRule(i);
	let duration = rule.style.animationDuration;
	let delay = rule.style.animationDelay;
	duration = duration == '' ? 25 : parseInt(duration);
	delay = delay == '' ? 0 : parseInt(delay);
	setTimeout(callback, delay * 1000, duration, el[i]);
}
function callback(duration, elem) {
	setInterval(setText, duration * 1000, elem);
}

function setText(elem) {
	let index = Math.floor(Math.random() * arr.length);
	elem.innerHTML = arr[index];
	// let minhw = Math.floor(Math.random() * 10 + 2);
	// elem.style.minHeight = minhw.toString() + 'vw';
	// elem.style.minWidth = elem.style.minHeight;
}

function findRule(index) {
	index = index + 1;
	let selectorText = '.circles li:nth-child(' + index + ')';
	for (j = 0; j < sheet.length; j++) {
		if (sheet[j].selectorText == selectorText) return sheet[j];
	}
}
