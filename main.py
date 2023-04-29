from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from datetime import datetime
from typing import Optional


def get_habits(num: int) -> list[str]:
    """get habits to query"""
    habits = []
    for i in range(num):
        habits.append(input(f'Habit {i + 1}:'))
    return habits


def get_blocking_times() -> Optional[list]:
    """get blocking time(s)"""
    blocking_times = []
    i = 1

    print('Please list all of your blocking times as interval HH:MM - HH:MM')
    while True:
        user_input = input(f'Blocking times {i}:')
        i += 1

        if user_input == '':
            break

        blocking_times.append(tuple(user_input.split(' - ')))

    return blocking_times


def generate_prompt(habits: list[str], blocking_times: Optional[list]) -> str:
    """generate string prompt"""
    # TODO: Make examples for reproducibility
    examples = ""
    prmt = examples + "\n"
    prmt += "Given that I want to build the following habits:\n"
    for i in range(len(habits)):
        prmt += f'{i + 1}. [{habits[i]}]\n'

    if blocking_times:
        prmt += "DO NOT SCHEDULE AT THE FOLLOWING TIMES:\n"
        for time in blocking_times:
            prmt += f"[{time[0]} to {time[1]}]\n"

    prmt += "Make a formatted schedule in a table with the following format:" \
            "[time: start - end] | [activity]"
    return prmt


def run_scraper(query: str) -> str:
    """run scraper, get answer"""
    options = EdgeOptions().add_argument(argument=['start-fullscreen'])
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    driver.maximize_window()

    driver.get('https://www.perplexity.ai')
    search_box = driver.find_element(
        by=By.XPATH,
        value='//textarea[@placeholder="Ask anything..."]')

    driver.implicitly_wait(20)
    search_box.send_keys(query + Keys.ENTER)
    answer = driver.find_element(by=By.CLASS_NAME, value='prose')
    table = answer.find_element(by=By.XPATH, value='//table[@class="border w-full border-borderMain dark:border-borderMainDark"]')

    return table.text


def parse_answer(answer: str) -> str:
    """parse answer from scraper into something more manageable"""
    return answer


if __name__ == "__main__":
    habits = get_habits(3)
    blocking_times = get_blocking_times()
    prompt = generate_prompt(habits, blocking_times)
    print(prompt)
    print('-----------------------------------------------------------------------------------')
    answer = run_scraper(prompt)
    result = parse_answer(answer)
    print(result)
