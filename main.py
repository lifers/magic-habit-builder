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


def generate_prompt(habits: list[str], blocking_times: Optional[list]) -> str:
    """generate string prompt"""


def run_scraper(query: str) -> str:
    """run scraper, get answer"""
    options = EdgeOptions().add_argument('--headless')
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

    driver.get('https://www.perplexity.ai')
    search_box = driver.find_element(
        by=By.XPATH,
        value='//textarea[@placeholder="Ask anything..."]')
    
    search_box.send_keys(query + Keys.ENTER)
    driver.implicitly_wait(10)
    answer = driver.find_element(by=By.CLASS_NAME, value='prose')

    return answer.text


def parse_answer(answer: str) -> str:
    """parse answer from scraper into something more manageable"""


if __name__ == "__main__":
    habits = get_habits(3)
    blocking_times = get_blocking_times()
    prompt = generate_prompt(habits, blocking_times)
    answer = run_scraper(prompt)
    result = parse_answer(answer)
    print(result)
