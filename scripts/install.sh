#!/bin/zsh
# Fallback installer: copies the Dynamo agents, skills, knowledge and team rules into one venture folder for Claude Code.
# Prefer the plugin (auto-updates with every commit):  claude plugin marketplace add amalshurrab/dynamo && claude plugin install dynamo@dynamo
# usage: scripts/install.sh /path/to/venture [agent ...]   (no agent names = the lead and all thirteen). Re-run to update.
set -e
HERE="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${1:?usage: install.sh /path/to/venture [agent ...]}"; shift || true
mkdir -p "$DEST/.claude/agents" "$DEST/.claude/skills" "$DEST/.claude/dynamo/knowledge" "$DEST/marketing"
if [[ $# -eq 0 ]]; then AGENTS=(dynamo mukhattit wassam naqqash lawwan rawi muharrir bannaa maher mudaqqiq nashir mulin safeer mudawwin); else AGENTS=("$@"); fi
for a in "${AGENTS[@]}"; do
  [[ -f "$HERE/agents/$a.md" ]] || { echo "no such agent: $a"; exit 1; }
  # agents reference ${CLAUDE_PLUGIN_ROOT}; outside the plugin that is .claude/dynamo
  sed 's#\${CLAUDE_PLUGIN_ROOT}#.claude/dynamo#g' "$HERE/agents/$a.md" > "$DEST/.claude/agents/$a.md"
  rm -rf "$DEST/.claude/agents/$a-knowledge"   # pre-plugin layout
  [[ -d "$HERE/knowledge/$a" ]] && { rm -rf "$DEST/.claude/dynamo/knowledge/$a"; cp -R "$HERE/knowledge/$a" "$DEST/.claude/dynamo/knowledge/$a"; }
  echo "agent  $a"
done
for s in "$HERE"/skills/*/; do
  n="$(basename "$s")"; rm -rf "$DEST/.claude/skills/$n"; cp -R "$s" "$DEST/.claude/skills/$n"
  find "$DEST/.claude/skills/$n" -name '*.md' -exec sed -i '' 's#\${CLAUDE_PLUGIN_ROOT}#.claude/dynamo#g' {} +
  echo "skill  $n"
done
cp "$HERE/TEAM.md" "$DEST/.claude/dynamo/TEAM.md"; rm -f "$DEST/.claude/DYNAMO-TEAM.md" "$DEST/.claude/agents/DYNAMO-TEAM.md"
[[ -f "$DEST/marketing/venture-profile.md" ]] || { cp "$HERE/venture-profile.template.md" "$DEST/marketing/venture-profile.md"; echo "profile marketing/venture-profile.md (fill it in)"; }
echo "done: $DEST  (open a NEW Claude Code session, then /dynamo)"
