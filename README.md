# XdbLocation
是一个离线IP地址定位库和IP定位数据管理的库


* PyPI package: https://pypi.org/project/xdb_location/
* Github: https://github.com/gunhe/xdb_location

# 安装

## 稳定版本

要安装Xdb_Location，请在终端中运行以下命令：

```sh
uv add xdb_location
```

或者，如果你更喜欢使用 `pip`:

```sh
pip install xdb_location
```

## 源码安装

Xdb_Location的源文件可以从以下网址下载 [Github repo](https://github.com/gunhe/xdb_location).

您可以克隆公共存储库:

```sh
git clone git://github.com/gunhe/xdb_location
```

或者下载 [tarball](https://github.com/gunhe/xdb_location/tarball/master):

```sh
curl -OJL https://github.com/gunhe/xdb_location/tarball/master
```

一旦你有了源代码的副本，你就可以用以下方式安装它：

```sh
cd xdb_location
uv pip install .
```

## 使用
```bash
from xdb_location.xdb_location import searchWithContent
target_ip_location = searchWithContent(target_ip="1.15.241.228")
print(target_ip_location)
```

# 数据生成

```bash
git clone https://github.com/gunhe/xdb_location.git
cd xdb_location
# 测试数据生成
uv run xdb_location ./src/xdb_location/data/ip.test.txt ./ip2region.test.xdb
# ipv4 数据生成
uv run xdb_location ./src/xdb_location/data/ipv4_source.txt ./ip2region.ipv4_source.xdb
# ipv6 数据生成
uv run xdb_location ./src/xdb_location/data/ipv6_source.txt ./ip2region.ipv6_source.xdb
```

## 参考

[uv](https://docs.astral.sh/uv/)

[Publishing your package](https://docs.astral.sh/uv/guides/package/)

[Using uv in GitHub Actions](https://docs.astral.sh/uv/guides/integration/github/#publishing-to-pypi)

[Typer](https://typer.tiangolo.com/tutorial/)

[Cookiecutter](https://github.com/audreyfeldroy/cookiecutter)

[audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)

[https://github.com/lionsoul2014/ip2region](https://github.com/lionsoul2014/ip2region)


