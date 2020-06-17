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
	'Law',
	'NEET',
	'JEE'
]; //All the text that will float in the animation editable and appendable
var el = document.getElementsByClassName('circles')[0];
el = el.children;
let sheet = document.styleSheets[3].cssRules;
for (var i = 0; i < el.length; i++) {
	setText(el[i]); //setting el[i].innerhtml to one of the elements from array randomly
	let rule = findRule(i); //importing style of the ith element from animation <li>'s
	let duration = rule.style.animationDuration;
	let delay = rule.style.animationDelay;
	duration = duration == '' ? 25 : parseInt(duration); //mimicking the same style for durations and delay from the style sheet
	delay = delay == '' ? 0 : parseInt(delay); //changing innerHtml of the <li>'s after each animation
	setTimeout(callback, delay * 1000, duration, el[i]);
}
function callback(duration, elem) {
	//Changes the innerHtml of the floating elements after each animation round
	setInterval(setText, duration * 1000, elem);
}

function setText(elem) {
	//Sets the innetHtml of the  elem to a randomly selected text from teh array
	let index = Math.floor(Math.random() * arr.length);
	elem.innerHTML = arr[index];
}

function findRule(index) {
	//Returns the style of teh asked element
	index = index + 1;
	let selectorText = '.circles li:nth-child(' + index + ')';
	for (j = 0; j < sheet.length; j++) {
		if (sheet[j].selectorText == selectorText) return sheet[j];
	}
}
