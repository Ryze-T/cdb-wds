# cdb-wds
利用白名单文件 cdb.exe 执行 shellcode

cdb.exe：自带微软签名的白名单文件<br>
calc.wds：示例wds文件，用于启动calc<br>
shellcode2wds.py：处理脚本，将处理后的shellcode转为wds格式<br>

参考文章(使用说明): [cdb执行shellcode | Ryze (ryze-t.com)](https://ryze-t.com/2022/03/23/cdb执行shellcode/)

真实环境中进行测试前先在同版本虚拟机中测试，若想反弹shell，要用 reverse tcp 的shellcode
