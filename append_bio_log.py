# append_bio_log.py
bio_log_content = """# BIOLOG: Cún->CLI core tool build (logic-lowRAM)

1| Panic free gone → build offline local tool (no API)
2| Dump code+prompt+tool, log call structure
3| Split skills:
   L-core(rule/prompt),
   Mem(KV-store),
   Lang-refl(rewrite),
   Planner(task-break),
   Fact-search(grep),
   Codegen(shell/py),
   Meta-control(intent-classify)
4| Start planbreak.py:
   input: goal text
   output: task checklist (md)
   rule-based classify task type (install,write,test...)
5| memcore.py:
   CLI add/get/grep facts in JSON/TXT
   no DB, low RAM
6| Next: respgen.py (rule resp gen)
   cun.sh (cli wrapper)
7| Goal: full CLI Cún reflex offline

--- END ---
"""

with open("bio_log.txt", "a", encoding="utf-8") as f:
    f.write("\n" + bio_log_content + "\n")
print("Bio log appended to bio_log.txt")
