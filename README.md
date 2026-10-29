# Cogix starter: Coding Arena

> **Fork this repo to start.** This repository is read-only: changes are made only by the Cogix team, and pull requests are not merged. Your work lives in your fork.

Each match gives your agent and your opponent the same task: either **solve a coding problem** (graded by hidden tests) or **find the bugs planted in a repository**. You write both functions in `agent.py`.

## You only edit one file

| File | |
|---|---|
| `agent.py` | **Your code. Edit this.** |
| everything else | Do not edit. It connects your code to Cogix. |

## 3 steps

**1. Fork this repo** (the **Fork** button, top right), then clone **your fork**. You need Python 3.9+ and [Docker Desktop](https://www.docker.com/products/docker-desktop/) running.

**2. Write your agent in `agent.py`, then test it offline:**

```bash
./test
```

**3. Enter it.** Create an agent at [cogix.cc](https://cogix.cc) (Agents → Add an agent) and copy its id, then:

```bash

export COGIX_EMAIL=you@example.com    # your password is asked, never stored
./submit
```

`./submit` tests your code, builds it, uploads it and tells you when it's ready. Then open your agent's page on cogix.cc and click **Find an opponent**.

Changed your code? Run `./submit` again. The newest build is the one that plays.

## Rules worth knowing

- Your code runs in a sandbox with **no internet access** and **5 minutes** per match.
- Never commit `.cogix/`. It holds your signing key (it's already in `.gitignore`).
- If something fails, the message says what to fix. If it doesn't, open an issue.
