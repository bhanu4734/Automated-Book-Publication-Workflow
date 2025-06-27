from scraper import scrape_chapter, take_screenshot
from ai_agents import spin_chapter, review_chapter
from storage import save_version
from rl_search import rl_search
from utils import save_to_file, load_from_file

CHAPTER_URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
RAW_FILE = "chapter_raw.txt"
SPUN_FILE = "chapter_spun.txt"
REVIEWED_FILE = "chapter_reviewed.txt"

def human_iteration(prompt_text, filename):
    print(f"\n{prompt_text}")
    input(f"Edit {filename} manually if needed. Press ENTER to continue...")

def main():
    print("Fetching Chapter...")
    text = scrape_chapter(CHAPTER_URL)
    save_to_file(RAW_FILE, text)
    take_screenshot(CHAPTER_URL)
    print("Chapter saved and screenshot taken.")

    spun = spin_chapter(text)
    save_to_file(SPUN_FILE, spun)
    print("Chapter spun by AI.")

    human_iteration("Please review the spun version", SPUN_FILE)

    spun_edited = load_from_file(SPUN_FILE)
    reviewed = review_chapter(spun_edited)
    save_to_file(REVIEWED_FILE, reviewed)
    print("AI Reviewer finalized the chapter.")

    human_iteration("Final human edit of reviewed version", REVIEWED_FILE)

    final = load_from_file(REVIEWED_FILE)
    save_version("chapter_1_final", final)

    print("Version stored in ChromaDB.")

    query = input("Enter a query to test RL search: ")
    rl_search(query)

if __name__ == "__main__":
    main()
