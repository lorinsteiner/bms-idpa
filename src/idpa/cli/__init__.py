import typer

from idpa.cli.commands.dev import dev
from idpa.cli.commands.main import main
from idpa.cli.commands.pilot import pilot
from idpa.lib.dev import IS_DEV

app = typer.Typer()

app.command()(main)
app.command()(pilot)

if IS_DEV:
    app.command()(dev)
