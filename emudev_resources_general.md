__**General Resources**__

- **Overview of emulation development: <https://stackoverflow.com/a/448689>**
- **Architecture overview of various consoles: <https://copetti.org/projects/consoles>**
- An introduction: <http://emulator101.com>
- Docs for various systems: <https://github.com/shonumi/Emu-Docs> (combine with resources below)
- Emulation blogs: <https://dolphin-emu.org/blog>, <https://byuu.net>, <http://emudev.de>, <http://www.noxa.org/blog/category/coding/emulation/>, <http://melonds.kuribo64.net/>, <https://pcsx2.net/developer-blog.html>, <https://shonumi.github.io/articles.html>, etc
- Subreddit: <https://www.reddit.com/r/EmuDev>
- Building a computer from scratch: <https://www.nand2tetris.org>
- Books (not necessary): 
    - <http://www.noxa.org/blog/2011/08/21/emulation-books>
    - <http://www.codeslinger.co.uk/files/emu.pdf>
- Write & run 8-bit code in the browser: <https://8bitworkshop.com>
- Our website: <https://emudev.org/> (in construction)

Most people start with a CHIP-8 emulator. As with any system, see <#482208284032499713> to get started.
*Note*: A great guide that still keeps it challenging is <https://tobiasvl.github.io/blog/write-a-chip-8-emulator/>.

After that, you can pretty much move to whatever system you want to. You don't _have_ to "work your way up" to it as many seem to think (relevant opinionated thread here: <https://goo.gl/CAvrd4>).
Just make sure you have the basics down first, study the source code of existing emulators (super important) and if you get stuck, ask questions here or in the subreddit.
If you contribute to a project that has its own community/resources, you should probably prioritize that.

**Explanations for some terms you might come across:**
(for more info, look at source code of existing emulators, or ask others)

**HLE vs LLE** (High Level Emulation vs Low Level Emulation)
- <https://alexaltea.github.io/blog/posts/2018-04-18-lle-vs-hle>
- <http://emulation.gametechwiki.com/index.php/High/Low_level_emulation>

**CPU emulation, cached interpeters, dynarecs/JITs and AOTs** (Just-In-Time and Ahead-of-Time compilers)
- Code Translation Techniques: <http://www.noxa.org/blog/2011/08/21/building-an-xbox-360-emulator-part-6-code-translation-techniques/>
- Writing a Cached Interpreter: <https://emudev.org/2021/01/31/cached-interpreter.html>
- Faster interpreters: <http://www.emulators.com/docs/nx25_nostradamus.htm>
- Computed goto: https://eli.thegreenplace.net/2012/07/12/computed-goto-for-efficient-dispatch-tables
**JIT/AOT:**
- Wikipedia: <https://www.wikiwand.com/en/Just-in-time_compilation>  (just for an overview of what it is)
- <https://github.com/spencertipping/jit-tutorial>
- <http://blog.reverberate.org/2012/12/hello-jit-world-joy-of-simple-jits.html>
- <https://emudev.org/docs/1964-recompiling-engine-documentation.pdf>
- <https://bheisler.github.io/post/experiments-in-nes-jit-compilation>
- <https://andrewkelley.me/post/jamulator.html> (**AOT**. most other links here are about **JIT**ing)
- <https://www.davidsharp.com/tarmac/> (see pdf at the end)

**fastmem** (Fast memory accesses using host MMU)
- <https://wheremyfoodat.github.io/software-fastmem>
- <https://dolphin-emu.org/blog/2016/09/06/booting-the-final-gc-game> (mentioned in "Theory 3")
- Faster interpreters: <https://www.alchemistowl.org/pocorgtfo/pocorgtfo06.pdf> (Section 3.4)
- <http://man7.org/linux/man-pages/man2/mprotect.2.html> (Unix API)
- <https://docs.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-virtualprotect> (Windows API)

**Software Rasterization** (for emulating 3D systems)
- <https://fgiesen.wordpress.com/2013/02/17/optimizing-sw-occlusion-culling-index>

**Audio**
- <https://nicolasallemand.com/2019/12/12/let-there-be-sound>
- <https://redream.io/posts/improving-audio-video-synchronization-multi-sync>

**FPGAs**
- <https://zipcpu.com>
- <https://www.walknsqualk.com/post/014-tiny-fpga-bx>

**Integrated Circuits**
- <https://www.icreversing.com/chips> (IC library)

---

**Reverse Engineering**
- In emulation, RE-ing is often needed for system BIOSes, operating systems, drivers, OS modules and games to aid in understanding of what the hardware does & emulate it properly when the documentation is insufficient or incomplete (ie. always).
- Huge topic & and it depends on what you want to do, but as a general resource I've heard good things about <https://beginners.re> (older but free mirror: <https://mirrors.ocf.berkeley.edu/parrot/misc/openbooks/programming/ReverseEngineeringForBeginners.en.pdf>)
- These videos from LiveOverflow & stacksmashing are a fun introduction to some fundamental concepts: <https://www.youtube.com/playlist?list=PLniOzp3l9V82onKsktyyKlIenAAUj45Mk>
- There are _way_ too many resources about this. It's a skill used in many disciplines. Look around, find what you like (otherwise you might not be motivated for long).

- For **static analysis**, the industry standard tool is **Ghidra <https://ghidra-sre.org/>**. There are loaders/extensions for pretty much all consoles/processors, search for them.
    - *Sidenote*: An alternative and also industry-standard tool (more on the enterprise side) is IDA Pro/HexRays <https://www.hex-rays.com/ida-pro>. I don't personally recommend it, Ghidra is better in a lot of things. Also if you want to get it legally, it costs multiple thousands of dollars vs. Ghidra being free & open source.

- For **dynamic analysis**, the standard tool that's cross-platform and supports many architectures is **gdb**.
    - Many emulators implement "gdbstub"s that allow them to use a gdb client to debug guest code just like you would debug something running on the host. Meaning, you would be able to place breakpoints, step, etc via any gdb interface (ie. gdbgui), on GameBoy code or whatever you're emulating.
        - IDA Pro has debugging support that works with gdbstubs.
        - <https://gef.readthedocs.io>
        - <https://www.gdbgui.com>
    - Other projects choose to make their own integrated debuggers with (ie. <https://github.com/ocornut/imgui>). This is perhaps more work, but more flexible (and many people don't like gdb).
    - For x86, the industry standard tool is <https://github.com/x64dbg/x64dbg>.
    - Frida: <https://frida.re>
    - <http://reddit.com/r/ReverseEngineering> and <http://reddit.com/r/REGames>

**Contributing**

Have something to add to this list? Submit a pull request [Here](https://github.com/emudev-org/discord-resources/blob/main/emudev_resources_general.md)


**Note: If you're new here, scroll up to the top!**