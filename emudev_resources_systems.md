# System-specific Resources

Below are some useful resources for various popular systems. If you're unsure what you want to work on we recommend starting with a **CHIP-8** tutorial, of which there are many (just Google it).

After that, move to whatever system you want to. You don't need to "work your way up" to it or whatever as many seem to think. ([relevant thread](https://reddit.com/r/EmuDev/comments/8ve8lu/i_give_up_some_ramblings_of_someone_who_took_over/e1muyme/?context=3)). Just make sure you have the basics down first, remember to study the source code of existing emulators (super important) and if you get stuck, ask questions on this server or in the emudev subreddit: <https://reddit.com/r/EmuDev>.

For potentially more resources on your system, also see pinned messages in relevant system channels.

**Note:** A great introduction to any system is to read its [Architecture of Consoles](https://www.copetti.org/writings/consoles) entry, if available.

# Systems

## CHIP-8
See the HIgh-level guide if you want detailed step-by-step instructions, otherwise use the `References`.

There are no "full" tutorials for other systems, so using references will be a bit more challenging but more realistic and perhaps more helpful in the long run, assuming you'll want to move on to other systems after CHIP-8.
- **[High-level guide to making a CHIP-8 emulator](https://web.archive.org/web/20250703101753/https://tobiasvl.github.io/blog/write-a-chip-8-emulator/)**
- References:
  - **[CHIP-8 Technical Reference](https://github.com/mattmikolay/chip-8/wiki/CHIP%E2%80%908-Technical-Reference)**
  - [CHIP-8 Instruction Set](https://github.com/mattmikolay/chip-8/wiki/CHIP%E2%80%908-Instruction-Set)
  - **[CHIP-8 & Variants Opcode Table](https://chip8.gulrak.net/)**
  - **[Laurence Scotford's Chip-8/VIP Research](https://www.laurencescotford.net/tag/cosmac-vip/)**
- Test ROMs:
  - **<https://github.com/Timendus/chip8-test-suite>**
  - *More are available for various needs, ask in the relevant channel.
- Other resources:
  - [Awesome Chip-8 - A collection of links](https://github.com/tobiasvl/awesome-chip-8)
  - [Known Chip-8 variants and offshoots](https://chip-8.github.io/extensions/)
  - [VIPER magazines and more](https://github.com/trapexit/chip-8_documentation/tree/master)
  - [ROM compatibility issues](https://github.com/tomdaley92/Kiwi8/issues/9)
  - [Database of platform/rom settings](https://github.com/chip-8/chip-8-database/)
  - [Writing a CHIP-8 interpreter for the COSMAC ELF](https://cdn.discordapp.com/attachments/465586212804100106/482263592696152074/ELF_CHIP-8_Interpreter.pdf)
  - [COSMAC VIP manual](https://cdn.discordapp.com/attachments/465586212804100106/482263593753247744/VIP_Manual_Game_Manual_I.pdf)

## Bytepusher
- <https://esolangs.org/wiki/BytePusher>

## Pac-Man
- See Z80 resources
- [Pac-Man emulation guide](https://www.lomont.org/software/games/pacman/PacmanEmulation.pdf)
- [Disassembly](http://cubeman.org/arcade-source/pacman.asm)

## Space Invaders
- See 8080 resources
- [SN76477N technical data](https://web.archive.org/web/20150425030455/http://www.emutalk.net/attachment.php?attachmentid=34143&d=1160668005)
- [General info on Space Invaders](http://www.brentradio.com/SpaceInvaders.htm)
- [Space Invaders disassembly and info](https://computerarcheology.com/Arcade/SpaceInvaders)
- [CPU tests](https://altairclone.com/downloads/cpu_tests) (need a CP/M implementation or to fake it to some extent, see CP/M section and [this Discord message](https://discord.com/channels/465585922579103744/466417993912680459/735434453228191794))

## Casio PV-1000
- See Z80 resources
- [Casio PV-1000 Obscure Wiki](https://obscure.nesdev.org/wiki/Casio_PV-1000)
- [Casio PV-1000 Hardware notes](https://notes.world3.net/retro_computing/casio_pv-1000.html)
- [Casio PV-1000 Emulation notes](https://yughias.github.io/pages/pv-1000/documentation/docs.html)

## CP/M
- See 8080 resources
- [General CP/M info](https://en.m.wikipedia.org/wiki/CP/M)
- [Zero page breakdown](https://en.m.wikipedia.org/wiki/Zero_page_(CP/M))
- [CP/M BDOS system calls](https://www.seasip.info/Cpm/bdos.html)
- [CP/M Programmer's Guide](https://cdn.discordapp.com/attachments/466417993912680459/735454519701536788/cpm3-pgr.pdf)
- [CP/M-86 System Guide](https://cdn.discordapp.com/attachments/466417993912680459/735455014100926544/CPM-86_System_Guide.pdf)

## Game Boy / Game Boy Color
- [Pandocs](https://gbdev.io/pandocs)
- [The Cycle-Accurate GB Docs](https://github.com/AntonioND/giibiiadvance/blob/master/docs/TCAGBD.pdf)
- [Opcode table](https://izik1.github.io/gbops/table/table.html)
- [List of GB opcodes and their behavior](https://rednex.github.io/rgbds/gbz80.7.html)
- [GB instruction decoding table](https://cdn.discordapp.com/attachments/465586075830845475/742438340078469150/SM83_decoding.pdf)
- [Decoding GB opcodes algorithmically](https://gb-archive.github.io/salvage/decoding_gbz80_opcodes/Decoding%20Gamboy%20Z80%20Opcodes.html)
- [A journey into GB emulation](https://robertovaccari.com/blog/2020_09_26_gameboy)
- <http://www.codeslinger.co.uk/pages/projects/gameboy.html>
- [WIP tutorial on writing a GB emulator in Rust](https://rylev.github.io/DMG-01/public/book/)
- [GameBoy Emulator Development Guide](https://hacktix.github.io/GBEDG)
- Test ROMs:
  - [Blargg's test ROMs](https://github.com/retrio/gb-test-roms)
  - [Mooneye-gb test ROMs](https://github.com/Gekkio/mooneye-gb/tree/master/tests)
  - [dmg-acid (rendering test)](https://github.com/mattcurrie/dmg-acid2)
  - [cgb-acid (rendering test)](https://github.com/mattcurrie/cgb-acid2)
  - [PeterLemon's GB demos](https://github.com/PeterLemon/GB)
  - [Test ROM execution logs](https://github.com/wheremyfoodat/Gameboy-logs)
- [Bootrom disassembly](https://gist.github.com/6063288)
- [The Ultimate Game Boy Talk](https://youtu.be/HyzD8pNlpwI)
- [Other valuable resources](https://github.com/avivace/awesome-gbdev)
- [Notes by GhostSonic on GB sound emulation](https://www.reddit.com/r/EmuDev/comments/5gkwi5/gb_apu_sound_emulation/dat3zni)
- [Explanation of binary-coded decimals and the DAA instruction](https://ehaskins.com/2018-01-30%20Z80%20DAA)
- [Guide to the half-carry flag](https://robdor.com/2016/08/10/gameboy-emulator-half-carry-flag)

## Game Boy Advance
- See relevant ARM resources below (the ARM7TDMI used in the GBA implements ARMv4T)
- [GBATEK](https://problemkaputt.de/gbatek.htm)
- [no$gba](https://problemkaputt.de/gba.htm) (get the debug version)
- [TONC (GBA tutorial and demos)](https://www.coranac.com/projects/tonc)
- <https://nba-emu.github.io/hw-docs>
- [Cycle counting on the GBA](https://mgba.io/2015/06/27/cycle-counting-prefetch)
- [Decoding the ARM7TDMI Instruction Set (Game Boy Advance)](https://www.gregorygaines.com/blog/decoding-the-arm7tdmi-instruction-set-game-boy-advance/)
- Test ROMs:
  - [Various test ROMs, including an archive of TONC binaries](https://github.com/shonumi/Emu-Docs/tree/master/GameBoy%20Advance/test_roms)
  - <https://github.com/destoer/armwrestler-gba-fixed>
  - <https://github.com/DenSinH/FuzzARM>
  - <https://github.com/jsmolka/gba-suite>
  - <https://github.com/destoer/gba_tests>
  - <https://github.com/PeterLemon/GBA>
  - <https://github.com/ladystarbreeze/gba-tests/tree/master/dma-test>
  - <https://github.com/mgba-emu/suite>
  - <https://github.com/nba-emu/hw-test>
  - <https://gbadev.net/gbadoc/>
  - [Testrom Execution Logs](https://github.com/skylersaleh/GBA-Logs)
- [mGBA blog](https://mgba.io) (particularly the "development" and "emulation" tags)
- Homebrew development:
  - <https://patater.com/gbaguy/gbaasm.htm>

## Nintendo DS
- See relevant ARM resources below (the DS uses an ARM7TDMI and an ARM946E-S, implementing respectively ARMv4 and ARMv5TE)
- [GBATEK](https://problemkaputt.de/gbatek.htm)
- Datasheets:
  - [RTC (NDS/Lite)](https://www.digchip.com/datasheets/download_datasheet.php?id=836843&part-number=S-35180A-T8T1)
  - [RTC (DSi)](https://pdf1.alldatasheet.com/datasheet-pdf/view/222304/SII/S-35190A.html)
  - [Touchscreen Controller (NDS)](https://www.ti.com/lit/ds/symlink/tsc2046.pdf)
  - [Firmware Flash (NDS)](https://www.digikey.com/htmldatasheets/production/258121/0/0/1/m45pe20.pdf)
- [Other docs](https://github.com/shonumi/Emu-Docs/tree/master/Nintendo%20DS)
- Test ROMs:
  - <https://github.com/mic-/armwrestler>
    - [Built ROM](https://cdn.discordapp.com/attachments/667132407262216272/732206968252661800/armwrestler.nds)
  - <https://github.com/Arisotura/arm7wrestler>
    - [Built ROM](https://cdn.discordapp.com/attachments/667132407262216272/732206999890165780/arm7wrestler.nds)
  - <https://tcrf.net/Aging_Card_NTR>
- [Sample homebrew programs](https://github.com/devkitPro/nds-examples)
- [Arisotura's blog](https://melonds.kuribo64.net)
- [Ongoing rasterizer timing research](https://melonds.kuribo64.net/board/thread.php?pid=6560#6560)

## Nintendo 3DS
- See relevant ARM resources below (the 3DS's ARM11 MPCore implements ARMv6K, not plain ARMv6, so you'll have toat the ARMv7-AR manual too for the few additions; the ARM9 is the same as on the Nintendo DS)
- [GBATEK](https://problemkaputt.de/gbatek.htm)
- [The 3DBrew wiki](https://www.3dbrew.org/wiki/Main_Page)
- [Libctru demos](https://github.com/devkitPro/3ds-examples)
- [CRO documentation](https://gist.github.com/wwylele/325d53ee6a0f1dff6aa3473377335d93)
- [Audio tests](https://github.com/Panda3DS-emu/3ds-audio)
- [CTRPF cheat code documentation](https://gist.github.com/Nanquitas/d6c920a59c757cf7917c2bffa76de860)
- [Subv's additional findings on the kernel's threading system](https://gist.github.com/Subv/02f29bd9f1e5deb7aceea1e8f019c8f4) (meant to complement the relevant 3DBrew page)
- [Simple hommebrew userland tests](https://github.com/wheremyfoodat/Panda3DS/tree/master/tests)
- [DSP1 binary loader for Ghidra](https://github.com/SachinVin/Dsp1LoaderGhidra) (For DSP .cdc firmware files, you can dump them from hardware or Panda3DS)
- [Teak DSP Ghidra SLEIGH plugin](https://github.com/SachinVin/TeakLite-SLEIGH/tree/main)
- [Teakra](https://github.com/wwylele/teakra): Teak DSP assembly, disassembly and emulation library
- [3DS hacking guide](https://3ds.hacks.guide/)
- [Documentation of some system archives](https://github.com/B3n30/citra_system_archives) (Mii data, OS font, etc) and Python scripts for generating non-copyrighted replacements.

## Nintendo Entertainment System
- See 65xx family resources
- [6502 instruction set reference](https://www.masswerk.at/6502/6502_instruction_set.html)
- [The NesDev wiki](https://wiki.nesdev.org)
- [NES emulator development guide](https://nesdev.org/NES%20emulator%20development%20guide.txt)
- [Overview of writing a NES emulator](https://yizhang82.dev/nes-emu-overview)
- [Articles on writing a NES emulator (among other things)](https://emudev.de/nes-emulator/overview)
- [Sample ROMs](https://github.com/PeterLemon/NES)

## Super Nintendo Entertainment System
- See 65xx family resources
- [fullsnes](https://problemkaputt.de/fullsnes.htm)
- [65c816 primer](https://softpixel.com/~cwright/sianse/docs/65816NFO.HTM)
- [YouTube playlist](https://www.youtube.com/playlist?list=PLHQ0utQyFw5KCcj1ljIhExH_lvGwfn6GV)
- [Adventures in Retro Development: SNES Edition](https://mynameismjp.wordpress.com/2019/01/14/adventures-in-retro-development-snes-edition) (focuses on homebrew development environment)
- [Anomie's SNES docs](https://www.romhacking.net/?page=documents&platform=9&author=548)
- [WIP Super Mario World disassembly](https://raw.githubusercontent.com/gnaghi/SMWDisC/master/SMWDisC.txt)
- [SNES development wiki](https://wiki.superfamicom.org):
  - [65c816 CPU reference](https://wiki.superfamicom.org/65816-reference)
  - [SPC-700 APU reference](https://wiki.superfamicom.org/spc700-reference)
  - [Capcom Cx4 coprocessor docs](https://wiki.superfamicom.org/capcom-cx4-hitachi-hg51b169)
- Test ROMs:
  - <https://gitlab.com/higan/snes-test-roms>
  - <https://github.com/PeterLemon/SNES>
  - [Blargg's SPC SNES test ROMs](https://forums.nesdev.org/viewtopic.php?f=12&t=18005)
  - [More of Blargg's SNES test ROMs](https://web.archive.org/web/20150601173734/http://blargg.8bitalley.com/parodius/snes-tests)
- [SNES sprite engine design guidelines](https://megacatstudios.com/blogs/retro-development/snes-sprite-engine-design-guidelines)
- [SNES programming book](https://en.wikibooks.org/wiki/Super_NES_Programming)
  - [Super FX tutorial](https://en.wikibooks.org/wiki/Super_NES_Programming/Super_FX_tutorial)

## Nintendo Virtual Boy
- [Some homebrew ROMs](https://www.virtual-boy.com/homebrew)
- [Screen test ROM](https://www.virtual-boy.com/forums/t/virtual-boy-test-rom)
- <https://files.virtual-boy.com/download/978651/stsvb.html>
⠀
## Nintendo 64
- See MIPS resources
- <https://n64.readthedocs.io>
- <https://n64brew.dev>
- [Notes and resources](https://github.com/Dillonb/n64-resources)
- [Development resources](https://ultra64.ca/resources/documentation)
- [Info on the N64's boot code](https://www.retroreversing.com/n64bootcode)
- [Test ROMs](https://github.com/PeterLemon/N64)
- [Fork of the above test ROMs, with a few more ones](https://github.com/fraser125/N64) (significantly outdated)
- <https://github.com/lemmy-64/n64-systemtest>
- [RSP docs](https://github.com/rasky/r64emu/blob/master/doc/rsp.md)
- [Other resources](https://n64.dev)
- 64DD: <https://github.com/LuigiBlood/64dd/wiki>
- [Parallel-RDP](https://github.com/Themaister/parallel-rdp): RDP emulation plugin using Vulkan + compute shaders

## Nintendo GameCube / Nintendo Wii
- See PowerPC resources
- YAGCD: <http://hitmen.c02.at/files/yagcd/index.html> (mirror: <https://www.gc-forever.com/yagcd>)
- [GameCube resources GitHub repository](https://github.com/DenSinH/GameCubeResources)
- [Gamecube Apploader RE](https://www.gc-forever.com/wiki/index.php?title=Apploader)
- [GC/Wii games with debug symbols](https://wiki.dolphin-emu.org/index.php?title=Ships_with_Debugging_Symbols)
- [Dolphin hardware tests](https://github.com/dolphin-emu/hwtests)
- [GC/Wii games that use the Zelda DSP microcode](https://wiki.dolphin-emu.org/index.php?title=Category:Zelda_ucode_games)
- [Gekko/Broadway/Espresso Ghidra plugin](https://github.com/aldelaro5/ghidra-gekko-broadway-lang)
- [DSP HLE (Dolphin)](https://blog.lse.epita.fr/2012/12/03/emulating-the-gamecube-audio-processing-in-dolphin.html)
- [Dolwin docs](https://github.com/ogamespec/dolwin-docs)
- [Wii hacking guide](https://wii.hacks.guide/)

## Nintendo Wii U
- See PowerPC resources
- [WiiUBrew](https://wiiubrew.org/wiki/Main_Page)

## PlayStation 1
- See MIPS resources
- [Guide to writing a PSX emulator](https://github.com/simias/psx-guide)
  - [Rendered](https://cdn.discordapp.com/attachments/492036343376117778/492037613721616406/guide.PDF)
- [psx-spx (original)](https://problemkaputt.de/psx-spx.htm)
- [psx-spx (modernized and actively maintained)](https://psx-spx.consoledev.net/)
- [PSX reverse engineering project](https://github.com/ogamespec/psxdev/tree/master/reverse)
- [BIOS info](http://wiki.psxdev.ru/index.php/BIOS)
  - [Translated](https://translate.google.com/translate?sl=auto&tl=en&u=http://wiki.psxdev.ru/index.php/BIOS)
- [The PSX GPU texture pipeline and how to emulate it](https://www.reddit.com/r/EmuDev/comments/fmhtcn)
- [PSX EXE header](http://www.emulatronia.com/doctec/consolas/psx/exeheader.txt) (also see "CDROM File Formats" section in psx-spx)
- [Difficult-to-emulate games](https://github.com/stenzek/duckstation/wiki/Difficult-to-Emulate-Games)
- [Dithering on the PS1](https://www.youtube.com/watch?v=3XDyQnY5GHI)
- [PSX system software reverse engineering project](https://github.com/ogamespec/psxdev/tree/master/reverse)
- [Other PSX documentation (including a CPU reference manual)](http://hitmen.c02.at/html/psx_docs.html)
- [PSX GTE docs/reverse engineering](https://github.com/ogamespec/pops-gte)
- [PSX MDEC & CD-ROM info](https://github.com/m35/jpsxdec/blob/readme/jpsxdec/PlayStation1_STR_format.txt)
- [PlayStation emulator development info](https://drhell.web.fc2.com/ps1/index.html)
  - [Translated](https://translate.google.com/translate?sl=auto&tl=en&u=http%3A%2F%2Fdrhell.web.fc2.com%2Fps1%2Findex.html)
- [LSI LR33000 CPU (PSX's MIPS core) docs collection](https://github.com/novak36/emulation-docs/tree/main/Sony%20Playstation%201)
- Test ROMs:
  - [Amidog's tests](https://emulation.gametechwiki.com/index.php/PS1_Tests)
  - <https://github.com/PeterLemon/PSX>
  - <https://github.com/JaCzekanski/ps1-tests>
  - <https://github.com/simias/psx-hardware-tests/tree/master/tests>
  - <https://github.com/grumpycoders/pcsx-redux/tree/main/src/mips/tests>
  - [PSX demos](https://www.pouet.net/prodlist.php?order=thumbup&platform%5B0%5D=Playstation&page=1)
- Open-source BIOS: <https://github.com/grumpycoders/pcsx-redux/tree/main/src/mips/openbios>

## PlayStation 2
- See MIPS resources
- [PS2TEK](https://psi-rockin.github.io/ps2tek)
- [PS2 docs](https://web.archive.org/web/20191102085229/https://hwdocs.webs.com/ps2)
- [PS2 unofficial clang erratum](https://github.com/ZirconiumX/ps2-clang-patches/blob/master/erratum/unofficial-erratum.md)
- [GS Mode Selector](https://web.archive.org/web/20191111013442/https://psx-scene.com/forums/f291/gs-mode-selector-development-feedback-61808)
- [PS2 busses](https://web.archive.org/web/20191112223653/https://assemblergames.com/threads/the-playstation-2-busses-dev9.67961)
- [Emulating PS2 Floating-Point Numbers: IEEE 754 Differences (Part 1)](https://www.gregorygaines.com/blog/emulating-ps2-floating-point-nums-ieee-754-diffs-part-1/)

## PlayStation 3
- <https://github.com/RPCS3/rpcs3/wiki/Developer-Information>
- <https://www.psdevwiki.com/ps3>

## PlayStation 4
- [Reverse Engineering PlayStation 4](https://emulation.gametechwiki.com/index.php/PlayStation_4_emulators#Reverse_engineering_PlayStation_4)
- [Southern Islands Programming Guide](https://www.amd.com/content/dam/amd/en/documents/radeon-tech-docs/programmer-references/si_programming_guide_v2.pdf) (misc. docs including PM4 packet layout)
- [Radeon Sea Islands 3D/Compute Register Reference Guide](https://www.x.org/docs/AMD/old/CIK_3D_registers_v2.pdf)

## PlayStation Portable
- Hardware
  - <http://hitmen.c02.at/files/yapspd/psp_doc/>
  - <https://www.ppsspp.org/docs/psp-hardware/>
  -  <https://github.com/uofw/upspd/wiki>
- [PSPSDK for writing homebrew](https://pspdev.github.io/pspsdk/index.html)
- [PRXTool](https://github.com/tyranid/prxtool)
- [Texture swizzling](https://forums.ps2dev.org/viewtopic.php?t=3021)
- [VFPU reverse engineering and implementation](https://github.com/jpcsp/jpcsp/blob/master/src/jpcsp/Allegrex/VfpuState.java)
- [Opcode decoding and instruction names](https://github.com/jpcsp/jpcsp/blob/master/src/jpcsp/Allegrex/Instructions.java)
- [Unofficial Firmware, based on reverse engineering by folks from the PSP Homebrew Community](https://github.com/uofw/uofw)
- Plugins for Reverse Engineering
  - [Resolve NIDS](https://github.com/pspdev/psp-ghidra-scripts/tree/master)
  - [Allegrex Ghidra plugin](https://github.com/kotcrab/ghidra-allegrex)
- [Allegrex Opcode Table](http://hlide.free.fr/)
- [PSP Test Suite](https://github.com/hrydgard/pspautotests)

## PlayStation Vita
- VitaSDK docs: <https://docs.vitasdk.org/>
- VitaSDK Github repos with homebrew samples, a developer toolchain, and more: <https://github.com/vitasdk>
- Guide for decompiling PS Vita SELFs with Ghidra: <https://forum.devchroma.nl/index.php?topic=88.0>

## PC Engine (TurboGrafx-16)
- [HuC6280 Opcode Matrix](https://www.chrismcovell.com/PCEdev/HuC6280_opcodes.html)
- [HuC6280 Opcode Documentation](http://shu.emuunlim.com/download/pcedocs/pce_cpu.html)
- [Huc6280 Assembly Guide](https://www.chibiakumas.com/6502/pcengine.php)
- [PC Engine Developer Docs](https://archive.org/details/PCEDev/Hu7%20CD%20System%20-%20BIOS%20Manual/)
- [PC Engine Tech Docs](https://raw.githubusercontent.com/asterick/TurboSharp/refs/heads/master/Text/pcetech.txt)
- [VDC Programmers Reference](https://datacrystal.tcrf.net/wiki/VDC_Programmers_Reference_(Turbo-Grafx_16))
- [VDC Documentation](https://raw.githubusercontent.com/franckverrot/EmulationResources/refs/heads/master/consoles/pc-engine/vdcdox.txt)
- [VDC Useful Timings](https://pcengine.proboards.com/post/7633/thread)
- [MagicKit Docs of Hardware Registers](http://www.magicengine.com/mkit/)

## Sega Game Gear
- [VDP test ROM](https://www.retrorgb.com/game-gear-vdp-test-software.html)
- [Button test ROM](https://github.com/GameGearSamples/ButtonTest)
- [Krom's demos](https://github.com/PeterLemon/GG)

## Sega Master System
- See Z80 resources
- [SMS info](https://www.smspower.org/Development)
  - [BIOS documentation](https://www.smspower.org/Development/BIOSes)
  - [Memory map](https://www.smspower.org/Development/MemoryMap)
  - [Z80 info](https://www.smspower.org/Development/Z80-Index)
  - [Video Hardware](https://www.smspower.org/Development/VDPRegisters)
  - [Sound Hardware](https://www.smspower.org/Development/SN76489)
- <http://www.codeslinger.co.uk/pages/projects/mastersystem.html>
- Test ROMs:
  - [Homebrew test cases](https://www.smspower.org/Homebrew/NotOnlyWords-SMS)
  - [ZEXALL test ROM](https://www.smspower.org/Homebrew/ZEXALL-SMS) (doesn't require any hardware, it can log to an IO port)
  - [PeterLemon's SMS demos](https://github.com/PeterLemon/SMS)
  - [VDP test ROM](https://www.smspower.org/Homebrew/SMSVDPTest-SMS)
  - [WIP test suite](https://github.com/sverx/SMSTestSuite)

## Sega Genesis / Mega Drive
- See Z80 and m68k resources
- [Collection of docs](https://segaretro.org/Mega_Drive_official_documentation)
- <http://gendev.spritesmind.net/forum/viewtopic.php?f=2&t=2227>
- [CPU test ROM](https://github.com/flamewing/68k-bcd-verifier)
- [VDP test ROM](http://gendev.spritesmind.net/forum/viewtopic.php?f=8&t=1585)
- [Development tools list](http://techdocs.exodusemulator.com/Console/SegaMegaDrive/Software.html)

## Sega Saturn
- [SH-2 programming manual](https://antime.kapsi.fi/sega/files/h12p0.pdf)
  - [Instruction set summary/table](https://shared-ptr.com/sh_insns.html)
- [Yabause wiki](https://wiki.yabause.org/) (check the Sega Saturn Specifications section)
- [Collection of docs](https://segaretro.org/Saturn_official_documentation)
  - [The main page](https://segaretro.org/Sega_Saturn) has tons of details on the hardware, games, history, etc.
  - [More complete collection](https://techdocs.exodusemulator.com/Console/SegaSaturn/Documentation.html)
  - [sattech](https://web.archive.org/web/20140318183509/http://cgfm2.emuviews.com/txt/sattech.txt)
- [Signal traces of various chips](https://github.com/srg320/Saturn_hw)
  - [Partial CDBlock ROM decompilation](https://github.com/srg320/Saturn_hw/tree/main/CDB)
- [GAM1 test ROM, harnessing most hardware](https://segaxtreme.net/threads/sega-saturn-sample-by-sega.24264)
- Misc homebrew:
  - <http://www.rockin-b.de/saturn.html>
  - <https://reddit.com/r/SegaSaturn/comments/223cdp/best_saturn_homebrews_available_atm>
  - [SegaXtreme forum](https://segaxtreme.net/forums/saturn-dev.34/)
    - Keep an eye on the *SEGA Saturn Nth Anniversary Game Competition* threads, there's often a ton of fantastic homebrew there
- [libyaul](https://github.com/yaul-org/libyaul) (for homebrew development)
  - [Examples](https://github.com/yaul-org/libyaul-examples)
  - [Docker image](https://github.com/yaul-org/libyaul-docker)
  - Works well on WSL too
- [240p test suite](https://github.com/ArtemioUrbina/240pTestSuite)
  - [Saturn version](https://github.com/ArtemioUrbina/240pTestSuite/tree/master/240psuite/Saturn/240pTestSuite)
  - [Precompiled image](https://segaxtreme.net/attachments/240p-7z.9354/)
- CD-ROM and image formats
  - [ECMA-130 spec](https://ecma-international.org/wp-content/uploads/ECMA-130_2nd_edition_june_1996.pdf)
  - [Raw optical disc format](https://github.com/libyal/libodraw/blob/main/documentation/Optical%20disc%20RAW%20format.asciidoc)
  - [Cue sheet format](https://problemkaputt.de/psxspx-cdrom-disk-images-cue-bin-cdt-cdrwin.htm), [2](https://github.com/libyal/libodraw/blob/main/documentation/CUE%20sheet%20format.asciidoc)
  - [CCD/IMG/SUB formats](https://problemkaputt.de/psxspx-cdrom-disk-images-ccd-img-sub-clonecd.htm)
  - [MDS/MDF formats](https://problemkaputt.de/psxspx-cdrom-disk-images-mds-mdf-alcohol-120.htm), [2](https://github.com/sizious/img4dc/blob/master/mds4dc/doc/mdf_mds.txt), [3](https://git.libretro.com/libretro/play/-/blob/red_faction_2/Source/discimages/MdsDiscImage.cpp?ref_type=heads)
  - ISO is just a BIN with either 2048 or 2352 byte sectors; check if the file is divisible by one of these sizes and build a single data track with the whole file's contents

## Sega Dreamcast
- [System Architecture Manual](https://segaretro.org/images/7/78/DreamcastDevBoxSystemArchitecture.pdf)
- [SH4 Processor Manual](https://raw.githubusercontent.com/Kochise/dreamcast-docs/master/CPU/DOCS/h14th002d2.pdf)
- [ARM7DI Processor Manual](https://developer.arm.com/documentation/ddi0027/latest/)


## Atari 8-bit Computers
- [Altirra Hardware Reference Manual](https://www.virtualdub.org/downloads/Altirra%20Hardware%20Reference%20Manual.pdf)

## Commodore 64
- See 6502 resources in the [65xx family section](#65xx-family) (the C64 uses a 6510)
- [MCS6500 family programming manual](http://archive.6502.org/books/mcs6500_family_programming_manual.pdf) (doesn't respond to https://)
- Summary of single-cycle execution with the [6502 addressing modes](https://xotmatrix.github.io/6502/6502-single-cycle-execution.html)
- [C64 wiki](https://www.c64-wiki.com)
- [VICE test ROMs](https://vice-emu.pokefinder.org/index.php/Testbench)
- [SID manual](http://archive.6502.org/datasheets/mos_6581_sid.pdf) (doesn't respond to https://)
- [C64 assembly language programming](https://www.retro-programming.de)
  - [Translated](https://translate.google.com/translate?sl=auto&tl=en&u=https%3A%2F%2Fwww.retro-programming.de)
- [Scanline missing cycles](http://www.antimon.org/dl/c64/code/missing.txt)
- [Opening the borders](http://www.antimon.org/dl/c64/code/opening.txt)
- [Info on the VIC-II](http://www.zimmers.net/cbmpics/cbm/c64/vic-ii.txt)
- [SID info](http://www.oxyron.de/html/registers_sid.html) (doesn't respond to https://)
- Programming the C64's SID:
  - [Part 1](https://www.atarimagazines.com/compute/issue49/424_1_Programming_64_Sound.php)
  - [Part 2](https://www.atarimagazines.com/compute/issue50/277_1_Programming_64_Sound.php)
- [6502 decimal mode](https://www.atarimagazines.com/compute/issue50/268_1_MACHINE_LANGUAGE.php)
- [The Commodore 64 Music Book](https://archive.org/details/The_Commodore_64_Music_Book)
- [C64 user's guide (start of sound chapter)](https://archive.org/details/Commodore_64_Users_Guide_1984_Commodore/page/n87)

## Mac
- See Motorola 68K / PowerPC resources
- [Apple's guide to the macintosh family hardware](https://archive.org/details/apple-guide-macintosh-family-hardware) (400 MB pdf)
- [Inside Macintosh Volume III](https://vintageapple.org/inside_o/pdf/Inside_Macintosh_Volume_III_1985.pdf)
- [Macintosh error codes](https://discussions.apple.com/thread/1883152?sortBy=best)

## MSX
- See Z80 resources
- [Test ROMs](https://github.com/PeterLemon/MSX)

## ZX Spectrum
- <https://spectrumforeveryone.com/technical>
- <https://worldofspectrum.org/faq/resources/documents.htm>
- [Krom's demos](https://github.com/PeterLemon/ZXSpectrum)
- <https://github.com/redcode/ZXSpectrum/wiki/Tests>

## Amiga
- [Info on the Amiga and "Another World"](https://fabiensanglard.net/another_world_polygons_amiga500/index.html)

## Xbox
- [Xbox architecture](https://www.copetti.org/projects/consoles/xbox)

## Neo Geo
- [Development wiki](https://wiki.neogeodev.org/index.php?title=Main_Page) (has overviews of every piece of hardware)
- [Sample ROMs](https://github.com/PeterLemon/NEO-GEO)

## Neo Geo Pocket (Color)
- [Toshiba TLCS-900/H CPU Manual](https://toshiba.semicon-storage.com/info/catalog_en_20010831_ALT00146.pdf?did=7768)
- [TMP95CS64F Manual](https://datasheetspdf.com/pdf-file/1217217/Toshiba/TMP95CS64F/1) (thought to be the microcontroller the NGPC is based around)
- [NGPC Memory Map/Technical Reference](https://github.com/OpenEmu/NeoPop-Core/blob/master/Core/docs/Memory%20Map.txt)
  - Older similar documents:
  - <http://neopocott.emuunlim.com/docs/tech-11.txt>
  - <http://devrs.com/ngp/files/ngpctech.txt>
- [Archive of More Resources](https://archive.org/details/neopop_source)
- [Homebrew Development Kit](http://sebastianmihai.com/neogeo-pocket-ngcollector.html)
- [More Homebrew](https://thor.pdroms.de/#ngpcdev)

## V.Smile
- <https://vtech.pulkomandy.tk/>

## Pokémon Mini
- <https://www.pokemon-mini.net/documentation>

## Tamagotchi
- [Tech specs and resources](https://tama.loociano.com)
- [ROM dump and reverse engineering](https://hackaday.com/2013/05/24/tamagotchi-rom-dump-and-reverse-engineering)
  - [Archive of linked article](https://web.archive.org/web/20180831183942/https://www.kwartzlab.ca/2013/05/first-glimpse-soul-tamagotchi)
  - [ROM dump GitHub repository](https://github.com/natashenka/Tamagotchi-Hack/tree/master/codedump)

## Multiple systems
- <https://www.zophar.net/documents.html>
- <http://www.emulator101.com>
- <http://hitmen.c02.at/index.html>
- <http://www.codeslinger.co.uk> (doesn't respond to https://, disable extensions such as HTTPS Everywhere if it doesn't load)
- <https://emudev.de>
- Shonumi's blog: <https://shonumi.github.io>
- Shell-storm multi-architecture assembler and disassembler: <http://shell-storm.org/online/Online-Assembler-and-Disassembler>
- 8bitworkshop IDE: <https://8bitworkshop.com/redir.html>
- A list of helpful patents for various systems, include Gamecube, Wii, N64 and more: <https://gist.github.com/sylvieee-iot/5636d376302569833b0787abc62b7758>
- 240p test suite, supporting multiple systems: <https://sourceforge.net/projects/testsuite240p/files/Sega_Genesis-MegaDrive-SegaCD_MegaCD>

# Processors and architectures

## 65xx family
- <https://www.westerndesigncenter.com/wdc/documentation/w65c816s.pdf>
- [Programming manual](https://www.nesdev.org/w/images/default/7/76/Programmanual.pdf)
- [6502 decimal mode](https://www.atarimagazines.com/compute/issue50/268_1_MACHINE_LANGUAGE.php)

## 8080
- [8080 tutorial (among other things)](http://www.emulator101.com)
- [Assembly programming manual](https://altairclone.com/downloads/manuals/8080%20Programmers%20Manual.pdf)
- [Datasheet](https://altairclone.com/downloads/manuals/8080%20Data%20Sheet.pdf)
- [Instruction table](https://tobiasvl.github.io/optable/intel-8080/classic)
- [Loading test ROMs that require a CP/M implementation/stub](https://discord.com/channels/465585922579103744/466417993912680459/735434453228191794)

## Z80
- [Z80 CPU User Manual](https://www.zilog.com/force_download.php?filepath=YUhSMGNEb3ZMM2QzZHk1NmFXeHZaeTVqYjIwdlpHOWpjeTk2T0RBdlZVMHdNRGd3TG5Ca1pnPT0=)
- [Z80 heaven](http://z80-heaven.wikidot.com)
- [Z80 instruction table](http://clrhome.org/table)
- [The undocumented Z80 documented](http://www.z80.info/zip/z80-documented.pdf)
- [Z80 undocumented behavior](https://baltazarstudios.com/zilog-z80-undocumented-behavior)
- [Z80 undocumented instructions](http://www.z80.info/z80undoc.htm)
- [Z80 test ROMs](https://github.com/superzazu/z80/tree/master/roms)
- [Loading test ROMs that require a CP/M implementation/stub](https://discord.com/channels/465585922579103744/466417993912680459/735434453228191794)
- <https://github.com/redcode/Z80/wiki/Technical-literature>
- <https://github.com/redcode/Z80/wiki/Tests>

## Misc
- [Single Step Tests](https://github.com/SingleStepTests): Instruction tests for various CPUs in JSON format, mostly generated from emulators

## Motorola 68k
- [Instruction set reference](http://wpage.unina.it/rcanonic/didattica/ce1/docs/68000.pdf) (just a summary for each instruction, doesn't respond to https://)
- [Programmer's reference manual](https://www.nxp.com/docs/en/reference-manual/M68000PRM.pdf)
- [Instruction overview](http://goldencrystal.free.fr/M68kOpcodes.pdf)
- [Prefetch information](http://pasti.fxatari.com/68kdocs/68kPrefetch.html)

## PowerPC
- [IBM's PowerPC Architecture Book](https://www.ibm.com/developerworks/systems/library/es-archguide-v2.html)
- [PowerPC 750CL manual](https://github.com/wheremyfoodat/Panda3DS/blob/cdn/docs/ppc_750cl.pdf) (Mostly similar to the GC/Wii/Wii U CPUs)
- [VMX128-type opcodes found on the Xbox 360 processor](http://biallas.net/doc/vmx128/vmx128.txt)

## ARM
- [ARM instruction set info for the ARM7TDMI-S](https://vision.gel.ulaval.ca/~jflalonde/cours/1001/h17/docs/arm-instructionset.pdf) (not the full document, which apparently can't be found anymore)
- [ARM7TDMI datasheet](https://www.dwedit.org/files/ARM7TDMI.pdf) (contains info about ARM and thumb instruction sets)
- [ARM7TDMI Technical Reference Manual](https://documentation-service.arm.com/static/5f4786a179ff4c392c0ff819)
- [ARM7TDMI-S Technical Reference Manual](https://documentation-service.arm.com/static/5e8e13a9fd977155116a3368) (doesn't contain instruction descriptions, but has info on timing)
- [ARMv5TE Reference Manual](https://web.archive.org/web/20231212000012/https://cdn.discordapp.com/attachments/667132407262216272/733255145495986246/ARMv5TE_reference_manual.pdf) (contains a few corrections to the original documents)
- [ARM9E-S Technical Reference Manual](https://documentation-service.arm.com/static/5e8e2f18fd977155116a77fb) (contains info on timing that applies to all ARM9\*E-S processors)
- [ARM946E-S Technical Reference Manual](https://documentation-service.arm.com/static/5f032835cafe527e86f5b8ad)
- [ARMv6 Reference Manual](https://www.scs.stanford.edu/~zyedidia/docs/arm/armv6.pdf)
- [ARMv7-A/R Reference Manual](https://documentation-service.arm.com/static/5f1074ce0daa596235e834b5)
- [ARM11 MPCore Technical Reference Manual](https://documentation-service.arm.com/static/5e8e1e0388295d1e18d368b2)

## ARM64
- [ARMv8 and ARMv9 A-Profile Architecture manual](https://developer.arm.com/documentation/ddi0487/latest/)
- [ARM64 cheatsheet](https://github.com/wheremyfoodat/Panda3DS/blob/cdn/docs/arm64_cheat_sheet.pdf)
- [NEON intrinsic reference](https://arm-software.github.io/acle/neon_intrinsics/advsimd.html)

## x86
- [8086 family user's manual](https://edge.edx.org/c4x/BITSPilani/EEE231/asset/8086_family_Users_Manual_1_.pdf)
- [Intel® 64 and IA-32 manuals](https://software.intel.com/content/www/us/en/develop/articles/intel-sdm.html)
- [8088 CPU Tests](https://github.com/SingleStepTests/8088)
- [8086 CPU Tests](https://github.com/SingleStepTests/8086)
- [NEC V20 CPU Tests](https://github.com/SingleStepTests/v20)
- [80286 CPU Tests](https://github.com/SingleStepTests/80286)
- [80386 CPU Tests](https://github.com/SingleStepTests/80386)
- [80386 Test ROM](https://github.com/barotto/test386.asm)
- [Felix Cloutier's x86 and AMD64 instruction reference](https://www.felixcloutier.com/x86)
- [Agner Fog's software optimization resources](https://www.agner.org/optimize)
- [x86 Intrinsics](https://software.intel.com/sites/landingpage/IntrinsicsGuide)
- [Sandpile](https://sandpile.org)
- [Opcode and Instruction Reference](http://ref.x86asm.net/coder.html)
- [x86-64 opcode table](http://ref.x86asm.net/coder64.html)
- [OSDev wiki encoding page](https://wiki.osdev.org/X86-64_Instruction_Encoding)

## MIPS
- [MIPS64 Instruction Set Reference Manual](https://s3-eu-west-1.amazonaws.com/downloads-mips/documents/MD00087-2B-MIPS64BIS-AFP-6.06.pdf)
- [IDT R30xx Family Software Reference Manual](https://cgi.cse.unsw.edu.au/~cs3231/doc/R3000.pdf) (PS1 CPU, PS2 IOP)
- [VR43xx CPU manual](http://datasheets.chipdb.org/NEC/Vr-Series/Vr43xx/U10504EJ7V0UMJ1.pdf) (Nintendo 64)

## Itanium
- [Itanium Architecture Software Developer's Manual](https://cdn.discordapp.com/attachments/698838582181363752/805813408309837904/itanium-architecture-vol-1-2-3-4-reference-set-manual.pdf) ([original](https://www.intel.com/content/dam/doc/manual/itanium-architecture-vol-1-2-3-4-reference-set-manual.pdf))
- [Itanium System Abstraction Layer Specification](https://cdn.discordapp.com/attachments/698838582181363752/805813867694653500/itanium-system-abstraction-layer-specification.pdf) ([original](https://www.intel.com/content/dam/www/public/us/en/documents/specification-updates/itanium-system-abstraction-layer-specification.pdf))
- [460GX Chipset Developer's Manual](https://cdn.discordapp.com/attachments/698838582181363752/805814367097716766/460gx.pdf) ([original](https://www.manualslib.com/manual/77665/Intel-460gx.html))
- [Intel® E8870IO Server I/O Hub Datasheet](https://cdn.discordapp.com/attachments/698838582181363752/805814970977747015/e8870io-server-io-hub-datasheet.pdf) ([original](https://www.intel.com/content/dam/doc/datasheet/e8870io-server-io-hub-datasheet.pdf))
- [Intel® E8870 SNC Datasheet](https://cdn.discordapp.com/attachments/698838582181363752/805815757861945344/e8870-snc-datasheet.pdf) ([original](https://pccomponents.com/datasheets/INTEL-251112.PDF))

**Contributing**

Have something to add to this list? Submit a pull request [here](https://github.com/emudev-org/discord-resources/blob/main/emudev_resources_systems.md).

**Note: If you're new here, scroll up to the top!**
