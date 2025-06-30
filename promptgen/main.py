import sys
from prompt_core import set_template, render_prompt

def usage():
    print("Usage:")
    print("  python3 main.py save [template_name]")
    print("  python3 main.py gen [template_name] key=value ...")
    print("Nếu không truyền template_name thì mặc định là 'default'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "save":
        name = sys.argv[2] if len(sys.argv) > 2 else "default"
        print(f"Nhập template cho '{name}', Ctrl+D để kết thúc:")
        content = sys.stdin.read()
        set_template(name, content)
        print(f"✅ Lưu template '{name}' thành công.")
    elif cmd == "gen":
        if len(sys.argv) < 3:
            usage()
            sys.exit(1)
        name = sys.argv[2]
        vars_dict = {}
        for pair in sys.argv[3:]:
            if '=' not in pair:
                print(f"Sai định dạng: {pair}")
                sys.exit(1)
            k, v = pair.split('=', 1)
            vars_dict[k] = v
        result, err = render_prompt(name, vars_dict)
        if result and not err:
            print(result)
        elif err:
            print(f"❌ Template '{name}' không tồn tại. Có: {err}")
        else:
            print(f"⚠ {result}")
    else:
        usage()
