# 使用prettytable和colorama制作漂亮的cmd命令行界面 #
## 一、插件的作用 ##
**prettytable**这个插件的作用是在cmd命令行界面输出美观的表格页面，而**colorama**的作用是设置命令行界面文字的前景色、背景色、以及样式，让你的命令行软件获得更好的视觉效果。
## 二、插件的安装 ##
- **prettytable**的安装：`pip install PrettyTable`    
- **colorama**的安装：`pip install colorama`

## 三、使用介绍    
- **prettytable**使用介绍    
1. **prettytable**创建表格：
	```python
	import prettytable as pt
	tb = pt.PrettyTable()
	tb.field_names = ["1月2日", "1月3日", "1月4日", "1月5日"]
	tb.add_row(["星期一", "星期二", "星期三", "星期四"])
	tb.add_row(["12°","11°", "13°", "11°"])
	tb.add_row(["多云","晴", "阴", "小雨"])
	print(tb)
	```
	输出结果如下：
![](https://i.imgur.com/PcyDfmu.png)
2. 重要的api：
 - `tb.add_row()`添加一行数据
 - `tb.add_column()`添加一列数据
 - `tb.set_style(pt.MSWORD_FRIENDLY)`设置输出风格为**MSWORD_FRIENDLY**     
 ![](https://i.imgur.com/nLOFCBC.png)
 - `tb.set_style(pt.PLAIN_COLUMNS)`设置输出风格为**PLAIN_COLUMNS**     
 ![](https://i.imgur.com/HtgUEMq.png)
 - `tb.set_style(pt.DEFAULT)`设置输出风格为**pt.DEFAULT**     
 ![](https://i.imgur.com/PcyDfmu.png)
 - `tb.set_style(pt.RANDOM)`设置输出风格为**pt.RANDOM**
 - `tb.get_string()`获取表格字符串
 - `tb.sortby = "col_name"`设定排序方式
 - `tb.left_padding_width = 0`设定左侧不填充空白字符
 - `tb.border = 0`不显示边框
 - `tb.get_html_string()`输出html代码
 	```html
	<table>
	    <tr>
	        <th>1月2日</th>
	        <th>1月3日</th>
	        <th>1月4日</th>
	        <th>1月5日</th>
	    </tr>
	    <tr>
	        <td>星期一</td>
	        <td>星期二</td>
	        <td>星期三</td>
	        <td>星期四</td>
	    </tr>
	    <tr>
	        <td>12°</td>
	        <td>11°</td>
	        <td>13°</td>
	        <td>11°</td>
	    </tr>
	    <tr>
	        <td>多云</td>
	        <td>晴</td>
	        <td>阴</td>
	        <td>小雨</td>
	    </tr>
	</table>

	```
- **colorama**使用介绍
1. 可用格式常数
 - Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.（前景色）
 - Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.（背景色）
 - Style: DIM, NORMAL, BRIGHT, RESET_ALL（DIM：低亮度（仅Linux下有效），NORMAL：正常亮度，BRIGHT：高亮度，RESET_ALL：重置所有属性）
2. 使用案例
	```python
	import colorama as ca
	print(ca.Fore.RED + 'some red text')
	print('still red')
	print(ca.Back.GREEN + 'and with a green background')
	print(ca.Style.DIM + 'and in dim text')
	print(ca.Style.RESET_ALL)
	print('back to normal now')
	```
结果：
![](https://i.imgur.com/in1WV1M.png)
3. 自动重置设置
```python
import colorama as ca
ca.init(autoreset=True)
print(ca.Fore.RED + 'some red text')
print('automatically back to default color again')
```
结果：
![](https://i.imgur.com/qrwBcpy.png)
## 四、cmd天气预报案例

