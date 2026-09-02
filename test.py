#!/usr/bin/env python

"""Transparent public tests for PGE 323M Assignment 3."""

from math import isclose
from pathlib import Path
import re
import unittest

from assignment3 import (
    add_well_activity,
    add_well_activity_from_file,
    get_bhp_well_values,
    get_bhp_well_values_from_file,
    read_well_activity,
    read_well_parameters,
    water_rel_perm,
)


class TestAgentInstructions(unittest.TestCase):
    def test_required_contract(self):
        path = Path("AGENTS.md")
        self.assertTrue(path.is_file(), "Create AGENTS.md at the repository root")

        text = " ".join(path.read_text(encoding="utf-8").lower().split())
        required = (
            "submit assignment 3",
            "wait for approval",
            "do not edit",
            "readme.md",
            "test.py",
            "well_activity.csv",
            "wells.yml",
            "assignment3.py",
            "agents.md",
            "environment.yml",
            ".gitignore",
            ".github/",
            ".devcontainer/",
            "python -m unittest -v",
            "git status --short",
            "git diff --check",
            "git add -- agents.md assignment3.py",
            "git commit",
            "git push",
            "github actions",
            "never bypass",
            "stop",
        )
        for fragment in required:
            self.assertIn(fragment, text, f"AGENTS.md is missing: {fragment}")

        self.assertIsNone(
            re.search(r"\bgit\s+add\s+\.(?:\s|$)", text),
            "AGENTS.md must not use broad staging with 'git add .'",
        )


class TestAssignment3Public(unittest.TestCase):
    def test_water_rel_perm(self):
        actual = water_rel_perm(0.6, 0.2, 0.2, 3)
        expected = (0.0, 0.075, 0.6)
        self.assertEqual(len(actual), 3)
        for value, target in zip(actual, expected):
            self.assertTrue(isclose(value, target, abs_tol=1.0e-12))

    def test_read_well_activity(self):
        records = read_well_activity("well_activity.csv")
        self.assertEqual(records[0], ["well1", "producing", "0"])
        self.assertEqual(records[-1], ["well3", "shut-in", "7000"])
        self.assertEqual(len(records), 9)

    def test_add_well_activity(self):
        records = [["well1", "producing", "0"]]
        result = add_well_activity(records, "well2", "shut-in", 100)
        result = add_well_activity(result, "well3", "injecting", "10")
        self.assertIs(result, records)
        self.assertEqual(
            result,
            [
                ["well1", "producing", "0"],
                ["well3", "injecting", "10"],
                ["well2", "shut-in", "100"],
            ],
        )

    def test_add_well_activity_from_file(self):
        result = add_well_activity_from_file(
            "well_activity.csv", "well4", "injecting", 1000
        )
        self.assertEqual(result[3], ["well4", "injecting", "1000"])
        self.assertEqual([int(record[2]) for record in result], sorted(int(record[2]) for record in result))

    def test_read_well_parameters(self):
        parameters = read_well_parameters("wells.yml")
        self.assertIn("rate", parameters["wells"])
        self.assertIn("bhp", parameters["wells"])

    def test_get_bhp_well_values(self):
        parameters = {"wells": {"bhp": {"values": 10.0}}}
        self.assertEqual(get_bhp_well_values(parameters), 10.0)

    def test_get_bhp_well_values_from_file(self):
        self.assertEqual(
            get_bhp_well_values_from_file("wells.yml"),
            [2200.0, 2000.0],
        )


if __name__ == "__main__":
    unittest.main()
