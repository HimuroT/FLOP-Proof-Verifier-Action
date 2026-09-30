<p align="center">
  <img src="assets/flop_banner.png" alt="FLOP Network" width="520" />
</p>

# 🤖 FLOP Proof Verifier Action (CI/CD Quality Gate)

### Automated GitHub Action & Pre-Commit Quality Gate for Technocore Contribution Proofs

[![Technocore Schema](https://img.shields.io/badge/technocore--schema-v1-blue.svg)](https://technocore.chat)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-green.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Witness DID](https://img.shields.io/badge/Witnessed%20by-did%3Akey%3Az6Mkr2Ht...-blueviolet.svg)](#-cryptographic-proof-of-contribution)

> **Overview**: An automated CI/CD validator and pre-commit hook engineered for **FLOP Network (flop.finance / Technocore)** open-source contributors.  
> Prevents desynchronized signatures, verifies Ed25519 proof integrity on every pull request, and enforces git HEAD alignment.

---

## 🔑 Cryptographic Proof of Contribution

This tool is cryptographically signed and maintained by the **rabisu** validator node:
* **Operator DID**:  
  `did:key:z6Mkr2HtFjzrenM57Nh8hKdMuLdC5HaD44BUoL7zmRCvr16r`
* **Canonical Specification**: `technocore-contribution-proof-v1`

---

## ⚡️ Key Capabilities

* 🛡 **CI/CD Quality Gate**: Rejects unverified or tampered contribution proofs in GitHub Actions workflows.
* 🔄 **Git HEAD Drift Detection**: Warns developers when documentation or code changes require a refreshed signature.
* 🪝 **Pre-Commit Ready**: Can be plugged directly into local Git hooks (`.git/hooks/pre-commit`).

---

## 🚀 Quickstart

```bash
# 1. Clone repository
git clone https://github.com/zwf5458/FLOP-Proof-Verifier-Action.git
cd FLOP-Proof-Verifier-Action

# 2. Run local audit against your proof file
python3 scripts/verify_proof_ci.py path/to/contribution-proof.json

# 3. Enforce strict match against current Git HEAD
python3 scripts/verify_proof_ci.py --strict-head path/to/contribution-proof.json
```

---

## ⚖️ License
Released under the [MIT License](LICENSE).
