# Python 环境搭建
# 1.安装解释器
1. Python是解释型语言因此需要安装Python的解释器。
2. 目前Python解释器最新版本为python3.12.
3. 安装方式：
   * 前往Python官网下载对应安装包[Python](https://www.python.org/)（点击前往）
   * 使用包管理器下载：Windows（winget install python）、macOS（brew install python）、Debian（sudo apt install python）、Fedora（sudo dnf install python）、ArchLinux（sudo pacman -S python）
   * 源码编译（不推荐）
**下载后打开终端输入以下命令检测是否安装成功**
~~~python
python --version
python 3.12.***
~~~
如果出现Python对应版本号，则安装成功！

# 2.编辑器和IDE
在编码过程中难免出现代码错误，错误的原因千奇百怪，常见的有以下几种：代码逻辑错误、缩进错误、字符拼写错误等。随着项目的规模越来越庞大，代码越来越复杂，管理就困难。所以一款好的编辑器或IDE就显得尤为重要！
## 什么是编辑器和IDE
1. 编辑器
   代码编辑器是一种用来编写代码的文本程序，我们可以使用代码编辑器打开项目文件，输入代码内容，保存和执行代码。一般现代的编辑器都带有简单的代码高亮，智能补全，语法分析等功能。还有的编辑器比较古老只能在终端使用，只具备简单的编辑和保存功能。这里推荐一款微软出品的智能编辑器[VScode](https://code.visualstudio.com/)，该编辑器自带的功能就已经十分强大，你还可以通过安装插件的方式将其打造成为具备IDE功能的编辑器，安装好VScode后，在插件搜索python插件就可以编写和允许python插件了。此外推荐的编辑器还有[Sublime Text](https://www.sublimetext.com/)，终端编辑器[Vim](https://www.vim.org/)，[NeoVim](https://neovim.io/)(Vim升级版)。
2. IDE(Integrated Development Environment)
   IDE全称集成开发环境，是一种极为强大的开发工具，包括代码编辑，代码补全，语法分析，逻辑分析，虚拟环境，版本管理等功能。IDE功能丰富，体积较大，占用内存较多。Python IDE推荐[PyCharm](https://www.jetbrains.com/pycharm/)。

## 3.运行你的第一个Python程序
> 打开你的开发工具或使用终端输入vim，编写你的第一个python代码。这里文件示例为main.py
~~~python
print("Hello World") # 按照程序员的惯例，打印Hello World(你好世界)!
~~~
编辑保存代码后，点击你的开发工具的运行按钮或打开终端输入以下命令:
> python main.py # 然后回车
> Hello World # 输出内容
到此位置你的第一Python程序，运行成功！