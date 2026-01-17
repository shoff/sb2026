B5 Draw Helper Caller Scan

Helper 005aadc0 FUN_005aadc0
  via: via_thunk:0041139c
  callsite: 005b67a7
  caller: FUN_005b6790 @ 005b6790
  setup_window:
    005b676d  MOV EAX,dword ptr [ECX]
    005b676f  PUSH EDX
    005b6770  MOV EDX,dword ptr [EBP + 0xc]
    005b6773  PUSH EDX
    005b6774  MOV EDX,dword ptr [EBP + 0x8]
    005b6777  PUSH EDX
    005b6778  CALL dword ptr [EAX + 0x2c]
    005b677b  POP EBP
    005b677c  RET 0xc
    005b6790  PUSH EBP
    005b6791  MOV EBP,ESP
    005b6793  MOV EAX,ECX
    005b6795  MOV ECX,dword ptr [EAX + 0x14]
    005b6798  TEST ECX,ECX
    005b679a  JZ 0x005b67b9
    005b679c  MOV DL,byte ptr [EAX + 0x10]
    005b679f  TEST DL,DL
    005b67a1  JZ 0x005b67b0
    005b67a3  MOV AL,byte ptr [EAX + 0x11]
    005b67a6  PUSH EAX

