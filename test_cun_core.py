# test_cun_core.py
import subprocess

def run_cmd(args, input_text=None):
    proc = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = proc.communicate(input=input_text)
    return proc.returncode, out.strip(), err.strip()

def test_planbreak():
    goal = "Viết parser đơn giản. Test code. Sửa lỗi."
    code, out, err = run_cmd(["python3", "planbreak.py"], input_text=goal)
    assert code == 0, f"planbreak.py lỗi, stderr={err}"
    assert "- [ ] (write) Viết parser đơn giản" in out
    assert "- [ ] (test) Test code" in out
    assert "- [ ] (debug) Sửa lỗi" in out
    print("planbreak.py test passed.")

def test_memcore():
    # Xoá file mem.json nếu có
    import os
    if os.path.exists("mem.json"):
        os.remove("mem.json")
    # Thêm nhớ
    code, out, err = run_cmd(["python3", "memcore.py", "add", "testkey", "testvalue"])
    assert code == 0, f"memcore.py add lỗi, stderr={err}"
    # Lấy nhớ
    code, out, err = run_cmd(["python3", "memcore.py", "get", "testkey"])
    assert "testvalue" in out, f"memcore.py get không ra value, out={out}"
    # Grep nhớ
    code, out, err = run_cmd(["python3", "memcore.py", "grep", "test"])
    assert "testkey" in out, "memcore.py grep không tìm ra key"
    # Dump nhớ
    code, out, err = run_cmd(["python3", "memcore.py", "dump"])
    assert "testkey" in out and "testvalue" in out, "memcore.py dump không đúng"
    print("memcore.py test passed.")

def test_respgen():
    code, out, err = run_cmd(["python3", "respgen.py"], input_text="hello")
    assert code == 0, "respgen.py lỗi khi nhập hello"
    assert len(out) > 0, "respgen.py không trả lời"
    code2, out2, err2 = run_cmd(["python3", "respgen.py", "thanks"])
    assert code2 == 0 and len(out2) > 0, "respgen.py lỗi khi truyền args"
    print("respgen.py test passed.")

if __name__ == "__main__":
    test_planbreak()
    test_memcore()
    test_respgen()
    print("Tất cả test xong, mày chạy được rồi.")
