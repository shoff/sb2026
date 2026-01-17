B6 Unblock Report
Target: 0x0040B979
Function before: thunk_FUN_005b6790 @ 0040b979
Function after: thunk_FUN_005b6790 @ 0040b979
Thunk resolved to: 005b6790

Direct code refs to target:
  (none)

Direct data refs to target:
  015498cc

Known data xref: 015498cc
Table base: 015498a0
Table entries: 39
Table targets (first 64):
  0: 0041a195
  1: 0041020d
  2: 00426f49
  3: 00423a47
  4: 0041df8e
  5: 0041f7da
  6: 00421ef4
  7: 0040dc97
  8: 00415406
  9: 00428349
  10: 00408f99
  11: 0040b979
  12: 00405f4c
  13: 00410154
  14: 00405a8d
  15: 00425e00
  16: 00402f22
  17: 00415feb
  18: 00404a16
  19: 0041b1b7
  20: 004103cf
  21: 0042659e
  22: 0040d57b
  23: 0041f36b
  24: 004066db
  25: 00420b85
  26: 0040fbaf
  27: 004114e1
  28: 0040817f
  29: 0040b17c
  30: 0040c6cb
  31: 0040844f
  32: 00420cd9
  33: 00422449
  34: 00423547
  35: 0040dd0f
  36: 00424442
  37: 00422e62
  38: 00407bb2

Found callers (direct/indirect) near table refs:
  callsite=005b5bd3 kind=INDIRECT_CALL caller=FUN_005b5b00 @ 005b5b00 details=near ref 005b5b5f tableBase 015498a0
  callsite=005b5c14 kind=INDIRECT_CALL caller=FUN_005b5b00 @ 005b5b00 details=near ref 005b5b5f tableBase 015498a0
  callsite=005b5d9b kind=INDIRECT_CALL caller=FUN_005b5d20 @ 005b5d20 details=near ref 005b5d69 tableBase 015498a0
  callsite=005b5f41 kind=INDIRECT_CALL caller=FUN_005b5e30 @ 005b5e30 details=near ref 005b5e81 tableBase 015498a0
  callsite=005b5f41 kind=INDIRECT_CALL caller=FUN_005b5ef0 @ 005b5ef0 details=near ref 005b5f10 tableBase 015498a0
  callsite=005b5ffb kind=INDIRECT_CALL caller=FUN_005b5ef0 @ 005b5ef0 details=near ref 005b5f10 tableBase 015498a0
  callsite=005b70e0 kind=INDIRECT_CALL caller=FUN_005b6fe0 @ 005b6fe0 details=near ref 005b7031 tableBase 015498a0

Actions:
  Thunk-like first ins at 0040b979 is JMP -> 005b6790
  Expanded pointer-table base from 015498cc back to 015498a0
  Scanned pointer table at 015498a0 entries=39

Warnings:
  (none)
