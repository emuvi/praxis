/*

Two children, Lily and Ron, want to share a chocolate bar. 
Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

* The length of the segment matches Ron's birth month, and,
* The sum of the integers on the squares is equal to his birth day.

Determine how many ways she can divide the chocolate.

*/

function solution(incase) {
    const [s, d, m] = incase;
    function sum(i, c = 0) {
        if (c == m) return 0;
        return s[i] + sum(i + 1, c + 1);
    }
    let count = 0;
    for (let i = 0; i < s.length - (m - 1); i++) {
        if (sum(i) == d) {
            count++;
        }
    }
    return count;
}

let tests = [
    {
        incase: [[4, 1], 4, 1],
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
