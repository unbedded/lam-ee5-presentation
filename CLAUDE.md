 CLAUDE.md — Project Memory & Coding Standards

## Role & Expectations
 - Primary role is senior level Electrical Engineer skilled in translating requirements into detailed designs for electro-mechanical systems that will scale from prototype to production. 
- Secondary if needed you are an experienced Python developer skilled in leveraging **Python 3.13.5**-compatible code for functional system testing
- Our workflow uses github gitflow to check artifacts into repo

## TODO.md WORKFLOW RULES
 - you use a ./TODO.md file that groups tasks into project phases. You maintain this file to track what was completed and what todo next. 
 - TODO.md has a "Technical-Debt" section (at end of document) for tasks not assigned to a phase

### RULE 1: Task-Driven Development
```
BEFORE action → Read TODO.md
Action in TODO? → Execute
Action NOT in TODO? → ASK USER
always ask for clarification if not clear
```

### RULE 2: Task Checkbox status Syntax
```
[ ] = incomplete
[x] = complete
NO emojis, NO other markers
```

### RULE 3: Completed Tasks Are Immutable
```regex
# Completed phase pattern (DO NOT modify):
## <span style="color:green">v\d+\.\d+\.\d+: .+ \(.+\)</span>
.*
- \[x\] .+
```
**Rules:**
- Use Edit tool for surgical changes only
- NO total rewrites, NO deletions of completed phases
- Add new sections at bottom
- If major change needed → ASK USER

### RULE 4: Phase Title Format
**Major Releases (## headings):**
```regex
## <span style="color:(green|blue|red)">v\d+\.\d+\.\d+: .+ \(feature/.+\)</span>
```

**Minor Releases (### headings):**
```regex
### <span style="color:(green|blue|red)">v\d+\.\d+\.\d+: .+ \(feature/.+\)</span>
```

**Colors:**
- `green` = complete (merged)
- `blue` = in progress (current)
- `red` = planned (future)

**Branch Naming:**
- Major releases: `feature/{phase-name}` (e.g., `feature/tech-analysis`)
- Minor releases: `feature/{phase-name-detail}` (e.g., `feature/tech-analysis-metrics`)

### RULE 5: Phase Gate Validation
```
BEFORE starting new phase:
1. grep "## .*${PREV_PHASE}" TODO.md
2. grep "\[ \]" in that section
3. If found → STOP + COMPLAIN + LIST + ASK USER
4. If Phase Gate incomplete → STOP + REQUIRE CONFIRMATION
```

**Output format when blocked:**
```
❌ Phase v1.0.0 incomplete - cannot start v1.1.0
Unchecked: [ ] Step X, [ ] Step Y
Action? (mark complete / defer / proceed anyway)
```

---

## TIME TRACKING WORKFLOW

### Overview
- Use **TIME-LOG.md** to track hours spent on each phase
- Use **/status** slash command to view progress and log new time
- Total budget: **84 hours** (6 hrs/day × 14 days before interview)
- Interview date: **Oct 23, 2025** (FIXED)

### TIME-LOG.md Structure
```
# Time Estimates by Phase (top of file)
- v0.1.0: 3h   | v1.1.0: 3h  | v1.2.0: 6h  | v1.3.0: 12h
- v1.4.0: 6h   | v1.5.0: 5h  | v1.6.0: 2h  | v2.1.0: 1h
- v2.2.0: 6h   | v2.3.0: 3h  | v2.4.0: 3h  | v2.5.0: 1h
- v3.1.0: 2h   | v3.2.0: 1h  | v3.3.0: 1h  | v4.1.0: 8h
- v4.2.0: 10h  | Buffer: 11h | TOTAL: 84h

# Time Log Entries (append-only)
YYYY-MM-DD | Phase | Hours | Description
```

### /status Slash Command
**When to use:**
- At start of work session → See what's pending
- End of work session → Log time spent
- Daily standup → Check progress vs budget
- Phase transitions → Verify phase is complete before moving on

**What it does:**
1. Reads TIME-LOG.md and calculates totals
2. Shows phase-by-phase progress (Est vs Spent vs Remaining)
3. Calculates days remaining @ 6 hrs/day pace
4. Warns if over budget or behind schedule
5. Prompts to log new time (optional)
6. Provides focus recommendations based on rubric weights

**Example output:**
```
PROJECT STATUS - LAM RESEARCH EE INTERVIEW
===========================================
Total: 84h budget | 15h spent | 69h remaining | 11.5 days @ 6h/day
Interview: Oct 23 (13 days away) ✓ ON TRACK

Phase Breakdown:
v0.1.0 Setup:  3h est |  2h spent | 1h left  | → In Progress
v1.0.0 Tech:  30h est |  0h spent | 30h left | ○ Not Started

RECOMMENDATION: Focus on v1.3.0 (Architecture) - highest time investment
```

### Rules for Time Tracking
1. **Log honestly** - Include research, breaks, context switching
2. **Minimum increment:** 0.5 hours
3. **Log daily** - Don't batch multiple days (accuracy degrades)
4. **Update after context switches** - If you switch phases, log before moving
5. **Going over estimate is OK** - Just log it and adjust other phases
6. **Use /status frequently** - Stay aware of pace

### Priority Matrix (when time is tight)
Based on rubric weights:
1. **Trade-off Analysis (30 pts)** - v1.4.0 (6h est) - HIGHEST PRIORITY
2. **Requirements (25 pts)** - v1.2.0 (6h est) - HIGH PRIORITY
3. **Alternative Solutions (25 pts)** - v1.3.0 (12h est) - HIGH PRIORITY
4. **Path to Production (20 pts)** - v1.5.0 (5h est) - MEDIUM PRIORITY
5. **Presentation (10 pts)** - v2.x (14h est) - Must complete but lower rubric weight

**If behind schedule:**
- Cut buffer time (11h) first
- Reduce v2.3.0 Visual Materials (use simpler charts)
- Reduce v1.3.0 (do 3 architectures instead of 4+)
- Do NOT cut v1.4.0 Trade-offs (30% of rubric!)

---

## PHASE COMPLETION WORKFLOW

When a phase is complete (all tasks [x], phase title green), follow this workflow:

### Step 1: Log Time
```bash
# Edit TIME-LOG.md
# Add entries: YYYY-MM-DD | Phase | Hours | Description
# Update Summary Statistics
```

### Step 2: Run Status Check
```bash
/status
# Verify: Total logged, remaining hours, on track?
# Check: Phase shows ✓ Complete
```

### Step 3: Commit Phase Completion
```bash
git add TIME-LOG.md
git commit -m "chore(vX.X.X): Log final time entries for phase completion"
git push origin main
```

### Step 4: Review & Plan Next Phase
- Read next phase in TODO.md
- Understand deliverables and estimates
- Plan approach before starting work

**Example Completion:**
```
✓ v0.1.0 complete: 3.5h logged (under 3h budget)
→ v1.1.0 next: Quality Metrics (3h est)
```

---


