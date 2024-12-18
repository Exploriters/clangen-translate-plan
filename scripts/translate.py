from scripts.game_structure.game_essentials import game

class translate():
    ''' 翻译文本的词典，请按照各自的语言排好。 '''
    dicts = {
        "chinese": {
            #region ========== UNIVERSAL ==========
            "universal.Open Data Directory": "打开文件目录",
            "universal.Opens the data directory.<br>This is where save files<br>and logs are stored.": "打开文件目录。<br>也就是存档与日志的所在处。",
            #endregion
            #region ========== PRONOUNS ==========
            "pronouns.he": "他",
            "pronouns.him": "他",
            "pronouns.his": "他的",
            "pronouns.himself": "他自己",
            "pronouns.she": "她",
            "pronouns.her": "她",
            "pronouns.hers": "她的",
            "pronouns.herself": "她自己",
            "pronouns.they": "祂",
            "pronouns.them": "祂",
            "pronouns.theirs": "祂的",
            "pronouns.themself": "祂自己",
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
            "windows.[subject] are quick.<br>": "[subject]很迅速。<br>",
            "windows.[subject] is quick.<br>": "[subject]很迅速。<br>",
            "windows.Everyone saw [object]. <br>": "所有猫都看见了[object]。<br>",
            "windows.[poss] paw slipped.<br>": "[poss]爪子打滑了。<br>",
            "windows.That den is [inposs].<br>": "那个巢穴是[inposs]。<br>",
            "windows.This cat hunts by [self].<br>": "这猫正凭[self]在狩猎。<br>",
            "windows.Kill Cat": "杀死猫咪",
            "windows.<b>-- How did this cat die? --</b>": "<b>—— 这只猫是怎么死的？——</b>",
            "windows.If this is checked, the leader will lose all {PRONOUN/m_c/poss} lives": "若启用此项，族长将会失去{PRONOUN/m_c/poss}所有生命",
            "windows.This cat died when {PRONOUN/m_c/subject}...": "这只猫{PRONOUN/m_c/subject}死于……",
            "windows.{VERB/m_c/were/was} killed by a higher power.": "被某种不可名状的强大力量杀死了。",
            "windows.Take all the leader's lives": "夺走族长的所有生命",
            "windows.{VERB/m_c/were/was} killed by something unknowable to even StarClan": "被某种甚至星族都对此一无所知的东西杀害了",
            "windows.This cat was killed by a higher power.": "这只猫被某种不可名状的强大力量杀死了。",
            "windows.Update in progress.": "正在更新中…",
            "windows.Downloading update...": "正在下载更新…",
            "windows.The game will automatically restart in 3...": "游戏将在3秒后自动重启…",
            "windows.The game will automatically restart in [time]...": "游戏将在[time]秒后自动重启…",
            "windows.<strong>Update to ClanGen [latest_version_number]</strong>": "<strong>版本更新[latest_version_number]可用于Clangen</strong>",
            "windows.Your current version: [current_version_number]": "当前版本：[current_version_number]",
            "windows.Install update now?": "现在更新？(别！",
            "windows.Don't ask again": "不再询问",
            "windows.continue": "继续",
            "windows.cancel": "取消",
            "windows.Prevent fading": "阻止消散",
            "windows.Prevent kits": "阻止拥有后代",
            "windows.Prevent retirement": "阻止退休",
            "windows.Limit romantic interactions and mate changes": "限制浪漫互动与恋爱几率",
            "windows.The afterlife guide can never fade.": "来生引者永远不会消散。",
            "windows.Prevents cat from fading away after being dead for 202 moons.": "阻止猫咪在去世202月后消散。",
            "windows.Prevent the cat from adopting or having kittens.": "阻止猫咪领养或生育小猫",
            "windows.Allow cat to retiring automatically.": "允许猫咪自动退休。",
            "windows.Prevent cat from retiring automatically.": "阻止猫咪自动退休。",
            "windows.Prevent cat from automatically taking a mate, breaking up, or having romantic interactions with non-mates.": "阻止猫自动恋爱、分手或与非伴侣进行浪漫互动。",
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
            #region ========== WARRIOR DEN ==========
            "warriorDen.This screen allows you to manage your warriors more effectively! You can give them a <br>specific focus, which will provide some benefits (and possibly some negatives) to your <br>Clan.  Some focuses are not available in classic mode.  Click on each focus to see a <br>description of what they will do.  Focuses that target other Clans will allow you to <br>choose which Clans you target.  Your focus can only be changed every 3 moons, <br>so choose carefully.": "此页面允许你更有效地管理你的武士！你可以给他们一个特定的<br>专注项，这将为你的族群提供一些增益（也可能有一些惩罚）。<br>一些专注项在经典模式下不可用。<br>单击专注项以查看关于此专注项对武士行为影响的说明。<br>针对其他族群的专注允许你选择将哪个族群作为你的目标。<br>专注项每3个月只能更换一次，所以要慎重选择。",
            "warriorDen.Change Focus": "修改专注项",

            #region ====== CLAN SETTING ======
            "setting.Business As Usual": "一切照常",
            "setting.The Clan has no specific focus and won't get any bonuses.": "族群不会专注于任何特殊的事情，<br>也不会得到任何加成。",
            "setting.Feeding the Clan": "喂饱族群",
            "setting.The Clan will focus on hunting, each working warrior (including deputy and leader) and each working apprentice will gather additional prey on each moonskip.": "族群将会专注于狩猎，每只可工作的武士<br>（包括副族长和族长）和每只可工作的学徒<br>将在每次月份跳过时获取额外的猎物。",
            "setting.Assisting with Herb Gathering": "协助采集药草",
            "setting.The Clan will focus on herb gathering, each medicine cat and medicine cat apprentice will gather additional herbs on each moonskip due to extra help from the warriors.": "族群将会专注于药草采集，由于武士们的<br>额外帮助，每只巫医和巫医学徒将在每次<br>月份跳过时采集到额外的药草。",
            "setting.Threatening Outsiders": "威胁族群外的猫",
            "setting.The relationship with cats outside of the Clan decreases due to intentionally threatening behavior from your warriors.": "与族群外的猫的关系将因为你的武士们的<br>恶意威胁行为而降低。",
            "setting.Entreating with Outsiders": "联合族群外的猫",
            "setting.The relationship with cats outside of the Clan increases as your warriors make efforts to sow seeds of friendship.": "与族群外的猫的关系将因为你的武士们所<br>努力撒播的友谊之种而增加。",
            "setting.Resting and Recovering": "修生养息",
            "setting.The Clan will take more care and time in their tasks and therefore the rate of injuries, illnesses and outbreaks will be reduced.": "族群会在他们的任务当中花费更多的时间、<br>更为小心谨慎。因此，他们遭遇伤病的<br>几率会降低。",
            "setting.Sabotaging Other Clans": "妨碍其他族群",
            "setting.Your mediator and warriors work together to undermine the other Clans. Only available if you have a working mediator. Selecting this will also allow you to choose which Clans you target.": "你的斡旋猫和武士联合起来以妨碍其他族群<br>仅在你有可工作的斡旋猫时可用。当你专注<br>于此项时，你可以选择将哪个族群作为<br>你的目标。",
            "setting.Helping Other Clans": "帮助其他族群",
            "setting.Your mediator and warriors work together to help the other Clans with whatever they need. Only available if you have a working mediator. Selecting this will also allow you to choose which Clans you target.": "你的斡旋猫和武士联合起来以在其他族群<br>需要帮助时施以援手。仅在你有可工作的<br>斡旋猫时可用。当你专注于此项时，你<br>可以选择将哪个族群作为你的目标。",
            "setting.Raiding Other Clans": "掠夺其他族群",
            "setting.Your warriors begin crossing borders for resources. Prey and herbs will greatly increase each moonskip, but injuries and illnesses will increase and the relationship with other Clans decrease. You will be able to choose which Clans you target.": "你的武士开始跨过边界并掠夺资源。在每次<br>月份跳过时所收获的猎物和药草将会大大<br>增加，但与此同时武士们受到的伤病也会<br>增加，且与其他族群的关系将会降低。你<br>可以选择将哪个族群作为你的目标。",
            "setting.Hoarding Resources": "囤积资源",
            "setting.Your warriors begin stockpiling as many resources as they can get their paws on, regardless of their own safety. Prey and herbs will increase each moonskip, but injuries and illnesses will also increase.": "你的武士不顾自身安危地开始储存尽可能多<br>的资源。猎物和药草会增加，但遭遇的伤病<br>也会增加。",
            #endregion
            #endregion
        }
    }

    def tran(self, rep = []):
        '''
        翻译指定的文本内容！
        :param self: 【必须】需要被翻译的文本的唯一标识符。
        :param rep: 【可选】由替换文本组成的数组，格式为：[[替换词1, 目标词1],[替换词2, 目标词2]]
        :return: 返回翻译后的文本为字符串。
        '''
        language = game.settings["language"]
        if language == "english":
            return str(self)[str(self).index('.')+1:]
        else:
            result = translate.dicts.get(language).get(self,str(self)[str(self).index('.')+1:])
            if len(rep) > 0 :
                for i in range(0, len(rep), 1):
                    result = result.replace(str(rep[i][0]), str(rep[i][1]))
            return result
