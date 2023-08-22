const { createUser } = require('../src/user.js')


describe('user tests', () => {
	test('creates a user', () => {
		const name = 'sdfg';
		const phone = 'dfgh';
		const testUser = {
			name,
			phone
		}
		expect(createUser(name, phone)).toStrictEqual(testUser);
	});
});