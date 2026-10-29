"""Your Coding Arena agent. THIS IS THE ONLY FILE YOU EDIT.

Every match draws one of two tasks, and your opponent gets the same one:

  solve_coding(task, tools)  write a solution that passes hidden tests
  find_bugs(task, tools)     report the bugs planted in a repository

Test offline with ./test, then enter with ./submit.
"""

import os


def solve_coding(task, tools):
    """Write the solution file. Whatever is written when you return is graded.

    task["spec"]        the problem statement (markdown)
    task["entrypoint"]  the file to write, e.g. "solution.py"
    task["starter"]     {filename: content}, the interface to fill in
    task["visible"]     example inputs and outputs
    """
    entry = task.get("entrypoint", "solution.py")
    code = task.get("starter", {}).get(entry, "")
    # TODO: replace the starter with a real solution.
    tools.write_file(entry, code)


def find_bugs(task, tools):
    """Report bugs as you find them. Wrong reports cost points, so be sure.

    task["repo_dir"]      the repository to read
    task["bug_taxonomy"]  the allowed bug_type values
    task["max_reports"]   the most reports you may send
    """
    repo = task["repo_dir"]
    for root, _dirs, files in os.walk(repo):
        for name in files:
            path = os.path.join(root, name)
            rel = os.path.relpath(path, repo)
            # TODO: read the file and look for bugs. Example report:
            # tools.submit_report({"file": rel, "line": 42,
            #                      "bug_type": "off_by_one",
            #                      "description": "loop stops one short"})
            _ = rel
