# WinREPL
WinREPL is a "read-eval-print loop" shell on Windows that is useful for testing/learning x86 and x64 assembly.

Pre-compiled binaries are available at: https://github.com/zerosum0x0/WinREPL/releases/

![WinREPL](/screenshot.png?raw=true "WinREPL")

zerosum0x0/WinREPL is similar to yrp604/rappel (Linux) and Tyilo/asm_repl (Mac), but with a slightly different methodology that should allow for tricks such as self-modifying shellcode crypting/encoding. There is also enferex/asrepl for a Unicorn (emulated) version, but WinREPL is completely native inside a Windows process context.

### Methodology
WinREPL is a debugger (parent process) that hollows out a copy of itself (child process).

1. Parent process retrieves input from the user
2. Machine code is generated with the ASMTK library
3. Resulting bytes are written to a child process thread context
4. Child process thread is resumed
5. Parent process polls for debug events

### Commands
Multiple assembly mnemonics can be executed on a single line by separating with semi-colons. Refer to ASMTK documentation for  other syntactic sugar.

Besides being a raw assembler, there are a few extra commands.

```
.help                   Show this help screen.
.registers              Show more detailed register info.
.read addr size         Read from a memory address.
.write addr hexdata     Write to a memory address.
.allocate size          Allocate a memory buffer.
.loadlibrary path       Load a DLL into the process.
.kernel32 func          Get address of a kernel32 export.
.shellcode hexdata      Execute raw shellcode.
.peb                    Loads PEB into accumulator.
.reset                  Start a new environment.
.quit                   Exit the program.
```

The following commands are not yet implemented but on the Todo list:

```
.dep addr size [0/1]    Enable or disable NX-bit.
.stack                  Dump current stack memory contents.
.string data            Push a string onto the stack.
.errno                  Get last error code in child process.
```

Create a GitHub issue to request other commands.

### Other Todo
As always happens, code is rushed and awful.

1. Clean up the hodge-podge of C and C++... just make it all C++
2. Look into label support
3. Better error handling for debug events
4. Better command mappings
5. Support for AT&T syntax
6. Support for ARM architecture
7. Perhaps integration with Unicorn for obscure architectures?
8. Print useful error messages for debug exceptions like access violations

### Building
As I don't want to go to prison, the provided binaries (./bin/winrepl_x86.exe and ./bin/winrepl_x64.exe) are not backdoored. That said, this program works via sorcery that is probably suspicious to antivirus.

You should be able to just initialize the git submodules and build with Visual Studio.

### License
ZLIB, a super permissive license. Thanks @mrexodia
