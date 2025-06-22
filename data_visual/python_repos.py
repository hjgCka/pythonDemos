import requests

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#将响应转换为字典
response_dict = r.json()

#处理结果
print(response_dict.keys())

print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

#探索有关仓库信息
repo_dicts = response_dict['items']
print(f"Repositories found: {len(repo_dicts)}")

#研究第一个仓库
repo_dict = repo_dicts[0]
print(f"\nkeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)