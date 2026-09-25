def authenticate_user(username, password):
    # Placeholder implementation - replace with actual authentication logic
    if username == "student" and password == "password":
        return True
    else:
        return False


if __name__ == "__main__":
    print(authenticate_user("student", "password"))