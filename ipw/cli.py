#!/usr/bin/env python3

import random
import string
import pyperclip
import questionary
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import os
from datetime import datetime
from zxcvbn import zxcvbn

console = Console()

INSTALL_DIR = os.path.expanduser("~/.ipw-cli")
SAVE_DIR = os.path.join(INSTALL_DIR, "saved_passwords")


def save_password_to_file(password: str):
    os.makedirs(SAVE_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"password_{timestamp}.txt"
    file_path = os.path.join(SAVE_DIR, filename)

    with open(file_path, "w") as f:
        f.write(password + "\n")

    console.print(f"[blue]✔ Saved to {file_path}[/blue]")

def generate_password(
    length: int, use_upper: bool, use_lower: bool, use_digits: bool, use_symbols: bool
) -> str:
    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("At least one character set must be selected.")

    return "".join(random.choice(char_pool) for _ in range(length))


def password_strength(password: str) -> str:
    result = zxcvbn(password)
    score = result['score']  # 0–4

    feedback = {
        0: "[red]Very Weak[/red]",
        1: "[red]Weak[/red]",
        2: "[yellow]Fair[/yellow]",
        3: "[green]Strong[/green]",
        4: "[bold green]Very Strong[/bold green]",
    }

    return feedback.get(score, "[grey]Unknown[/grey]")


def show_summary(length, use_upper, use_lower, use_digits, use_symbols, password):
    table = Table(title="Password Configuration Summary")
    table.add_column("Setting", justify="left", style="cyan")
    table.add_column("Value", justify="left")

    table.add_row("Length", str(length))
    table.add_row("Uppercase", str(use_upper))
    table.add_row("Lowercase", str(use_lower))
    table.add_row("Digits", str(use_digits))
    table.add_row("Symbols", str(use_symbols))
    table.add_row("Strength", password_strength(password))
    table.add_row("Password", f"[bold green]{password}[/bold green]")

    console.print(table)


def run():
    console.print(
        Panel.fit("🔐 [bold magenta]Interactive Password Wizard (ipw)[/bold magenta]")
    )

    length = int(questionary.text("🔢 Password Length?", default="12").ask())

    choices = questionary.checkbox(
        "✅ Select character types to include:",
        choices=[
            {"name": "Uppercase Letters", "value": "upper", "checked": True},
            {"name": "Lowercase Letters", "value": "lower", "checked": True},
            {"name": "Numbers", "value": "digits", "checked": True},
            {"name": "Symbols", "value": "symbols", "checked": True},
        ],
    ).ask()

    use_upper = "upper" in choices
    use_lower = "lower" in choices
    use_digits = "digits" in choices
    use_symbols = "symbols" in choices

    try:
        password = generate_password(
            length, use_upper, use_lower, use_digits, use_symbols
        )

        show_summary(length, use_upper, use_lower, use_digits, use_symbols, password)

        if questionary.confirm("📋 Copy to clipboard?").ask():
            pyperclip.copy(password)
            console.print("[green]✔ Copied to clipboard[/green]")

        if questionary.confirm("💾 Save to file?").ask():
            save_password_to_file(password)

    except ValueError as e:
        console.print(f"[red]Error: {e}[/red]")
