# FSManager (File System Manager)

**File System Manager** is a Python script for managing file system operations such as creating directories, moving files and directories, and removing files and directories.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)

## Installation

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/fsm.git
cd fsm
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

## Usage

1. **Edit the script**: Modify `run_fsm.py` to specify the source and destination paths for your file operations.
2. **Run the script**:
```bash
python run_fsm.py
```

## Examples

**Creating a Directory**:
```python
mkdir('/path/to/new_directory')
```

**Moving a File**:
```python
mv('/path/to/source/file.txt', '/path/to/destination/file.txt')
```

**Moving a Directory**:
```python
mvdir('/path/to/source_directory', '/path/to/destination_directory')
```

**Removing a File**:
```python
rm('/path/to/file.txt')
```

**Removing a Directory**:
```python
rmdir('/path/to/directory')
```

## License

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
