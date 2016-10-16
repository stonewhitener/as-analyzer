# AS Analyzer

An AS path analyzer for the `show route terse` command of Junos OS.

Junos OS の `show route terse` コマンドの結果から AS パスを解析します．

https://www.juniper.net/documentation/en_US/junos16.1/topics/reference/command-summary/show-route-terse.html

# Usage
## path.py

`show route terse` コマンドで得られる BGP 経路情報から AS パスを抽出します．

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
それぞれのパスの先頭に任意の AS 番号を付加する場合は，`-p, --prefix` オプションを使います．

例えば，

```
$ python path.py -l 2013.txt 2013-path.txt
もしくは
$ python path.py --legacy 2013.txt 2013-path.txt
```

とすると，

```
3567 6789
234
3456 4567 4567 5678
 :
```

というパスリストが得られます．
パス上の AS 番号の重複を除去する場合は，次のようにします．

```
$ python path.py -lu 2013.txt 2013-path.txt
もしくは
$ python path.py --legacy --unique 2013.txt 2013-path.txt
```

```
3567 6789
234
3456 4567 5678
 :
```

さらに，これをソートして出力する場合は，次のようにします．

```
$ python path.py -lus 2013.txt 2013-path.txt
もしくは
$ python path.py --legacy --unique --sort 2013.txt 2013-path.txt
```

```
234
3456 4567 5678
3567 6789
 :
```

それぞれのパスの先頭に任意の AS 番号を付加する場合は，次のようにします．

```
$ python path.py -lusp1234 2013.txt 2013-path.txt
もしくは
$ python path.py --legacy --unique --sort --prefix 1234 2013.txt 2013-path.txt
```

```
1234 234
1234 3456 4567 5678
1234 3567 6789
 :
```


## corepath.py

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

## sort.py

パスリストをソートして出力します．

```
usage: sort.py [-h] <input_file> <output_file>

Sort the specified AS path list.

positional arguments:
  <input_file>   input the AS path list from <input_file>
  <output_file>  output the sorted AS path list into <output_file>

optional arguments:
  -h, --help     show this help message and exit
```

## unique.py

パス上の AS 番号の重複を削除したパスリストを出力します．

```
usage: unique.py [-h] <input_file> <output_file>

Remove the AS number duplicates for the each paths with the specified AS path
list.

positional arguments:
  <input_file>   input the AS path list from <input_file>
  <output_file>  output the non-duplicate AS path list into <output_file>

optional arguments:
  -h, --help     show this help message and exit
```

## count.py

パスリストを使ってパス数，出現する AS の数を調べたり，パス長のヒストグラムを作成します．

```
usage: count.py [-h] <input_file>

Inspect the number of paths, ASes, and show the path length hist gram.

positional arguments:
  <input_file>  input the AS path list from <input_file>

optional arguments:
  -h, --help    show this help message and exit
```
