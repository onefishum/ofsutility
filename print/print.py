import sys

class Print(object):
    """ 
        # 用于实现打印，linux支持 color 参数
        > color值为：RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE（默认）
    ``` python 
        from print import Print
        print = Print()
        print ("onefish", Print, color = 'YELLOW')
        print ("onefish ", "test")
    ```
    """


    def __init__(self) -> None:
        # 颜色
        self.color= {'RED':'\033[91m','GREEN':'\033[92m','YELLOW':'\033[93m', 'BLUE':'\033[94m',
                'MAGENTA':'\033[95m','CYAN':'\033[96m', 'WHITE':'\033[97m','RESET':'\033[0m'
                }
        # 具体操作系统
        self.platform = sys.platform
        pass

    def reset_color(self):
        """
        重置颜色到默认状态
        """
        print(self.color['RESET'])
        
    def __call__(self, *args, **kwds):
        """
            用于实现打印，linux支持 color 参数
            color值为：RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE（默认）

        """
        # 在 linux 下，使用 color 颜色
        if self.platform == 'linux':
            # print (RED + args[0]+"test"+RESET)
            if 'color' in kwds:
                color = kwds['color'].upper()
                if color in self.color:
                    print(self.color[color])
            else:
                print(self.color['WHITE'])
        print (args)

        # 在linux 下，重置颜色
        self.reset_color()
        pass


