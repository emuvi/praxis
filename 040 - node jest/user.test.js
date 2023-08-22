const { createUser } = require('./user.js')

test('creates a user', () => {
	const name = 'sdfg';
	const phone = 'dfgh';
	const testUser = {
		name,
		phone
	}
	expect(createUser(name, phone)).toStrictEqual(testUser);
})