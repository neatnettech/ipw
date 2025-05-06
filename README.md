# 🔐 ipw – Interactive Password Wizard

![CI](https://github.com/neatnettech/ipw/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/github/license/neatnettech/ipw)
![Version](https://img.shields.io/github/v/tag/neatnettech/ipw)

**ipw** just a tool to create a password in quick and easy way

---

## 🚀 Features

- ✅ interactive CLI
- ✅ configurable password length and character types
- ✅ clipboard copy
- ✅ auto-saving passwords to timestamped files
- ✅ safe local install and linking via install script

---

## 📦 Installation

### 🧰 One-liner (recommended)

```bash
curl -sSL https://raw.githubusercontent.com/neatnettech/ipw/main/install.sh | bash
```

This installs ipw to ```~/.ipw-cli``` and links the CLI to ```~/.local/bin/ipw```.
Make sure ```~/.local/bin``` is in your ```$PATH```.

## 💻 Usage

Follow the guided wizard to:
	•	Choose password length
	•	Select character types (uppercase, lowercase, digits, symbols)
	•	Copy to clipboard
	•	Save to local password vault (in ```~/.ipw-cli/saved_passwords```)

## 🛠 Local Development

```bash
git clone https://github.com/neatnettech/ipw.git
cd ipw
poetry install
poetry run ipw
```

## Optional: Activate Shell

```bash
poetry shell
ipw
```

## 📝 Saved Passwords

When saving, passwords are stored in:
```
~/.ipw-cli/saved_passwords/password_YYYYMMDD_HHMMSS.txt
```


## 🍺 Homebrew (optional)

Coming soon: Homebrew install support via custom tap.

## 📜 License

MIT © neatnettech