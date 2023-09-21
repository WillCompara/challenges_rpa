from playwright.sync_api import Playwright, sync_playwright
import glob


with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.expect_response(
                lambda res: res.url.startswith("https://rpachallenge.com/assets/downloadFiles/",
            page.goto("https://rpachallenge.com/")
                
                )
        )
        
        #page.goto("https://rpachallenge.com/")
        #page.get_by_role("link", name="Download Excel cloud_download").click()
        folder_path = "C:\\Users\\William\\Downloads"
        folder_path = r"C:\Users\William\Downloads"
        print(folder_path)
        page.pause()
        list_of_files = glob.glob(folder_path)
        last_modified_file = max(list_of_files, key=os.path.getmtime)
        print("Last modified file:", last_modified_file)
        page.pause()