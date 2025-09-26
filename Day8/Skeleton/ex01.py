from playwright.sync_api import sync_playwright
import time

# Step 1. Create a browser
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    # headless=False to see the browser
    # or headless=True to run in the background, hard to debug

    # Step 2. Create a new BrowserContext
    context = browser.new_context()
    page = context.new_page()

    # Step 3. Open a page
    page.goto("https://reddit.com")
    page.wait_for_selector("summary")  # wait for the page to load
    # Step 4. Interact with the page
    for anchor in page.query_selector_all("a"):
        print(anchor.inner_html())
    # Let the user actually see something!
    #
    time.sleep(5)
    # browser.close()
    context.close()
