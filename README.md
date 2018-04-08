# 環境構築方法

頻繁に環境構築するので備忘録

### 前提としてる環境

|||
|:-:|:--:|
|仮想環境|VirtualBox or VMware|
|仮想OS|Ubuntu14.04 or 16.04|
|Python|Python3.5.3|

## インストールするもの

|||
|:-:|:--:|
|pythonのバージョン管理|pyenv|
|pythonのパッケージ管理|pip 9.0.3|
|opencv|opencv 3.4.0|
|tensorflow|tensorflow 1.7.0|
|Keras|2.1.5|
|git||

tensorflowはGoogleが提供する深層学習のライブラリ.
Kerasを使うと深層学習の関数が綺麗にまとまり扱いやすい.裏でtensorflowが動く.

## 1.pipのインストール

```
$ sudo apt-get update
$ sudo apt-get install python-pip python3-pip
```

**pipのアップグレード**

```
$ pip install --upgrade pip
```

**バージョン確認方法**

```
$ pip list
```

## 2.pyenvのインストール

**gitのインストール**

```
$ sudo apt-get install git
```

**pyenvに必要なライブラリをインストール**

```
$ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils
```

**gitからpyenvをクローン**


```
$ git clone https://github.com/yyuu/pyenv.git ~/.pyenv
```

**bashrcを反映**

```
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
$ exec $SHELL
```

## 3.python3をインストール

```
$ pyenv install 3.5.3
```

**デフォルトで動くpythonのバージョンを3.5にする**

```
$ pyenv global 3.5.3
```

## 4.Opencvのインストール

```
$ pip install opencv-python
```

## 5.tensorflowのインストール

```
$ pip install tensorflow
```

## 6.Kerasのインストール

```
$ pip install keras
```
