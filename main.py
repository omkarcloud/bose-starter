import importlib
if __name__ == "__main__":
    Task = importlib.import_module('src.scraper').Task
    t = Task()
    t.begin_task()