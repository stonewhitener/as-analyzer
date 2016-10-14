## Usage
### path.py

BGP 経路情報から AS パスを抽出します．

```
usage: path.py [-h] [-l] [-u] [-s] [-p <number>] <input_file> <output_file>

Extract the AS paths from the specified BGP route information.

positional arguments:
  <input_file>          input the BGP route information from <input_file>
  <output_file>         output the AS path list into <output_file>

optional arguments:
  -h, --help            show this help message and exit
  -l, --legacy          indicate the legacy format BGP route information
  -u, --unique          remove the duplicates in the path
  -s, --sort            sort the path list
  -p <number>, --prefix <number>
                        add the specified number to the start of the each path
```

古い形式の BGP 経路情報を使用する場合は，`-l, --legacy` オプションを付与します．
パス上の AS 番号の重複を除去するには，`-u, --unique` オプションを付与します．
パスリストをソートして出力するには， `-s, --sort` オプションを付与します．

例えば，

```
$ python path.py -l -u -s 2013.txt 2013-path.txt
```

とすると，

```
234
3456 4567 5678
3567 6789
 :
```

それぞれのパスの先頭に任意の AS 番号を付加する場合は，

```
$ python path.py -l -s -p 1234 2013.txt 2013-path.txt
```

とすると，

```
1234 234
1234 3456 4567 5678
1234 3567 6789
 :
```

というパスリストが得られます．

### corepath.py

パスリストからコアパスを抽出します．

```
usage: corepath.py [-h] [-s] <input_file> <output_file>

Create a core AS path list with the specified AS path list

positional arguments:
  <input_file>   input the BGP route information from <input_file>
  <output_file>  output the AS path list into <output_file>

optional arguments:
  -h, --help     show this help message and exit
  -s, --sort     sort the core path list
```

コアパスのリストをソートして出力するには， `-s, --sort` オプションを付与します．

例えば，次のように使用します．

```
$ python corepath.py -s 2015-path.txt 2015-corepath.txt
```
