"""Make the CLI runnable using python -m django_pre_commit_hooks."""

from .cli import app

app(prog_name="django-pre-commit-hooks")
