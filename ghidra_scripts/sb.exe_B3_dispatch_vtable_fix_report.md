B3 Dispatch Vtable Fix Report
Vtable base: 0154ebd8

Slot +0x0 @ 0154ebd8
  rawTarget: 00424f7d
  resolvedTarget: 006fd070
  thunkKind: JMP
  functionBody: 006fd070 .. 006fd092

Slot +0x4 @ 0154ebdc
  rawTarget: null
  resolvedTarget: null
  thunkKind: null

Slot +0x8 @ 0154ebe0
  rawTarget: 0159a7d0
  resolvedTarget: null
  thunkKind: null

Slot +0xc @ 0154ebe4
  rawTarget: 0041a195
  resolvedTarget: 0043cc70
  thunkKind: JMP
  functionBody: 0043cc70 .. 0043cc73
  disasmPreview:
    0043cc70  MOV EAX,dword ptr [ECX + 0x4]
    0043cc73  RET
    0043cc90  PUSH EBP
    0043cc91  MOV EBP,ESP
    0043cc93  PUSH -0x1
    0043cc95  PUSH 0xd16073
    0043cc9a  MOV EAX,FS:[0x0]
    0043cca0  PUSH EAX
    0043cca1  MOV dword ptr FS:[0x0],ESP
    0043cca8  PUSH ECX
    0043cca9  PUSH EBX
    0043ccaa  MOV EBX,ECX
    0043ccac  PUSH ESI
    0043ccad  PUSH EDI
    0043ccae  MOV dword ptr [EBP + -0x10],EBX
    0043ccb1  MOV EDI,dword ptr [EBX + 0x4]
    0043ccb4  MOV ESI,dword ptr [EBX]
    0043ccb6  CMP ESI,EDI
    0043ccb8  MOV dword ptr [EBP + -0x4],0x0
    0043ccbf  JZ 0x0043ccf1
    0043ccc1  MOV EAX,dword ptr [ESI]
    0043ccc3  MOV dword ptr [ESI],0x0
    0043ccc9  TEST EAX,EAX
    0043cccb  JZ 0x0043cce4
    0043cccd  CMP EAX,-0x1
    0043ccd0  JZ 0x0043cce4
    0043ccd2  MOV ECX,dword ptr [EAX + 0x8]
    0043ccd5  PUSH ESI
    0043ccd6  MOV EDX,dword ptr [ECX + 0x4]
    0043ccd9  LEA ECX,[EDX + EAX*0x1 + 0x8]

Slot +0x10 @ 0154ebe8
  rawTarget: 0041e8c6
  resolvedTarget: 006f9eb0
  thunkKind: JMP
  functionBody: 006f9eb0 .. 006f9ed0

Slot +0x14 @ 0154ebec
  rawTarget: 00426f49
  resolvedTarget: 005311b0
  thunkKind: JMP
  functionBody: 005311b0 .. 005311d3
  disasmPreview:
    005311b0  PUSH ESI
    005311b1  MOV ESI,ECX
    005311b3  LEA EAX,[ESI + 0x4]
    005311b6  PUSH EAX
    005311b7  CALL 0x0040bdc5
    005311bc  ADD ESP,0x4
    005311bf  TEST EAX,EAX
    005311c1  JNZ 0x005311d0
    005311c3  TEST ESI,ESI
    005311c5  JZ 0x005311d0
    005311c7  MOV EDX,dword ptr [ESI]
    005311c9  PUSH 0x1
    005311cb  MOV ECX,ESI
    005311cd  CALL dword ptr [EDX + 0x4]
    005311d0  POP ESI
    005311d1  RET 0x4
    005311f0  MOV CL,byte ptr [0x01aae710]
    005311f6  MOV AL,0x1
    005311f8  TEST AL,CL
    005311fa  JNZ 0x00531204
    005311fc  OR CL,AL
    005311fe  MOV byte ptr [0x01aae710],CL
    00531204  PUSH 0x4202fc
    00531209  CALL 0x00cd891e
    0053120e  POP ECX
    0053120f  RET
    00531220  PUSH EBP
    00531221  MOV EBP,ESP
    00531223  PUSH -0x1
    00531225  PUSH 0xd2af6e

Slot +0x18 @ 0154ebf0
  rawTarget: 004040cf
  resolvedTarget: 006caa00
  thunkKind: JMP
  functionBody: 006caa00 .. 006caa02

Slot +0x1c @ 0154ebf4
  rawTarget: 0041faf5
  resolvedTarget: 006f9e70
  thunkKind: JMP
  functionBody: 006f9e70 .. 006f9e93

Slot +0x20 @ 0154ebf8
  rawTarget: 00428fab
  resolvedTarget: 006f9f70
  thunkKind: JMP
  functionBody: 006f9f70 .. 006fa47e

Slot +0x24 @ 0154ebfc
  rawTarget: 0040e7af
  resolvedTarget: 006caa20
  thunkKind: JMP
  functionBody: 006caa20 .. 006caa22

Slot +0x28 @ 0154ec00
  rawTarget: 00408855
  resolvedTarget: 006fa620
  thunkKind: JMP
  functionBody: 006fa620 .. 006fa637

Slot +0x2c @ 0154ec04
  rawTarget: 0041a7e9
  resolvedTarget: 006fa650
  thunkKind: JMP
  functionBody: 006fa650 .. 006fa680

