# Auth0 + Gradio + FastAPI Web Application Seed

This is a seed project that demonstrates how to create a web application using Gradio and FastAPI with Auth0 authentication. This template provides a secure web interface with authentication flow.

## Features

- Auth0 Authentication
- Protected routes with session management
- Gradio web interface
- FastAPI backend
- Secure login/logout flow

## Prerequisites

- Python 3.12 or higher
- Poetry (Python package manager)
- Auth0 account and application credentials

## Configuration

The application reads its configuration from environment variables. You can copy the `.env.example` file and fill in your Auth0 credentials:

```bash
cp .env.example .env
```

Then edit the `.env` file with your Auth0 credentials:

```env
# Auth0 credentials
AUTH0_DOMAIN=your-tenant.auth0.com
AUTH0_CLIENT_ID=your-client-id
AUTH0_CLIENT_SECRET=your-client-secret
```

These values can be found in your Auth0 Dashboard under Application Settings.

### Auth0 Setup

1. Create a new Application in Auth0 Dashboard
2. Set the following in your Auth0 Application settings:
   - Application Type: `Regular Web Application`
   - Allowed Callback URLs: `http://localhost:8000/auth`
   - Allowed Logout URLs: `http://localhost:8000`
   - Allowed Web Origins: `http://localhost:8000`

## Installation

1. Install Poetry if you haven't already:
```bash
pipx install poetry
```

2. Install dependencies using Poetry:
```bash
poetry install
```

For more detailed information about setting up Poetry and managing dependencies, you can refer to this article:
https://medium.com/@ren.nakamura/building-a-robust-prototyping-environment-with-poetry-and-ruff-part-1-670921fd9510

## Project Structure

```
.
├── application/
│   ├── app.py            # FastAPI application
│   └── interfaces/       # Interface components
│       ├── login.py      # Login interface
│       ├── logout.py     # Logout interface
│       └── main_app.py   # Main application interface
├── .env                  # Environment variables (created from .env.example)
├── .env.example          # Example environment variables
├── pyproject.toml        # Poetry configuration
└── README.md            # Project documentation
```

## Running the Application

1. Activate Poetry shell:
```bash
poetry shell
```

2. Start the server:
```bash
python application/app.py
```

3. Access the application at `http://localhost:8000`

## Code Style

This project uses Ruff for code formatting and linting. The configuration includes:
- pycodestyle errors (E)
- pyflakes (F)
- flake8-bugbear (B)
- isort (I)

To run the linter:
```bash
poetry run ruff check .
```

To format code:
```bash
poetry run ruff format .
```

### Pre-commit Setup

1. Install pre-commit:
```bash
pipx install pre-commit
```

2. Install the pre-commit hooks:
```bash
pre-commit install
```

3. (Optional) Run against all files:
```bash
pre-commit run --all-files
```

For more detailed information about setting up Poetry and managing dependencies, you can refer to this article:
https://medium.com/@ren.nakamura/building-a-robust-prototyping-environment-with-poetry-and-ruff-part-2-f615235052b0

## Available Routes

- `/` - Home route (redirects to login if not authenticated)
- `/login-page` - Login interface
- `/demo` - Protected main application (requires authentication)
- `/logout` - Logout endpoint

## Session Management

The application uses `SessionMiddleware` for maintaining user sessions. Sessions are stored server-side and referenced by a cookie.

## Development Notes

- All protected routes check for valid session
- Auth0 credentials must be properly configured
- Session secret key should be kept secure
- Development server runs on port 8000 by default

## Customization

You can customize the application by:
1. Modifying Gradio interfaces in the `interfaces/` directory
2. Adding new routes in `app.py`
3. Extending session management
4. Adding additional middleware

## Troubleshooting

Common issues:

### Auth0 Configuration Issues
- Verify your Auth0 settings match your environment variables
- Check that all required URLs are properly configured in Auth0 Dashboard
- Ensure your application type is set to "Regular Web Application"

### Session Issues
- Check that your AUTH0_SECRET is properly set in .env
- Clear browser cookies if you experience login loops
- Verify that SessionMiddleware is properly configured

### Development Environment Issues
- Make sure you're using Python 3.12 or higher
- Try `poetry env remove` and `poetry install` to reset the environment
- Check that all required environment variables are set

### Callback URL Errors
- Verify that the callback URLs in Auth0 match your development environment
- Check for any port conflicts if you've modified the default port
