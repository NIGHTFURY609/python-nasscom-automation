



# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # import time

# # def wait_for_manual_login(driver):
# #     # This function pauses execution until you hit Enter in the console
#         # print("Please log in manually. Waiting 60 seconds before continuing...")
#         # time.sleep(60)


# # def navigate_to_group(driver, group_name):
# #     groups_link = WebDriverWait(driver, 10).until(
# #         EC.element_to_be_clickable((By.LINK_TEXT, "Groups"))
# #     )
# #     groups_link.click()
# #     time.sleep(2)
# #     group_link = WebDriverWait(driver, 10).until(
# #         EC.element_to_be_clickable((By.LINK_TEXT, group_name))
# #     )
# #     group_link.click()
# #     print(f"Navigated to group: {group_name}")

# # def complete_pathway_chapter(driver):
# #     # Click "Get Started" three times for chapter steps
# #     for i in range(3):
# #         get_started = WebDriverWait(driver, 10).until(
# #             EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Get Started')]"))
# #         )
# #         get_started.click()
# #         print(f"Chapter step {i+1}: Clicked Get Started.")
# #         time.sleep(2)
# #     # Click "Get Started" on course material
# #     WebDriverWait(driver, 10).until(
# #         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Get Started')]"))
# #     ).click()
# #     print("Clicked Get Started on course material.")
# #     time.sleep(2)
# #     # Click "View Content" then "Mark as Complete"
# #     WebDriverWait(driver, 10).until(
# #         EC.element_to_be_clickable((By.LINK_TEXT, "View Content"))
# #     ).click()
# #     print("Clicked View Content.")
# #     time.sleep(2)
# #     WebDriverWait(driver, 10).until(
# #         EC.element_to_be_clickable((By.LINK_TEXT, "Mark as Complete"))
# #     ).click()
# #     print("Clicked Mark as Complete.")
# #     time.sleep(2)

# # def take_quiz(driver):
# #     # Launch the quiz
# #     WebDriverWait(driver, 10).until(
# #         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Launch')]"))
# #     ).click()
# #     print("Clicked Launch to start the quiz.")
# #     time.sleep(2)
# #     # Start Quiz
# #     WebDriverWait(driver, 10).until(
# #         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Start Quiz')]"))
# #     ).click()
# #     print("Clicked Start Quiz.")
# #     time.sleep(2)
# #     # Answer quiz questions (assuming 5 questions)
# #     for q in range(1, 6):
# #         print(f"Answering Question {q}")
# #         radio_option = WebDriverWait(driver, 10).until(
# #             EC.element_to_be_clickable((By.XPATH, "(//input[@type='radio'])[1]"))
# #         )
# #         radio_option.click()
# #         time.sleep(1)
# #         WebDriverWait(driver, 10).until(
# #             EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit')]"))
# #         ).click()
# #         time.sleep(1)
# #         if q < 5:
# #             WebDriverWait(driver, 10).until(
# #                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next Question')]"))
# #             ).click()
# #             print("Moved to the next question.")
# #             time.sleep(2)
# #         else:
# #             WebDriverWait(driver, 10).until(
# #                 EC.element_to_be_clickable((By.LINK_TEXT, "View Result"))
# #             ).click()
# #             print("Clicked View Result.")
# #             time.sleep(2)
# #             WebDriverWait(driver, 10).until(
# #                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]"))
# #             ).click()
# #             print("Clicked Continue.")
# #             time.sleep(2)
# #             WebDriverWait(driver, 10).until(
# #                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Process My Result & Close')]"))
# #             ).click()
# #             print("Processed quiz result and closed quiz.")
# #             time.sleep(2)

# # def return_to_pathway(driver):
# #     driver.back()
# #     print("Returned to the pathway page.")
# #     time.sleep(2)

# # def main():
# #     # Setup WebDriver using Service (update the path as needed)
# #     service_obj = Service(r"C:\Users\jeswi\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
# #     driver = webdriver.Chrome(service=service_obj)
# #     driver.maximize_window()

# #     try:
# #         # Open the website and wait for manual login
# #         driver.get("https://www.futureskillsprime.in/")
# #         wait_for_manual_login(driver)
# #         time.sleep(7)
# #         # Navigate to the desired group (replace with your actual group name)
# #         navigate_to_group(driver, "KTU-SCMS SCHOOL OF ENGINEE")
        
        
# #         # Click initial "Get Started" to enter the pathway
# #         WebDriverWait(driver, 10).until(
# #             EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Get Started')]"))
# #         ).click()
# #         print("Entered the pathway by clicking initial Get Started.")
# #         time.sleep(2)
        
# #         # Loop through pathway chapters (adjust number as needed)
# #         num_chapters = 3  # Example: repeat for 3 chapters
# #         for chapter in range(1, num_chapters + 1):
# #             print(f"\n--- Processing Chapter {chapter} ---")
# #             complete_pathway_chapter(driver)
# #             take_quiz(driver)
# #             return_to_pathway(driver)
# #             time.sleep(2)
        
# #         print("\nCourse automation completed successfully.")
# #     except Exception as e:
# #         print("An error occurred during automation:", e)
# #     finally:
# #         driver.quit()

# # if __name__ == "__main__":
# #     main()





# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# def complete_pathway_chapter(driver):
#     # Click "Get Started" three times for chapter steps
#     for i in range(3):
#         get_started = WebDriverWait(driver, 15).until(
#             EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Get Started')]"))
#         )
#         get_started.click()
#         print(f"Chapter step {i+1}: Clicked Get Started.")
#         time.sleep(2)
    
#     # Click "Get Started" on course material
#     material_button = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Get Started')]"))
#     )
#     material_button.click()
#     print("Clicked Get Started on course material.")
#     time.sleep(2)
    
#     # Click "View Content" then "Mark as Complete"
#     view_content = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.LINK_TEXT, "View Content"))
#     )
#     # Click the "View Content" hyperlink (assumes it opens a new tab)
#     view_content = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.LINK_TEXT, "View Content"))
#     )
#     view_content.click()
#     time.sleep(2)

#     # Switch to the last opened tab and close it
#     driver.switch_to.window(driver.window_handles[-1])
#     driver.close()

#     # Optionally, switch back to the original tab (assumed to be the first)
#     driver.switch_to.window(driver.window_handles[0])
#     time.sleep(2)


#     mark_complete = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.LINK_TEXT, "Mark as Complete"))
#     )
#     mark_complete.click()
#     print("Clicked Mark as Complete.")
#     time.sleep(2)

# def take_quiz(driver):
#     # Click the "Launch" button to open the quiz
#     launch_button = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Launch')]"))
#     )
#     launch_button.click()
#     print("Clicked Launch to start the quiz.")
#     time.sleep(2)
    
#     # Click the "Start Quiz" button
#     start_quiz = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Start Quiz')]"))
#     )
#     start_quiz.click()
#     print("Clicked Start Quiz.")
#     time.sleep(2)
    
#     # Answer quiz questions (assuming 5 questions)
#     for q in range(1, 6):
#         print(f"Answering Question {q}...")
#         # Wait for a radio button to be clickable and select the first option
#         radio_option = WebDriverWait(driver, 15).until(
#             EC.element_to_be_clickable((By.XPATH, "(//input[@type='radio'])[1]"))
#         )
#         radio_option.click()
#         time.sleep(1)
#         submit_button = WebDriverWait(driver, 15).until(
#             EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit')]"))
#         )
#         submit_button.click()
#         time.sleep(1)
        
#         if q < 5:
#             next_question = WebDriverWait(driver, 15).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next Question')]"))
#             )
#             next_question.click()
#             print("Moved to the next question.")
#             time.sleep(2)
#         else:
#             view_result = WebDriverWait(driver, 15).until(
#                 EC.element_to_be_clickable((By.LINK_TEXT, "View Result"))
#             )
#             view_result.click()
#             print("Clicked View Result for the quiz.")
#             time.sleep(2)
#             continue_button = WebDriverWait(driver, 15).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]"))
#             )
#             continue_button.click()
#             print("Clicked Continue.")
#             time.sleep(2)
#             process_close = WebDriverWait(driver, 15).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Process My Result & Close')]"))
#             )
#             process_close.click()
#             print("Processed quiz result and closed quiz.")
#             time.sleep(2)

# def return_to_pathway(driver):
#     driver.back()
#     print("Returned to the pathway page.")
#     time.sleep(2)

# def main():
#     # Setup WebDriver using the Service class (update the path as needed)
#     service_obj = Service(r"C:\Users\jeswi\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
#     driver = webdriver.Chrome(service=service_obj)
#     driver.maximize_window()

#     try:
#         # Open the homepage
#         driver.get("https://www.futureskillsprime.in/")
#         print("Please manually log in and navigate to your course pathway page (where 'Get Started' is visible).")
#         print("Please log in manually. Waiting 60 seconds before continuing...")
#         time.sleep(60)

#         # Now the script will automate the rest of the course.
#         print("Starting course automation...")
        
#         # For each chapter in the pathway, complete the chapter and take the quiz.
#         num_chapters = 3  # Adjust as needed
#         for chapter in range(1, num_chapters + 1):
#             print(f"\n--- Processing Chapter {chapter} ---")
#             complete_pathway_chapter(driver)
#             take_quiz(driver)
#             return_to_pathway(driver)
#             time.sleep(2)
        
#         print("\nCourse automation completed successfully.")
#     except Exception as e:
#         print("An error occurred during automation:", e)
#     finally:
#         driver.quit()

# if __name__ == "__main__":
#     main()




# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# def complete_pathway_chapter(driver, repeat_get_started=True):
#     if repeat_get_started:
#         # Click "Get Started" three times for lesson steps
#         for i in range(3):
#             get_started = WebDriverWait(driver, 15).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Get Started')]"))
#             )
#             driver.execute_script("arguments[0].scrollIntoView(true);", get_started)
#             time.sleep(1)
#             driver.execute_script("arguments[0].click();", get_started)
#             print(f"Lesson step {i+1}: Clicked Get Started.")
#             time.sleep(2)
#     else:
#         print("Skipping initial 'Get Started' clicks for the first lesson.")

#     # Click "Get Started" on the course material
#     get_started = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Get Started')]"))
#     )
#     driver.execute_script("arguments[0].scrollIntoView(true);", get_started)
#     time.sleep(1)
#     driver.execute_script("arguments[0].click();", get_started)
#     print("Clicked Get Started on course material.")
#     time.sleep(2)
    
#     # Store the original window handle before clicking "View Content"
#     original_window = driver.current_window_handle
    
#     # Click the "View Content" hyperlink (assumed to open a new tab)
#     view_content = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.LINK_TEXT, "View Content"))
#     )
#     view_content.click()
#     print("Clicked View Content; new tab should open.")
#     time.sleep(2)
    
#     # Wait for new tab(s) to open
#     WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    
#     # Close all extra tabs (any handle not equal to the original_window)
#     all_handles = driver.window_handles
#     for handle in all_handles:
#         if handle != original_window:
#             try:
#                 driver.switch_to.window(handle)
#                 driver.close()
#                 print(f"Closed extra tab: {handle}")
#             except Exception as e:
#                 print("Error closing tab:", e)
    
#     # Switch back to the original window
#     try:
#         driver.switch_to.window(original_window)
#     except Exception as e:
#         print("Error switching back to the original window:", e)
#     time.sleep(2)
    
#     # Click "Mark as Complete" hyperlink
#     mark_complete = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.LINK_TEXT, "Mark as Complete"))
#     )
#     mark_complete.click()
#     print("Clicked Mark as Complete.")
#     time.sleep(2)


# def take_quiz(driver):
#     # Launch the quiz
#     launch_button = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Launch')]"))
#     )
#     launch_button.click()
#     print("Clicked Launch to start the quiz.")
#     time.sleep(2)
    
#     # Click the "Start Quiz" button
#     start_quiz = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Start Quiz')]"))
#     )
#     start_quiz.click()
#     print("Clicked Start Quiz.")
#     time.sleep(2)
    
#     # Answer quiz questions (assuming 5 questions)
#     for q in range(1, 6):
#         print(f"Answering Question {q}...")
#         radio_option = WebDriverWait(driver, 15).until(
#             EC.element_to_be_clickable((By.XPATH, "(//input[@type='radio'])[1]"))
#         )
#         radio_option.click()
#         time.sleep(1)
#         submit_button = WebDriverWait(driver, 15).until(
#             EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit')]"))
#         )
#         submit_button.click()
#         time.sleep(1)
#         if q < 5:
#             next_question = WebDriverWait(driver, 15).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next Question')]"))
#             )
#             next_question.click()
#             print("Moved to the next question.")
#             time.sleep(2)
#         else:
#             view_result = WebDriverWait(driver, 15).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'View Result')]"))
#             )
#             view_result.click()
#             print("Clicked View Result for the quiz.")
#             time.sleep(2)
#             continue_button = WebDriverWait(driver, 15).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]"))
#             )
#             continue_button.click()
#             print("Clicked Continue.")
#             time.sleep(2)
#             process_close = WebDriverWait(driver, 15).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Process My Result & Close')]"))
#             )
#             process_close.click()
#             print("Processed quiz result and closed quiz.")
#             time.sleep(2)

# def process_pathway(driver, num_lessons):
#     """
#     Loops through the lessons in the pathway.
#     For the first lesson, it skips the repeated "Get Started" clicks.
#     For subsequent lessons, it performs the full cycle.
#     After processing all lessons, the quiz is taken.
#     """
#     for lesson in range(1, num_lessons + 1):
#         print(f"\n--- Processing Lesson {lesson} of the pathway ---")
#         if lesson == 1:
#             complete_pathway_chapter(driver, repeat_get_started=False)
#         else:
#             complete_pathway_chapter(driver, repeat_get_started=True)
#         time.sleep(2)
    
#     print("\nAll lessons processed. Proceeding to quiz...")
#     take_quiz(driver)

# def main():
#     # Setup WebDriver using Service (update the path as needed)
#     service_obj = Service(r"C:\Users\jeswi\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
#     driver = webdriver.Chrome(service=service_obj)
#     driver.maximize_window()

#     try:
#         # Open the website and allow manual login and pathway selection.
#         driver.get("https://www.futureskillsprime.in/")
#         print("Please manually log in and select the pathway from which you want to start.")
#         input("After you've clicked your desired pathway and the page is loaded, press Enter to continue automation...")

#         # Ask for the number of lessons in the pathway.
#         num_lessons = int(input("Enter the number of lessons in this pathway: "))
        
#         # Process the pathway lessons and then take the quiz.
#         process_pathway(driver, num_lessons)
        
#         print("\nCourse automation completed successfully.")
#     except Exception as e:
#         print("An error occurred during automation:", e)
#     finally:
#         driver.quit()

# if __name__ == "__main__":
#     main()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def wait_and_click(driver, locator, timeout=10):
    """Wait for an element to be clickable and click it."""
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
    element.click()
    return element
    try:
        cookie_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Accept Cookies')]")
        cookie_btn.click()
        time.sleep(1)
    except:
        pass  # If no cookie popup, ignore

def process_lessons(driver):
    """
    Process each lesson:
    - Click the lesson's "Get Started" button.
    - Click the "View Content" link, switch to new tab, and close it.
    - Click the "Mark as Complete" link.
    """
    # Locate all lesson cards that have a "Get Started" button.
    lesson_buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'Get Started')]")
    print(f"Found {len(lesson_buttons)} lesson(s) for processing.")

    for idx, lesson in enumerate(lesson_buttons):
        try:
            # Open the lesson
            lesson.click()
            print(f"Lesson {idx+1}: 'Get Started' clicked.")
            time.sleep(2)  # wait for lesson content to load

            # Click the "View Content" hyperlink
            view_content = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "View Content"))
            )
            view_content.click()
            print(f"Lesson {idx+1}: 'View Content' clicked.")
            time.sleep(2)

            # Handle the new tab if it opens
            if len(driver.window_handles) > 1:
                driver.switch_to.window(driver.window_handles[-1])
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                print(f"Lesson {idx+1}: New tab closed.")
            else:
                print(f"Lesson {idx+1}: New tab did not open as expected.")



        except Exception as e:
            print(f"Error processing lesson {idx+1}: {e}")
    try:
        # Wait for the link to be clickable
        link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(normalize-space(text()), 'Mark as Complete')]"))
        )
        
        # Scroll to the link (in case it’s off-screen)
        driver.execute_script("arguments[0].scrollIntoView(true);", link)
        time.sleep(1)
        
        # Attempt a normal click
        link.click()
        print("Successfully clicked 'Mark as Complete' via normal click.")

    except Exception as e:
        print("Normal click failed, trying JavaScript click. Error:", e)
        try:
            # If normal click fails, do a JS click as a fallback
            link = driver.find_element(By.XPATH, "//a[contains(normalize-space(text()), 'Mark as Complete')]")
            driver.execute_script("arguments[0].scrollIntoView(true);", link)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", link)
            print("Successfully clicked 'Mark as Complete' via JavaScript.")
        except Exception as ex:
            print("Could not click 'Mark as Complete' at all. Error:", ex)
    

def process_quiz(driver):
    """
    Process the quiz:
    - Launch quiz via the "Launch" button.
    - Click "Start Quiz".
    - For each question (assumed to be 5), select the first radio button, submit, and click next.
    - For the final question, view result, continue, and close the quiz.
    """
    try:
        # Launch quiz
        launch_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Launch')]"))
        )
        launch_button.click()
        print("Quiz: 'Launch' button clicked.")
        time.sleep(2)

        # Click the "Start Quiz" button on the quiz page
        start_quiz = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Start Quiz')]"))
        )
        start_quiz.click()
        print("Quiz: 'Start Quiz' button clicked.")
        time.sleep(2)

        # Process quiz questions; adjust the range if there are more than 5
        for q in range(5):
            # Wait for radio buttons to appear and select the first option
            radios = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//input[@type='radio']"))
            )
            if radios:
                radios[0].click()
                print(f"Quiz Q{q+1}: First answer selected.")
            else:
                print(f"Quiz Q{q+1}: No radio buttons found.")
            time.sleep(1)

            # Submit the answer
            wait_and_click(driver, (By.XPATH, "//button[contains(text(),'Submit')]"), timeout=10)
            print(f"Quiz Q{q+1}: Answer submitted.")
            time.sleep(2)

            if q < 4:
                # For questions 1-4, click "Next Question"
                wait_and_click(driver, (By.XPATH, "//button[contains(text(),'Next Question')]"), timeout=10)
                print(f"Quiz Q{q+1}: Moved to next question.")
                time.sleep(2)
            else:
                # For the last question, click "View Result"
                wait_and_click(driver, (By.XPATH, "//button[contains(text(),'View Result')]"), timeout=10)
                print("Quiz Q5: 'View Result' clicked.")
                time.sleep(2)

        # Continue after viewing results
        wait_and_click(driver, (By.XPATH, "//button[contains(text(),'Continue')]"), timeout=10)
        print("Quiz: 'Continue' clicked.")
        time.sleep(2)
        wait_and_click(driver, (By.XPATH, "//button[contains(text(),'Process My Result & Close')]"), timeout=10)
        print("Quiz: 'Process My Result & Close' clicked. Quiz complete.")
        time.sleep(2)
        driver.back()  # Return to the pathway page
        print("Returned to pathway page.")
        time.sleep(2)

    except Exception as e:
        print("Error during quiz processing:", e)

def automate_chapter(driver):
    """
    Automate one chapter of the pathway:
    - Optionally click the chapter-level "Get Started" buttons (if available).
    - Process all lessons.
    - Process the quiz at the end of the chapter.
    """
    # If the chapter contains multiple sections that require clicking "Get Started" (three times)
    for i in range(3):
        try:
            # Use an indexed XPath to click distinct chapter sections if they exist
            section = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"(//button[contains(text(),'Get Started')])[{i+1}]"))
            )
            section.click()
            print(f"Chapter section {i+1}: 'Get Started' clicked.")
            time.sleep(2)
        except Exception as e:
            print(f"Error clicking chapter section {i+1}: {e}")

    # Process lessons within the chapter
    process_lessons(driver)

    # Process the quiz at the end of the chapter
    process_quiz(driver)

def main():
    # Initialize the WebDriver (ensure chromedriver is installed and in your PATH)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.futureskillsprime.in/")

    # Pause to allow manual login and navigation to the pathway page.
    input("Please log in and navigate to your pathway page, then press Enter to continue...")

    while True:
        automate_chapter(driver)
        cont = input("Chapter automation complete. Continue with the next chapter? (y/n): ")
        if cont.lower() != 'y':
            break

    driver.quit()

if __name__ == "__main__":
    main()
