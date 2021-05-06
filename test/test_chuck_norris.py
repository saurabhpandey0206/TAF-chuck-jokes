import pytest


@pytest.mark.usefixtures("test_setup")
class TestChuckJokes:
    SUCCESS_CODE = 200
    NOT_FOUND = 404
    BAD_REQUEST = 400

    def test_get_random_joke(self):
        """
        test to verify that a random joke can be fetched successfully
        """
        status_code, res = pytest.chuck_jokes.get_random_joke()
        assert status_code == TestChuckJokes.SUCCESS_CODE, f"expected: {TestChuckJokes.SUCCESS_CODE}, got: {status_code}"
        assert res['value'], "did not get Joke"

    def test_get_categories(self):
        """
        test to check categories of jokes are returned successfully
        """
        status_code, res = pytest.chuck_jokes.get_all_categories()
        assert status_code == TestChuckJokes.SUCCESS_CODE, f"expected: {TestChuckJokes.SUCCESS_CODE}, got: {status_code}"
        assert len(res) > 1, "did not get enough categories"

    @pytest.mark.parametrize("category", ['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money', 'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel'])
    def test_get_a_category_joke(self, category):
        """
        test to verify a category joke can be fetched
        """
        status_code, res = pytest.chuck_jokes.get_category_joke(category)
        assert status_code == TestChuckJokes.SUCCESS_CODE, f"expected: {TestChuckJokes.SUCCESS_CODE}, got: {status_code}"
        assert res['value'], "did not get Joke"

    @pytest.mark.parametrize("query", ["123", "1234", "h"*120])
    def test_valid_query_joke(self, query):
        """
        test to verify query test with valid queries
        """
        status_code, res = pytest.chuck_jokes.query_joke(query)
        assert status_code == TestChuckJokes.SUCCESS_CODE, f"expected: {TestChuckJokes.SUCCESS_CODE}, got: {status_code}"
        for res in res['result']:
            assert query in res['value'], f"{query} not found in result"

    @pytest.mark.parametrize("category", ['phone', '', '23', '@'])
    def test_get_a_category_joke_with_invalid_category(self, category):
        """
        test to verify that with invalid category name joke can not be fetched
        """
        expected_error = f'No jokes for category "{category}" found.'
        status_code, res = pytest.chuck_jokes.get_category_joke(category)
        assert status_code == TestChuckJokes.NOT_FOUND, f"expected: {TestChuckJokes.NOT_FOUND}, got: {status_code}"
        assert expected_error in res['message'], f"expected {expected_error}, got: {res['message']}"

    @pytest.mark.parametrize("query", ['12', "h"*121])
    def test_valid_query_joke_with_invalid_range(self, query):
        """
        test to verify with query size<3
        """
        expected_error = "search.query: size must be between 3 and 120"
        status_code, res = pytest.chuck_jokes.query_joke(query)
        assert status_code == TestChuckJokes.BAD_REQUEST, f"expected: {TestChuckJokes.BAD_REQUEST}, got: {status_code}"
        assert expected_error in res['message'], f"expected {expected_error}, got: {res['message']}"
