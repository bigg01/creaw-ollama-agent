from langchain_community.tools import DuckDuckGoSearchRun

def main()  -> None:
    search = DuckDuckGoSearchRun()
    return search.run("Hello, how are you?")

if __name__ == "__main__":
    print(main())