import requests

def get_github_repositories(query, max_results=10):
    base_url = "https://api.github.com/search/repositories"
    params = {"q": query, "sort": "stars", "order": "desc", "per_page": max_results}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        print(f"Error: {response.status_code}")
        return []

def print_repository_info(repo):
    print(f"Name: {repo['name']}")
    print(f"Owner: {repo['owner']['login']} - {repo['owner']['html_url']}")
    print(f"URL: {repo['html_url']}")
    print(f"Description: {repo['description']}")

    repo_languages_url = f"https://api.github.com/repos/{repo['owner']['login']}/{repo['name']}/languages"
    languages_response = requests.get(repo_languages_url)
    repo_languages = languages_response.json()

    print(f"Languages: {', '.join(repo_languages) if repo_languages else 'Not available'}")

    print("-" * 50)

def main():
    # Set the search query
    search_query = "Monitoreng"

    # Set the maximum number of results you want
    max_results = 10

    repositories = get_github_repositories(search_query, max_results)

    if repositories:
        print(f"Top {max_results} repositories related to '{search_query}':")
        for index, repo in enumerate(repositories, start=1):
            print(f"\nRepository #{index}:")
            print_repository_info(repo)
    else:
        print(f"No repositories found for '{search_query}'.")

if __name__ == "__main__":
    main()
