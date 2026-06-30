# 4-scripting

This repository contains two simple scripts that take a user's name as a command-line argument and print a greeting along with the current date and time.

## Files

* `hello.sh` - Bash script
* `hello.py` - Python script

## Running the Bash Script

### About Bash

Bash is an **interpreted scripting language**. It is executed by the Bash interpreter and is not compiled before running.

### Make the Script Executable

```bash
chmod +x hello.sh
```

### Execute the Script

```bash
./hello.sh YourName
```

Or:

```bash
bash hello.sh YourName
```

## Running the Python Script

### About Python

Python is an **interpreted programming language**. Python code is executed by the Python interpreter.

### Execute the Script

```bash
python3 hello.py YourName
```

## Example Output

```text
Hello YourName, right now the time is Mon Jun 30 20:15:42 IST 2026
```
