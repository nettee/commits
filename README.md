# Git 提交管理

本仓库包含两个用于管理 Git 提交的 Python 脚本。

## 工作流程

使用 `dump_commits.py` 从一个仓库中提取提交历史

```python
python dump_commits.py <提交数量>
```

使用 `load_commits.py` 在另一个仓库中重建相同的历史

```python
python load_commits.py
```

## dump_commits.py

用于提取 Git 仓库中的最近提交信息并将其保存到 JSON 文件中。

- 获取 Git 历史中指定数量的最近提交
- 对于每个提交，收集：
  - 提交信息
  - 新增文件（包含内容）
  - 修改的文件（包含内容）
  - 删除的文件
- 将所有收集的信息保存到 JSON 文件（`commits_content.json`）

## load_commits.py

用于从之前生成的 JSON 文件中应用提交，以重建 Git 历史。

- 从 `commits_content.json` 文件加载提交信息
- 对于每个提交：
  - 创建新增的文件及其内容
  - 更新修改的文件及其内容
  - 删除已移除的文件
  - 使用原始提交信息创建 Git 提交
