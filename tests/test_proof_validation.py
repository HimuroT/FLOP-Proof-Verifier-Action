#!/usr/bin/env python3
"""
Unit tests for Technocore Proof Verifier CI logic and Pre-Commit hook.
"""

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.pre_commit_hook import check_proof_file


class TestProofValidation(unittest.TestCase):

    def setUp(self):
        self.temp_dir = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_missing_file(self):
        non_existent = self.temp_dir / "missing.json"
        ok, msg = check_proof_file(non_existent)
        self.assertFalse(ok)
        self.assertIn("does not exist", msg)

    def test_invalid_json(self):
        bad_json = self.temp_dir / "bad.json"
        bad_json.write_text("{ unquoted_key: 123", encoding="utf-8")
        ok, msg = check_proof_file(bad_json)
        self.assertFalse(ok)
        self.assertIn("Invalid JSON syntax", msg)

    def test_missing_fields(self):
        incomplete = self.temp_dir / "incomplete.json"
        incomplete.write_text(json.dumps({
            "did": "did:key:z6Mk...",
            "commit": "08f6da1c6594c583e7bc3875277b0b35139c2dfd"
        }), encoding="utf-8")
        ok, msg = check_proof_file(incomplete)
        self.assertFalse(ok)
        self.assertIn("Missing or empty required field", msg)

    def test_invalid_commit_length(self):
        short_commit = self.temp_dir / "short_commit.json"
        short_commit.write_text(json.dumps({
            "did": "did:key:z6Mkr2HtFjzrenM57Nh8hKdMuLdC5HaD44BUoL7zmRCvr16r",
            "type": "technocore-contribution-proof-v1",
            "artifact_url": "https://github.com/zwf5458/FLOP-Proof-Verifier-Action",
            "commit": "08f6da1", # Only 7 chars
            "signature": "mock_sig_xyz",
            "signed_at": "2026-09-30T10:00:00Z"
        }), encoding="utf-8")
        ok, msg = check_proof_file(short_commit)
        self.assertFalse(ok)
        self.assertIn("Must be exactly 40 hex characters", msg)

    def test_valid_proof(self):
        valid = self.temp_dir / "valid.json"
        valid.write_text(json.dumps({
            "did": "did:key:z6Mkr2HtFjzrenM57Nh8hKdMuLdC5HaD44BUoL7zmRCvr16r",
            "type": "technocore-contribution-proof-v1",
            "artifact_url": "https://github.com/zwf5458/FLOP-Proof-Verifier-Action",
            "commit": "08f6da1c6594c583e7bc3875277b0b35139c2dfd",
            "signature": "valid_signature_placeholder",
            "signed_at": "2026-09-30T10:00:00Z"
        }), encoding="utf-8")
        ok, msg = check_proof_file(valid)
        self.assertTrue(ok)
        self.assertIn("verified", msg)


if __name__ == "__main__":
    unittest.main()
