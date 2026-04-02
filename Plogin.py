from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        page.wait_for_selector("//input[@name='username']").type("admin")
        page.wait_for_selector("//input[@name='password']").type("admin123")
        page.wait_for_selector('//button[@type="submit"]').click()
        page.wait_for_timeout(3000)

#run terminal command                                         #generate reports in command
# pytest Playwright/Plogin.py --html=report.html              # --html=report.html