# Stage build pack

Read when creating or auditing a stage. Use the applicable sections. Explain when a feature stays manual or is not included. Do not hide a missing decision by marking it not applicable.

## System and stage

- **Name and number:** Use the agreed system, pipeline and stage name.
- **Purpose:** What changes for the customer or staff here?
- **Starts when:** Exact event and conditions for entry; who or what changes the stage.
- **Finished when:** Business result needed before moving on; pauses, closure and re-entry where relevant.
- **Next stage:** Exact record that moves, who moves it and required checks.

## Workflows and connected steps

Give each main/connected workflow a stable name. For each specify:

- What starts it and which record it belongs to.
- What it reads and where the information comes from.
- Actions in order, including waits, choices and staff work.
- What gets saved, where, and what another step uses later.
- Message/task recipients and who is responsible for acting.
- Stop/pause/cancel rules, including replies, manual intervention, closure and reopening.
- How it recognises work already completed.
- What happens on failure, missing information or an unclear result; alert owner and safe resumption.

For n8n or another integration tool, name the actual source event, account connection, data read, record match, actions, saved result and failure route. Specify nodes/actions and field mappings where verified; mark unverified choices as account checks. “Sync to CRM” is not a build instruction.

## Everything this stage uses

- **Records and fields:** Name, record type, purpose, data type, options/default, required moment, writer and next reader. Define shared fields once. Enquiry-specific progress must not live only on a shared contact.
- **Saved values and tags:** Purpose, initial value, updater and timing. Avoid competing ways to track one status.
- **Forms:** Fields, required/optional rules, validation, record destination, assignment, confirmation and staff alert.
- **Calendar:** Agreed settings, booking form, messages and staff action. Slot spacing and appointment length are separate choices.
- **Emails/messages:** Actual reusable subject/body, sender/reply-to, recipient rule, filled-in details, appearance, links/files, timing, approval and stopping rules. A message title alone is unfinished.
- **Documents/payments:** Approved source/version, selection rule, filled-in details, signers/order, send/completion proof, invoice/payment reference, manual bank checks and release conditions.
- **Files:** Source, naming, permissions, approved version, storage, links, upload/send action and replacement rules.
- **Staff tasks:** One owner, action, correct record, due time, completion proof and cover/escalation.
- **Shared work:** Link to its definition; explain what the stage gives it and receives back.

Record supplied values faithfully. For unknown values show the question and affected step. Suggestions must be labelled; do not invent an approved cadence, address, legal term, price or timezone.

## What you need first

List access, client answers, documents, samples and shared setup. Separate upfront inputs from assets the builder creates. Name earlier stages that supply information and other stages affected by a settings change.

## Check before marking this stage finished

For each meaningful check give starting records, action, expected messages/files/changes and things that must stay unchanged. Cover:

- Normal path and handoff to the next stage.
- Missing required information or unavailable approved file.
- Repeat events, late updates and paused/closed records.
- One person with two jobs, enquiries or businesses where relevant.
- Failed actions and recovery without duplicate sends or wrong-record changes.
- Staff work completed versus merely assigned.

Mark checks **Not run**, **Passed** or **Failed**, with actual evidence when run. Required connected work and relevant shared checks must pass before live readiness. For planning only, distinguish a complete stage pack from a live stage that has not been built or tested.
