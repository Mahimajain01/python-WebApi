# import pytest
# from app import app  # Import your Flask app from your main application file

# @pytest.fixture
# def client():
#     app.config["TESTING"] = True
#     with app.test_client() as client:
#         yield client

# def test_home_route(client):
#     """Test if the home route returns a 200 status code"""
#     response = client.get("/")
#     assert response.status_code == 200
