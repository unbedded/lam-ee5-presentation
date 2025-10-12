---
description: Complete current phase, update TODO/TIME-LOG, commit and push
---

# Phase Completion Automation

Automate phase completion workflow using existing TODO.md and TIME-LOG.md files.

## Your Tasks

### 1. Validate Current Phase (1 min)

Read TODO.md:
- Find phase with `<span style="color:blue">` (current in-progress phase)
- Check ALL tasks under this phase are `[x]`
- Check Phase Gate section (if exists) all `[x]`

**If ANY `[ ]` found:**
```
❌ PHASE INCOMPLETE: v[X].[X].[X] [Phase Name]

Unchecked items:
- [ ] Task description
- [ ] Another task

Action: Complete tasks first, then run /phase-complete
```
**STOP - Do not proceed**

### 2. Prompt for Time Logging (30 sec)

Get today's date (YYYY-MM-DD)

Check TIME-LOG.md for today's entries

**Only if NO entries today:**
Prompt user: "No time logged today. Hours spent? (e.g., 1.5 or 'skip'): "

If hours entered, prompt: "Description: "

Append to TIME-LOG.md:
```
YYYY-MM-DD | vX.X.X | Xh | Description
```

### 3. Calculate Time Summary (1 min)

Read TIME-LOG.md:
- Sum all hours for current phase
- Get phase estimate from table
- Calculate total project hours
- Calculate remaining (84h - total)

Read TODO.md to get phase name

### 4. Update README.md (2 min)

Read README.md and verify/update:

**Directory Structure section:**
- Check if any new files/directories created this phase
- Add them to the ASCII tree with descriptions
- Remove any deleted files/directories
- Update any renamed files

**Build Structure section:**
- Document new slash commands (if created)
- Document new Makefile targets (if added)
- Update data flow diagrams (if SSOT or generators changed)
- Update dependency mappings (if new workflows added)

**Version at top:**
- Update `**Current Version:** vX.X.X` to match completed phase

**If changes needed:**
Prompt user: "README.md updates needed for this phase. Proceed with auto-update? (yes/no): "

If yes, update README.md and save

If no, warn user and continue (but note in commit message)

### 5. Update TODO.md Colors (30 sec)

Current phase: `<span style="color:blue">` → `<span style="color:green">`

Next phase (first red after current): `<span style="color:red">` → `<span style="color:blue">`

Save TODO.md

### 6. Update TIME-LOG.md Summary (30 sec)

Update "Summary Statistics" section:
```markdown
- **Total Logged:** [X] hours
- **Total Remaining:** [X] hours
- **Average Daily Pace:** [X] hrs/day (over [X] days)
- **Projected Completion:** YYYY-MM-DD
- **On Track?:** [✅ YES / ⚠️ BEHIND / 🎯 AHEAD]
```

Save TIME-LOG.md

### 7. Commit and Push (1 min)

Stage: `git add TODO.md TIME-LOG.md README.md`

Commit message format:
```
chore(vX.X.X): Complete [Phase Name] phase

Time: [X]h logged / [Y]h est ([Over/Under] by [Z]h)
Project: [X]h / 84h ([%] complete)
Status: [✅ ON TRACK / ⚠️ BEHIND]

Next: v[X].[X].[X] [Phase Name]
```

Push: `git push origin main`

### 8. Display Summary (output)

```
✅ PHASE COMPLETE: v[X].[X].[X] [Phase Name]
================================================================

Time Performance:
  Phase: [X]h / [Y]h est ([Over/Under] by [Z]h)

Project Status:
  Total: [X]h / 84h ([%])
  Remaining: [X]h ([X] days @ 6h/day)
  Status: [✅ ON TRACK / ⚠️ BEHIND / 🎯 AHEAD]

✓ Committed and pushed to main

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

→ NEXT PHASE: v[X].[X].[X] [Phase Name]

  Estimate: [X]h
  Key Tasks: [First 3 tasks from TODO.md]
```

## Error Handling

**Git push fails:**
Show error, tell user to manually push

**No blue phase found:**
Show error, tell user to check TODO.md

## Notes

- Only prompt user for time logging if needed
- All other steps are automatic
- Clear, concise output
- Validate before committing
