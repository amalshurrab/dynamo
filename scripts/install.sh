#!/bin/zsh
# Install the Dynamo agents and skills into a venture folder for Claude Code.
# usage: scripts/install.sh /path/to/venture [agent ...]
# With no agent names, installs the lead and all thirteen. Re-run to update; it overwrites only Dynamo files.
set -e
HERE="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${1:?usage: install.sh /path/to/venture [agent ...]}"; shift || true
mkdir -p "$DEST/.claude/agents" "$DEST/.claude/skills" "$DEST/marketing"
if [[ $# -eq 0 ]]; then AGENTS=(dynamo mukhattit wassam naqqash lawwan rawi muharrir bannaa maher mudaqqiq nashir mulin safeer mudawwin); else AGENTS=("$@"); fi
for a in "${AGENTS[@]}"; do
  [[ -f "$HERE/agents/$a.md" ]] || { echo "no such agent: $a"; exit 1; }
  cp "$HERE/agents/$a.md" "$DEST/.claude/agents/$a.md"
  [[ -d "$HERE/agents/$a-knowledge" ]] && { rm -rf "$DEST/.claude/agents/$a-knowledge"; cp -R "$HERE/agents/$a-knowledge" "$DEST/.claude/agents/$a-knowledge"; }
  echo "agent  $a"
done
for s in "$HERE"/skills/*/; do
  n="$(basename "$s")"; rm -rf "$DEST/.claude/skills/$n"; cp -R "$s" "$DEST/.claude/skills/$n"; echo "skill  $n"
done
cp "$HERE/TEAM.md" "$DEST/.claude/DYNAMO-TEAM.md"
[[ -f "$DEST/marketing/venture-profile.md" ]] || { cp "$HERE/venture-profile.template.md" "$DEST/marketing/venture-profile.md"; echo "profile marketing/venture-profile.md (fill it in)"; }
echo "done: $DEST"
