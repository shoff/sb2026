Merge-Roles Scan (vtable 0x015498A0 vs offsets +0x10/+0x11/+0x14)

Targets:
  VTABLE_BASE = 0x015498A0
  VCALL_SLOT = +0x28
  FUN_005b6760 = 0x005B6760
  FUN_005b6790 = 0x005B6790
  OFFSETS = +0x10, +0x11, +0x14

thunk_FUN_005b6760 @ 00408f99  (00408f99..00408f9d)
  DIRECT_CALLS:
    00408f99  target=005b6760  ins=JMP 0x005b6760

thunk_FUN_005b6790 @ 0040b979  (0040b979..0040b97d)
  DIRECT_CALLS:
    0040b979  target=005b6790  ins=JMP 0x005b6790

FUN_004595b0 @ 004595b0  (004595b0..0045979e)
  VCALLS_SLOT+0x28:
    00459694  vtableReg=EDX  objBaseReg=(unknown)  ins=CALL dword ptr [EDX + 0x28]

FUN_0045c3a0 @ 0045c3a0  (0045c3a0..0045cc88)
  VCALLS_SLOT+0x28:
    0045c3d6  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0045c3d1  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0045c424  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0045c41b  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0045c436  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0045c42d  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0045c50c  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0045c500  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0045c724  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0045c718  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0045c763  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0045c757  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0045c782  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0045c776  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0045c8b9  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0045c8aa  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0045c8c4  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0045c8bc  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0045c951  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0045c942  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0045c95c  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0045c954  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0045c9e8  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0045c9d9  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0045ca1c  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0045ca0d  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0045ca50  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0045ca48  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0045ca88  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0045ca7d  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0045cab3  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0045caaa  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0045cad6  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0045cacd  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0045cbbe  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0045cbb5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0045ee80 @ 0045ee80  (0045ee80..0045ef3a)
  VCALLS_SLOT+0x28:
    0045eedf  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0045eed3  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0045ef08  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0045eefc  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00493250 @ 00493250  (00493250..0049328a)
  VCALLS_SLOT+0x28:
    0049326b  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00493268  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_004a8510 @ 004a8510  (004a8510..004a8579)
  VCALLS_SLOT+0x28:
    004a8547  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 004a853c  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    004a8555  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 004a854a  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    004a8571  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 004a8566  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_004d4890 @ 004d4890  (004d4890..004d4a4d)
  VCALLS_SLOT+0x28:
    004d48be  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 004d48b3  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    004d48d8  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 004d48cc  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    004d4900  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 004d48f4  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    004d49b3  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 004d49a7  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    004d4a29  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 004d4a1d  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0050ebe0 @ 0050ebe0  (0050ebe0..0050ec2d)
  VCALLS_SLOT+0x28:
    0050ebfb  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0050ebf0  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0050ec09  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0050ebfe  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0050ec17  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0050ec0c  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00512880 @ 00512880  (00512880..00512912)
  VCALLS_SLOT+0x28:
    005128a0  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0051289e  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    005128ac  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 005128a7  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00512c10 @ 00512c10  (00512c10..00512c4a)
  VCALLS_SLOT+0x28:
    00512c3b  vtableReg=EAX  objBaseReg=EDI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00512c2e  MOV EAX,dword ptr [EDI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EDI -> []

FUN_00518510 @ 00518510  (00518510..005185e2)
  VCALLS_SLOT+0x28:
    0051855f  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00518558  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00518740 @ 00518740  (00518740..005187bc)
  VCALLS_SLOT+0x28:
    00518792  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00518784  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00519d50 @ 00519d50  (00519d50..00519d66)
  VCALLS_SLOT+0x28:
    00519d60  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00519d5d  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_0051a380 @ 0051a380  (0051a380..0051a3ca)
  VCALLS_SLOT+0x28:
    0051a393  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0051a38e  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0051b410 @ 0051b410  (0051b410..0051b4ea)
  VCALLS_SLOT+0x28:
    0051b463  vtableReg=EDX  objBaseReg=EBX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0051b459  MOV EDX,dword ptr [EBX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EBX -> []

FUN_0051c590 @ 0051c590  (0051c590..0051c5a6)
  VCALLS_SLOT+0x28:
    0051c5a0  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0051c59d  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_0051c810 @ 0051c810  (0051c810..0051c826)
  VCALLS_SLOT+0x28:
    0051c820  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0051c81d  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00531c80 @ 00531c80  (00531c80..00531d3d)
  VCALLS_SLOT+0x28:
    00531cbc  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00531cb8  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    00531cca  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00531cc6  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    00531cd8  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00531cd4  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    00531ce6  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00531ce2  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    00531cf4  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00531cf0  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    00531d02  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00531cfe  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    00531d10  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00531d0c  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    00531d1e  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00531d1a  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00533730 @ 00533730  (00533730..00533a46)
  VCALLS_SLOT+0x28:
    005339bb  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 005339b7  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    005339cc  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 005339c8  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    005339dd  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 005339d9  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    005339ee  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 005339ea  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    005339ff  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 005339fb  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    00533a10  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00533a0c  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    00533a21  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00533a1d  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    00533a32  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00533a2e  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_005355b0 @ 005355b0  (005355b0..00535606)
  VCALLS_SLOT+0x28:
    005355e7  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 005355e3  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_005362a0 @ 005362a0  (005362a0..00536331)
  VCALLS_SLOT+0x28:
    005362db  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 005362d7  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    005362e9  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 005362e5  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    005362f7  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 005362f3  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    00536305  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00536301  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00536f10 @ 00536f10  (00536f10..00537179)
  VCALLS_SLOT+0x28:
    00537130  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0053712c  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    00537141  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0053713d  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    00537152  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0053714e  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    00537163  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0053715f  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_0053da20 @ 0053da20  (0053da20..0053da36)
  VCALLS_SLOT+0x28:
    0053da30  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0053da2d  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_0053eb00 @ 0053eb00  (0053eb00..0053eb15)
  VCALLS_SLOT+0x28:
    0053eb0f  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0053eb0d  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_0053ed60 @ 0053ed60  (0053ed60..0053ede7)
  VCALLS_SLOT+0x28:
    0053ed72  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0053ed6a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0053ed87  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0053ed7f  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0053ed92  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0053ed8a  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0053ed9d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0053ed95  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0053f750 @ 0053f750  (0053f750..0053f766)
  VCALLS_SLOT+0x28:
    0053f760  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0053f75d  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00540ed0 @ 00540ed0  (00540ed0..00541027)
  VCALLS_SLOT+0x28:
    00540ff4  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00540feb  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_005424f0 @ 005424f0  (005424f0..005425ec)
  VCALLS_SLOT+0x28:
    0054251c  vtableReg=EAX  objBaseReg=EBX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00542518  MOV EAX,dword ptr [EBX]
      seenFieldOffsetsOnBase: [16]
    00542542  vtableReg=ESI  objBaseReg=ECX  ins=CALL dword ptr [ESI + 0x28]
      loadEvidence: 0054253e  MOV ESI,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EBX -> [16]
    ECX -> []

FUN_005436d0 @ 005436d0  (005436d0..005436e6)
  VCALLS_SLOT+0x28:
    005436e0  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 005436dd  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00543910 @ 00543910  (00543910..00543926)
  VCALLS_SLOT+0x28:
    00543920  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0054391d  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00543f80 @ 00543f80  (00543f80..00544012)
  VCALLS_SLOT+0x28:
    00543fa6  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00543fa4  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    00543fd0  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00543fc3  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: [16, 20]
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> [16, 20]
    ECX -> []

FUN_00544080 @ 00544080  (00544080..005440b0)
  VCALLS_SLOT+0x28:
    00544095  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00544093  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00544270 @ 00544270  (00544270..00544286)
  VCALLS_SLOT+0x28:
    00544280  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0054427d  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00544680 @ 00544680  (00544680..005446f8)
  VCALLS_SLOT+0x28:
    005446b5  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 005446b3  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00549eb0 @ 00549eb0  (00549eb0..0054a138)
  VCALLS_SLOT+0x28:
    0054a054  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0054a052  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_0054a240 @ 0054a240  (0054a240..0054a2f0)
  VCALLS_SLOT+0x28:
    0054a285  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0054a283  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_0054ddb0 @ 0054ddb0  (0054ddb0..0054ddc6)
  VCALLS_SLOT+0x28:
    0054ddc0  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0054ddbd  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_0054ea00 @ 0054ea00  (0054ea00..0054ea6f)
  VCALLS_SLOT+0x28:
    0054ea48  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0054ea3c  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0054efa0 @ 0054efa0  (0054efa0..0054efef)
  VCALLS_SLOT+0x28:
    0054efc2  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0054efb6  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0054f510 @ 0054f510  (0054f510..0054f580)
  VCALLS_SLOT+0x28:
    0054f554  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0054f548  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0055a880 @ 0055a880  (0055a880..0055a8ad)
  VCALLS_SLOT+0x28:
    0055a896  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0055a886  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_005614a0 @ 005614a0  (005614a0..005614d7)
  VCALLS_SLOT+0x28:
    005614c0  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 005614b0  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: [20]
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> [20]

FUN_00561670 @ 00561670  (00561670..005616a7)
  VCALLS_SLOT+0x28:
    00561690  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00561680  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: [20]
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> [20]

FUN_0056e410 @ 0056e410  (0056e410..00570c01)
  VCALLS_SLOT+0x28:
    0056f4c4  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0056f4c2  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00599fe0 @ 00599fe0  (00599fe0..0059a0bd)
  VCALLS_SLOT+0x28:
    0059a033  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0059a030  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_0059a7d0 @ 0059a7d0  (0059a7d0..0059a9bb)
  VCALLS_SLOT+0x28:
    0059a94d  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0059a94b  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_005b5b00 @ 005b5b00  (005b5b00..005b5c28)
  VTABLE_WRITES:
    005b5b5f  baseReg=ESI  ins=MOV dword ptr [ESI],0x15498a0
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> [16, 17, 20]
  MERGE_SIGNALS:
    STRONG_MERGE_SIGNAL: vtableWriteBaseReg=ESI has offsets {0x10,0x11,0x14}

FUN_005b5d20 @ 005b5d20  (005b5d20..005b5db5)
  VTABLE_WRITES:
    005b5d69  baseReg=ESI  ins=MOV dword ptr [ESI],0x15498a0
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> [16, 17, 20]
  MERGE_SIGNALS:
    STRONG_MERGE_SIGNAL: vtableWriteBaseReg=ESI has offsets {0x10,0x11,0x14}

FUN_005b5e30 @ 005b5e30  (005b5e30..005b5eb4)
  VTABLE_WRITES:
    005b5e81  baseReg=ESI  ins=MOV dword ptr [ESI],0x15498a0
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> [16, 17, 20]
  MERGE_SIGNALS:
    STRONG_MERGE_SIGNAL: vtableWriteBaseReg=ESI has offsets {0x10,0x11,0x14}

FUN_005b5ef0 @ 005b5ef0  (005b5ef0..005b5f7c)
  VTABLE_WRITES:
    005b5f10  baseReg=ESI  ins=MOV dword ptr [ESI],0x15498a0
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> [20]

FUN_005b6fe0 @ 005b6fe0  (005b6fe0..005b7150)
  VTABLE_WRITES:
    005b7031  baseReg=EDI  ins=MOV dword ptr [EDI],0x15498a0
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EDI -> [16, 17, 20]
  MERGE_SIGNALS:
    STRONG_MERGE_SIGNAL: vtableWriteBaseReg=EDI has offsets {0x10,0x11,0x14}

FUN_005b7ff0 @ 005b7ff0  (005b7ff0..005b8078)
  VCALLS_SLOT+0x28:
    005b8052  vtableReg=EDX  objBaseReg=EAX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 005b8049  MOV EDX,dword ptr [EAX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EAX -> []

FUN_005dfeb0 @ 005dfeb0  (005dfeb0..005dfeec)
  VCALLS_SLOT+0x28:
    005dfed3  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 005dfed1  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_005f87a0 @ 005f87a0  (005f87a0..005f8dae)
  VCALLS_SLOT+0x28:
    005f89ce  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 005f89ca  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_0062ff60 @ 0062ff60  (0062ff60..0063003d)
  VCALLS_SLOT+0x28:
    0062ff6f  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0062ff6a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00635520 @ 00635520  (00635520..006359bf)
  VCALLS_SLOT+0x28:
    00635565  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00635563  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00635651  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00635648  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00635674  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0063566b  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00635714  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0063570b  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00635779  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00635770  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0063579f  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00635796  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0064ba00 @ 0064ba00  (0064ba00..0064ba1d)
  VCALLS_SLOT+0x28:
    0064ba17  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0064ba10  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00672d20 @ 00672d20  (00672d20..00672fbc)
  VCALLS_SLOT+0x28:
    00672d33  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00672d2b  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00672d3e  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00672d36  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00672d6a  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00672d62  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00672ded  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00672de5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00672ea8  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00672ea0  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00672eb6  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00672eab  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00672ec4  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00672eb9  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00672ef2  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00672ee7  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00686290 @ 00686290  (00686290..00686307)
  VCALLS_SLOT+0x28:
    006862a3  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0068629b  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    006862ae  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 006862a6  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_006965e0 @ 006965e0  (006965e0..00696804)
  VCALLS_SLOT+0x28:
    0069676e  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0069676c  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00697590 @ 00697590  (00697590..006977f5)
  VCALLS_SLOT+0x28:
    0069775f  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0069775d  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_006c89b0 @ 006c89b0  (006c89b0..006c89e8)
  VCALLS_SLOT+0x28:
    006c89bf  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 006c89ba  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_006c94b0 @ 006c94b0  (006c94b0..006c9544)
  VCALLS_SLOT+0x28:
    006c94db  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 006c94d3  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_006dc710 @ 006dc710  (006dc710..006dc918)
  VCALLS_SLOT+0x28:
    006dc7cf  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 006dc7c5  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_006dc9e0 @ 006dc9e0  (006dc9e0..006dcc78)
  VCALLS_SLOT+0x28:
    006dcad4  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 006dcaca  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_006e1ab0 @ 006e1ab0  (006e1ab0..006e1aeb)
  VCALLS_SLOT+0x28:
    006e1acd  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 006e1ac5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_006e2e60 @ 006e2e60  (006e2e60..006e2f47)
  VCALLS_SLOT+0x28:
    006e2ed4  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 006e2ecc  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_006ef510 @ 006ef510  (006ef510..006ef649)
  VCALLS_SLOT+0x28:
    006ef559  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 006ef551  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    006ef564  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 006ef55c  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    006ef56f  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 006ef567  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_006f7190 @ 006f7190  (006f7190..006f7287)
  VCALLS_SLOT+0x28:
    006f71ba  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 006f71b2  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    006f71f2  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 006f71ea  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_006fa650 @ 006fa650  (006fa650..006fa680)
  VCALLS_SLOT+0x28:
    006fa662  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 006fa65a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_006fae20 @ 006fae20  (006fae20..006fae50)
  VCALLS_SLOT+0x28:
    006fae3d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 006fae35  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    006fae48  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 006fae40  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_006faef0 @ 006faef0  (006faef0..006faf2b)
  VCALLS_SLOT+0x28:
    006faf02  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 006faefa  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_006fafb0 @ 006fafb0  (006fafb0..006fb001)
  VCALLS_SLOT+0x28:
    006fafc2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 006fafba  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_006fb920 @ 006fb920  (006fb920..006fb934)
  VCALLS_SLOT+0x28:
    006fb92e  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 006fb92c  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_006fbfc0 @ 006fbfc0  (006fbfc0..006fc0aa)
  VCALLS_SLOT+0x28:
    006fbfed  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 006fbfe8  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    006fc01c  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 006fc017  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    006fc04b  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 006fc046  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    006fc086  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 006fc081  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00700780 @ 00700780  (00700780..007007ef)
  VCALLS_SLOT+0x28:
    007007e7  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007007dc  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00701100 @ 00701100  (00701100..00701130)
  VCALLS_SLOT+0x28:
    00701112  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0070110a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00701fd0 @ 00701fd0  (00701fd0..0070201d)
  VCALLS_SLOT+0x28:
    00701fe2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00701fda  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007028a0 @ 007028a0  (007028a0..007028da)
  VCALLS_SLOT+0x28:
    007028b5  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007028aa  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00703250 @ 00703250  (00703250..007032f6)
  VCALLS_SLOT+0x28:
    00703270  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00703265  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00705160 @ 00705160  (00705160..00705369)
  VCALLS_SLOT+0x28:
    007051f1  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007051e6  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00705204  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007051f9  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00705212  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00705207  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00705220  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00705215  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0070522e  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00705223  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0070524c  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00705241  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0070525a  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0070524f  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00705268  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0070525d  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00705276  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0070526b  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00705284  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00705279  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007052b0  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007052a5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007052be  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007052b3  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007052f8  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007052ed  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00705306  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007052fb  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007060f0 @ 007060f0  (007060f0..007061d9)
  VCALLS_SLOT+0x28:
    0070616f  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00706164  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007061a7  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0070619c  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007061d1  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007061c6  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007075d0 @ 007075d0  (007075d0..00707615)
  VCALLS_SLOT+0x28:
    007075f0  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007075e8  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00708020 @ 00708020  (00708020..00708087)
  VCALLS_SLOT+0x28:
    00708032  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0070802a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00709430 @ 00709430  (00709430..007094e9)
  VCALLS_SLOT+0x28:
    00709442  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0070943a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0070944d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00709445  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007094c5  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007094ba  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0070af00 @ 0070af00  (0070af00..0070afb6)
  VCALLS_SLOT+0x28:
    0070af1d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0070af15  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0070af28  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0070af20  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0070afa0  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0070af95  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0070b7f0 @ 0070b7f0  (0070b7f0..0070b84d)
  VCALLS_SLOT+0x28:
    0070b802  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0070b7fa  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0070c620 @ 0070c620  (0070c620..0070c650)
  VCALLS_SLOT+0x28:
    0070c632  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0070c62a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0070cfd0 @ 0070cfd0  (0070cfd0..0070d000)
  VCALLS_SLOT+0x28:
    0070cfe2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0070cfda  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0070d830 @ 0070d830  (0070d830..0070d863)
  VCALLS_SLOT+0x28:
    0070d85b  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0070d850  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0070e890 @ 0070e890  (0070e890..0070e9a7)
  VCALLS_SLOT+0x28:
    0070e8bb  vtableReg=EDX  objBaseReg=EBX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0070e8b3  MOV EDX,dword ptr [EBX]
      seenFieldOffsetsOnBase: (none)
    0070e8d2  vtableReg=EDX  objBaseReg=EBX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0070e8ca  MOV EDX,dword ptr [EBX]
      seenFieldOffsetsOnBase: (none)
    0070e8dd  vtableReg=EDX  objBaseReg=EBX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0070e8d5  MOV EDX,dword ptr [EBX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EBX -> []

FUN_0070fa80 @ 0070fa80  (0070fa80..0070facd)
  VCALLS_SLOT+0x28:
    0070fa9d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0070fa95  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0070faa8  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0070faa0  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00710850 @ 00710850  (00710850..00710883)
  VCALLS_SLOT+0x28:
    00710862  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0071085a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00711dd0 @ 00711dd0  (00711dd0..00711ea4)
  VCALLS_SLOT+0x28:
    00711ded  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00711de5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00713670 @ 00713670  (00713670..0071377d)
  VCALLS_SLOT+0x28:
    0071368e  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00713686  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00713699  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00713691  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007136b8  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007136ad  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00714b10 @ 00714b10  (00714b10..00714c18)
  VCALLS_SLOT+0x28:
    00714b5b  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00714b53  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00715730 @ 00715730  (00715730..007157f9)
  VCALLS_SLOT+0x28:
    00715743  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0071573e  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00716370 @ 00716370  (00716370..0071642a)
  VCALLS_SLOT+0x28:
    007163ce  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007163c6  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007173b0 @ 007173b0  (007173b0..007173e0)
  VCALLS_SLOT+0x28:
    007173c2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007173ba  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00719270 @ 00719270  (00719270..007194bb)
  VCALLS_SLOT+0x28:
    0071928d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00719285  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0071929b  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00719290  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007192dd  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007192d2  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0071932d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00719322  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00719349  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0071933e  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0071a370 @ 0071a370  (0071a370..0071a3bf)
  VCALLS_SLOT+0x28:
    0071a390  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0071a388  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0071a39b  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0071a393  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0071a3a9  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0071a39e  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0071ad20 @ 0071ad20  (0071ad20..0071ad68)
  VCALLS_SLOT+0x28:
    0071ad3d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0071ad35  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0071bb10 @ 0071bb10  (0071bb10..0071bba5)
  VCALLS_SLOT+0x28:
    0071bb2d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0071bb25  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0071bb3b  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0071bb30  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0071c620 @ 0071c620  (0071c620..0071c65d)
  VCALLS_SLOT+0x28:
    0071c632  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0071c62a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0071dbf0 @ 0071dbf0  (0071dbf0..0071ddd5)
  VCALLS_SLOT+0x28:
    0071dc02  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0071dbfa  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0071e890 @ 0071e890  (0071e890..0071e8cd)
  VCALLS_SLOT+0x28:
    0071e8a2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0071e89a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0071fdd0 @ 0071fdd0  (0071fdd0..0071fe31)
  VCALLS_SLOT+0x28:
    0071fdf9  vtableReg=EDX  objBaseReg=EDI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0071fdf1  MOV EDX,dword ptr [EDI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EDI -> []

FUN_00720840 @ 00720840  (00720840..007208b7)
  VCALLS_SLOT+0x28:
    00720873  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0072086b  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00722c90 @ 00722c90  (00722c90..00722cc7)
  VCALLS_SLOT+0x28:
    00722ca2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00722c9a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00723600 @ 00723600  (00723600..00723637)
  VCALLS_SLOT+0x28:
    00723612  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0072360a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00724a90 @ 00724a90  (00724a90..00724b03)
  VCALLS_SLOT+0x28:
    00724aa2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00724a9a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00724aad  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00724aa5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00724ab8  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00724ab0  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00725310 @ 00725310  (00725310..00725340)
  VCALLS_SLOT+0x28:
    00725322  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0072531a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00725bf0 @ 00725bf0  (00725bf0..00725c23)
  VCALLS_SLOT+0x28:
    00725c1b  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00725c10  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00726d40 @ 00726d40  (00726d40..00726dee)
  VCALLS_SLOT+0x28:
    00726d52  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00726d4a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00726dae  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00726da3  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00729020 @ 00729020  (00729020..0072926c)
  VCALLS_SLOT+0x28:
    00729033  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0072902b  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00729097  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0072908c  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0072911b  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00729113  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007291bd  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007291b5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00729e90 @ 00729e90  (00729e90..00729ea4)
  VCALLS_SLOT+0x28:
    00729e9e  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00729e9c  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_0072a9a0 @ 0072a9a0  (0072a9a0..0072a9d3)
  VCALLS_SLOT+0x28:
    0072a9b2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0072a9aa  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0072c7a0 @ 0072c7a0  (0072c7a0..0072c7e1)
  VCALLS_SLOT+0x28:
    0072c7bd  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0072c7b5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0072c7cb  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0072c7c0  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0072dc30 @ 0072dc30  (0072dc30..0072ddeb)
  VCALLS_SLOT+0x28:
    0072dc51  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0072dc46  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0072dc5f  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0072dc54  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0072dc6d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0072dc62  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0072dc7b  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0072dc70  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0072ea70 @ 0072ea70  (0072ea70..0072eaa0)
  VCALLS_SLOT+0x28:
    0072ea8d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0072ea85  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0072f750 @ 0072f750  (0072f750..0072f7a3)
  VCALLS_SLOT+0x28:
    0072f78d  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0072f785  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0072f798  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0072f790  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007300c0 @ 007300c0  (007300c0..007300e5)
  VCALLS_SLOT+0x28:
    007300d2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007300ca  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007300dd  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007300d5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00730770 @ 00730770  (00730770..007307ab)
  VCALLS_SLOT+0x28:
    00730782  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0073077a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0073078d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00730785  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00730a30 @ 00730a30  (00730a30..00730a55)
  VCALLS_SLOT+0x28:
    00730a42  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00730a3a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00730a4d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00730a45  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00730ec0 @ 00730ec0  (00730ec0..00730f17)
  VCALLS_SLOT+0x28:
    00730ed2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00730eca  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00730edd  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00730ed5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00730ee8  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00730ee0  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00730ef3  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00730eeb  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00731350 @ 00731350  (00731350..007313a7)
  VCALLS_SLOT+0x28:
    00731362  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0073135a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0073136d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00731365  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00731378  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00731370  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00731383  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0073137b  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00733650 @ 00733650  (00733650..007336bf)
  VCALLS_SLOT+0x28:
    0073369c  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00733690  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00734dd0 @ 00734dd0  (00734dd0..00734e33)
  VCALLS_SLOT+0x28:
    00734df2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00734deb  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00734dfd  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00734df5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00735610 @ 00735610  (00735610..00735635)
  VCALLS_SLOT+0x28:
    00735622  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0073561a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0073562d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00735625  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00737f90 @ 00737f90  (00737f90..00738032)
  VCALLS_SLOT+0x28:
    00737fc1  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00737fb9  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0073db80 @ 0073db80  (0073db80..0073dcd0)
  VCALLS_SLOT+0x28:
    0073dbc3  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0073dbb8  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0073dbf4  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0073dbec  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0073fc50 @ 0073fc50  (0073fc50..0073fcb8)
  VCALLS_SLOT+0x28:
    0073fc62  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0073fc5a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0073fc70  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0073fc65  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00740860 @ 00740860  (00740860..00740985)
  VCALLS_SLOT+0x28:
    0074089a  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0074088f  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007408a8  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0074089d  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007408fb  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007408f0  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00740903  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007408fe  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00741420 @ 00741420  (00741420..00741445)
  VCALLS_SLOT+0x28:
    0074143d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00741435  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00741d70 @ 00741d70  (00741d70..00741dfc)
  VCALLS_SLOT+0x28:
    00741d82  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00741d7a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00741dd8  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00741dcd  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00742ed0 @ 00742ed0  (00742ed0..00742f1f)
  VCALLS_SLOT+0x28:
    00742efb  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00742ef0  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00742f09  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00742efe  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00743e80 @ 00743e80  (00743e80..00743fa5)
  VCALLS_SLOT+0x28:
    00743eb4  vtableReg=EDX  objBaseReg=EBX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00743eac  MOV EDX,dword ptr [EBX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EBX -> []

FUN_00744cf0 @ 00744cf0  (00744cf0..00744d15)
  VCALLS_SLOT+0x28:
    00744d02  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00744cfa  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00744d0d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00744d05  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007455f0 @ 007455f0  (007455f0..00745604)
  VCALLS_SLOT+0x28:
    007455fe  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007455fc  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00746290 @ 00746290  (00746290..007462d1)
  VCALLS_SLOT+0x28:
    007462a2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0074629a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007462ad  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007462a5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00747500 @ 00747500  (00747500..0074762d)
  VCALLS_SLOT+0x28:
    007475fe  vtableReg=EDX  objBaseReg=EDI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007475f6  MOV EDX,dword ptr [EDI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EDI -> []

FUN_007482b0 @ 007482b0  (007482b0..0074831b)
  VCALLS_SLOT+0x28:
    007482c2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007482ba  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007482cd  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007482c5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007482db  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007482d0  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00748ca0 @ 00748ca0  (00748ca0..00748cc5)
  VCALLS_SLOT+0x28:
    00748cbd  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00748cb5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007496d0 @ 007496d0  (007496d0..0074977a)
  VCALLS_SLOT+0x28:
    007496e2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007496da  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00749756  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0074974b  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0074a770 @ 0074a770  (0074a770..0074a7b4)
  VCALLS_SLOT+0x28:
    0074a7a4  vtableReg=EDX  objBaseReg=EBX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0074a799  MOV EDX,dword ptr [EBX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EBX -> []

FUN_0074bec0 @ 0074bec0  (0074bec0..0074bed4)
  VCALLS_SLOT+0x28:
    0074bece  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0074becc  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_0074fbd0 @ 0074fbd0  (0074fbd0..0074fc37)
  VCALLS_SLOT+0x28:
    0074fbe2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0074fbda  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0074fbed  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0074fbe5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0074fbfb  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0074fbf0  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00753640 @ 00753640  (00753640..00753665)
  VCALLS_SLOT+0x28:
    00753652  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0075364a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00754500 @ 00754500  (00754500..00754584)
  VCALLS_SLOT+0x28:
    00754560  vtableReg=EDX  objBaseReg=EDI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00754558  MOV EDX,dword ptr [EDI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EDI -> []

FUN_00754ea0 @ 00754ea0  (00754ea0..00754ec5)
  VCALLS_SLOT+0x28:
    00754eb2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00754eaa  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0075d290 @ 0075d290  (0075d290..0075d381)
  VCALLS_SLOT+0x28:
    0075d333  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0075d32e  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0075fcc0 @ 0075fcc0  (0075fcc0..0075fcd4)
  VCALLS_SLOT+0x28:
    0075fcce  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0075fccc  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00761860 @ 00761860  (00761860..00761a2f)
  VCALLS_SLOT+0x28:
    0076189e  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00761893  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007618ac  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007618a1  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00761928  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0076191d  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0076193b  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00761930  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00761959  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0076194e  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00761995  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0076198a  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007619d9  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007619d1  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00763430 @ 00763430  (00763430..00763471)
  VCALLS_SLOT+0x28:
    00763469  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0076345e  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00764c50 @ 00764c50  (00764c50..00764c75)
  VCALLS_SLOT+0x28:
    00764c62  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00764c5a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00765430 @ 00765430  (00765430..00765455)
  VCALLS_SLOT+0x28:
    0076544d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00765445  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007657f0 @ 007657f0  (007657f0..00765839)
  VCALLS_SLOT+0x28:
    00765826  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0076581e  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007660f0 @ 007660f0  (007660f0..0076636a)
  VCALLS_SLOT+0x28:
    00766245  vtableReg=EDX  objBaseReg=EDI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00766233  MOV EDX,dword ptr [EDI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EDI -> []

FUN_00768350 @ 00768350  (00768350..00768380)
  VCALLS_SLOT+0x28:
    00768362  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0076835a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00768e20 @ 00768e20  (00768e20..00768e45)
  VCALLS_SLOT+0x28:
    00768e32  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00768e2a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0076a930 @ 0076a930  (0076a930..0076a98a)
  VCALLS_SLOT+0x28:
    0076a942  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0076a93a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0076bcc0 @ 0076bcc0  (0076bcc0..0076bda2)
  VCALLS_SLOT+0x28:
    0076bd34  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0076bd2c  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0076bd3f  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0076bd37  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0076bd4d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0076bd42  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0076bd5b  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0076bd50  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0076bd7f  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0076bd7a  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0076bd8d  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0076bd82  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0076c5f0 @ 0076c5f0  (0076c5f0..0076c62b)
  VCALLS_SLOT+0x28:
    0076c602  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0076c5fa  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0076cd90 @ 0076cd90  (0076cd90..0076cda4)
  VCALLS_SLOT+0x28:
    0076cd9e  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0076cd9c  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_007716a0 @ 007716a0  (007716a0..007717a1)
  VCALLS_SLOT+0x28:
    00771750  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00771745  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00771c40 @ 00771c40  (00771c40..00771d21)
  VCALLS_SLOT+0x28:
    00771ca6  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00771c9e  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00771cb1  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00771ca9  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00773e90 @ 00773e90  (00773e90..00773eb5)
  VCALLS_SLOT+0x28:
    00773ea2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00773e9a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00773ead  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00773ea5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00775200 @ 00775200  (00775200..00775244)
  VCALLS_SLOT+0x28:
    00775228  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00775220  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0077523c  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00775231  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007759e0 @ 007759e0  (007759e0..00775a2a)
  VCALLS_SLOT+0x28:
    00775a0b  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00775a03  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00777e80 @ 00777e80  (00777e80..00777f00)
  VCALLS_SLOT+0x28:
    00777ece  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00777ec3  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00778910 @ 00778910  (00778910..00778924)
  VCALLS_SLOT+0x28:
    0077891e  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0077891c  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_0077ad10 @ 0077ad10  (0077ad10..0077ae62)
  VCALLS_SLOT+0x28:
    0077ad2e  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0077ad26  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0077ad4e  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0077ad46  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0077ad83  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0077ad7e  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0077adc4  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0077adbc  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0077dd30 @ 0077dd30  (0077dd30..0077dd60)
  VCALLS_SLOT+0x28:
    0077dd42  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0077dd3a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00780d80 @ 00780d80  (00780d80..00780e0b)
  VCALLS_SLOT+0x28:
    00780db1  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00780da6  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00780dbf  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00780db4  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007813b0 @ 007813b0  (007813b0..00781463)
  VCALLS_SLOT+0x28:
    007813e2  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007813d7  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007813f0  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007813e5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00781910 @ 00781910  (00781910..007819c3)
  VCALLS_SLOT+0x28:
    00781942  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00781937  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00781950  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00781945  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00786440 @ 00786440  (00786440..007864b1)
  VCALLS_SLOT+0x28:
    00786471  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00786466  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0078647f  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00786474  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00786860 @ 00786860  (00786860..007868a7)
  VCALLS_SLOT+0x28:
    00786883  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00786878  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007878e0 @ 007878e0  (007878e0..0078790b)
  VCALLS_SLOT+0x28:
    007878f5  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007878ea  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00788250 @ 00788250  (00788250..00788275)
  VCALLS_SLOT+0x28:
    0078826d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00788265  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0078d5a0 @ 0078d5a0  (0078d5a0..0078d5d0)
  VCALLS_SLOT+0x28:
    0078d5c8  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0078d5c0  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0078ebe0 @ 0078ebe0  (0078ebe0..0078ec13)
  VCALLS_SLOT+0x28:
    0078ebf2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0078ebea  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0078f570 @ 0078f570  (0078f570..0078f5a9)
  VCALLS_SLOT+0x28:
    0078f582  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0078f57a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00790740 @ 00790740  (00790740..007907dd)
  VCALLS_SLOT+0x28:
    00790791  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00790789  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0079079c  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00790794  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00790f70 @ 00790f70  (00790f70..00790f95)
  VCALLS_SLOT+0x28:
    00790f8d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00790f85  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00791870 @ 00791870  (00791870..00791895)
  VCALLS_SLOT+0x28:
    00791882  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0079187a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0079188d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00791885  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00792160 @ 00792160  (00792160..00792185)
  VCALLS_SLOT+0x28:
    00792172  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0079216a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0079217d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00792175  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00792af0 @ 00792af0  (00792af0..00792b20)
  VCALLS_SLOT+0x28:
    00792b02  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00792afa  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00795590 @ 00795590  (00795590..00795671)
  VCALLS_SLOT+0x28:
    007955ae  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007955a6  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00795ec0 @ 00795ec0  (00795ec0..00795f14)
  VCALLS_SLOT+0x28:
    00795edd  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00795ed5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00799e50 @ 00799e50  (00799e50..00799e96)
  VCALLS_SLOT+0x28:
    00799e62  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00799e5a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0079ad30 @ 0079ad30  (0079ad30..0079ad6b)
  VCALLS_SLOT+0x28:
    0079ad42  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0079ad3a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0079bd80 @ 0079bd80  (0079bd80..0079c0a8)
  VCALLS_SLOT+0x28:
    0079bd93  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0079bd8b  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0079cf90 @ 0079cf90  (0079cf90..0079cfa4)
  VCALLS_SLOT+0x28:
    0079cf9e  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0079cf9c  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_0079db60 @ 0079db60  (0079db60..0079db90)
  VCALLS_SLOT+0x28:
    0079db72  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0079db6a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0079db7d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0079db75  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0079ec20 @ 0079ec20  (0079ec20..0079ec50)
  VCALLS_SLOT+0x28:
    0079ec32  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0079ec2a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007a3010 @ 007a3010  (007a3010..007a3035)
  VCALLS_SLOT+0x28:
    007a3022  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007a301a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007a3b30 @ 007a3b30  (007a3b30..007a3b71)
  VCALLS_SLOT+0x28:
    007a3b42  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007a3b3a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007a3b4d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007a3b45  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007a4a90 @ 007a4a90  (007a4a90..007a4b1f)
  VCALLS_SLOT+0x28:
    007a4aa2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007a4a9a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007a4aad  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007a4aa5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007a5a60 @ 007a5a60  (007a5a60..007a5aaf)
  VCALLS_SLOT+0x28:
    007a5a72  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007a5a6a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007a5a7d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007a5a75  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007a5a8b  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007a5a80  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007a5a99  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007a5a8e  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007a6460 @ 007a6460  (007a6460..007a64d6)
  VCALLS_SLOT+0x28:
    007a6472  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007a646a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007a71f0 @ 007a71f0  (007a71f0..007a7283)
  VCALLS_SLOT+0x28:
    007a7220  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007a7218  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007a8590 @ 007a8590  (007a8590..007a85f8)
  VCALLS_SLOT+0x28:
    007a85a2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007a859a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007a98e0 @ 007a98e0  (007a98e0..007a98f4)
  VCALLS_SLOT+0x28:
    007a98ee  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007a98ec  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_007aa1a0 @ 007aa1a0  (007aa1a0..007aa1d3)
  VCALLS_SLOT+0x28:
    007aa1bd  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007aa1b5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007aa1cb  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007aa1c0  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007ad800 @ 007ad800  (007ad800..007ad841)
  VCALLS_SLOT+0x28:
    007ad812  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007ad80a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007ae9b0 @ 007ae9b0  (007ae9b0..007aea7b)
  VCALLS_SLOT+0x28:
    007ae9c5  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007ae9ba  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007ae9d3  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007ae9c8  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007af730 @ 007af730  (007af730..007af77f)
  VCALLS_SLOT+0x28:
    007af742  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007af73a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007af75b  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007af750  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007b03c0 @ 007b03c0  (007b03c0..007b0425)
  VCALLS_SLOT+0x28:
    007b041c  vtableReg=EAX  objBaseReg=EDI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007b0411  MOV EAX,dword ptr [EDI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EDI -> []

FUN_007b3070 @ 007b3070  (007b3070..007b31f4)
  VCALLS_SLOT+0x28:
    007b311f  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b3110  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007b3140  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b3138  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007b3171  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b3169  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007b53e0 @ 007b53e0  (007b53e0..007b5410)
  VCALLS_SLOT+0x28:
    007b53fd  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b53f5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007b5408  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b5400  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007b56b0 @ 007b56b0  (007b56b0..007b56e0)
  VCALLS_SLOT+0x28:
    007b56cd  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b56c5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007b56d8  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b56d0  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007b5bd0 @ 007b5bd0  (007b5bd0..007b5c00)
  VCALLS_SLOT+0x28:
    007b5bed  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b5be5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007b5bf8  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b5bf0  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007b60b0 @ 007b60b0  (007b60b0..007b60e0)
  VCALLS_SLOT+0x28:
    007b60cd  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b60c5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007b60d8  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b60d0  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007b6720 @ 007b6720  (007b6720..007b6750)
  VCALLS_SLOT+0x28:
    007b673d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b6735  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007b6748  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b6740  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007b6be0 @ 007b6be0  (007b6be0..007b6c10)
  VCALLS_SLOT+0x28:
    007b6bfd  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b6bf5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007b6c08  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b6c00  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007b6e90 @ 007b6e90  (007b6e90..007b6ec0)
  VCALLS_SLOT+0x28:
    007b6ead  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b6ea5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007b7160 @ 007b7160  (007b7160..007b7190)
  VCALLS_SLOT+0x28:
    007b717d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b7175  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007b7188  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b7180  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007b7410 @ 007b7410  (007b7410..007b7440)
  VCALLS_SLOT+0x28:
    007b742d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b7425  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007b7890 @ 007b7890  (007b7890..007b78cb)
  VCALLS_SLOT+0x28:
    007b78a2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007b789a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007b78ad  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b78a5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007b7b30 @ 007b7b30  (007b7b30..007b7b55)
  VCALLS_SLOT+0x28:
    007b7b4d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b7b45  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007b7dc0 @ 007b7dc0  (007b7dc0..007b7de5)
  VCALLS_SLOT+0x28:
    007b7ddd  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b7dd5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007b8050 @ 007b8050  (007b8050..007b8075)
  VCALLS_SLOT+0x28:
    007b806d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b8065  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007b88d0 @ 007b88d0  (007b88d0..007b8907)
  VCALLS_SLOT+0x28:
    007b88e2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007b88da  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007b88ed  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007b88e5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007b8cc0 @ 007b8cc0  (007b8cc0..007b8ce5)
  VCALLS_SLOT+0x28:
    007b8cd2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007b8cca  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007be7a0 @ 007be7a0  (007be7a0..007be7ed)
  VCALLS_SLOT+0x28:
    007be7cf  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007be7c7  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007bf170 @ 007bf170  (007bf170..007bf195)
  VCALLS_SLOT+0x28:
    007bf182  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007bf17a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007c0290 @ 007c0290  (007c0290..007c0326)
  VCALLS_SLOT+0x28:
    007c02a2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007c029a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007c0c60 @ 007c0c60  (007c0c60..007c0c85)
  VCALLS_SLOT+0x28:
    007c0c72  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007c0c6a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007c2630 @ 007c2630  (007c2630..007c2676)
  VCALLS_SLOT+0x28:
    007c2642  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007c263a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007c38e0 @ 007c38e0  (007c38e0..007c3926)
  VCALLS_SLOT+0x28:
    007c38f2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007c38ea  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007c43c0 @ 007c43c0  (007c43c0..007c4433)
  VCALLS_SLOT+0x28:
    007c43dd  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007c43d5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007c4f80 @ 007c4f80  (007c4f80..007c5005)
  VCALLS_SLOT+0x28:
    007c4fa8  vtableReg=EAX  objBaseReg=EBX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007c4fa0  MOV EAX,dword ptr [EBX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EBX -> []

FUN_007c5d00 @ 007c5d00  (007c5d00..007c5d58)
  VCALLS_SLOT+0x28:
    007c5d12  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007c5d0a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007c6830 @ 007c6830  (007c6830..007c6898)
  VCALLS_SLOT+0x28:
    007c6842  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007c683a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007c70b0 @ 007c70b0  (007c70b0..007c70ef)
  VCALLS_SLOT+0x28:
    007c70c2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007c70ba  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007c8670 @ 007c8670  (007c8670..007c86d9)
  VCALLS_SLOT+0x28:
    007c8686  vtableReg=EAX  objBaseReg=EBX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007c867c  MOV EAX,dword ptr [EBX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EBX -> []

FUN_007c9b00 @ 007c9b00  (007c9b00..007c9b48)
  VCALLS_SLOT+0x28:
    007c9b3d  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007c9b35  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007cb710 @ 007cb710  (007cb710..007cb724)
  VCALLS_SLOT+0x28:
    007cb71e  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007cb71c  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_007cdcb0 @ 007cdcb0  (007cdcb0..007cdde6)
  VCALLS_SLOT+0x28:
    007cdd92  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007cdd8a  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007d0f80 @ 007d0f80  (007d0f80..007d0fa5)
  VCALLS_SLOT+0x28:
    007d0f92  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007d0f8a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007d0f9d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007d0f95  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007d2050 @ 007d2050  (007d2050..007d2064)
  VCALLS_SLOT+0x28:
    007d205e  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007d205c  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_007d2890 @ 007d2890  (007d2890..007d290a)
  VCALLS_SLOT+0x28:
    007d289f  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007d289a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007d37a0 @ 007d37a0  (007d37a0..007d389c)
  VCALLS_SLOT+0x28:
    007d37ef  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007d37ea  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007d48e0 @ 007d48e0  (007d48e0..007d4923)
  VCALLS_SLOT+0x28:
    007d48f5  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007d48ea  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007d4903  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007d48f8  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007d5700 @ 007d5700  (007d5700..007d573b)
  VCALLS_SLOT+0x28:
    007d5712  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007d570a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007d571d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007d5715  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007d5728  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007d5720  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007d5733  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007d572b  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007d5cf0 @ 007d5cf0  (007d5cf0..007d5d2b)
  VCALLS_SLOT+0x28:
    007d5d02  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007d5cfa  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007d5d0d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007d5d05  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007d5d18  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007d5d10  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007d5d23  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007d5d1b  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007d6600 @ 007d6600  (007d6600..007d663e)
  VCALLS_SLOT+0x28:
    007d6612  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007d660a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007d661d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007d6615  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007d6628  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007d6620  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007d6b80 @ 007d6b80  (007d6b80..007d6bbe)
  VCALLS_SLOT+0x28:
    007d6b92  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007d6b8a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007d6b9d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007d6b95  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007d6ba8  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007d6ba0  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007d7020 @ 007d7020  (007d7020..007d7034)
  VCALLS_SLOT+0x28:
    007d702e  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007d702c  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_007db270 @ 007db270  (007db270..007db490)
  VCALLS_SLOT+0x28:
    007db2ca  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007db2c8  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_007dbba0 @ 007dbba0  (007dbba0..007dc04f)
  VCALLS_SLOT+0x28:
    007dbd44  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007dbd3d  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007dbd51  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007dbd47  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007dbd5e  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007dbd54  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007dbd6b  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007dbd61  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007dbdd5  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007dbdbc  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007dbe08  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007dbdec  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007dbe2d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007dbe1f  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007dbe3d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007dbe32  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007dbe4d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007dbe42  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007dc480 @ 007dc480  (007dc480..007dc628)
  VCALLS_SLOT+0x28:
    007dc549  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007dc547  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    007dc557  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007dc555  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_007dcae0 @ 007dcae0  (007dcae0..007dcb65)
  VCALLS_SLOT+0x28:
    007dcb10  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007dcb0e  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    007dcb49  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007dcb46  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_007e4ad0 @ 007e4ad0  (007e4ad0..007e4b0a)
  VCALLS_SLOT+0x28:
    007e4b02  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007e4af7  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007e5e20 @ 007e5e20  (007e5e20..007e5ecd)
  VCALLS_SLOT+0x28:
    007e5e61  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007e5e56  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007e5e6f  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007e5e64  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007e5eb6  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007e5eae  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007e9720 @ 007e9720  (007e9720..007e9d9a)
  VCALLS_SLOT+0x28:
    007e9741  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007e9736  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007eaea0 @ 007eaea0  (007eaea0..007eaf0f)
  VCALLS_SLOT+0x28:
    007eaedd  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007eaed2  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007eba70 @ 007eba70  (007eba70..007ebb27)
  VCALLS_SLOT+0x28:
    007ebaa3  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007eba88  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007ed280 @ 007ed280  (007ed280..007ed638)
  VCALLS_SLOT+0x28:
    007ed34b  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007ed343  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007ed4a5  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007ed493  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007f1070 @ 007f1070  (007f1070..007f11c4)
  VCALLS_SLOT+0x28:
    007f1096  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007f108e  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007f1128  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007f1120  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007f1b70 @ 007f1b70  (007f1b70..007f1baa)
  VCALLS_SLOT+0x28:
    007f1ba2  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007f1b97  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007f2460 @ 007f2460  (007f2460..007f24a8)
  VCALLS_SLOT+0x28:
    007f2492  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007f2487  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007f24a0  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007f2495  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007f2de0 @ 007f2de0  (007f2de0..007f2e1a)
  VCALLS_SLOT+0x28:
    007f2e12  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007f2e07  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007f4840 @ 007f4840  (007f4840..007f4a0f)
  VCALLS_SLOT+0x28:
    007f48ab  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007f48a0  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007f48b9  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007f48ae  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007f7240 @ 007f7240  (007f7240..007f74ce)
  VCALLS_SLOT+0x28:
    007f725e  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007f7256  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007f7269  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007f7261  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007f72bd  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007f72b8  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007f732d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007f7328  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007f7412  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007f740a  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007f741f  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007f7417  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007f88f0 @ 007f88f0  (007f88f0..007f89de)
  VCALLS_SLOT+0x28:
    007f890d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007f8905  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007f891b  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007f8910  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007f8929  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007f891e  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007fa6c0 @ 007fa6c0  (007fa6c0..007fa92c)
  VCALLS_SLOT+0x28:
    007fa6f6  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007fa6ee  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007fa704  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007fa6f9  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007fa712  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007fa707  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007fa78a  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007fa77f  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007fa798  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007fa78d  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007fa8d5  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007fa8c6  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007faed0 @ 007faed0  (007faed0..007faf21)
  VCALLS_SLOT+0x28:
    007faee2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007faeda  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007fc4e0 @ 007fc4e0  (007fc4e0..007fc608)
  VCALLS_SLOT+0x28:
    007fc506  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007fc4fe  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007fc529  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007fc521  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007fc565  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007fc55d  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007fc581  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007fc576  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007fc5a5  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007fc59a  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007fd3d0 @ 007fd3d0  (007fd3d0..007fd426)
  VCALLS_SLOT+0x28:
    007fd3e5  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 007fd3da  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007fd3f3  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007fd3e8  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_007fe3b0 @ 007fe3b0  (007fe3b0..007fe46b)
  VCALLS_SLOT+0x28:
    007fe3cd  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007fe3c5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007fe3db  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007fe3d0  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    007fe3e9  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 007fe3de  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00800460 @ 00800460  (00800460..0080079d)
  VCALLS_SLOT+0x28:
    0080049e  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00800493  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    008004ac  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 008004a1  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00800711  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00800706  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00800747  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0080073f  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00805750 @ 00805750  (00805750..0080598c)
  VCALLS_SLOT+0x28:
    0080578f  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00805784  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0080587e  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00805876  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    008058cb  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 008058c3  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00805934  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0080592c  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_008069e0 @ 008069e0  (008069e0..00806a60)
  VCALLS_SLOT+0x28:
    00806a12  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00806a07  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0080ab40 @ 0080ab40  (0080ab40..0080b247)
  VCALLS_SLOT+0x28:
    0080ab99  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0080ab8e  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0080aba7  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0080ab9c  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0080ae1d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0080ae18  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0080ae5b  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0080ae56  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0080af5e  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0080af59  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0080af9c  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0080af97  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0080b08b  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0080b083  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0080b19a  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0080b18b  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0080d2a0 @ 0080d2a0  (0080d2a0..0080d2e2)
  VCALLS_SLOT+0x28:
    0080d2bd  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0080d2b5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0080e540 @ 0080e540  (0080e540..0080e5bc)
  VCALLS_SLOT+0x28:
    0080e572  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0080e567  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0080e580  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0080e575  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0080f7a0 @ 0080f7a0  (0080f7a0..0080f8b6)
  VCALLS_SLOT+0x28:
    0080f7b3  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0080f7ab  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0080f7d8  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0080f7d3  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_008101d0 @ 008101d0  (008101d0..00810215)
  VCALLS_SLOT+0x28:
    0081020d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00810202  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00811260 @ 00811260  (00811260..0081131a)
  VCALLS_SLOT+0x28:
    008112a6  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0081129b  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    008112b4  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 008112a9  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    008112ee  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 008112e9  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00811d90 @ 00811d90  (00811d90..00811ef6)
  VCALLS_SLOT+0x28:
    00811db9  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00811db1  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00811ec7  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00811ebc  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00811ee0  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00811ed5  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00811eee  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00811ee3  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00813680 @ 00813680  (00813680..008138b3)
  VCALLS_SLOT+0x28:
    00813886  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00813882  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_008142c0 @ 008142c0  (008142c0..008142d7)
  VCALLS_SLOT+0x28:
    008142d2  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 008142d0  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00814650 @ 00814650  (00814650..00814688)
  VCALLS_SLOT+0x28:
    00814662  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0081465a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00815080 @ 00815080  (00815080..0081530b)
  VCALLS_SLOT+0x28:
    008152de  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 008152da  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00825b20 @ 00825b20  (00825b20..00825d52)
  VCALLS_SLOT+0x28:
    00825d25  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00825d21  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_008269a0 @ 008269a0  (008269a0..00826bd2)
  VCALLS_SLOT+0x28:
    00826ba5  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00826ba1  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00827ec0 @ 00827ec0  (00827ec0..0082814e)
  VCALLS_SLOT+0x28:
    00827fff  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00827ffb  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00828d40 @ 00828d40  (00828d40..00828fce)
  VCALLS_SLOT+0x28:
    00828e7f  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00828e7b  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00829d70 @ 00829d70  (00829d70..00829ffe)
  VCALLS_SLOT+0x28:
    00829eaf  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00829eab  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0082ad60 @ 0082ad60  (0082ad60..0082afee)
  VCALLS_SLOT+0x28:
    0082ae9f  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0082ae9b  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0082bd50 @ 0082bd50  (0082bd50..0082bfde)
  VCALLS_SLOT+0x28:
    0082be8f  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0082be8b  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0082d5d0 @ 0082d5d0  (0082d5d0..0082d802)
  VCALLS_SLOT+0x28:
    0082d7d5  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0082d7d1  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0082e3b0 @ 0082e3b0  (0082e3b0..0082e63e)
  VCALLS_SLOT+0x28:
    0082e4ef  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0082e4eb  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00830b60 @ 00830b60  (00830b60..00830d92)
  VCALLS_SLOT+0x28:
    00830d65  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00830d61  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00831660 @ 00831660  (00831660..0083168b)
  VCALLS_SLOT+0x28:
    00831675  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0083166a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00832670 @ 00832670  (00832670..00832726)
  VCALLS_SLOT+0x28:
    008326a2  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00832697  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00833ad0 @ 00833ad0  (00833ad0..00833d02)
  VCALLS_SLOT+0x28:
    00833cd5  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00833cd1  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_008356f0 @ 008356f0  (008356f0..00835745)
  VCALLS_SLOT+0x28:
    00835713  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00835708  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00850d10 @ 00850d10  (00850d10..00850d59)
  VCALLS_SLOT+0x28:
    00850d2a  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00850d23  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00850e60 @ 00850e60  (00850e60..00850e99)
  VCALLS_SLOT+0x28:
    00850e76  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00850e6f  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00850eb0 @ 00850eb0  (00850eb0..00850ee4)
  VCALLS_SLOT+0x28:
    00850ec1  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00850eba  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00900170 @ 00900170  (00900170..009001b6)
  VCALLS_SLOT+0x28:
    009001a1  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00900191  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_009001f0 @ 009001f0  (009001f0..00900236)
  VCALLS_SLOT+0x28:
    00900221  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00900211  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00900270 @ 00900270  (00900270..009002b6)
  VCALLS_SLOT+0x28:
    009002a1  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00900291  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_009002f0 @ 009002f0  (009002f0..00900336)
  VCALLS_SLOT+0x28:
    00900321  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00900311  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00900370 @ 00900370  (00900370..009003b6)
  VCALLS_SLOT+0x28:
    009003a1  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00900391  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_009003f0 @ 009003f0  (009003f0..00900436)
  VCALLS_SLOT+0x28:
    00900421  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00900411  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00900470 @ 00900470  (00900470..009004b6)
  VCALLS_SLOT+0x28:
    009004a1  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00900491  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00900540 @ 00900540  (00900540..009005c9)
  VCALLS_SLOT+0x28:
    00900555  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0090054e  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0090058a  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0090057f  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00918da0 @ 00918da0  (00918da0..00918fdd)
  VCALLS_SLOT+0x28:
    00918df4  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00918de8  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00918e0b  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00918e05  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00938600 @ 00938600  (00938600..00938786)
  VCALLS_SLOT+0x28:
    0093863b  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0093861c  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_009389d0 @ 009389d0  (009389d0..00938bde)
  VCALLS_SLOT+0x28:
    00938a0c  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00938a0a  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    00938af5  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00938af3  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_0093a110 @ 0093a110  (0093a110..0093aea8)
  VCALLS_SLOT+0x28:
    0093a8c7  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0093a8c5  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    0093aadc  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0093aada  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    0093ab4c  vtableReg=EDX  objBaseReg=EBX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0093ab44  MOV EDX,EBX
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EBX -> []
    ECX -> []

FUN_0093b330 @ 0093b330  (0093b330..0093b4d7)
  VCALLS_SLOT+0x28:
    0093b38a  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0093b388  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    0093b46e  vtableReg=EBX  objBaseReg=EDI  ins=CALL dword ptr [EBX + 0x28]
      loadEvidence: 0093b45c  MOV EBX,dword ptr [EDI]
      seenFieldOffsetsOnBase: (none)
    0093b480  vtableReg=EDX  objBaseReg=EBX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0093b479  MOV EDX,dword ptr [EBX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EBX -> []
    ECX -> []
    EDI -> []

FUN_00948e30 @ 00948e30  (00948e30..00949050)
  VCALLS_SLOT+0x28:
    00948e9a  vtableReg=EDX  objBaseReg=EBX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00948e89  MOV EDX,dword ptr [EBX]
      seenFieldOffsetsOnBase: (none)
    00948f23  vtableReg=EDX  objBaseReg=EBX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00948f19  MOV EDX,dword ptr [EBX]
      seenFieldOffsetsOnBase: (none)
    00948f5b  vtableReg=EDX  objBaseReg=EBX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00948f4d  MOV EDX,dword ptr [EBX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EBX -> []

FUN_00958900 @ 00958900  (00958900..00958a59)
  VCALLS_SLOT+0x28:
    00958939  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00958937  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    00958a3e  vtableReg=EDX  objBaseReg=(unknown)  ins=CALL dword ptr [EDX + 0x28]
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00959e50 @ 00959e50  (00959e50..00959fc2)
  VCALLS_SLOT+0x28:
    00959fad  vtableReg=EDX  objBaseReg=(unknown)  ins=CALL dword ptr [EDX + 0x28]

FUN_0095c590 @ 0095c590  (0095c590..0095c772)
  VCALLS_SLOT+0x28:
    0095c62f  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0095c62d  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_0095c840 @ 0095c840  (0095c840..0095c8d9)
  VCALLS_SLOT+0x28:
    0095c894  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0095c892  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_0095dc40 @ 0095dc40  (0095dc40..0095dfa7)
  VCALLS_SLOT+0x28:
    0095dd39  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 0095dd33  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_0096c8d0 @ 0096c8d0  (0096c8d0..0096ccf8)
  VCALLS_SLOT+0x28:
    0096c955  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0096c951  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    0096c9b9  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 0096c9af  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_009d5f83 @ 009d5f83  (009d5f83..009d6db5)
  VCALLS_SLOT+0x28:
    009d6c27  vtableReg=EDX  objBaseReg=(unknown)  ins=CALL dword ptr [EDX + 0x28]

FUN_009e0260 @ 009e0260  (009e0260..009e1483)
  VCALLS_SLOT+0x28:
    009e053b  vtableReg=EAX  objBaseReg=EDX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 009e0515  MOV EAX,dword ptr [EDX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EDX -> []

FUN_009eb280 @ 009eb280  (009eb280..009ed77d)
  VCALLS_SLOT+0x28:
    009ec78a  vtableReg=EDX  objBaseReg=(unknown)  ins=CALL dword ptr [EDX + 0x28]

FUN_009ee860 @ 009ee860  (009ee860..009efea2)
  VCALLS_SLOT+0x28:
    009ee9a9  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 009ee9a5  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    009eea0d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 009eea03  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    009eeaee  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 009eeae4  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    009eeb10  vtableReg=EAX  objBaseReg=(unknown)  ins=CALL dword ptr [EAX + 0x28]
    009eeb38  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 009eeb2e  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    009ef18b  vtableReg=EDX  objBaseReg=EAX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 009ef189  MOV EDX,dword ptr [EAX]
      seenFieldOffsetsOnBase: (none)
    009ef6ab  vtableReg=EDX  objBaseReg=(unknown)  ins=CALL dword ptr [EDX + 0x28]
    009ef84d  vtableReg=EDX  objBaseReg=(unknown)  ins=CALL dword ptr [EDX + 0x28]
    009ef95c  vtableReg=EDX  objBaseReg=(unknown)  ins=CALL dword ptr [EDX + 0x28]
    009efc5d  vtableReg=EDX  objBaseReg=(unknown)  ins=CALL dword ptr [EDX + 0x28]
    009efc70  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 009efc6c  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    009efc92  vtableReg=EDX  objBaseReg=(unknown)  ins=CALL dword ptr [EDX + 0x28]
    009efcba  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 009efcb0  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []
    EAX -> []

FUN_009f1de0 @ 009f1de0  (009f1de0..009f2725)
  VCALLS_SLOT+0x28:
    009f1e86  vtableReg=EDX  objBaseReg=EAX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 009f1e61  MOV EDX,dword ptr [EAX]
      seenFieldOffsetsOnBase: (none)
    009f1fd8  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 009f1fd6  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []
    EAX -> []

FUN_009f29b0 @ 009f29b0  (009f29b0..009f2f18)
  VCALLS_SLOT+0x28:
    009f2a73  vtableReg=EDX  objBaseReg=EAX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 009f2a4e  MOV EDX,dword ptr [EAX]
      seenFieldOffsetsOnBase: (none)
    009f2b76  vtableReg=EAX  objBaseReg=(unknown)  ins=CALL dword ptr [EAX + 0x28]
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EAX -> []

FUN_009f57e0 @ 009f57e0  (009f57e0..009f5e47)
  VCALLS_SLOT+0x28:
    009f5af8  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 009f5af6  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_009f8cc0 @ 009f8cc0  (009f8cc0..009f8fb1)
  VCALLS_SLOT+0x28:
    009f8f9a  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 009f8f95  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_009fc500 @ 009fc500  (009fc500..009fc614)
  VCALLS_SLOT+0x28:
    009fc558  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 009fc554  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00a07680 @ 00a07680  (00a07680..00a0770b)
  VCALLS_SLOT+0x28:
    00a076a0  vtableReg=EAX  objBaseReg=(unknown)  ins=CALL dword ptr [EAX + 0x28]

FUN_00a0a640 @ 00a0a640  (00a0a640..00a0ac7b)
  VCALLS_SLOT+0x28:
    00a0a812  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00a0a80e  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00a0a876  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00a0a86c  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00a0aa53  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00a0aa4a  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00a0aa75  vtableReg=EAX  objBaseReg=(unknown)  ins=CALL dword ptr [EAX + 0x28]
    00a0aa9d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00a0aa93  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00a0eb60 @ 00a0eb60  (00a0eb60..00a10079)
  VCALLS_SLOT+0x28:
    00a0ee9f  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00a0ee9d  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    00a0f177  vtableReg=EDX  objBaseReg=(unknown)  ins=CALL dword ptr [EDX + 0x28]
    00a0f43a  vtableReg=EDX  objBaseReg=(unknown)  ins=CALL dword ptr [EDX + 0x28]
    00a0f678  vtableReg=EDX  objBaseReg=(unknown)  ins=CALL dword ptr [EDX + 0x28]
    00a0f7a0  vtableReg=EAX  objBaseReg=(unknown)  ins=CALL dword ptr [EAX + 0x28]
    00a0f8c9  vtableReg=EAX  objBaseReg=(unknown)  ins=CALL dword ptr [EAX + 0x28]
    00a0fa55  vtableReg=EAX  objBaseReg=(unknown)  ins=CALL dword ptr [EAX + 0x28]
    00a0fb57  vtableReg=EDX  objBaseReg=(unknown)  ins=CALL dword ptr [EDX + 0x28]
    00a0fc98  vtableReg=EDX  objBaseReg=(unknown)  ins=CALL dword ptr [EDX + 0x28]
    00a0fdbf  vtableReg=EAX  objBaseReg=(unknown)  ins=CALL dword ptr [EAX + 0x28]
    00a0fe76  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00a0fe74  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00a1cfa0 @ 00a1cfa0  (00a1cfa0..00a1cff5)
  VCALLS_SLOT+0x28:
    00a1cfec  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00a1cfe6  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00a1d040 @ 00a1d040  (00a1d040..00a1d077)
  VCALLS_SLOT+0x28:
    00a1d06e  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00a1d069  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00a1dd20 @ 00a1dd20  (00a1dd20..00a1e0f3)
  VCALLS_SLOT+0x28:
    00a1e08d  vtableReg=EAX  objBaseReg=EDI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00a1e089  MOV EAX,dword ptr [EDI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EDI -> []

FUN_00a1f4f0 @ 00a1f4f0  (00a1f4f0..00a1f752)
  VCALLS_SLOT+0x28:
    00a1f66b  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00a1f661  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00a28c40 @ 00a28c40  (00a28c40..00a28f71)
  VCALLS_SLOT+0x28:
    00a28cd8  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00a28cd4  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00a28d3c  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00a28d32  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00a2a4e0 @ 00a2a4e0  (00a2a4e0..00a2a876)
  VCALLS_SLOT+0x28:
    00a2a56c  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00a2a562  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00a2a588  vtableReg=EDX  objBaseReg=(unknown)  ins=CALL dword ptr [EDX + 0x28]
    00a2a591  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00a2a58d  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00a304d0 @ 00a304d0  (00a304d0..00a30672)
  VCALLS_SLOT+0x28:
    00a30544  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00a3051c  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00a30588  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00a3057e  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00a59970 @ 00a59970  (00a59970..00a59bb4)
  VCALLS_SLOT+0x28:
    00a59a81  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00a59a77  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00a59d70 @ 00a59d70  (00a59d70..00a59e2b)
  VCALLS_SLOT+0x28:
    00a59dbf  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00a59db5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00a9a4a0 @ 00a9a4a0  (00a9a4a0..00a9a808)
  VCALLS_SLOT+0x28:
    00a9a5dd  vtableReg=EDX  objBaseReg=ECX  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00a9a5db  MOV EDX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
    00a9a7b1  vtableReg=EDX  objBaseReg=EDI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00a9a7ad  MOV EDX,dword ptr [EDI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []
    EDI -> []

FUN_00aaca60 @ 00aaca60  (00aaca60..00aad2f2)
  VCALLS_SLOT+0x28:
    00aacbe0  vtableReg=EAX  objBaseReg=EDI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00aacbd3  MOV EAX,dword ptr [EDI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EDI -> []

FUN_00abb540 @ 00abb540  (00abb540..00abbd70)
  VCALLS_SLOT+0x28:
    00abbb2e  vtableReg=EAX  objBaseReg=EDX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00abbb0e  MOV dword ptr [EAX],EDX
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EDX -> []

FUN_00abc0c0 @ 00abc0c0  (00abc0c0..00abc124)
  VCALLS_SLOT+0x28:
    00abc0f7  vtableReg=EAX  objBaseReg=ECX  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00abc0f5  MOV EAX,dword ptr [ECX]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ECX -> []

FUN_00b374c0 @ 00b374c0  (00b374c0..00b376bb)
  VCALLS_SLOT+0x28:
    00b3755c  vtableReg=EAX  objBaseReg=EDI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00b3752c  MOV EAX,dword ptr [EDI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EDI -> []

FUN_00b37fa0 @ 00b37fa0  (00b37fa0..00b3abf1)
  VCALLS_SLOT+0x28:
    00b38631  vtableReg=EDX  objBaseReg=(unknown)  ins=CALL dword ptr [EDX + 0x28]
    00b38780  vtableReg=EAX  objBaseReg=(unknown)  ins=CALL dword ptr [EAX + 0x28]
    00b3a46c  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00b3a466  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00b3a6d7  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00b3a6d1  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00b51700 @ 00b51700  (00b51700..00b528c7)
  VCALLS_SLOT+0x28:
    00b51e2c  vtableReg=EDX  objBaseReg=EDI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00b51e27  MOV EDX,dword ptr [EDI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EDI -> []

FUN_00b7be90 @ 00b7be90  (00b7be90..00b7c88b)
  VCALLS_SLOT+0x28:
    00b7bec9  vtableReg=EAX  objBaseReg=FS  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00b7be93  MOV EAX,FS:[0x0]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    FS -> []

FUN_00b8dcd0 @ 00b8dcd0  (00b8dcd0..00b8de65)
  VCALLS_SLOT+0x28:
    00b8ddfb  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00b8ddf1  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00ba05d0 @ 00ba05d0  (00ba05d0..00ba06b4)
  VCALLS_SLOT+0x28:
    00ba064c  vtableReg=EDX  objBaseReg=(unknown)  ins=CALL dword ptr [EDX + 0x28]

FUN_00bc7730 @ 00bc7730  (00bc7730..00bc7a8c)
  VCALLS_SLOT+0x28:
    00bc7a18  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00bc7a13  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00bc8c00 @ 00bc8c00  (00bc8c00..00bc8e0f)
  VCALLS_SLOT+0x28:
    00bc8da4  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00bc8d9f  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00bc8f20 @ 00bc8f20  (00bc8f20..00bc9330)
  VCALLS_SLOT+0x28:
    00bc8feb  vtableReg=EDX  objBaseReg=(unknown)  ins=CALL dword ptr [EDX + 0x28]
    00bc9219  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00bc9214  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00bdaf10 @ 00bdaf10  (00bdaf10..00bdaffd)
  VCALLS_SLOT+0x28:
    00bdaf97  vtableReg=EDX  objBaseReg=(unknown)  ins=CALL dword ptr [EDX + 0x28]

FUN_00bfa220 @ 00bfa220  (00bfa220..00bfa28d)
  VCALLS_SLOT+0x28:
    00bfa22f  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00bfa22a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00bfa23a  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00bfa232  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00bfa245  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00bfa23d  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00bfa7e0 @ 00bfa7e0  (00bfa7e0..00bfa88b)
  VCALLS_SLOT+0x28:
    00bfa812  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00bfa80d  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00c15a50 @ 00c15a50  (00c15a50..00c15c47)
  VCALLS_SLOT+0x28:
    00c15a60  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00c15a5b  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00c15a76  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c15a6e  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00c15bc0  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c15bb5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00c19030 @ 00c19030  (00c19030..00c190d0)
  VCALLS_SLOT+0x28:
    00c19043  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00c1903b  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00c1a4c0 @ 00c1a4c0  (00c1a4c0..00c1a57b)
  VCALLS_SLOT+0x28:
    00c1a4d3  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00c1a4cb  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00c1a4de  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c1a4d6  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00c1a680 @ 00c1a680  (00c1a680..00c1a6ed)
  VCALLS_SLOT+0x28:
    00c1a692  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00c1a68a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00c1a69d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c1a695  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00c22f20 @ 00c22f20  (00c22f20..00c22f7c)
  VCALLS_SLOT+0x28:
    00c22f3d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c22f35  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00c22f48  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c22f40  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00c22f53  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c22f4b  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00c234c0 @ 00c234c0  (00c234c0..00c23510)
  VCALLS_SLOT+0x28:
    00c234f9  vtableReg=EDX  objBaseReg=EDI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c234f1  MOV EDX,dword ptr [EDI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    EDI -> []

FUN_00c23e00 @ 00c23e00  (00c23e00..00c23e9e)
  VCALLS_SLOT+0x28:
    00c23e1d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c23e15  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00c23e28  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c23e20  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00c23e33  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c23e2b  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00c23e5f  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c23e57  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00c24840 @ 00c24840  (00c24840..00c2489c)
  VCALLS_SLOT+0x28:
    00c2485d  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c24855  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00c24868  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c24860  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00c24873  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c2486b  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00c24cd0 @ 00c24cd0  (00c24cd0..00c24d2c)
  VCALLS_SLOT+0x28:
    00c24ced  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c24ce5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00c24cf8  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c24cf0  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00c24d03  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c24cfb  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00c51a10 @ 00c51a10  (00c51a10..00c51af9)
  VCALLS_SLOT+0x28:
    00c51a2e  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c51a26  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00c51a39  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c51a31  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00c51aa8  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c51aa0  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00c5bb50 @ 00c5bb50  (00c5bb50..00c5bc31)
  VCALLS_SLOT+0x28:
    00c5bb63  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00c5bb5e  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00c5bbf7  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c5bbef  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00c5cb10 @ 00c5cb10  (00c5cb10..00c5cb60)
  VCALLS_SLOT+0x28:
    00c5cb37  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c5cb2f  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00c5d850 @ 00c5d850  (00c5d850..00c5d8a5)
  VCALLS_SLOT+0x28:
    00c5d860  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00c5d85c  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00c5d86b  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c5d863  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00c61430 @ 00c61430  (00c61430..00c6150d)
  VCALLS_SLOT+0x28:
    00c61454  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c61448  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00c61497  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c61486  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00c614a2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00c6149a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00c62c00 @ 00c62c00  (00c62c00..00c62cc7)
  VCALLS_SLOT+0x28:
    00c62c20  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c62c18  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00c62c2b  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c62c23  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00c62c36  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c62c2e  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00c63cc0 @ 00c63cc0  (00c63cc0..00c63d1c)
  VCALLS_SLOT+0x28:
    00c63cd2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00c63cca  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00c6ae90 @ 00c6ae90  (00c6ae90..00c6af14)
  VCALLS_SLOT+0x28:
    00c6aea2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00c6ae9a  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00c75ae0 @ 00c75ae0  (00c75ae0..00c75b47)
  VCALLS_SLOT+0x28:
    00c75af2  vtableReg=EAX  objBaseReg=ESI  ins=CALL dword ptr [EAX + 0x28]
      loadEvidence: 00c75aea  MOV EAX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00c75afd  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c75af5  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
    00c75b08  vtableReg=EDX  objBaseReg=ESI  ins=CALL dword ptr [EDX + 0x28]
      loadEvidence: 00c75b00  MOV EDX,dword ptr [ESI]
      seenFieldOffsetsOnBase: (none)
  BASE_REG_FIELD_OFFSETS_OBSERVED:
    ESI -> []

FUN_00cb54d0 @ 00cb54d0  (00cb54d0..00cb5650)
  VCALLS_SLOT+0x28:
    00cb5625  vtableReg=ECX  objBaseReg=(unknown)  ins=CALL dword ptr [ECX + 0x28]

FUN_00cb58b0 @ 00cb58b0  (00cb58b0..00cb5a33)
  VCALLS_SLOT+0x28:
    00cb5a08  vtableReg=ECX  objBaseReg=(unknown)  ins=CALL dword ptr [ECX + 0x28]

FUN_00cb5d50 @ 00cb5d50  (00cb5d50..00cb5dae)
  VCALLS_SLOT+0x28:
    00cb5d7d  vtableReg=EAX  objBaseReg=(unknown)  ins=CALL dword ptr [EAX + 0x28]

FUN_00cd6ee0 @ 00cd6ee0  (00cd6ee0..00cd7112)
  VCALLS_SLOT+0x28:
    00cd6f34  vtableReg=ESP  objBaseReg=(unknown)  ins=CALL dword ptr [ESP + 0x28]

