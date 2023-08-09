function solution(path) {
    let level = 0;
    let valleys = 0;
    let kinds = path.split('');
    for (let kind of kinds) {
        if (kind === 'D') {
            if (level === 0) {
                valleys++;
            } 
            level--;
        } else {
            level++;            
        }
    } 
    return valleys;
}

let tests = [
    {
        incase: 'UDDDUDUU',
        expect: 1,
    },
];

for (let i = 0; i < tests.length; i++) {
    let test = tests[i];
    let incase = test.incase;
    let expect = test.expect;
    let result = solution(incase);
    if (expect === result) {
        console.log("Test", i, "success!");
    } else {
        console.log("Test", i, " fail!!!");
        console.log("InCase:");
        console.log(incase);
        console.log("Expect:");
        console.log(expect);
        console.log("Result:");
        console.log(result);
    }
}
