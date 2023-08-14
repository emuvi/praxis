function designerPdfViewer(h, word) {
    let max = 0;
	let chars = word.split('');
	for (let ch of chars) {
		let index = ch.charCodeAt(0) - 97;
		let height = h[index];
		max = Math.max(max, height);
	}
	return max * chars.length;
}


function solution() {
	let tests = [
		{
			incase: {
				h: [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
				w: "abc"
			},
			expect: 9
		},
		{
			incase: {
				h: [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7],
				w: "zaba"
			},
			expect: 28
		}
	];
	for (let i in tests) {
		let incase = tests[i].incase;
		let expect = tests[i].expect;
		let result = designerPdfViewer(incase.h, incase.w);
		if (result === expect) {
			console.log("Ok in ", i);
		} else {
			console.log("Fail in ", i);
		}
	}
}