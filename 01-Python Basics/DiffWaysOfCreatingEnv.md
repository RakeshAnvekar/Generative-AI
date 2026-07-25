# Why Create Separate Virtual Environments?

A virtual environment is an isolated Python environment that allows each project to have its own Python packages and dependencies.

It is considered a **best practice** to create a separate virtual environment for every project because different projects may require different versions of Python libraries and packages.

---

## Method 1: Using Python's Built-in `venv` (Recommended)

Python provides a built-in module called `venv` for creating virtual environments.

### Create a Virtual Environment

```bash
python -m venv myenv
```

### Activate the Environment

**Windows**

```bash
myenv\Scripts\activate
```

**macOS/Linux**

```bash
source myenv/bin/activate
```

> **Note:** When you create a virtual environment using `venv`, it uses the same Python version that is currently installed on your system.

For example, if your system has **Python 3.12.6**, the virtual environment will also use **Python 3.12.6**.

To verify the Python version:

```bash
python --version
```

---

## Method 2: Using `virtualenv`

The `virtualenv` package offers additional features and allows you to create environments using a specific Python interpreter.

### Install

```bash
pip install virtualenv
```

### Create an Environment

```bash
virtualenv virtual_env
```

### Create an Environment with a Specific Python Version

```bash
virtualenv -p python3.12 virtual_env
```

or on Windows

```bash
virtualenv -p C:\Python312\python.exe virtual_env
```

### Activate

```bash
virtual_env\Scripts\activate
```

---

## Method 3: Using Conda

If you're using **Anaconda** or **Miniconda**, you can create environments using Conda.

### Create an Environment

```bash
conda create -n myenv python=3.12
```

or create it inside the project folder

```bash
conda create -p venv python=3.12
```

### Activate

```bash
conda activate myenv
```

or

```bash
conda activate ./venv
```

---

# Benefits of Using Separate Virtual Environments

- Prevents dependency conflicts between projects.
- Allows each project to use different versions of the same package.
- Makes projects easier to maintain and reproduce.
- Keeps the global Python installation clean.
- Makes it easier to share the project using a `requirements.txt` file.
- Reduces the risk of accidentally breaking another project by upgrading or removing packages.

---

# Example

## Project A

```text
Python      : 3.12
FastAPI     : 0.115
LangChain   : 0.3
OpenAI      : 1.97
```

## Project B

```text
Python      : 3.10
Django      : 5.2
NumPy       : 2.0
Pandas      : 2.2
```

If both projects shared the same environment, package version conflicts could occur.

By creating a separate virtual environment for each project, each project's dependencies remain isolated and independent.

---

# Best Practice

✅ Create a new virtual environment for every project.

✅ Store all project dependencies in a `requirements.txt` file.

✅ Never commit your virtual environment (`venv/`) to Git. Instead, add it to your `.gitignore` file.

This approach ensures your project is clean, portable, and easy for others to set up.