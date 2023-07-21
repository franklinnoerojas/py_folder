from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://github.com/login")
    page.get_by_label("Username or email address").click()
    page.get_by_label("Username or email address").fill("franklin.noe.pena@outlook.com")
    page.get_by_label("Username or email address").press("Tab")
    page.get_by_label("Password").fill("AmazonessX0224.")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("link", name="franklinnoerojas/play2").click()
    page.get_by_role("link", name="Settings Settings").click()
    page.get_by_label("Repository name").click()
    page.get_by_label("Repository name").fill("play_demo2")
    page.get_by_role("button", name="Rename").click()
    page.get_by_label("Open user account menu").click()
    page.get_by_role("link", name="Sign out").click()
    page.get_by_role("button", name="Sign out").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
