import unittest
from app import app, mongo

class UserRoutesTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.client.testing = True

    def test_get_users(self):
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        # Further assertions to check the response content

    def test_create_user(self):
        response = self.client.post('/users', json={
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 201)
        # Further assertions to check the response content

    def test_get_user(self):
        # First, create a user to test fetching it
        response = self.client.post('/users', json={
            'name': 'Jane Doe',
            'email': 'jane.doe@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 201)
        user_id = response.get_json()['_id']
        response = self.client.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)
        # Further assertions to check the response content

    def test_update_user(self):
        # First, create a user to test updating it
        response = self.client.post('/users', json={
            'name': 'Alice',
            'email': 'alice@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 201)
        user_id = response.get_json()['_id']
        response = self.client.put(f'/users/{user_id}', json={
            'name': 'Alice Updated',
            'email': 'alice.updated@example.com',
            'password': 'newpassword123'
        })
        self.assertEqual(response.status_code, 200)
        # Further assertions to check the response content

    def test_delete_user(self):
        # First, create a user to test deleting it
        response = self.client.post('/users', json={
            'name': 'Bob',
            'email': 'bob@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 201)
        user_id = response.get_json()['_id']
        response = self.client.delete(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)
        # Further assertions to check the response content

if __name__ == '__main__':
    unittest.main()
