# BrightScript Known Issues

## Subroutine declaration incorrectly allows return type to be defined

A subroutine is defined as a function shortcut which returns type void, by either explicitly calling, “return“ or not including a return. The BrightScript subroutine **incorrectly** allows a subroutine to declare a return type allowing the subroutine to compile. A subroutine can “return” or not include a return, but if a subroutine should return a variable, we recommend declaring a function with a return type.

See [Program Statements | ProgramStatements-Function()AsType/EndFunction](../language-reference/program-statements.md) for more information about subroutines and functions. It correctly mentions that a subroutine only returns a void type (“The `Sub` statement can be used instead of `Function` as a shortcut for creating a function with return type `Void`").