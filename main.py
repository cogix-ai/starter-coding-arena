"""DO NOT EDIT. Connects agent.py to the Cogix runtime. Edit agent.py instead."""

import sys

from cogix_sdk import Agent

import agent as yours

app = Agent(name="coding-arena-agent", version="1.0.0")
app.challenge("coding_duel")(yours.solve_coding)
app.challenge("bug_hunt_race")(yours.find_bugs)


def selftest() -> None:
    import tempfile
    from cogix_sdk.batch import Tools

    tools = Tools({"challenge_id": "coding_duel", "entrypoint": "solution.py",
                   "spec": "Return the sum of two integers.",
                   "starter": {"solution.py": "def add(a, b):\n    raise NotImplementedError\n"}})
    yours.solve_coding(tools.task, tools)
    assert "solution.py" in tools.files(), "solve_coding() must write the entrypoint file"
    print("coding task: OK, wrote", ", ".join(sorted(tools.files())))

    with tempfile.TemporaryDirectory() as repo:
        with open(f"{repo}/main.go", "w") as f:
            f.write("package main\n\nfunc main() {}\n")
        tools = Tools({"challenge_id": "bug_hunt_race", "repo_dir": repo, "max_reports": 36,
                       "line_tolerance": 3, "bug_taxonomy": ["off_by_one", "wrong_operator"]})
        yours.find_bugs(tools.task, tools)
        print(f"bug hunt: OK, {len(tools.reports())} report(s)")


if __name__ == "__main__":
    if sys.argv[1:] == ["selftest"]:
        selftest()
    else:
        sys.exit(app.run_batch())
