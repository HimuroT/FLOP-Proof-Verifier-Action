#!/usr/bin/env python3
"""
Git Pre-Commit Hook for FLOP Technocore Repositories
Verifies that contribution-proof.json is well-formed and valid before committing changes.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def check_proof_file(proof_path: Path) -> tuple[bool, str]:
    if not proof_path.exists():
        return False, f"Proof file does not exist at: {proof_path}"

    try:
        data = json.loads(proof_path.read_text(encoding="utf-8"))
    except Exception as e:
        return False, f"Invalid JSON syntax in proof: {e}"

    required_keys = ["did", "type", "artifact_url", "commit", "signature", "signed_at"]
    for key in required_keys:
        if key not in data or not data[key]:
            return False, f"Missing or empty required field '{key}' in proof."

    commit_sha = data["commit"]
    if len(commit_sha) != 40 or not all(c in "0123456789abcdefABCDEF" for c in commit_sha):
        return False, f"Invalid commit SHA format: '{commit_sha}'. Must be exactly 40 hex characters."

    if not data["did"].startswith("did:key:z"):
        return False, f"Invalid DID format: '{data['did']}'. Must begin with 'did:key:z'."

    return True, "Proof structure and commit SHA format verified."


def main():
    repo_root = Path.cwd()
    proof_path = repo_root / "contribution-proof.json"

    # Also check proof/ subfolder if exists
    if not proof_path.exists() and (repo_root / "proof" / "contribution-proof.json").exists():
        proof_path = repo_root / "proof" / "contribution-proof.json"

    print("🔎 Technocore Pre-Commit Hook: Verifying contribution proof...")
    ok, msg = check_proof_file(proof_path)
    if not ok:
        print(f"❌ [Pre-Commit FAILED]: {msg}", file=sys.stderr)
        sys.exit(1)

    print(f"✔ [Pre-Commit PASSED]: {msg}")
    sys.exit(0)


if __name__ == "__main__":
    main()
