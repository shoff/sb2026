# Allocator/Ctor Small-Object Report

- Program: sb.exe
- Timestamp: 2026-01-14 22:18:07
- Allocator: 00cd8970
- Total allocator CALL refs: 226
- Matched size calls: 22

## SIZE 0x24

- allocCalls: 7
- ctorCalls: 5
- thisResolved: 5
- callees: 4

### CALLEE FUN_00cd9870 @ 00cd9870

- ctorCalls: 2
- thisResolved: 2
- writesToThis: 246
- dispKnown: 176
- dispUnknown: 70
- listNext(+0x24): 2
- listPrev(+0x28): 2
- bulkInit(STOS*): 4
- bulkInitOnThis: 4

Alloc callsites:
- 00cd9b38
- 00cf0368

Ctor callsites:
- 00cd9b6e
- 00cf03bc

Top offsets:
- 0x4 : 46
- 0x44 : 20
- 0x84 : 14
- 0xc : 12
- 0x8 : 10
- 0x14 : 10
- 0x148 : 8
- 0x20 : 6
- 0x144 : 6
- 0x10 : 6
- 0x18 : 6
- 0x1c : 6
- 0xc4 : 4
- 0x104 : 4
- 0x58 : 4
- 0x24 : 2
- 0x28 : 2
- 0x2c : 2
- 0x30 : 2
- 0x34 : 2
- 0x38 : 2
- 0x1f : 2

Writes to [this+0x24]:
- 00cda6e7  dword ptr [ECX + 0x24]
- 00cda6e7  dword ptr [ECX + 0x24]

Writes to [this+0x28]:
- 00cda6f1  dword ptr [EDX + 0x28]
- 00cda6f1  dword ptr [EDX + 0x28]

Sample writes (first 40):
- 00cd999d  MOV dword ptr [EAX + 0x4]
- 00cd99f4  MOV dword ptr [EDX]
- 00cd9a0a  MOV dword ptr [ECX]
- 00cd9a12  MOV dword ptr [EAX + 0x8]
- 00cd9a55  MOV dword ptr [EAX]
- 00cd9a5e  MOV dword ptr [ECX + 0x4]
- 00cd9a68  MOV dword ptr [EDX + 0x8]
- 00cd9a72  MOV dword ptr [EAX + 0xc]
- 00cd9a7c  MOV dword ptr [ECX + 0x10]
- 00cd9a86  MOV dword ptr [EDX + 0x14]
- 00cd9a90  MOV dword ptr [EAX + 0x18]
- 00cd9a9a  MOV dword ptr [ECX + 0x1c]
- 00cd9ad2  MOV dword ptr [ECX]
- 00cd9bee  MOV dword ptr [ECX]
- 00cd9bf6  MOV dword ptr [EAX + 0x4]
- 00cd9bff  MOV dword ptr [EDX + 0x8]
- 00cd9c08  MOV dword ptr [ECX + 0xc]
- 00cd9c36  MOV dword ptr [EDX + 0x8]
- 00cd9c42  MOV dword ptr [EDX + 0x4]
- 00cd9c4d  MOV dword ptr [EDX]
- 00cd9c58  MOV dword ptr [EDX + 0x4]
- 00cd9c71  MOV dword ptr [EDX]
- 00cd9c80  MOV dword ptr [EAX + 0xc]
- 00cd9cbd  MOV dword ptr [EAX + 0x4]
- 00cd9cc7  MOV dword ptr [ECX + 0xc]
- 00cd9db6  MOV dword ptr [EAX + 0xc]
- 00cd9dc0  MOV dword ptr [ECX + 0x4]
- 00cd9dcf  MOV dword ptr [EAX]
- 00cd9dde  MOV dword ptr [ECX + 0x4]
- 00cd9e1c  MOV dword ptr [ECX + EDX*0x4]
- 00cd9e36  MOV dword ptr [EDX + 0x4]
- 00cd9e8e  MOV dword ptr [ECX + 0x4]
- 00cd9f1a  MOV dword ptr [EDX + 0x4]
- 00cd9f6c  MOV dword ptr [EDX + EAX*0x4]
- 00cd9fa8  MOV dword ptr [ECX + 0x4]
- 00cda05c  MOV byte ptr [EAX]
- 00cda2a6  MOV dword ptr [ECX + EDX*0x4]
- 00cda2b8  MOV dword ptr [ECX + 0x4]
- 00cda2da  MOV dword ptr [EDX + ECX*0x4]
- 00cda34e  MOV dword ptr [ECX + EAX*0x4]

### CALLEE FUN_00ce0c50 @ 00ce0c50

- ctorCalls: 1
- thisResolved: 1
- writesToThis: 56
- dispKnown: 29
- dispUnknown: 27
- listNext(+0x24): 0
- listPrev(+0x28): 0
- bulkInit(STOS*): 2
- bulkInitOnThis: 2

Alloc callsites:
- 00ce4478

Ctor callsites:
- 00ce4576

Top offsets:
- 0x4 : 7
- 0x148 : 3
- 0xc : 3
- 0x17c : 3
- 0x40 : 2
- 0x144 : 2
- 0x44 : 2
- 0x8 : 2
- 0xffffffffffffffff : 1
- 0x1 : 1
- 0xfffffffffffffffc : 1
- 0x14c : 1
- 0x10 : 1

Sample writes (first 40):
- 00ce0dbe  MOV dword ptr [ECX]
- 00ce0e1c  MOV dword ptr [EAX]
- 00ce0e2d  MOV dword ptr [ECX + 0x8]
- 00ce0e36  MOV dword ptr [EAX + 0x10]
- 00ce0edd  MOV dword ptr [ECX]
- 00ce1156  MOV dword ptr [EDX]
- 00ce1170  MOV dword ptr [EAX]
- 00ce13ef  MOV dword ptr [EAX]
- 00ce140b  MOV dword ptr [ECX + 0x4]
- 00ce1587  MOV dword ptr [EAX]
- 00ce167e  MOV dword ptr [EAX]
- 00ce18a6  MOV dword ptr [ECX]
- 00ce19b2  MOV dword ptr [ECX + 0x144]
- 00ce19e0  MOV dword ptr [EAX]
- 00ce19e9  MOV dword ptr [ECX + 0x144]
- 00ce19f6  MOV dword ptr [EDX + 0x148]
- 00ce1a03  MOV dword ptr [EAX + 0x17c]
- 00ce1ae0  MOV dword ptr [EAX + EDX*0x4 + 0x14c]
- 00ce1af6  MOV dword ptr [ECX + 0x148]
- 00ce1b3b  MOV dword ptr [EAX + 0x17c]
- 00ce1b63  MOV dword ptr [ECX]
- 00ce1b96  MOV dword ptr [EDX + 0x17c]
- 00ce1baf  MOV dword ptr [EDX + 0x148]
- 00ce1bd7  MOV dword ptr [EAX]
- 00ce1d60  MOV byte ptr [EDX]
- 00ce1d78  MOV byte ptr [EAX]
- 00ce1d91  MOV byte ptr [EDX]
- 00ce1dab  MOV byte ptr [EAX]
- 00ce1dba  MOV byte ptr [EAX + 0x1]
- 00ce1dd6  MOV byte ptr [EDX]
- 00ce1dee  MOV byte ptr [EAX]
- 00ce1dff  MOV byte ptr [ECX]
- 00ce1e18  MOV byte ptr [ECX + -0x1]
- 00ce2204  MOV dword ptr [EDX + 0x4]
- 00ce2293  MOV dword ptr [ECX + 0xc]
- 00ce22d8  MOV dword ptr [EAX + ECX*0x4]
- 00ce22e7  MOV dword ptr [EDX + 0x4]
- 00ce2350  MOV dword ptr [EDX + -0x4]
- 00ce236b  MOV dword ptr [ECX]
- 00ce2383  MOV dword ptr [EDX + 0x4]

### CALLEE FUN_00ce0cd0 @ 00ce0cd0

- ctorCalls: 1
- thisResolved: 1
- writesToThis: 56
- dispKnown: 29
- dispUnknown: 27
- listNext(+0x24): 0
- listPrev(+0x28): 0
- bulkInit(STOS*): 2
- bulkInitOnThis: 2

Alloc callsites:
- 00cd9878

Ctor callsites:
- 00cd99fc

Top offsets:
- 0x4 : 7
- 0x148 : 3
- 0xc : 3
- 0x17c : 3
- 0x40 : 2
- 0x144 : 2
- 0x44 : 2
- 0x8 : 2
- 0xffffffffffffffff : 1
- 0x1 : 1
- 0xfffffffffffffffc : 1
- 0x14c : 1
- 0x10 : 1

Sample writes (first 40):
- 00ce0dbe  MOV dword ptr [ECX]
- 00ce0e1c  MOV dword ptr [EAX]
- 00ce0e2d  MOV dword ptr [ECX + 0x8]
- 00ce0e36  MOV dword ptr [EAX + 0x10]
- 00ce0edd  MOV dword ptr [ECX]
- 00ce1156  MOV dword ptr [EDX]
- 00ce1170  MOV dword ptr [EAX]
- 00ce13ef  MOV dword ptr [EAX]
- 00ce140b  MOV dword ptr [ECX + 0x4]
- 00ce1587  MOV dword ptr [EAX]
- 00ce167e  MOV dword ptr [EAX]
- 00ce18a6  MOV dword ptr [ECX]
- 00ce19b2  MOV dword ptr [ECX + 0x144]
- 00ce19e0  MOV dword ptr [EAX]
- 00ce19e9  MOV dword ptr [ECX + 0x144]
- 00ce19f6  MOV dword ptr [EDX + 0x148]
- 00ce1a03  MOV dword ptr [EAX + 0x17c]
- 00ce1ae0  MOV dword ptr [EAX + EDX*0x4 + 0x14c]
- 00ce1af6  MOV dword ptr [ECX + 0x148]
- 00ce1b3b  MOV dword ptr [EAX + 0x17c]
- 00ce1b63  MOV dword ptr [ECX]
- 00ce1b96  MOV dword ptr [EDX + 0x17c]
- 00ce1baf  MOV dword ptr [EDX + 0x148]
- 00ce1bd7  MOV dword ptr [EAX]
- 00ce1d60  MOV byte ptr [EDX]
- 00ce1d78  MOV byte ptr [EAX]
- 00ce1d91  MOV byte ptr [EDX]
- 00ce1dab  MOV byte ptr [EAX]
- 00ce1dba  MOV byte ptr [EAX + 0x1]
- 00ce1dd6  MOV byte ptr [EDX]
- 00ce1dee  MOV byte ptr [EAX]
- 00ce1dff  MOV byte ptr [ECX]
- 00ce1e18  MOV byte ptr [ECX + -0x1]
- 00ce2204  MOV dword ptr [EDX + 0x4]
- 00ce2293  MOV dword ptr [ECX + 0xc]
- 00ce22d8  MOV dword ptr [EAX + ECX*0x4]
- 00ce22e7  MOV dword ptr [EDX + 0x4]
- 00ce2350  MOV dword ptr [EDX + -0x4]
- 00ce236b  MOV dword ptr [ECX]
- 00ce2383  MOV dword ptr [EDX + 0x4]

### CALLEE FUN_00ceb650 @ 00ceb650

- ctorCalls: 1
- thisResolved: 1
- writesToThis: 27
- dispKnown: 24
- dispUnknown: 3
- listNext(+0x24): 1
- listPrev(+0x28): 1
- bulkInit(STOS*): 0
- bulkInitOnThis: 0

Alloc callsites:
- 00ce8b98

Ctor callsites:
- 00ce8bbc

Top offsets:
- 0x4 : 3
- 0xc : 3
- 0x8 : 2
- 0x10 : 2
- 0x14 : 2
- 0x18 : 2
- 0x1c : 2
- 0x20 : 1
- 0x24 : 1
- 0x28 : 1
- 0x2c : 1
- 0x30 : 1
- 0x34 : 1
- 0x38 : 1
- 0x3c : 1

Writes to [this+0x24]:
- 00cecba4  dword ptr [EDX + 0x24]

Writes to [this+0x28]:
- 00cecdd0  dword ptr [EDX + 0x28]

Sample writes (first 40):
- 00ceb6e3  MOV dword ptr [EDX]
- 00ceb7c8  MOV dword ptr [EDX + 0x4]
- 00cebad8  MOV dword ptr [EDX + 0xc]
- 00cebd02  MOV dword ptr [EDX + 0x10]
- 00cebf98  MOV dword ptr [ECX + 0x14]
- 00cec29a  MOV dword ptr [EDX + 0x18]
- 00cec608  MOV dword ptr [EDX + 0x1c]
- 00cec90c  MOV dword ptr [EAX + 0x20]
- 00cecba4  MOV dword ptr [EDX + 0x24]
- 00cecdd0  MOV dword ptr [EDX + 0x28]
- 00cecf90  MOV dword ptr [EAX + 0x2c]
- 00ced0e4  MOV dword ptr [EDX + 0x30]
- 00ced1cc  MOV dword ptr [EDX + 0x34]
- 00ced248  MOV dword ptr [EAX + 0x38]
- 00ced251  MOV dword ptr [EDX + 0x3c]
- 00ced2f3  MOV dword ptr [EDX]
- 00ced3d8  MOV dword ptr [EDX + 0x4]
- 00ced52a  MOV dword ptr [ECX + 0x8]
- 00ced6e8  MOV dword ptr [EDX + 0xc]
- 00ced83c  MOV dword ptr [ECX + 0x10]
- 00ced924  MOV dword ptr [ECX + 0x14]
- 00ced9a0  MOV dword ptr [EDX + 0x18]
- 00ced9a9  MOV dword ptr [ECX + 0x1c]
- 00ceda53  MOV dword ptr [EDX]
- 00cedb09  MOV dword ptr [EAX + 0x4]
- 00cedc2c  MOV dword ptr [EAX + 0x8]
- 00cedd8b  MOV dword ptr [EAX + 0xc]

## SIZE 0x28

- allocCalls: 6
- ctorCalls: 6
- thisResolved: 6
- callees: 6

### CALLEE FUN_00cdf040 @ 00cdf040

- ctorCalls: 1
- thisResolved: 1
- writesToThis: 97
- dispKnown: 18
- dispUnknown: 79
- listNext(+0x24): 0
- listPrev(+0x28): 0
- bulkInit(STOS*): 2
- bulkInitOnThis: 2

Alloc callsites:
- 00cd9008

Ctor callsites:
- 00cd9125

Top offsets:
- 0x4 : 4
- 0x148 : 3
- 0x17c : 3
- 0x144 : 2
- 0x10 : 1
- 0xffffffffffffffff : 1
- 0x1 : 1
- 0x8 : 1
- 0xc : 1
- 0x14c : 1

Sample writes (first 40):
- 00cdf6c6  MOV dword ptr [EDX + 0x4]
- 00cdf6cf  MOV dword ptr [ECX]
- 00cdfd66  MOV dword ptr [EDX + 0x4]
- 00cdfd6f  MOV dword ptr [ECX]
- 00cdff9c  MOV byte ptr [ECX]
- 00cdffb5  MOV byte ptr [ECX]
- 00cdffce  MOV byte ptr [ECX]
- 00cdffe4  MOV byte ptr [ECX]
- 00cdfffd  MOV byte ptr [ECX]
- 00ce0016  MOV byte ptr [ECX]
- 00ce002f  MOV byte ptr [ECX]
- 00ce0045  MOV byte ptr [ECX]
- 00ce01af  MOV byte ptr [ECX]
- 00ce01c8  MOV byte ptr [ECX]
- 00ce01e1  MOV byte ptr [ECX]
- 00ce01f7  MOV byte ptr [ECX]
- 00ce0210  MOV byte ptr [ECX]
- 00ce0229  MOV byte ptr [ECX]
- 00ce0242  MOV byte ptr [ECX]
- 00ce0258  MOV byte ptr [ECX]
- 00ce0271  MOV byte ptr [ECX]
- 00ce028a  MOV byte ptr [ECX]
- 00ce02a3  MOV byte ptr [ECX]
- 00ce02b9  MOV byte ptr [ECX]
- 00ce02d2  MOV byte ptr [ECX]
- 00ce02eb  MOV byte ptr [ECX]
- 00ce0304  MOV byte ptr [ECX]
- 00ce031a  MOV byte ptr [ECX]
- 00ce051d  MOV byte ptr [ECX]
- 00ce0536  MOV byte ptr [ECX]
- 00ce054f  MOV byte ptr [ECX]
- 00ce0565  MOV byte ptr [ECX]
- 00ce057e  MOV byte ptr [ECX]
- 00ce0597  MOV byte ptr [ECX]
- 00ce05b0  MOV byte ptr [ECX]
- 00ce05c6  MOV byte ptr [ECX]
- 00ce072a  MOV byte ptr [ECX]
- 00ce0744  MOV byte ptr [ECX]
- 00ce075e  MOV byte ptr [ECX]
- 00ce0778  MOV byte ptr [ECX]

### CALLEE FUN_00ce0cd0 @ 00ce0cd0

- ctorCalls: 1
- thisResolved: 1
- writesToThis: 56
- dispKnown: 29
- dispUnknown: 27
- listNext(+0x24): 0
- listPrev(+0x28): 0
- bulkInit(STOS*): 2
- bulkInitOnThis: 2

Alloc callsites:
- 00ce7958

Ctor callsites:
- 00ce7a04

Top offsets:
- 0x4 : 7
- 0x148 : 3
- 0xc : 3
- 0x17c : 3
- 0x40 : 2
- 0x144 : 2
- 0x44 : 2
- 0x8 : 2
- 0xffffffffffffffff : 1
- 0x1 : 1
- 0xfffffffffffffffc : 1
- 0x14c : 1
- 0x10 : 1

Sample writes (first 40):
- 00ce0dbe  MOV dword ptr [ECX]
- 00ce0e1c  MOV dword ptr [EAX]
- 00ce0e2d  MOV dword ptr [ECX + 0x8]
- 00ce0e36  MOV dword ptr [EAX + 0x10]
- 00ce0edd  MOV dword ptr [ECX]
- 00ce1156  MOV dword ptr [EDX]
- 00ce1170  MOV dword ptr [EAX]
- 00ce13ef  MOV dword ptr [EAX]
- 00ce140b  MOV dword ptr [ECX + 0x4]
- 00ce1587  MOV dword ptr [EAX]
- 00ce167e  MOV dword ptr [EAX]
- 00ce18a6  MOV dword ptr [ECX]
- 00ce19b2  MOV dword ptr [ECX + 0x144]
- 00ce19e0  MOV dword ptr [EAX]
- 00ce19e9  MOV dword ptr [ECX + 0x144]
- 00ce19f6  MOV dword ptr [EDX + 0x148]
- 00ce1a03  MOV dword ptr [EAX + 0x17c]
- 00ce1ae0  MOV dword ptr [EAX + EDX*0x4 + 0x14c]
- 00ce1af6  MOV dword ptr [ECX + 0x148]
- 00ce1b3b  MOV dword ptr [EAX + 0x17c]
- 00ce1b63  MOV dword ptr [ECX]
- 00ce1b96  MOV dword ptr [EDX + 0x17c]
- 00ce1baf  MOV dword ptr [EDX + 0x148]
- 00ce1bd7  MOV dword ptr [EAX]
- 00ce1d60  MOV byte ptr [EDX]
- 00ce1d78  MOV byte ptr [EAX]
- 00ce1d91  MOV byte ptr [EDX]
- 00ce1dab  MOV byte ptr [EAX]
- 00ce1dba  MOV byte ptr [EAX + 0x1]
- 00ce1dd6  MOV byte ptr [EDX]
- 00ce1dee  MOV byte ptr [EAX]
- 00ce1dff  MOV byte ptr [ECX]
- 00ce1e18  MOV byte ptr [ECX + -0x1]
- 00ce2204  MOV dword ptr [EDX + 0x4]
- 00ce2293  MOV dword ptr [ECX + 0xc]
- 00ce22d8  MOV dword ptr [EAX + ECX*0x4]
- 00ce22e7  MOV dword ptr [EDX + 0x4]
- 00ce2350  MOV dword ptr [EDX + -0x4]
- 00ce236b  MOV dword ptr [ECX]
- 00ce2383  MOV dword ptr [EDX + 0x4]

### CALLEE FUN_00ce1ac0 @ 00ce1ac0

- ctorCalls: 1
- thisResolved: 1
- writesToThis: 107
- dispKnown: 79
- dispUnknown: 28
- listNext(+0x24): 3
- listPrev(+0x28): 2
- bulkInit(STOS*): 2
- bulkInitOnThis: 2

Alloc callsites:
- 00cf0a38

Ctor callsites:
- 00cf0a4f

Top offsets:
- 0x4 : 10
- 0x5c : 7
- 0xc : 6
- 0x14 : 6
- 0x40 : 4
- 0x44 : 4
- 0x8 : 3
- 0x10 : 3
- 0x18 : 3
- 0x24 : 3
- 0xfffffffffffffffc : 2
- 0x48 : 2
- 0x4c : 2
- 0x50 : 2
- 0x54 : 2
- 0x58 : 2
- 0x28 : 2
- 0x2c : 2
- 0x30 : 2
- 0x34 : 2
- 0x38 : 2
- 0x3c : 2
- 0xffffffffffffffff : 1
- 0x1 : 1
- 0x14c : 1
- 0x1c : 1
- 0x20 : 1
- 0x17c : 1

Writes to [this+0x24]:
- 00ce4063  dword ptr [ECX + 0x24]
- 00ce4270  dword ptr [EDX + 0x24]
- 00ce432b  dword ptr [EAX + 0x24]

Writes to [this+0x28]:
- 00ce406d  dword ptr [EDX + 0x28]
- 00ce4498  dword ptr [EDX + 0x28]

Sample writes (first 40):
- 00ce1ae0  MOV dword ptr [EAX + EDX*0x4 + 0x14c]
- 00ce1b3b  MOV dword ptr [EAX + 0x17c]
- 00ce1bd7  MOV dword ptr [EAX]
- 00ce1d78  MOV byte ptr [EAX]
- 00ce1dab  MOV byte ptr [EAX]
- 00ce1dba  MOV byte ptr [EAX + 0x1]
- 00ce1dd6  MOV byte ptr [EDX]
- 00ce1dee  MOV byte ptr [EAX]
- 00ce1dff  MOV byte ptr [ECX]
- 00ce1e18  MOV byte ptr [ECX + -0x1]
- 00ce2204  MOV dword ptr [EDX + 0x4]
- 00ce2293  MOV dword ptr [ECX + 0xc]
- 00ce22d8  MOV dword ptr [EAX + ECX*0x4]
- 00ce22e7  MOV dword ptr [EDX + 0x4]
- 00ce2350  MOV dword ptr [EDX + -0x4]
- 00ce236b  MOV dword ptr [ECX]
- 00ce2383  MOV dword ptr [EDX + 0x4]
- 00ce23b8  MOV dword ptr [EAX + EDX*0x4]
- 00ce23f7  MOV dword ptr [EDX + 0x4]
- 00ce2422  MOV dword ptr [ECX + 0xc]
- 00ce2467  MOV dword ptr [EAX + 0x4]
- 00ce24c9  MOV dword ptr [EAX + EDX*0x4]
- 00ce24d5  MOV dword ptr [EAX + EDX*0x4 + 0x4]
- 00ce24e2  MOV dword ptr [EAX + EDX*0x4 + 0x8]
- 00ce24ef  MOV dword ptr [EAX + EDX*0x4 + 0xc]
- 00ce2520  MOV dword ptr [EAX + EDX*0x4]
- 00ce25ad  MOV dword ptr [ECX + 0x44]
- 00ce25c6  MOV dword ptr [EAX]
- 00ce25fc  MOV dword ptr [ECX + 0x44]
- 00ce26c3  MOV dword ptr [EDX]
- 00ce2796  MOV dword ptr [EAX + 0x40]
- 00ce285a  MOV dword ptr [ECX]
- 00ce2865  MOV dword ptr [ECX + 0x40]
- 00ce3fb0  MOV dword ptr [ECX]
- 00ce3fdf  MOV dword ptr [EDX + EAX*0x4]
- 00ce4003  MOV dword ptr [EDX + 0x4]
- 00ce4021  MOV dword ptr [EDX + 0x8]
- 00ce4027  MOV dword ptr [ECX + 0xc]
- 00ce4031  MOV dword ptr [EDX + 0x10]
- 00ce403b  MOV dword ptr [EAX + 0x14]

### CALLEE FUN_00ce42a0 @ 00ce42a0

- ctorCalls: 1
- thisResolved: 1
- writesToThis: 81
- dispKnown: 47
- dispUnknown: 34
- listNext(+0x24): 1
- listPrev(+0x28): 1
- bulkInit(STOS*): 5
- bulkInitOnThis: 0

Alloc callsites:
- 00ce7bc8

Ctor callsites:
- 00ce7c0f

Top offsets:
- 0x4 : 6
- 0xc : 5
- 0x10 : 5
- 0x14 : 5
- 0x8 : 4
- 0x5c : 4
- 0x1aadd58 : 2
- 0x18 : 2
- 0xfffffffffffffffc : 1
- 0x24 : 1
- 0x1aae16c : 1
- 0x48 : 1
- 0x28 : 1
- 0x4c : 1
- 0x2c : 1
- 0x50 : 1
- 0x30 : 1
- 0x54 : 1
- 0x34 : 1
- 0x38 : 1
- 0x58 : 1
- 0x3c : 1

Writes to [this+0x24]:
- 00ce432b  dword ptr [EAX + 0x24]

Writes to [this+0x28]:
- 00ce4498  dword ptr [EDX + 0x28]

Sample writes (first 40):
- 00ce42b0  MOV dword ptr [EAX + 0x5c]
- 00ce42e2  MOV dword ptr [ECX + 0x4c]
- 00ce42fa  MOV dword ptr [ECX]
- 00ce431c  MOV dword ptr [EAX + 0x48]
- 00ce432b  MOV dword ptr [EAX + 0x24]
- 00ce4380  MOV dword ptr [EAX + 0x5c]
- 00ce43b2  MOV dword ptr [ECX + 0x54]
- 00ce43cf  MOV dword ptr [ECX + 0x50]
- 00ce4489  MOV dword ptr [EDX + 0xc]
- 00ce4498  MOV dword ptr [EDX + 0x28]
- 00ce44b0  MOV dword ptr [ECX + 0x14]
- 00ce44d8  MOV dword ptr [EDX]
- 00ce4516  MOV dword ptr [EDX]
- 00ce4520  MOV dword ptr [ECX + 0x4]
- 00ce4529  MOV dword ptr [ECX]
- 00ce4593  MOV dword ptr [EDX + 0x5c]
- 00ce4599  MOV dword ptr [EAX + 0x14]
- 00ce45c4  MOV dword ptr [EAX + EDX*0x4]
- 00ce45d6  MOV dword ptr [ECX + 0x18]
- 00ce45df  MOV dword ptr [ECX + 0x10]
- 00ce45ee  MOV dword ptr [EDX + 0x2c]
- 00ce45f4  MOV dword ptr [EAX + 0x14]
- 00ce4601  MOV dword ptr [ECX]
- 00ce4646  MOV dword ptr [EAX + EDX*0x4 + -0x4]
- 00ce4692  MOV dword ptr [EDX + 0x5c]
- 00ce46a6  MOV dword ptr [EDX + 0x34]
- 00ce46b4  MOV dword ptr [EDX + 0x10]
- 00ce46c2  MOV dword ptr [EDX + 0x18]
- 00ce46d1  MOV dword ptr [EDX + 0x14]
- 00ce46da  MOV dword ptr [EAX]
- 00ce46ea  MOV dword ptr [ECX + 0x14]
- 00ce46f9  MOV dword ptr [ECX + 0xc]
- 00ce4708  MOV dword ptr [ECX + 0x30]
- 00ce4730  MOV dword ptr [ECX + EDX*0x4]
- 00ce474f  MOV dword ptr [ECX + 0x4]
- 00ce4789  MOV dword ptr [ECX + 0x38]
- 00ce4792  MOV dword ptr [EDX]
- 00ce47f7  MOV dword ptr [EDX + 0x58]
- 00ce481c  MOV dword ptr [EDX + 0x3c]
- 00ce51b6  MOV word ptr [EDX]

### CALLEE FUN_00ce7950 @ 00ce7950

- ctorCalls: 1
- thisResolved: 1
- writesToThis: 55
- dispKnown: 30
- dispUnknown: 25
- listNext(+0x24): 0
- listPrev(+0x28): 0
- bulkInit(STOS*): 18
- bulkInitOnThis: 0

Alloc callsites:
- 00ce7c68

Ctor callsites:
- 00ce7ca6

Top offsets:
- 0x4 : 13
- 0xc : 9
- 0x8 : 4
- 0x14 : 2
- 0x10 : 1
- 0x18 : 1

Sample writes (first 40):
- 00ce7a1e  MOV dword ptr [ECX]
- 00ce7a38  MOV dword ptr [ECX + 0x4]
- 00ce7a4f  MOV dword ptr [ECX + 0x10]
- 00ce7a74  MOV dword ptr [ECX + 0x14]
- 00ce7aac  MOV dword ptr [ECX + 0x18]
- 00ce7b07  MOV dword ptr [ECX + 0x14]
- 00ce7ceb  MOV dword ptr [EAX]
- 00ce7fce  MOV dword ptr [EDX + 0x4]
- 00ce7fe0  MOV dword ptr [EAX + 0x8]
- 00ce82f3  MOV dword ptr [EAX]
- 00ce82fc  MOV dword ptr [ECX + 0x8]
- 00ce8306  MOV dword ptr [EDX + 0x4]
- 00ce838e  MOV dword ptr [EDX]
- 00ce83cc  MOV dword ptr [EAX]
- 00ce8452  MOV dword ptr [ECX + 0x4]
- 00ce845b  MOV dword ptr [EAX]
- 00ce8463  MOV dword ptr [EDX + 0x8]
- 00ce856f  MOV dword ptr [EAX + 0xc]
- 00ce8597  MOV dword ptr [ECX + 0xc]
- 00ce85b1  MOV dword ptr [EAX + 0xc]
- 00ce85bd  MOV dword ptr [ECX + 0xc]
- 00ce866e  MOV dword ptr [EAX + 0x4]
- 00ce8706  MOV dword ptr [ECX]
- 00ce8739  MOV dword ptr [ECX]
- 00ce8754  MOV dword ptr [EDX + 0x4]
- 00ce877a  MOV dword ptr [EAX]
- 00ce88b6  MOV dword ptr [EDX]
- 00ce88fa  MOV dword ptr [EDX]
- 00ce893d  MOV dword ptr [ECX]
- 00ce895d  MOV dword ptr [ECX + 0x4]
- 00ce897e  MOV dword ptr [ECX + 0x8]
- 00ce899f  MOV dword ptr [ECX + 0xc]
- 00ce89bf  MOV dword ptr [EAX + 0x4]
- 00ce89eb  MOV dword ptr [ECX + 0x4]
- 00ce8ab3  MOV dword ptr [EAX + 0xc]
- 00ce8b4b  MOV dword ptr [EDX + 0xc]
- 00ce8b73  MOV dword ptr [EAX + 0xc]
- 00ce9027  MOV dword ptr [EDX]
- 00ce9051  MOV dword ptr [EAX]
- 00ce962d  MOV dword ptr [EDX]

### CALLEE FUN_00ceb330 @ 00ceb330

- ctorCalls: 1
- thisResolved: 1
- writesToThis: 33
- dispKnown: 28
- dispUnknown: 5
- listNext(+0x24): 1
- listPrev(+0x28): 1
- bulkInit(STOS*): 0
- bulkInitOnThis: 0

Alloc callsites:
- 00ce85f8

Ctor callsites:
- 00ce86a0

Top offsets:
- 0x4 : 4
- 0x8 : 4
- 0xc : 4
- 0x10 : 2
- 0x14 : 2
- 0x18 : 2
- 0x1c : 2
- 0x20 : 1
- 0x24 : 1
- 0x28 : 1
- 0x2c : 1
- 0x30 : 1
- 0x34 : 1
- 0x38 : 1
- 0x3c : 1

Writes to [this+0x24]:
- 00cecba4  dword ptr [EDX + 0x24]

Writes to [this+0x28]:
- 00cecdd0  dword ptr [EDX + 0x28]

Sample writes (first 40):
- 00ceb381  MOV dword ptr [EAX]
- 00ceb42e  MOV dword ptr [ECX + 0x8]
- 00ceb482  MOV dword ptr [EAX + 0xc]
- 00ceb51d  MOV dword ptr [EDX]
- 00ceb566  MOV dword ptr [EAX + 0x4]
- 00ceb5b0  MOV dword ptr [ECX + 0x8]
- 00ceb5f7  MOV dword ptr [EDX + 0xc]
- 00ceb6e3  MOV dword ptr [EDX]
- 00ceb7c8  MOV dword ptr [EDX + 0x4]
- 00ceb91a  MOV dword ptr [ECX + 0x8]
- 00cebad8  MOV dword ptr [EDX + 0xc]
- 00cebd02  MOV dword ptr [EDX + 0x10]
- 00cebf98  MOV dword ptr [ECX + 0x14]
- 00cec29a  MOV dword ptr [EDX + 0x18]
- 00cec608  MOV dword ptr [EDX + 0x1c]
- 00cec90c  MOV dword ptr [EAX + 0x20]
- 00cecba4  MOV dword ptr [EDX + 0x24]
- 00cecdd0  MOV dword ptr [EDX + 0x28]
- 00cecf90  MOV dword ptr [EAX + 0x2c]
- 00ced0e4  MOV dword ptr [EDX + 0x30]
- 00ced1cc  MOV dword ptr [EDX + 0x34]
- 00ced248  MOV dword ptr [EAX + 0x38]
- 00ced251  MOV dword ptr [EDX + 0x3c]
- 00ced2f3  MOV dword ptr [EDX]
- 00ced3d8  MOV dword ptr [EDX + 0x4]
- 00ced52a  MOV dword ptr [ECX + 0x8]
- 00ced6e8  MOV dword ptr [EDX + 0xc]
- 00ced83c  MOV dword ptr [ECX + 0x10]
- 00ced924  MOV dword ptr [ECX + 0x14]
- 00ced9a0  MOV dword ptr [EDX + 0x18]
- 00ced9a9  MOV dword ptr [ECX + 0x1c]
- 00ceda53  MOV dword ptr [EDX]
- 00cedb09  MOV dword ptr [EAX + 0x4]

## SIZE 0x2c

- allocCalls: 5
- ctorCalls: 4
- thisResolved: 4
- callees: 4

### CALLEE FUN_00cd9870 @ 00cd9870

- ctorCalls: 1
- thisResolved: 1
- writesToThis: 123
- dispKnown: 88
- dispUnknown: 35
- listNext(+0x24): 1
- listPrev(+0x28): 1
- bulkInit(STOS*): 2
- bulkInitOnThis: 2

Alloc callsites:
- 00cf0558

Ctor callsites:
- 00cf05f6

Top offsets:
- 0x4 : 23
- 0x44 : 10
- 0x84 : 7
- 0xc : 6
- 0x8 : 5
- 0x14 : 5
- 0x148 : 4
- 0x20 : 3
- 0x144 : 3
- 0x10 : 3
- 0x18 : 3
- 0x1c : 3
- 0xc4 : 2
- 0x104 : 2
- 0x58 : 2
- 0x24 : 1
- 0x28 : 1
- 0x2c : 1
- 0x30 : 1
- 0x34 : 1
- 0x38 : 1
- 0x1f : 1

Writes to [this+0x24]:
- 00cda6e7  dword ptr [ECX + 0x24]

Writes to [this+0x28]:
- 00cda6f1  dword ptr [EDX + 0x28]

Sample writes (first 40):
- 00cd999d  MOV dword ptr [EAX + 0x4]
- 00cd99f4  MOV dword ptr [EDX]
- 00cd9a0a  MOV dword ptr [ECX]
- 00cd9a12  MOV dword ptr [EAX + 0x8]
- 00cd9a55  MOV dword ptr [EAX]
- 00cd9a5e  MOV dword ptr [ECX + 0x4]
- 00cd9a68  MOV dword ptr [EDX + 0x8]
- 00cd9a72  MOV dword ptr [EAX + 0xc]
- 00cd9a7c  MOV dword ptr [ECX + 0x10]
- 00cd9a86  MOV dword ptr [EDX + 0x14]
- 00cd9a90  MOV dword ptr [EAX + 0x18]
- 00cd9a9a  MOV dword ptr [ECX + 0x1c]
- 00cd9ad2  MOV dword ptr [ECX]
- 00cd9bee  MOV dword ptr [ECX]
- 00cd9bf6  MOV dword ptr [EAX + 0x4]
- 00cd9bff  MOV dword ptr [EDX + 0x8]
- 00cd9c08  MOV dword ptr [ECX + 0xc]
- 00cd9c36  MOV dword ptr [EDX + 0x8]
- 00cd9c42  MOV dword ptr [EDX + 0x4]
- 00cd9c4d  MOV dword ptr [EDX]
- 00cd9c58  MOV dword ptr [EDX + 0x4]
- 00cd9c71  MOV dword ptr [EDX]
- 00cd9c80  MOV dword ptr [EAX + 0xc]
- 00cd9cbd  MOV dword ptr [EAX + 0x4]
- 00cd9cc7  MOV dword ptr [ECX + 0xc]
- 00cd9db6  MOV dword ptr [EAX + 0xc]
- 00cd9dc0  MOV dword ptr [ECX + 0x4]
- 00cd9dcf  MOV dword ptr [EAX]
- 00cd9dde  MOV dword ptr [ECX + 0x4]
- 00cd9e1c  MOV dword ptr [ECX + EDX*0x4]
- 00cd9e36  MOV dword ptr [EDX + 0x4]
- 00cd9e8e  MOV dword ptr [ECX + 0x4]
- 00cd9f1a  MOV dword ptr [EDX + 0x4]
- 00cd9f6c  MOV dword ptr [EDX + EAX*0x4]
- 00cd9fa8  MOV dword ptr [ECX + 0x4]
- 00cda05c  MOV byte ptr [EAX]
- 00cda2a6  MOV dword ptr [ECX + EDX*0x4]
- 00cda2b8  MOV dword ptr [ECX + 0x4]
- 00cda2da  MOV dword ptr [EDX + ECX*0x4]
- 00cda34e  MOV dword ptr [ECX + EAX*0x4]

### CALLEE FUN_00cdb140 @ 00cdb140

- ctorCalls: 1
- thisResolved: 1
- writesToThis: 107
- dispKnown: 42
- dispUnknown: 65
- listNext(+0x24): 0
- listPrev(+0x28): 0
- bulkInit(STOS*): 0
- bulkInitOnThis: 0

Alloc callsites:
- 00ce36a8

Ctor callsites:
- 00ce36d9

Top offsets:
- 0x58 : 9
- 0x84 : 5
- 0x14 : 5
- 0x44 : 4
- 0x4 : 3
- 0x10 : 3
- 0xc4 : 2
- 0x148 : 2
- 0x8 : 2
- 0xc : 2
- 0x38 : 2
- 0x3c : 2
- 0x144 : 1

Sample writes (first 40):
- 00cdb1dd  MOV dword ptr [ECX + EDX*0x4 + 0x4]
- 00cdb1f0  MOV dword ptr [ECX + EAX*0x4 + 0xc4]
- 00cdb328  MOV dword ptr [ECX + EAX*0x4 + 0xc4]
- 00cdb34c  MOV dword ptr [ECX + 0x148]
- 00cdb4f6  MOV dword ptr [ECX]
- 00cdb50e  MOV dword ptr [EAX]
- 00cdb564  MOV dword ptr [ECX + EAX*0x4 + 0x84]
- 00cdb581  MOV dword ptr [ECX]
- 00cdb5a5  MOV dword ptr [EAX]
- 00cdb5bd  MOV dword ptr [EDX]
- 00cdb7c4  MOV byte ptr [EDX]
- 00cdbc07  MOV dword ptr [ECX + EAX*0x4 + 0x44]
- 00cdbc15  MOV dword ptr [EAX + EDX*0x4 + 0x84]
- 00cdbd12  MOV dword ptr [EAX]
- 00cdbd1a  MOV dword ptr [EDX + 0x144]
- 00cdbd2a  MOV dword ptr [EAX + 0x148]
- 00cdbd64  MOV dword ptr [EAX + EDX*0x4 + 0x44]
- 00cdbd78  MOV dword ptr [EDX + ECX*0x4 + 0x84]
- 00cdbef8  MOV dword ptr [EDX + ECX*0x4 + 0x44]
- 00cdbf06  MOV dword ptr [ECX + EAX*0x4 + 0x84]
- 00cdbf1a  MOV dword ptr [EAX + EDX*0x4 + 0x44]
- 00cdbf27  MOV dword ptr [EAX + EDX*0x4 + 0x84]
- 00cdbf81  MOV byte ptr [ECX]
- 00cdc264  MOV dword ptr [EAX + 0x14]
- 00cdc278  MOV dword ptr [ECX + 0x14]
- 00cdc281  MOV dword ptr [EDX + 0x10]
- 00cdc353  MOV dword ptr [EAX + EDX*0x4]
- 00cdc3dd  MOV dword ptr [EDX + ECX*0x4]
- 00cdc40d  MOV dword ptr [EAX + 0x58]
- 00cdc425  MOV dword ptr [EAX + 0x58]
- 00cdc4d1  MOV dword ptr [EDX + ECX*0x4]
- 00cdc580  MOV dword ptr [EDX + ECX*0x4]
- 00cdc60c  MOV dword ptr [EDX + ECX*0x4]
- 00cdc696  MOV dword ptr [EAX + EDX*0x4]
- 00cdc736  MOV dword ptr [EAX + 0x58]
- 00cdc7cf  MOV dword ptr [EAX]
- 00cdc84f  MOV dword ptr [EAX]
- 00cdc999  MOV dword ptr [EAX + EDX*0x4]
- 00cdc9b7  MOV dword ptr [ECX + EAX*0x4]
- 00cdc9ee  MOV dword ptr [EAX + EDX*0x4]

### CALLEE FUN_00cdf040 @ 00cdf040

- ctorCalls: 1
- thisResolved: 1
- writesToThis: 97
- dispKnown: 18
- dispUnknown: 79
- listNext(+0x24): 0
- listPrev(+0x28): 0
- bulkInit(STOS*): 2
- bulkInitOnThis: 2

Alloc callsites:
- 00cdfd88

Ctor callsites:
- 00cdff7a

Top offsets:
- 0x4 : 4
- 0x148 : 3
- 0x17c : 3
- 0x144 : 2
- 0x10 : 1
- 0xffffffffffffffff : 1
- 0x1 : 1
- 0x8 : 1
- 0xc : 1
- 0x14c : 1

Sample writes (first 40):
- 00cdf6c6  MOV dword ptr [EDX + 0x4]
- 00cdf6cf  MOV dword ptr [ECX]
- 00cdfd66  MOV dword ptr [EDX + 0x4]
- 00cdfd6f  MOV dword ptr [ECX]
- 00cdff9c  MOV byte ptr [ECX]
- 00cdffb5  MOV byte ptr [ECX]
- 00cdffce  MOV byte ptr [ECX]
- 00cdffe4  MOV byte ptr [ECX]
- 00cdfffd  MOV byte ptr [ECX]
- 00ce0016  MOV byte ptr [ECX]
- 00ce002f  MOV byte ptr [ECX]
- 00ce0045  MOV byte ptr [ECX]
- 00ce01af  MOV byte ptr [ECX]
- 00ce01c8  MOV byte ptr [ECX]
- 00ce01e1  MOV byte ptr [ECX]
- 00ce01f7  MOV byte ptr [ECX]
- 00ce0210  MOV byte ptr [ECX]
- 00ce0229  MOV byte ptr [ECX]
- 00ce0242  MOV byte ptr [ECX]
- 00ce0258  MOV byte ptr [ECX]
- 00ce0271  MOV byte ptr [ECX]
- 00ce028a  MOV byte ptr [ECX]
- 00ce02a3  MOV byte ptr [ECX]
- 00ce02b9  MOV byte ptr [ECX]
- 00ce02d2  MOV byte ptr [ECX]
- 00ce02eb  MOV byte ptr [ECX]
- 00ce0304  MOV byte ptr [ECX]
- 00ce031a  MOV byte ptr [ECX]
- 00ce051d  MOV byte ptr [ECX]
- 00ce0536  MOV byte ptr [ECX]
- 00ce054f  MOV byte ptr [ECX]
- 00ce0565  MOV byte ptr [ECX]
- 00ce057e  MOV byte ptr [ECX]
- 00ce0597  MOV byte ptr [ECX]
- 00ce05b0  MOV byte ptr [ECX]
- 00ce05c6  MOV byte ptr [ECX]
- 00ce072a  MOV byte ptr [ECX]
- 00ce0744  MOV byte ptr [ECX]
- 00ce075e  MOV byte ptr [ECX]
- 00ce0778  MOV byte ptr [ECX]

### CALLEE FUN_00cea2e0 @ 00cea2e0

- ctorCalls: 1
- thisResolved: 1
- writesToThis: 60
- dispKnown: 45
- dispUnknown: 15
- listNext(+0x24): 0
- listPrev(+0x28): 0
- bulkInit(STOS*): 2
- bulkInitOnThis: 0

Alloc callsites:
- 00ce9098

Ctor callsites:
- 00ce90ca

Top offsets:
- 0x4 : 13
- 0x8 : 10
- 0xc : 9
- 0x10 : 4
- 0x14 : 3
- 0x18 : 2
- 0x1c : 2
- 0x20 : 1
- 0xfffffffffffffffc : 1

Sample writes (first 40):
- 00cea342  MOV dword ptr [ECX]
- 00cea379  MOV dword ptr [EDX + 0x4]
- 00cea3b1  MOV dword ptr [ECX + 0x8]
- 00cea3e6  MOV dword ptr [EDX + 0xc]
- 00cea41b  MOV dword ptr [ECX + 0x10]
- 00cea576  MOV dword ptr [EDX + 0x4]
- 00cea627  MOV dword ptr [EAX + 0xc]
- 00cea7e2  MOV dword ptr [ECX + 0x4]
- 00cea806  MOV dword ptr [EDX + 0x4]
- 00cea867  MOV dword ptr [ECX + EAX*0x4 + -0x4]
- 00cea872  MOV dword ptr [EDX]
- 00cea8c0  MOV dword ptr [EDX + ECX*0x4]
- 00cea919  MOV dword ptr [EDX + ECX*0x4]
- 00ceab94  MOV dword ptr [EDX]
- 00ceabbe  MOV dword ptr [EAX]
- 00ceac35  MOV dword ptr [EAX]
- 00ceac81  MOV dword ptr [EAX + 0x4]
- 00ceacce  MOV dword ptr [EAX + 0x8]
- 00cead1b  MOV dword ptr [EAX + 0xc]
- 00cead90  MOV dword ptr [EAX]
- 00ceadf3  MOV dword ptr [EAX + 0x4]
- 00ceae54  MOV dword ptr [EAX + 0x8]
- 00ceaeda  MOV dword ptr [EAX]
- 00ceaf1a  MOV dword ptr [EAX + 0x4]
- 00ceaf5b  MOV dword ptr [EAX + 0x8]
- 00ceaf9c  MOV dword ptr [EAX + 0xc]
- 00ceb006  MOV dword ptr [EAX]
- 00ceb05d  MOV dword ptr [EAX + 0x4]
- 00ceb0b2  MOV dword ptr [EAX + 0x8]
- 00ceb119  MOV dword ptr [EAX]
- 00ceb12e  MOV dword ptr [ECX + 0x4]
- 00ceb156  MOV dword ptr [ECX + 0x8]
- 00ceb16c  MOV dword ptr [EDX + 0xc]
- 00ceb194  MOV dword ptr [EDX + 0x10]
- 00ceb1aa  MOV dword ptr [ECX + 0x14]
- 00ceb1d2  MOV dword ptr [ECX + 0x18]
- 00ceb1e8  MOV dword ptr [EDX + 0x1c]
- 00ceb238  MOV dword ptr [EDX]
- 00ceb24d  MOV dword ptr [ECX + 0x4]
- 00ceb289  MOV dword ptr [EDX + 0x8]

## SIZE 0x30

- allocCalls: 4
- ctorCalls: 1
- thisResolved: 1
- callees: 1

### CALLEE FUN_00cda500 @ 00cda500

- ctorCalls: 1
- thisResolved: 1
- writesToThis: 97
- dispKnown: 56
- dispUnknown: 41
- listNext(+0x24): 1
- listPrev(+0x28): 0
- bulkInit(STOS*): 0
- bulkInitOnThis: 0

Alloc callsites:
- 00ce97f8

Ctor callsites:
- 00ce9844

Top offsets:
- 0x4 : 7
- 0x44 : 7
- 0x84 : 7
- 0x58 : 5
- 0x148 : 4
- 0x144 : 3
- 0x10 : 3
- 0x14 : 3
- 0x20 : 2
- 0xc4 : 2
- 0x104 : 2
- 0x38 : 2
- 0x1c : 2
- 0x24 : 1
- 0x8 : 1
- 0xc : 1
- 0x30 : 1
- 0x18 : 1
- 0x3c : 1
- 0x1f : 1

Writes to [this+0x24]:
- 00cda6e7  dword ptr [ECX + 0x24]

Sample writes (first 40):
- 00cda6ab  MOV dword ptr [ECX + 0x4]
- 00cda6c9  MOV dword ptr [ECX + 0x10]
- 00cda6e7  MOV dword ptr [ECX + 0x24]
- 00cda705  MOV dword ptr [ECX + 0x30]
- 00cda723  MOV dword ptr [ECX + 0x38]
- 00cda736  MOV dword ptr [ECX + 0x1c]
- 00cdaabc  MOV dword ptr [ECX + 0x20]
- 00cdabb3  MOV dword ptr [ECX + 0x18]
- 00cdacce  MOV dword ptr [ECX + 0x20]
- 00cdae1f  MOV dword ptr [EDX + 0x1c]
- 00cdaf62  MOV dword ptr [EAX]
- 00cdafaa  MOV byte ptr [ECX + 0x1f]
- 00cdafb4  MOV dword ptr [EDX + 0x4]
- 00cdafc3  MOV dword ptr [EDX + 0x4]
- 00cdb09c  MOV dword ptr [ECX]
- 00cdb171  MOV dword ptr [EDX + 0x144]
- 00cdb1a7  MOV dword ptr [EDX + 0x148]
- 00cdb1dd  MOV dword ptr [ECX + EDX*0x4 + 0x4]
- 00cdb1f0  MOV dword ptr [ECX + EAX*0x4 + 0xc4]
- 00cdb206  MOV dword ptr [EDX + ECX*0x4 + 0x104]
- 00cdb25f  MOV dword ptr [EDX + ECX*0x4 + 0x44]
- 00cdb273  MOV dword ptr [EDX + ECX*0x4 + 0x84]
- 00cdb2c7  MOV dword ptr [EDX + ECX*0x4 + 0x4]
- 00cdb309  MOV dword ptr [EAX + EDX*0x4 + 0x44]
- 00cdb317  MOV dword ptr [EDX + ECX*0x4 + 0x84]
- 00cdb328  MOV dword ptr [ECX + EAX*0x4 + 0xc4]
- 00cdb339  MOV dword ptr [EAX + EDX*0x4 + 0x104]
- 00cdb34c  MOV dword ptr [ECX + 0x148]
- 00cdb359  MOV dword ptr [EDX + 0x144]
- 00cdb49c  MOV dword ptr [EDX + 0x148]
- 00cdb4a8  MOV dword ptr [EDX + ECX*0x4 + 0x4]
- 00cdb4cf  MOV dword ptr [EDX]
- 00cdb4de  MOV dword ptr [EAX]
- 00cdb4f6  MOV dword ptr [ECX]
- 00cdb50e  MOV dword ptr [EAX]
- 00cdb556  MOV dword ptr [EDX + ECX*0x4 + 0x44]
- 00cdb564  MOV dword ptr [ECX + EAX*0x4 + 0x84]
- 00cdb581  MOV dword ptr [ECX]
- 00cdb590  MOV dword ptr [EDX]
- 00cdb5a5  MOV dword ptr [EAX]

