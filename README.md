# Full Build Blueprint

A reusable AI skill for planning a complete CRM and business automation setup, stage by stage, in plain language.

The aim is simple: find the missing files, settings and business decisions **before** a builder reaches them halfway through the project.

## How it works

**System → Pipeline stage → Main workflow → Connected workflows → Smaller connected steps**

A stage is finished only when all its required connected work is complete. The plan covers the forms, fields, messages, calendars, files, staff tasks and checks that make that stage work.

The skill asks the assistant to:

- Understand the current process and the finished daily routine.
- Read what you already supplied, then ask unanswered questions in small rounds before writing the final blueprint.
- Gather the required inputs for the whole agreed project before kickoff.
- Give shared work one home and connect every stage that uses it.
- Walk through the build to find missing details.
- Explain what happens automatically and what staff still does.
- Create an expandable HTML map alongside a full blueprint when appropriate.
- Keep unanswered questions, unverified features and unrun tests visible.

## Install in Codex — easiest option

Paste this into a Codex chat:

```text
Use $skill-installer to install the full-build-blueprint skill from
https://github.com/csalamida/full-build-blueprint/tree/main/full-build-blueprint
```

If it is already installed, ask Codex to update the existing copy while keeping a backup. Do not create a second copy with the same skill name.

Codex detects installed skills automatically. If the skill does not appear, restart Codex and try again. See the [official skill documentation](https://developers.openai.com/codex/skills/).

## Install a downloaded copy

Choose **Code → Download ZIP** on GitHub, unzip it, and open a terminal in the extracted repository folder. Alternatively, clone the repository:

```sh
git clone https://github.com/csalamida/full-build-blueprint.git
cd full-build-blueprint
```

The local installer needs Python 3.9 or newer. It does not download anything or need extra Python packages.

**macOS / Linux:**

```sh
python3 scripts/install.py
```

**Windows, with the Python launcher installed:**

```powershell
py -3 scripts/install.py
```

By default, this script installs into `~/.agents/skills/full-build-blueprint`, the documented user skill location. If `CODEX_HOME` is set, this installer instead uses its `skills` folder for compatibility with an existing customised setup. You can always choose the destination explicitly.

Preview the destination without changing files:

```sh
python3 scripts/install.py --dry-run
```

For a skill used only in the current project:

```sh
python3 scripts/install.py --dest .agents/skills
```

For an existing installation in `~/.codex/skills`:

```sh
python3 scripts/install.py --dest ~/.codex/skills --update
```

Use `py -3` instead of `python3` for the equivalent Windows commands. A destination is the **parent skills folder**; the installer adds `full-build-blueprint` itself.

### Update and restore

Download/unzip the newest repository, or run `git pull --ff-only` in a clean clone. Then run the installer with the **same destination you used before**:

```sh
python3 scripts/install.py --update
```

Updates move the previous folder to a timestamped `skill-backups` folder outside the scanned skills folder. The script prints that backup's exact location. Local edits are retained in the backup; the new version does not merge them automatically. To restore, move the new installed folder aside and copy the backup back to the printed installation location.

Without `--update`, an existing installation is left untouched. If copying or activating an update fails, the existing installation is preserved or restored.

### Manual installation

Copy the **inner** `full-build-blueprint` folder into your chosen skills folder. Copy the whole folder, not just `SKILL.md`. The installed shape should be:

```text
skills/
└── full-build-blueprint/
    ├── SKILL.md
    ├── agents/openai.yaml
    └── references/
        ├── guided-interview.md
        ├── stage-build-pack.md
        └── small-details-review.md
```

Other assistants may use different discovery folders. Follow their installation instructions; the package here includes Codex metadata, not a universal auto-installer for every product.

## Just invoke the skill

In a private client chat, type:

```text
$full-build-blueprint
```

That is enough. You do not need a long prompt or any files to begin. The assistant reads what is already in the conversation, asks **one to three missing questions at a time**, and waits for your answers. Once enough is known, it creates the stage-by-stage blueprint and expandable HTML map.

If you have files, attach them in your private workspace. If you have none, it starts with what the business does, which process you want to improve and what the finished setup should do. It later separates files still to be supplied from files that need to be created.

## Choose a task when you need to

These are **chat shortcuts**, not terminal commands or built-in command-line flags. Type the skill name followed by a shortcut:

| Type in chat | What happens |
| --- | --- |
| `$full-build-blueprint` | Questions first, then the full blueprint and map. |
| `$full-build-blueprint --interview` | Questions only, followed by a recap and open items. |
| `$full-build-blueprint --draft` | A working draft now, with missing answers clearly marked. |
| `$full-build-blueprint --plan` | The full blueprint and map, using known answers and asking only what is still needed. |
| `$full-build-blueprint --audit` | Walk through an existing plan to find and address missing pieces. |
| `$full-build-blueprint --map` | An expandable HTML map of the known plan. |
| `$full-build-blueprint --resume` | Continue where the current interview or plan left off. |
| `$full-build-blueprint --help` | Show the available shortcuts. |

You can still use normal sentences, such as “Review my blueprint for missing calendar settings and email copy.” A clear request takes priority over the defaults. Compatible shortcuts can be combined, such as `--draft --map`.

The interview covers these topics **as needed**, skipping anything already answered:

1. The business and the desired result.
2. The real process, stage by stage.
3. People, records and source files.
4. Calendars, emails, documents and other small settings.
5. Exceptions, staff cover and things that can go wrong.
6. A recap, remaining questions and readiness to write the plan.

You can say “I don't know”, “ask the client” or “suggest something”. Unresolved items remain visible; they are not quietly invented. A working draft is not presented as ready to build while important answers or account checks are missing.

An audit needs a plan or a description of the current process. A map of an unfinished plan is labelled a working map. Resume uses available conversation history and private project notes; if no earlier answers are available, the assistant says so and starts with the opening questions.

Client files and interview notes belong in your private workspace, never in this public repository. The default integration preference is n8n. An explicitly chosen tool takes priority. The skill does not require HighLevel; keep the client's actual CRM and agreed scope.

## Included

| File | Purpose |
| --- | --- |
| [SKILL.md](full-build-blueprint/SKILL.md) | Main planning instructions |
| [Stage build pack](full-build-blueprint/references/stage-build-pack.md) | What each stage needs to include |
| [Small-details review](full-build-blueprint/references/small-details-review.md) | Build walkthrough covering easily missed settings and steps |
| [Guided interview](full-build-blueprint/references/guided-interview.md) | Adaptive question rounds before the final blueprint |
| [Skill metadata](full-build-blueprint/agents/openai.yaml) | Display name and example invocation |
| [Local installer](scripts/install.py) | Install, preview or update a downloaded copy |

## Check the installer

From the repository folder:

```sh
python3 -m unittest discover -s tests -v
```

The tests cover clean installation, existing-folder protection, dry runs, backup retention, incomplete sources, failed copying and recovery from a failed update.

## What this does not prove

A complete plan is not a completed live system. Written checks are not passed tests. The assistant must distinguish confirmed facts, suggestions, missing answers and features that still need to be checked in the actual account.

The skill does not grant permission to send messages, launch workflows, buy services, migrate records or delete old data.

This repository contains the reusable method only. It contains no client proposals, client files, credentials or account details.
