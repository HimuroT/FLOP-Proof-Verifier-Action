# Security & CI/CD Pipeline Policy

## 🔒 Security Standards for Technocore Proof Verifier Action

The **FLOP-Proof-Verifier-Action** repository provides automated CI/CD and pre-commit validation for decentralized contribution proofs across the Arthur Hayes FLOP Network and Technocore ecosystem. Because CI runners execute arbitrary pull request triggers, strict pipeline hygiene is enforced.

---

### 1. Minimal GitHub Actions Permissions

Workflow definitions provided in `templates/verify_proof.yml` enforce least-privilege permission scoping:
```yaml
permissions:
  contents: read
```
Workflows strictly forbid write access (`contents: write`) or administrative permissions, preventing privilege escalation from untrusted third-party pull requests.

---

### 2. Supply-Chain & Integrity Protections

* **Immutable Commit SHA Verification**: Proof verifiers check against strictly 40-character hexadecimal git commit hashes. Truncated or malformed hashes are immediately rejected.
* **Deterministic Ed25519 Cryptography**: Signatures are checked using standard multi-format decoding against the contributor's public `did:key` without downloading dynamic remote code at runtime whenever local tools are present.
* **Zero Secret Requirements**: Proof verification does not require GitHub access tokens or private keys to run.

---

### 3. Supported Versions

| Version | Supported          | Security Status |
| :---    | :---               | :---            |
| 1.1.x   | :white_check_mark: | Active Maintenance |
| 1.0.x   | :white_check_mark: | Maintenance Only |
| < 1.0   | :x:                | Deprecated |

---

### 4. Vulnerability Disclosure & Incident Response

If you find a security hole in the proof parser, pre-commit hook, or CI runner script:

* **Primary Maintainer DID (Tab 4 rabisu)**:  
  `did:key:z6Mkr2HtFjzrenM57Nh8hKdMuLdC5HaD44BUoL7zmRCvr16r`
* **Maintainer Namespace**: `zwf5458/FLOP-Proof-Verifier-Action`
* **Disclosure Method**: Do not publish security issues publicly. Contact node operators directly via Technocore node room or designated maintainer email. Reports will receive acknowledgement within 24 hours.
