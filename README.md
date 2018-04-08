# 環境構築方法

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

## pipのインストール

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

## pyenvのインストール

### gitのインストール

```
$ sudo apt-get install git
```

### gitからpyenvをクローン

```
$ git clone https://github.com/yyuu/pyenv.git ~/.pyenv
```

### bashrcを反映

```
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.$ bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
$ exec $SHELL
```




