const fetch = require("node-fetch");
const helpers = require("./global-setup");

describe("Electron app environment", function () {
	beforeAll(function (done) {
		helpers.startApplication("tests/configs/default.js");
		helpers.getDocument(done);
	});
	afterAll(function () {
		helpers.stopApplication();
	});

	it("get request from http://localhost:8080 should return 200", function (done) {
		fetch("http://localhost:8080").then((res) => {
			expect(res.status).toBe(200);
			done();
		});
	});

	it("get request from http://localhost:8080/nothing should return 404", function (done) {
		fetch("http://localhost:8080/nothing").then((res) => {
			expect(res.status).toBe(404);
			done();
		});
	});

	it("should show the title MagicMirror²", function () {
		const elem = document.querySelector("title");
		expect(elem).not.toBe(null);
		expect(elem.textContent).toBe("MagicMirror²");
	});
});
