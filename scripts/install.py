#!/usr/bin/env python3
"""Install the adjacent skill from a local repository/download. No network needed."""
import argparse
from datetime import datetime, timezone
import os
from pathlib import Path
import shutil
import sys
import tempfile
import uuid

NAME = "full-build-blueprint"
REQUIRED = (
    "SKILL.md",
    "agents/openai.yaml",
    "references/stage-build-pack.md",
    "references/small-details-review.md",
    "references/guided-interview.md",
)


def default_destination():
    codex_home = os.environ.get("CODEX_HOME")
    return Path(codex_home).expanduser() / "skills" if codex_home else Path.home() / ".agents" / "skills"


def install(source, parent, update=False, dry_run=False):
    source = Path(source).absolute()
    parent = Path(parent).expanduser().absolute()
    target = parent / NAME
    if source.is_symlink() or any(p.is_symlink() for p in source.rglob("*")):
        raise ValueError("The source skill must not contain symbolic links.")
    for rel in REQUIRED:
        if not (source / rel).is_file():
            raise ValueError(f"Missing required source file: {rel}")
    if source.resolve() == target.resolve():
        raise ValueError("The source is already the destination. Choose another destination.")
    if target.is_symlink():
        raise ValueError("The installed skill is a symbolic link. Resolve it manually first.")
    if target.exists() and (not target.is_dir() or not (target / "SKILL.md").is_file()):
        raise ValueError("The destination exists but is not a skill folder; it will not be replaced.")
    if target.exists() and not update:
        raise FileExistsError(f"Already installed at {target}. Use --update to keep a backup and replace it.")
    # Backups must not become duplicate discoverable skills.
    backup_parent = parent.parent / "skill-backups"
    for installed in (target, backup_parent):
        if source.resolve() == installed.resolve() or source.resolve() in installed.resolve().parents or installed.resolve() in source.resolve().parents:
            raise ValueError("Source and installation/backup paths must be separate.")
    if dry_run:
        return target, None
    parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{NAME}-", dir=parent))
    backup = None
    try:
        for rel in REQUIRED:
            output = staging / rel
            output.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source / rel, output)
        if target.exists():
            backup_parent.mkdir(parents=True, exist_ok=True)
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
            backup = backup_parent / f"{NAME}-{stamp}-{uuid.uuid4().hex[:8]}"
            target.rename(backup)
        try:
            staging.rename(target)
        except OSError:
            if backup is not None and not target.exists():
                backup.rename(target)
            raise
    finally:
        if staging.exists():
            shutil.rmtree(staging)
    return target, backup


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", type=Path, default=default_destination(), help="Parent skills folder; the skill name is added automatically.")
    parser.add_argument("--update", action="store_true", help="Replace an existing skill after moving it to a backup outside the skills folder.")
    parser.add_argument("--dry-run", action="store_true", help="Show the destination without changing files.")
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1] / NAME
    try:
        target, backup = install(source, args.dest, args.update, args.dry_run)
    except (OSError, ValueError) as error:
        print(f"Installation stopped: {error}", file=sys.stderr)
        return 1
    print(f"{'Would install' if args.dry_run else 'Installed'}: {target}")
    if backup:
        print(f"Previous version kept at: {backup}")
    if not args.dry_run:
        print("Start a new turn/session, then ask to use $full-build-blueprint.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
