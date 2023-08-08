function solution(incase) {
    let in_roll = 0;
    let max_in_roll = 0;
    while (incase > 0) {
        let is_one = incase % 2 != 0;
        if (is_one) {
            in_roll++;
        } else {
            max_in_roll = Math.max(max_in_roll, in_roll);
            in_roll = 0; 
        }
        incase = Math.floor(incase / 2);
    }
    max_in_roll = Math.max(max_in_roll, in_roll)
    return max_in_roll;
}

let tests = [
    {
        incase: 5,
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
