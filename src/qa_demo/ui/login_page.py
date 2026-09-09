class LoginPage:
    def __init__(self, page) -> None:
        self.page = page

    def login(self, username: str, password: str) -> None:
        self.page.fill("[data-testid='login']", username)
        self.page.fill("[data-testid='password']", password)
        self.page.click("[data-testid='submit']")
