from books.request.orders import add_order, delete_order, get_order, get_orders, edit_order


class TestOrders:
    def test_add_order_201(self):
        p = add_order(token='f6903ea4c6ea669997e4e2251699edc82e51c4e84bd6cb703a7f00e93ec8d553',
                      bookId=3, customerName="Lilie")
        assert p.status_code == 201, 'status code is not ok'

    def test_get_orders(self):
        r = get_orders(token='f6903ea4c6ea669997e4e2251699edc82e51c4e84bd6cb703a7f00e93ec8d553')
        assert r.json()[0]["customerName"] == "Lilie", 'customerName is not ok'
        assert r.json()[0]["bookId"] == 3, 'bookId is not ok'
        assert r.json()[1]["customerName"] == "Molly", 'customerName is not ok'
        assert r.json()[1]["bookId"] == 1, 'bookId is not ok'
        assert r.status_code == 200, 'status code is not ok'

    def test_get_order(self):
        r = get_order(token='f6903ea4c6ea669997e4e2251699edc82e51c4e84bd6cb703a7f00e93ec8d553',
                    id="IwPe9Tbs3B-FiICkk_bG-")
        expected = {
            "id": "IwPe9Tbs3B-FiICkk_bG-",
            "bookId": 1,
            "customerName": "Molly",
            "createdBy": "57ff2371096f2104c7690d1392c96aa18e9c078ce21a5797c4de06120199c7cf",
            "quantity": 1,
            "timestamp": 1670619301534
        }
        assert r.status_code == 200, 'status code not ok'
        assert r.json() == expected, 'book datat not ok'

    # def test_delete_order(self):
    #     d = delete_order(token='f6903ea4c6ea669997e4e2251699edc82e51c4e84bd6cb703a7f00e93ec8d553',
    #                      id="5fTWNUrV-bCa0RmHWtE7j")
    #     assert d.status_code == 204, 'status code is not ok'
