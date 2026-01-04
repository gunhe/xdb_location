# !/bin/bash
set -e
# 修改代码
# 提交代码
# 修改版本信息
# Bump version in pyproject.toml
version="0.1.34"
parent_dir=$(dirname "$(pwd)")
cd $parent_dir
uv version $version
git add ./bin/publish.sh
git add ./pyproject.toml
git commit -m "Bump version to v$version"
# 推送代码到远程仓库
git  push

# Create git tag and push
git tag -a v$version -m v$version
# proxychains git push --tags
git push origin v$version
