import pytest
from blog import create_app, db
from blog.models import User, Post

# Fixture to create and configure a new app instance for each test
@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    app.config['TESTING'] = True

    # Set up app context and create all database tables
    with app.app_context():
        db.create_all()

    yield app

    # Teardown: drop all database tables
    with app.app_context():
        db.drop_all()

# Fixture to provide a test client for the app
@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

# Test user registration
def test_register(client):
    """Test user registration."""
    response = client.post('/register', data=dict(
        username='test_user',
        email='test@example.com',
        password='password',
        confirmPassword='password'
    ), follow_redirects=True)

    # Check if registration successful message is present in response
    assert b'Registration successful! You can now log in.' in response.data

# Test user login
def test_login(client):
    """Test user login."""
    # Register a test user
    client.post('/register', data=dict(
        username='test_user',
        email='test@example.com',
        password='password',
        confirmPassword='password'
    ))

    # Attempt login with test user credentials
    response = client.post('/login', data=dict(
        email='test@example.com',
        password='password'
    ), follow_redirects=True)

    # Check if login successful message is present in response
    assert b'Login successful!' in response.data
