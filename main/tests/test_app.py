from main.App import App
def test_home():
      response = App.test_client().get('/')
      assert response.status_code == 200
def test_health():
     response = App.test_client().get('/health')
     assert b"OK" in response.data