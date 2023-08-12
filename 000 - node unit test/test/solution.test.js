const solution = require("../solution");

var assert = require("assert");
describe("Solution", function () {
    describe("sum()", function () {
        it("should return 3 to sum 1 + 2", function () {
            assert.equal(solution.sum(1, 2), 3);
        });
    });
});
