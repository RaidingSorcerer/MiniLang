# MiniLang - Phase 1

![Work in Progress](https://img.shields.io/badge/status-WIP-orange)

MiniLang is a simple Python interpreter that allows you to create and manipulate **INT** and **STR** variables. This is **Phase 1** of the project; more features are planned.

---

## Status

✅ Phase 1 complete: Basic interpreter working  
🚧 Phase 2 upcoming: Multi-word strings, file input/output, extra commands

---

## Features (Phase 1)

- Create variables with `SET` (INT or STR)
- Add values to variables with `ADD`
- Display variable values with `PRINT`
- Show all variables with `SHOW`
- Exit the interpreter with `EXIT`

---

## Commands

| Command | Syntax                                | Description                               |
| ------- | ------------------------------------- | ----------------------------------------- |
| SET     | `SET INT x 10` / `SET STR name Alice` | Creates a variable                        |
| ADD     | `ADD x 5` / `ADD name Bob`            | Adds value to existing variable           |
| PRINT   | `PRINT x`                             | Shows value and type of a variable        |
| SHOW    | `SHOW`                                | Lists all variables with values and types |
| EXIT    | `EXIT`                                | Quits the interpreter                     |

---

## Example Session

SET INT x 10
SET STR name Alice
ADD x 5
PRINT x
15 (INT)
ADD name Bob
SHOW
name=AliceBob (STR)
x=15 (INT)
EXIT
Exiting MiniLang...

---

## How to Run

```bash
python minilang.py
```
