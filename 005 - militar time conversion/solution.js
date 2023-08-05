/**
 * Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
 */

function solution(incase) {
    if (!incase) return incase;
    const format = "00:00:00AM";
    const time = incase.substring(0, format.length - 2);
    const hour = parseInt(time.substring(0, 2));
    const remain = time.substring(2);
    const period = incase.substring(format.length - 2);
    if (period === "AM") {
        return ("" + (hour == 12 ? 0 : hour)).padStart(2, "0") + remain;
    } else {
        return ("" + (hour == 12 ? 12 : hour + 12)) + remain;
    }
}

let tests = [
    {
        incase: "12:45:54PM",
        expect: "12:45:54",
    },
    {
        incase: "12:45:54AM",
        expect: "00:45:54",
    },
    {
        incase: "10:00:00AM",
        expect: "10:00:00",
    },
    {
        incase: "01:00:00PM",
        expect: "13:00:00",
    },
    {
        incase: "02:34:00PM",
        expect: "14:34:00",
    },
    {
        incase: "07:12:21PM",
        expect: "19:12:21",
    },
    {
        incase: "12:00:00AM",
        expect: "00:00:00",
    },
    {
        incase: "12:34:21AM",
        expect: "00:34:21",
    },
    {
        incase: "09:35:24AM",
        expect: "09:35:24",
    },
    {
        incase: "12:00:00PM",
        expect: "12:00:00",
    },
    {
        incase: "12:34:21PM",
        expect: "12:34:21",
    },
];

for (let i = 0; i < tests.length; i++) {
    let test = tests[i];
    let incase = test.incase;
    let expect = test.expect;
    let result = solution(incase);
    if (expect === result) {
        console.log('Test', i, 'success!');
    } else {
        console.log('Test', i, ' fail!!!');
        console.log('InCase:');
        console.log(incase);
        console.log('Expect:');
        console.log(expect);
        console.log('Result:');
        console.log(result);
    }
}
