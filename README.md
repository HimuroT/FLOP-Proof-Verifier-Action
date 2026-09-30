<p align="center">
  <img src="assets/flop_banner.png" alt="FLOP Network" width="520" />
</p>

# 🛡 FLOP Proof Verifier Action (CI/CD & Pre-Commit Audit)

### Automated GitHub Action & Pre-Commit Hook for Validating Technocore Proofs of Contribution

[![Technocore Schema](https://img.shields.io/badge/technocore--schema-v1-blue.svg)](https://technocore.chat)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-green.svg)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](tests/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Witness DID](https://img.shields.io/badge/Witnessed%20by-did%3Akey%3Az6Mkr2Ht...-blueviolet.svg)](#-cryptographic-proof-of-contribution)

> **Overview**: An automated CI/CD validator and pre-commit security tool for the **FLOP Network (flop.finance / Technocore)** ecosystem.  
> Ensures every contribution repository satisfies strict cryptographic Ed25519 signature standards, adheres to canonical schema structures, and guarantees exact 40-character commit SHA alignment.

---

## 🔑 Cryptographic Proof of Contribution

This tool is cryptographically signed and maintained by the **rabisu** validator node:
* **Operator DID**:  
  `did:key:z6Mkr2HtFjzrenM57Nh8hKdMuLdC5HaD44BUoL7zmRCvr16r`
* **Canonical Specification**: `technocore-contribution-proof-v1`
* **Witness File**: [`contribution-proof.json`](contribution-proof.json)

---

## ⚡️ Pipeline Flow & Capabilities

```text
  [ git commit / PR ]
           │
           ▼
┌───────────────────────────┐
│ scripts/pre_commit_hook.py│ ──> Validates schema, DID format & 40-char SHA
└──────────┬────────────────┘
           │ (Pass)
           ▼
┌───────────────────────────┐
│ GitHub Actions CI Runner  │
│ (verify_proof_ci.py)      │ ──> Verifies Ed25519 cryptographic signature
└──────────┬────────────────┘
           │ (Pass)
           ▼
[ 🟢 Release / Merged with Verified Proof ]
```

* 🛡 **Automated CI/CD Verification**: Plug-and-play workflow template to run on every `push` or `pull_request`.
* 🔐 **Ed25519 Cryptographic Proof Check**: Mathematically verifies that contribution claims were signed by the designated sovereign DID.
* 🪝 **Git Pre-Commit Hook**: Catches missing or malformed proof files, preventing invalid commits before they enter git history.
* 🧪 **Comprehensive Test Coverage**: Unit tests simulating corrupt proofs, truncated commit SHAs, and schema variations.

---

## 📁 Repository Structure

```text
FLOP-Proof-Verifier-Action/
├── templates/
│   └── verify_proof.yml          # GitHub Actions workflow template for child repositories
├── scripts/
│   ├── verify_proof_ci.py        # Core CLI and CI runner for proof verification
│   └── pre_commit_hook.py        # Local git pre-commit hook validator
├── tests/
│   └── test_proof_validation.py  # Unit tests for schema and hash validation
├── assets/
│   └── flop_banner.png           # Official visual branding
├── contribution-proof.json       # Cryptographic Ed25519 signature proof
├── SECURITY.md                   # CI/CD supply chain & security guidelines
├── LICENSE                       # MIT License
└── README.md
```

---

## 🚀 Usage Guide

### 1. Manual CLI Verification
```bash
# Verify a specific contribution-proof.json
python3 scripts/verify_proof_ci.py path/to/contribution-proof.json

# Enforce strict match against current git HEAD commit
python3 scripts/verify_proof_ci.py --strict-head contribution-proof.json
```

### 2. Install Pre-Commit Hook
```bash
# Install as local git pre-commit hook in your repository
cp scripts/pre_commit_hook.py .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

### 3. Add to GitHub Actions CI
Copy `templates/verify_proof.yml` into `.github/workflows/verify_proof.yml` in your target repository.

### 4. Run Test Suite
```bash
python3 -m unittest discover -s tests
```

---

## ⚖️ License
Released under the [MIT License](LICENSE).
