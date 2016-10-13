## Usage
### `pathlist.py`

```
Usage: pathlist.py -f {2013,2014,2015} [-s] <元データ> <パスリストの出力先>
```

`-f` でフォーマットを指定．`-s` をつけるとソートして出力．

#### 例

```
$ python pathlist.py --format 2015 --sort 2015.txt 2015-pathlist-sorted.txt
```

### `corepath.py`

```
Usage: corepath.py <入力パスリスト> <コアパスリストの出力先>
```

#### 例

```
$ python corepathlist.py 2015-pathlist-sorted.txt 2015-pathlist-core.txt
```
