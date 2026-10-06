# Full Build Blueprint

A reusable AI skill for planning a complete CRM and business automation setup, stage by stage, in plain language.

The aim is simple: find the missing files, settings and business decisions **before** a builder reaches them halfway through the project.

## How it works

**System → Pipeline stage → Main workflow → Connected workflows → Smaller connected steps**

A stage is finished only when all its required connected work is complete. The plan covers the forms, fields, messages, calendars, files, staff tasks and checks that make that stage work.

The skill asks the assistant to:

- Understand the current process and the finished daily routine.
- Gather the required inputs for the whole agreed project before kickoff.
- Give shared work one home and connect every stage that uses it.
- Walk through the build to find missing details.
- Explain what happens automatically and what staff still does.
- Create an expandable HTML map alongside a full blueprint when appropriate.
- Keep unanswered questions, unverified features and unrun tests visible.

## Use it

Copy the `full-build-blueprint` folder into your assistant's skills directory. Keep `SKILL.md`, `agents/` and `references/` together.

Then use a prompt such as:

> Use $full-build-blueprint to plan this client's CRM setup. Organise it by pipeline stage, include every connected step, and create an expandable HTML process map. Find the access, files, sample data and decisions we need before kickoff.

For a review of an existing plan:

> Use $full-build-blueprint to walk through this blueprint as if you were building it. Find missing calendar settings, email copy, forms, fields, file rules and staff actions. Add the missing details where the source gives an answer, and group unanswered questions for the client.

Supply the current client's process, existing blueprint and source documents in your own private workspace. They do not belong in this public repository.

The default integration preference is n8n. An explicitly chosen tool takes priority. The skill does not require HighLevel; keep the client's actual CRM and agreed scope.

## Included

| File | Purpose |
| --- | --- |
| [SKILL.md](full-build-blueprint/SKILL.md) | Main planning instructions |
| [Stage build pack](full-build-blueprint/references/stage-build-pack.md) | What each stage needs to include |
| [Small-details review](full-build-blueprint/references/small-details-review.md) | Build walkthrough covering easily missed settings and steps |
| [Skill metadata](full-build-blueprint/agents/openai.yaml) | Display name and example invocation |

## What this does not prove

A complete plan is not a completed live system. Written checks are not passed tests. The assistant must distinguish confirmed facts, suggestions, missing answers and features that still need to be checked in the actual account.

The skill does not grant permission to send messages, launch workflows, buy services, migrate records or delete old data.

This repository contains the reusable method only. It contains no client proposals, client files, credentials or account details.
