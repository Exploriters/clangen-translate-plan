# clangen翻译计划！
### [原版Discord频道](https://discord.gg/clangen) || [原版在线网页](https://clangen.io) || [Itch.io页面](https://sablesteel.itch.io/clan-gen-fan-edit) ||[模组Discord帖子](https://discord.com/channels/1003759225522110524/1280195222445228206)
## 描述
致力于为Clangen增加多语言支持（主要是汉化）的尝试！:D
## Clangen原版作者
Original creator: just-some-cat.tumblr.com
Fan-edit creator: SableSteel, and many others
## 如何游玩汉化版？
我不知道【草】实际上我对如何处理release毫无头绪，它总是引发各种我意想不到的混乱……不过好在我已经摸索到了办法，你可以通过加入QQ群以在群文件中简单地下载到可以开袋即食的release版本↓
QQ群：208213687
### 启用汉化步骤
1.下载群文件中，CLANGEN汉化版内，标注了PACKED的压缩包，解压缩后，你会在clangen文件夹内看见一个exe文件，双击即可运行。
2.游戏默认是英文，要启用中文，请点击settings+info，在里面点击language，随后选择chinese即可。
### Q&A
#### Q：箭头有字符显示问题！
A：箭头？那是因为clangen的箭头是用字体拼的，我已经快因此燃尽了，我所使用的notosans字体当中并没有clangen的自定义图标字体，也许我会在之后试着解决它。
#### Q：旧存档可以迁移到汉化版吗？
A：如果你能把存档迁移到汉化版对应的稳定版，那么你就完全可以把存档迁移至汉化版。
#### Q：汉化版是否提供更新支持？
A：如果不是什么稳定版确认了的大更新，我不会很想继续和这可怕的代码继续搏斗。但如果它更了，我不会掉队的。
#### Q：什么时候汉化版能够完成？
A：取决于参与者的数量和大家的进度，以及我的精力。对于非硬编码部分，如resources/dict内的所有内容，参与者可以自行翻译，其结果能被轻松地纳入到翻译字典当中，因此，它可以很快地发生进展——但是难点就在clangen从一开始就特喵根本没有考虑过语言这档子事，绝大多数的UI文本显示是完全硬编码的，因此我不得不一个个把它们修改掉，这几乎是最拖慢进度的地方。
#### Q：如果我想要创建一个别的语言给clangen，它可行吗？
A：是的，可行，只是需要修改一点代码来把它加入到游戏可选择的语言当中。我可能会优化它，取决于我的技术力吧。剩下的在translate.py当中创建对应的翻译字典即可。
#### Q：我坏档了！！！！
A：因为我确认汉化版几乎没有触碰影响实际游戏的代码，所以出现坏档在90%的情况下不是我的问题。不过，你可以加入群聊并提供报错日志，我可以试着帮你看看这个问题要如何解决。
要查看报错日志，请在电脑的系统搜索框当中输入cmd并回车以唤出cmd，然后将clangen的exe运行文件拖入cmd中以回车启动。随后，请截图**完整的**报错日志，并描述错误发生时的情况。我会尽力帮忙挽救存档。
#### Q：汉化版会夹带私货吗？
A：带了，但不多，也不算严重。提交的翻译会经过审核，与原文差异过大、夹带私货过量的都是无法通过的。
不过我坦白我在name.json里面藏了东西，不过那地方是私货聚集地我想也是广为人知的了.jpg
## Clangen汉化计划贡献者
Clangen汉化计划的进展离不开数不清的参与者们！大家的帮助是无比珍贵的！！
我们在这里且随时欢迎Clangen爱好者们与意图参与汉化的贡献者们的到来！↓
QQ群：208213687
## Clangen原版下载
[稳定版](https://clangen.io/download)
[dev版](https://clangen.io/download-development)
# 以下是原README.MD当中提供的如何从源文件运行Clangen的方法
## Running from source
ClanGen uses poetry to manage virtual environments. Therefore it is required to install the dependencies and run the game from source without manual tweaking.

### Installing python
ClanGen currently supports python versions >=3.8 and <3.13.

Download from the official python website here: https://www.python.org/downloads

Check if python is installed correctly by running `python3 --version`


### Installing poetry
Follow the instructions for installing poetry from the official website: https://python-poetry.org/docs/#installing-with-pipx

#### Linux, macOS, Windows (WSL)
Open a terminal and paste this:
```
python3 -m pip install pipx --user
python3 -m pipx install poetry
python3 -m pipx ensurepath
```
Then restart your terminal and check if poetry is installed by running `poetry --version`

#### Windows (Powershell)
Open a PowerShell window (Windows key and then enter `PowerShell`) and paste this:
```
py -m pip install pipx --user
py -m pipx install poetry
py -m pipx ensurepath
```
or in case you installed Python from the Windows Store:
```
python -m pip install pipx --user
python -m pipx install poetry
python -m pipx ensurepath
```
Then restart your terminal and check if poetry is installed by running `poetry --version`

### Running the game via the helper scripts
#### Linux, macOS
Double click the `run.sh` script or open it in the terminal via `./run.sh` with the current working directory set to the game's root directory.

#### Windows
Double click the `run.bat` script.

### Running the game via Visual Studio Code
To configure poetry to run with Visual Studio Code, open the ClanGen folder and run the following code snippet in the Visual Studio Code integrated terminal (Ctrl + ` to open the integrated terminal):
```
poetry config virtualenvs.in-project true
```

Now run the following command to create a virtual environment:
```
poetry install --no-root
```

It should have created a `.venv` folder in the root directory of the game.
If you don't see it, remove existing poetry virtual environments by running `poetry env remove python` and try again.

After that, ensure that you have the Python extension installed in Visual Studio Code. You can install it from the Extensions tab on the left sidebar. [(or click here)
](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

Then, open the Command Palette (Ctrl+Shift+P) and search for `Python: Select Interpreter`. Select the virtual environment created by poetry (it should mention a `.venv` somewhere).

Finally, open the `main.py` file and click the play button in the top right corner to run the game.


## Bug Reporting
We have migrated to GitHub Issues for bug reporting and tracking. We no longer review bug reports from the retired Google Form.

## Contributing
If you'd like to contribute to Clangen, please read our [Contributing guide](https://github.com/ClanGenOfficial/clangen/blob/development/CONTRIBUTING.md).
