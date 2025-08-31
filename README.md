# Paper Management System

## Admin Login System

The Paper Management System uses a custom User model with a 'role' field to determine if a user is an admin. The system provides two ways to create admin users:

### 1. Using the createsuperuser Command

The standard Django `createsuperuser` command has been customized to automatically set the user's role to 'ADMIN':

```bash
python manage.py createsuperuser
```

This will prompt you for a username, email, and password, and will create a user with both superuser privileges and the 'ADMIN' role.

### 2. Using the createsuperadmin Command

Alternatively, you can use the dedicated `createsuperadmin` command:

```bash
python manage.py createsuperadmin
```

This will prompt you for a username, email, and password. You can also provide these values as command-line arguments:

```bash
python manage.py createsuperadmin --username=admin --email=admin@example.com --password=securepassword
```

You can also use the `--noinput` flag to create a superadmin without interactive prompts:

```bash
python manage.py createsuperadmin --username=admin --email=admin@example.com --password=securepassword --noinput
```

### Admin Permissions

The system uses a custom permission class `IsAdmin` to restrict access to admin-only endpoints. This permission class checks if the authenticated user has the 'ADMIN' role.

### Admin Features

Admins have access to the following features:

1. Creating new users
2. Updating user status
3. Assigning paperwork to researchers
4. Setting and updating deadlines for paperwork
5. Reviewing paperwork
6. Accessing reports and statistics
7. Exporting data to CSV

### Login

Admins can log in using the standard login endpoint:

```
POST /auth/login/
{
  "username": "admin",
  "password": "password"
}
```

The response will include a token that should be included in the Authorization header for subsequent requests:

```
Authorization: Token <token>
```