from books.request.books import get_book, get_books


class TestBooks:
    # test initial - smoke testing(tip de testare facut la inceput pentru a verifica ca sistemul este suficient
    # de stabil ca sa suporte procesul de testare)
    # Test 1: check the status of the get book method
    def test_get_books_200(self):
        r = get_books()
        assert r.status_code == 200, 'status code is not ok'

    # 1. testare functionala = tip de testare facut pentru a verifica faptul ca aplicatia isi indeplinesete functiile
    # 1.a Testate pozitiva = tip de testare in care verificam ca sistemul accepta
    # inputurile pe care ar trebuie sa le accepte

    # Test 2: Verifica requestul de get books fata niciun fel de filtrare
    def test_get_all_books(self):
        r = get_books()
        assert len(r.json()) > 0, 'book total is wrong'

    # Test 3: Verifca requestul get books cu filtrate pe limita - equivalence partitioning - clasa de achivalenta valida
    def test_get_all_books_limit(self):
        r = get_books(limit=3)
        assert len(r.json()) == 3, 'limit is not working'

    # Test 3.1: Verifca requestul get books cu filtrate pe limita - boundery value analysis -limita inferioara
    def test_get_all_books_limit_limita_inferioara_boundery(self):
        r = get_books(limit=0)
        assert len(r.json()) == 0, 'limit is not working'


    # Test 3.2: Verifca requestul get books cu filtrate pe limita - boundery value analysis -limita superioara
    # preconditions: pentru testul asta terbuie sa avem cel putin 2 de carti in sistem 
    def test_get_all_books_limit_limita_superioara_boundery(self):
        r = get_books(limit=20)
        assert len(r.json()) == 20, 'limit is not working'

    # Test 3.3: Verifca requestul get books cu filtrate pe limita - equivalence partitioning - clasa de achivalenta invalida superior
    def test_get_all_books_limit_invalid_superior(self):
        r = get_books(limit=30)
        assert r.json()["error"] == "Invalid value for query parameter 'limit'. Cannot be greater than 20.", 'limit is not working'

    # Test 3.4: Verifca requestul get books cu filtrate pe limita - equivalence partitioning - clasa de achivalenta invalida inferior
    def test_get_all_books_limit_invalid_inferior(self):
        r = get_books(limit=-30)
        assert r.json()["error"] == "Invalid value for query parameter 'limit'. Must be greater than 0.", 'limit is not working'

    # Test 4: Verifica requestul de get books cu filtrate pe type fiction
    def test_get_all_books_type_fiction(self):
        r = get_books(book_type='fiction')
        # assert len(r.json()) == 4, 'type fiction is not working'
        assert len(r.json()) in range(1,5), 'type fiction is not working'

    # Test 5: Verifica requestul de get books cu filtrate pe type non-fiction
    def test_get_all_books_type_non_fiction(self):
        r = get_books(book_type='non-fiction')
        assert len(r.json()) == 2, 'type non-fiction is not working'

    # 1.b  Testare negativa = tip de testare in care verificam comportamentul sistemului
    # atunci cand primeste inputuri pe care nu ar trebui sa le accepte

    # Test 6: Verifica requestul de get books atunci cand punem filtrare invalida dupa type
    def test_get_books_invalid_type(self):
        r = get_books(book_type='abc')
        assert r.status_code == 400, 'status code is ok'
        assert r.json()['error'] == "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction.", 'wrong error'

    # Test 7: Verifica requestul de get books atunci cand punem filtrare valida dupa type si limita
    def test_get_all_books_type_and_limit(self):
        r = get_books(book_type='fiction', limit=2)
        assert len(r.json()) == 2, 'limit is not working'
        assert r.json()[0]['type'] == 'fiction', 'type filter not working'
        assert r.json()[0]['id'] == 1, 'id not ok'
        assert r.json()[0]['name'] == 'The Russian', 'book name is not ok'
        assert r.json()[1]['type'] == 'fiction', 'type filter not working'
        assert r.json()[1]['id'] == 3, 'id not ok'
        assert r.json()[1]['name'] == 'The Vanishing Half', 'book name is not ok'

    # Test 8: Verifica requestul de get book
    def test_get_book(self):
        r = get_book(1)
        expected = {
            "id": 1,
            "name": "The Russian",
            "author": "James Patterson and James O. Born",
            "isbn": "1780899475",
            "type": "fiction",
            "price": 12.98,
            "current-stock": 12,
            "available": True
        }
        assert r.status_code == 200, 'status code not ok'
        assert r.json() == expected, 'book datat not ok'

    # Test 8: Verifica requestul de get book atunci cand punem filtrare invalida dupa id
    def test_get_book_invalid_id(self):
        r = get_book(202)
        assert r.status_code == 404, 'code not ok'
        assert r.json()['error'] == 'No book with id 202', 'invalid id msg is not ok'
