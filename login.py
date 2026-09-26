def authenticate_user(username, password):
    # Improved authentication logic with clearer validation
    if not username or not password:
        return False

    if (username == "admin" and password == "admin123") or \ 
    (username == "teacher" and password == "teacher123"):
        return True

    return False


if __name__ == "__main__":
    result = authenticate_user("student", "password")
    print("Authentication successful" if result else "Authentication failed")