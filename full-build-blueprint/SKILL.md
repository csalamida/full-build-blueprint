---
name: full-build-blueprint
description: Interview the user and create or audit a complete CRM and business automation build plan, organised by system, pipeline stage and connected workflows. Use for full setup blueprints, stage build packs, expandable process maps, and build simulations that find missing details before implementation.
---

# Full Build Blueprint

Create a plan a builder can follow without repeatedly discovering missing files, settings or business decisions halfway through the work. Explain it so a nontechnical business owner can understand it too. A thorough plan cannot guarantee that account tests will reveal no surprises; make remaining checks visible.

## Default working style

- Organise work as **System → Pipeline stage → Main workflow → Connected workflows → Smaller connected steps**.
- A stage is the unit of completion. Include everything needed for that stage, even when part of it lives in another tool.
- Use stable names and numbering, such as `Buyer System / 1. New Lead / 1.1 Receive enquiry / 1.1.1 Match business / 1.2 Staff review`. Separately state what runs first and what can happen at the same time; numbering alone does not specify execution order.
- Give reusable work one clear home. Each stage links to it and explains how it uses it, rather than duplicating instructions.
- Prefer n8n where an integration tool is needed, unless the user has chosen another tool. Respect an existing agreed tool or an explicit choice of Make or another tool. Use the CRM's built-in actions where suitable.
- Use plain language, short sentences, headings and bullets. Say “connected steps”, “what you need first”, “what happens next” and “what to check”. Avoid “descendants”, “dependencies”, “orchestration” and similar jargon in user-facing content. Keep useful product names, such as custom fields, and explain their purpose.

## Establish the actual project

Read supplied sources and the current blueprint before extending it. Preserve agreed scope, stage names, manual work, fees and tool choices. Separate a business record's working status from a sales pipeline; do not create another pipeline merely to fit this template.

## Interview before the full blueprint

For a new full blueprint, read [the guided interview](references/guided-interview.md) and use it before drafting the final plan. Start by explaining what you already know from the sources. Ask the next small group of unanswered questions, wait for the reply, then choose the follow-up questions based on that reply. Do not post the entire questionnaire or the entire blueprint in the first turn.

Ask one to three questions per turn, with examples or simple options where helpful. Do not ask for facts already supplied, actual passwords, or decisions that only the builder can investigate. If all material answers are already available, skip redundant questions and proceed. A narrow edit or audit does not require restarting the interview.

An unknown answer is allowed: record who must confirm it, the affected stage and what stays off until confirmed. Offer a clearly labelled suggestion where useful. If the user requests a draft now or says to use judgment, honour that instruction and show open questions visibly. Do not present unresolved material business rules as an implementation-ready plan.

Before the final blueprint, give a short recap of the proposed daily process, scope, key rules and remaining questions. Invite correction only where it would resolve a consequential ambiguity; this recap is not a separate mandatory approval gate. Once material choices are clear, produce the full blueprint and map. Keep later account tests and reviews of the built system separate from client answers.

Describe the starting position and the finished daily routine: which tool staff uses for each job, which steps run automatically, which staff must perform, and where information is saved. “HighLevel manages it” is too vague. Creating a task does not complete the call, inspection, approval or handoff.

Use clear labels: **Confirmed**, **Suggested — needs approval**, **Missing — needs an answer**, **Account check needed**, **Not included**. For build progress use **Not built**, **Built — not tested**, **Tested**, **Ready for live use** only when evidence supports it. Written test instructions are not passed tests. Example IDs and proposed settings must not look like live, verified values.

Check current official documentation for uncertain platform capabilities. Check the actual account when available and authorised. General platform support does not prove the client's plan, permissions, sample data or signing needs will work. Never assume an API exists; name the actual intake route and how it will be proved.

## Assemble the complete plan

1. List the systems, pipelines/stages, people, records, sources, files and tools within scope. Identify the one place each piece of information belongs and how records connect.
2. Create **one whole-project kickoff checklist** covering access, source files, sample data and business decisions across all agreed phases. Separate received items from missing items. Reuse material already supplied. Phase payments do not justify discovering essential inputs later.
3. Prepare the shared setup once: users, permissions, fields and values, forms, calendars, senders, files, signing, integrations and imported data as relevant. Specify settings and who maintains them.
4. Write each stage using [the stage build pack](references/stage-build-pack.md). Give every required form, field, message, document, workflow and staff action a home in its stage or shared setup, plus links to all places that use it.
5. Walk through the work as if building and operating it. Read [the small-details review](references/small-details-review.md), selecting relevant areas. Look for missing decisions, disconnected steps, missing copy/settings and mismatched records. Repair the plan where evidence gives an answer; group unresolved choices into an upfront client question list.
6. Walk through the complete journey again, including handoffs between stages and tools. Continue while the walkthrough exposes meaningful gaps. Do not add speculative features or expand scope merely to make the document longer.

Known essential inputs must be ready and checked before confirming project kickoff. Client review of the built system, final migration checks and launch approval happen later; do not demand them before anything exists. Useful preparation can proceed while inputs are collected, but do not represent the promised build clock as running before readiness. Explain how unexpected account limitations or later changes affect dates and scope.

## Deliver the blueprint and map

For a full blueprint, provide:

- A short “Start here” summary and contents.
- The finished daily routine, explained by tool and job.
- The whole-project kickoff checklist and grouped missing questions, with who must answer and what each answer affects.
- Shared setup and complete stage build packs, including exact settings, reusable copy, files, staff work and checks wherever sources permit.
- Build order, stage completion checks, full-journey checks, data changeover, team guide and launch/handover requirements.
- An expandable HTML process map by default when appropriate for a full-blueprint request. For a narrow edit or audit, update only the requested material and existing map.

Use the same stage/workflow names in the document and map. Show real connections and distinguish **Automatic**, **Manual**, and **Both**, explaining the human part. Each stage opens to its workflows, settings, messages/files, staff work, what it needs first and completion checks. Link shared work to one shared detail entry. Surface unanswered questions and untested work. Never show completion merely because the plan is written.

Make the map usable without developer tools: readable labels, expandable branches, a clear detail panel or equivalent, and a visible key. Keep essential content available in standalone HTML without needing a temporary localhost server or remote library. If personal checklist notes are saved locally, explain that they are not evidence of a live-account test. Do not create a NotebookLM notebook or another external artifact unless requested.

## Completion and boundaries

Before handover, confirm every agreed stage has connected instructions; every referenced asset has a definition or visible missing item; transitions specify the right record; and automatic/manual work is explicit. Check the map's navigation, readability and agreement with the document. Use an appropriate document skill for native editing and layout checks when editing a live document.

Report what is ready to build, what needs a client answer, what needs an account test, and what has actually been built or tested. A blueprint is a planning deliverable, not permission to launch workflows, send messages, buy services, migrate records or delete old data. Such actions require the user's separately authorised task.

Do not embed private client files, account details, past fees or dates in this reusable skill. Use the current project's sources each time.
