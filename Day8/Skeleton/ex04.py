from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    # Launching a Browser
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://reddit.com")

    # Click the login button and enter id and password.
    page.locator("#login-button").click()
    page.locator("#login-username").click()
    # page.locator("#loginPassword").fill("your_password")
    # page.locator("#login-submit").click()

    time.sleep(10)
