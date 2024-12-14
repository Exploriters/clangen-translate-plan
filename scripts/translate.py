class translate():
    ''' 翻译文本的词典，请按照各自的语言排好。 '''
    dicts = {
        "chinese": {
            #region ========== UNIVERSAL ==========
            "universal.Open Data Directory": "打开文件目录",
            "universal.Opens the data directory.<br>This is where save files<br>and logs are stored.": "打开文件目录。<br>也就是存档与日志的所在处。",
            #endregion
            #region ========== START SCREEN ==========
            "start.Warning: This game contains mild depictions of gore, canon-typical violence and animal abuse.": "警告：本游戏包含关于血腥、传统意义暴力与虐待动物的温和描述。",
            "start.continue": "继续",
            "start.switch clan": "切换族群",
            "start.new clan": "新的族群",
            "start.settings + info": "设置&信息",
            "start.quit": "退出",
            "start.Check out our Twitter!": "访问我们的Twitter！",
            "start.Check out our Tumblr!": "访问我们的Tumblr！",
            "start.Join our Discord!": "加入我们的Discord！",
            #endregion
            #region ========== SETTING SCREEN ==========
            "setting.general settings": "常规设置",
            "setting.audio settings": "音频设置",
            "setting.info": "信息（会崩别点）",
            "setting.language": "语言选项",
            "setting.Save Settings": "保存设置",
            "setting.windowed": "窗口",
            "setting.fullscreen": "全屏",
            "setting.This will put the game into [screentext] mode.<br><br><b>Important:</b> This also saves all changed settings!": "这会让游戏转变为[screentext]模式。<br><br><b>注意：</b>这也会保存所有的设置修改！",
            "setting.Change the language of the game here. This has not been implemented yet.": "在这里修改你的语言设置，重启以完全应用",
            #region ====== GAME SETTING ======
            "setting.Dark mode": "深色模式",
            "setting.Camp backgrounds will match with the mode: nighttime for dark mode and daytime for light mode.": "营地背景会与模式相匹配：<br>深色模式时为夜间，<br>浅色模式时为日间",
            "setting.Ignore fullscreen scaling rules": "无视全屏大小规则",
            "setting.If enabled, fullscreen will display as large as possible (toggle fullscreen to update). This may include visual artifacts.": "若启用，全屏时将尽可能地将<br>画面显示得更大（切换全屏以<br>刷新）<br>这可能会影响到视觉效果",
            "setting.Disable sprite antialiasing": "禁用贴图抗锯齿",
            "setting.If enabled, sprites and patrol art will no longer be antialiased (\"blurry\"/\"smooth\") when in fullscreen.": "若启用，立绘和巡逻插图在<br>全屏时将不再抗锯齿（即“平<br>滑”或“模糊”）",
            "setting.Custom cursor": "自定义鼠标指针",
            "setting.The cursor will be replaced with a cat paw. The cursor is currently unfinished and is prone to crashing.": "鼠标指针将被替换为一个猫爪<br>指针当前是未完成的，容易<br>导致游戏崩溃",
            "setting.Keybinds": "键位绑定",
            "setting.Enables certain keybinds to be used throughout the menus for quick navigation.": "允许在整个菜单中使用某些<br>键位绑定以便快速导航",
            "setting.Enable Shaders": "启用光影",
            "setting.This will add a shading layer onto the cat sprites.": "这会在猫咪的立绘上增加一层<br>光影",
            "setting.Allow mild gore and blood in patrol artwork": "允许温和的血腥巡逻插图",
            "setting.Mild gore and blood will be allowed in the artwork displayed alongside patrols.": "温和的血腥巡逻插图会被允许<br>显示在巡逻左侧",
            "setting.Enable Discord integration": "启用Discord整合包",
            "setting.Discord will show info about your Clan, including your Clan name": "Discord会展示你族群的信息<br>包括你的族名",
            "setting.Check for updates": "检查更新",
            "setting.Automatically checks for updates on startup": "在启动时自动检查更新",
            "setting.Display changelog on startup": "启动时显示更新日志",
            "setting.Shows the changelog of the latest release on startup": "在启动时显示最新更新日志",
            "setting.Allow special date events": "允许特殊日期事件",
            "setting.Certain changes may be made to the game on special days such as April Fools": "在某些特殊的日子，<br>比如愚人节，游戏可能会发生<br>些许变化",
            "setting.Randomize relationship values when creating Clan": "在创建族群时随机关系值",
            "setting.Clan founder cats will start the game with established relationships.": "族群创建者在开始游戏时彼此<br>间将已然有关系联系",
            "setting.Use they/them as default pronouns": "将“祂/祂们”（they/them）作为默认代词",
            "setting.If this setting is on new cats will generate with they/them pronouns, regardless of gender.": "若启用，新猫生成时将使用<br>“祂/祂们”作为代词<br>无论此猫是什么性别",
            #endregion
            #endregion
            #region ========== WINDOWS ==========
            "windows.Would you like to save your game before exiting to the Main Menu? If you don't, progress<br>may be lost!": "你想要在退出前保存你的游戏吗？<br>如果不的话，你的进度可能会丢失！",
            "windows.Do you wish to delete [clanName]? This is permanent and cannot be undone.": "你想要删掉[clanName]吗？<br>这是永久性的而且无法被撤销！",
            "windows.Delete it!": "删了它！",
            "windows.No! Go back!": "不！刀下留族！",
            "windows.[clanName] has died out. For now, this is where their story ends. Perhaps it's time to tell a new tale?": "[clanName]已然灭亡了，这就是它们故事的终结。<br>也许是时候讲一个新故事了？",
            "windows.(leaving will not erase the save file)": "（离开并不会擦除存档文件）",
            "windows.begin anew": "另起篇章",
            "windows.not yet": "暂且观望",
            "windows.Change Cat Name": "修改猫名",
            "windows.-Change [catName]'s Name-": "修改[catName]的名字",
            "windows.Name Changed!": "名字已更改！",
            "windows.done": "完成",
            "windows.Randomize the prefix": "随机前缀",
            "windows.Randomize the suffix": "随机后缀",
            "windows.Remove the cat's special suffix": "移除猫咪的特殊后缀",
            "windows.Re-enable the cat's special suffix": "重新启用猫咪的特殊后缀",
            "windows.Create Cat Pronouns": "创建猫的称谓",
            "windows.Create new pronouns, <br>you have full control. <br>Test your created pronouns before saving them!": "创建新的称谓，你有绝对的控制权。<br>在你保存称谓前测试它们！",
            "windows.Pronoun Creation": "创建称谓",
            "windows.<b>Demo": "<b>测试",
            "windows.Subject": "主语",
            "windows.Object": "宾语",
            "windows.Possessive": "物主代词",
            "windows.Independent<br>Possessive": "<br>独立所有格代词",
            "windows.Reflexive": "反身代词",
            "windows.Singular": "单数形式",
            "windows.Plural": "复数形式",
            "windows.Pronoun saved and added to presets!": "称谓已被保存并加入到预设了！",
            "windows.save": "保存",
            "windows.Test Set": "测试组合",

            #region ====== SYMBOL ======
            "windows.Show Symbols With:": "按分类显示族徽：",
            "symbolTag.plant": "植物",
            "symbolTag.flower": "花朵",
            "symbolTag.tree": "树木",
            "symbolTag.leaf": "草叶",
            "symbolTag.other plant": "其他植物",
            "symbolTag.fruit": "水果",
            "symbolTag.animal": "动物",
            "symbolTag.cat": "猫咪",
            "symbolTag.fish": "鱼类",
            "symbolTag.bird": "鸟类",
            "symbolTag.mammal": "哺乳类",
            "symbolTag.bug": "昆虫",
            "symbolTag.other animal": "其他动物",
            "symbolTag.element": "元素",
            "symbolTag.water": "水",
            "symbolTag.fire": "火",
            "symbolTag.earth": "土",
            "symbolTag.air": "气",
            "symbolTag.light": "光",
            "symbolTag.location": "地点",
            "symbolTag.descriptor": "描述",
            "symbolTag.miscellaneous": "杂项",
            #endregion
            #endregion
        }
    }

    def tran(self, language = "english", rep = []):
        '''
        翻译指定的文本内容！
        :param self: 【必须】需要被翻译的文本的唯一标识符。
        :param language: 【可选】游戏的当前语言，一般来说应该是game.settings["language"]。若留空将默认使用english。
        :param rep: 【可选】由替换文本组成的数组，格式为：[[替换词1, 目标词1],[替换词2, 目标词2]]
        :return: 返回翻译后的文本为字符串。
        '''
        if language == "english":
            return str(self)[str(self).index('.')+1:]
        else:
            result = translate.dicts.get(language).get(self,str(self)[str(self).index('.')+1:])
            if len(rep) > 0 :
                for i in range(0, len(rep), 1):
                    result = result.replace(str(rep[i][0]), str(rep[i][1]))
            return result