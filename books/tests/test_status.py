from books.request.status import get_status


class TestStatus:
    def test_status(self):
        r = get_status()
        assert r.status_code == 200, 'status code is not ok'
