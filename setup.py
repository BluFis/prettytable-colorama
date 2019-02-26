# -*- coding: utf-8 -*-
from distutils.core import setup

import py2exe


options = {"py2exe":

               {"compressed": 1,#压缩

                "optimize": 2,

                "bundle_files": 3#所有文件打包成一个exe文件,64位环境下不支持

                }

           }

setup(

    version="1.0.0",

    description="cmd天气预报",

    name="cmd天气预报",

    options=options,

    zipfile=None,

    console=["prettytable&colorama.py"],

)