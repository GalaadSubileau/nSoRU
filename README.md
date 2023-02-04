# nSoRU

Author: GalaadSubileau

**nSoRU:** an n-th useless copy of Brainfuck

Only tool provided: translator.py, translates nSoRU files to Brainfuck code.

"Features" of the language:
 - Supports comments ("#")
 - Supports tabs
 
|nSoRU  |Brainfuck  |Meaning|
|---    |---        |---|
|`roses`  |`>`        |Increment the data pointer to point to the next cell to the right.|
|`are`    |`<`        |Decrement the data pointer (to point to the next cell to the left).|
|`red`    |`+`        |Increment (increase by one) the byte at the data pointer.|
|`violets`|`-`        |Decrement (decrease by one) the byte at the data pointer.|
|`blue`   |`.`        |Output the byte at the data pointer.|
|`sugar`  |`,`        |Accept one byte of input, storing its value in the byte at the data pointer.|
|`is`     |`[`        |If the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it *forward* to the command after the *matching* `]` command.|
|`sweet`  |`]`        |If the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it *back* to the command after the *matching* `[` command.|

Commands must be seperated by spaces.
