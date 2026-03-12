#!/usr/bin/env python3
"""
Long-Running Agent Harness

Orchestrates multiple AI agent sessions to complete complex projects.
Based on Anthropic's research on effective agent harnesses.

Usage:
    python harness.py init     # Run initial setup
    python harness.py status   # Check current progress
    python harness.py next     # Get next feature to work on
"""

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


class Harness:
    """Manages the long-running agent workflow."""

    def __init__(self, project_dir: str = "."):
        self.project_dir = Path(project_dir)
        self.feature_file = self.project_dir / "feature_list.json"
        self.progress_file = self.project_dir / "claude-progress.txt"
        self.init_script = self.project_dir / "init.sh"

    def _load_features(self) -> dict[str, Any]:
        """Load and parse feature_list.json."""
        if not self.feature_file.exists():
            return {"features": [], "metadata": {}}
        with open(self.feature_file) as f:
            return json.load(f)

    def _save_features(self, data: dict) -> None:
        """Save feature_list.json."""
        with open(self.feature_file, "w") as f:
            json.dump(data, f, indent=2)

    def _append_progress(self, message: str) -> None:
        """Append message to progress log."""
        timestamp = datetime.now().isoformat()
        with open(self.progress_file, "a") as f:
            f.write(f"\n[{timestamp}] {message}\n")

    def init(self) -> None:
        """Initialize the harness structure."""
        print("=== Initializing Long-Running Agent Harness ===\n")

        # Create feature_list.json if it doesn't exist
        if not self.feature_file.exists():
            template = {
                "project_name": "",
                "description": "",
                "features": [],
                "metadata": {
                    "version": "1.0.0",
                    "initialized": datetime.now().isoformat()
                }
            }
            self._save_features(template)
            print(f"Created: {self.feature_file}")

        # Create claude-progress.txt if it doesn't exist
        if not self.progress_file.exists():
            header = """================================================================================
PROJECT PROGRESS LOG
================================================================================

"""
            with open(self.progress_file, "w") as f:
                f.write(header)
            print(f"Created: {self.progress_file}")

        # Make init.sh executable
        if self.init_script.exists():
            self.init_script.chmod(0o755)
            print(f"Made executable: {self.init_script}")

        print("\nNext steps:")
        print("1. Edit feature_list.json with your project features")
        print("2. Customize init.sh for your project")
        print("3. Run: python harness.py status")

    def status(self) -> None:
        """Display current project status."""
        data = self._load_features()
        features = data.get("features", [])

        if not features:
            print("No features defined. Run 'python harness.py init' first.")
            return

        total = len(features)
        passing = sum(1 for f in features if f.get("passes", False))
        remaining = total - passing

        print(f"\n=== {data.get('project_name', 'Project')} Status ===\n")
        print(f"Total features: {total}")
        print(f"Completed: {passing} ({100 * passing // total}%)")
        print(f"Remaining: {remaining}")
        print()

        # Group by category
        by_category: dict[str, list] = {}
        for f in features:
            cat = f.get("category", "uncategorized")
            by_category.setdefault(cat, []).append(f)

        print("Features by category:")
        for cat, feats in sorted(by_category.items()):
            done = sum(1 for f in feats if f.get("passes", False))
            print(f"  {cat}: {done}/{len(feats)} complete")
            for f in feats:
                status = "PASS" if f.get("passes") else "FAIL"
                print(f"    [{status}] {f['id']}: {f['description'][:50]}")

    def next_feature(self) -> None:
        """Suggest the next feature to work on."""
        data = self._load_features()
        features = data.get("features", [])

        incomplete = [f for f in features if not f.get("passes", False)]

        if not incomplete:
            print("\n=== ALL FEATURES COMPLETE ===")
            print("Review feature_list.json and verify everything works!")
            return

        # Prioritize by category order
        category_priority = {
            "infrastructure": 0,
            "core": 1,
            "feature": 2,
            "polish": 3,
            "uncategorized": 4
        }

        incomplete.sort(
            key=lambda f: category_priority.get(f.get("category"), 4)
        )

        next_f = incomplete[0]

        print(f"\n=== Next Feature: {next_f['id']} ===\n")
        print(f"Category: {next_f.get('category', 'uncategorized')}")
        print(f"Description: {next_f['description']}")
        print(f"\nSteps:")
        for i, step in enumerate(next_f.get("steps", []), 1):
            print(f"  {i}. {step}")
        print(f"\nNotes: {next_f.get('notes', 'None')}")

    def complete_feature(self, feature_id: str, notes: str = "") -> None:
        """Mark a feature as complete."""
        data = self._load_features()

        for f in data.get("features", []):
            if f["id"] == feature_id:
                f["passes"] = True
                f["completed_at"] = datetime.now().isoformat()
                if notes:
                    f["notes"] = notes
                break
        else:
            print(f"Feature {feature_id} not found!")
            return

        # Update metadata
        completed = sum(1 for f in data["features"] if f.get("passes"))
        data["metadata"]["completed_features"] = completed
        data["metadata"]["last_updated"] = datetime.now().isoformat()

        self._save_features(data)
        self._append_progress(f"Completed feature {feature_id}: {notes}")

        print(f"Marked {feature_id} as complete!")

    def agent_session(self) -> None:
        """Run a complete agent session workflow."""
        print("=== Agent Session Starting ===\n")

        # Step 1: Get bearings
        print("1. Getting bearings...")
        subprocess.run(["bash", "-c", "pwd"])

        # Step 2: Run init script
        if self.init_script.exists():
            print("\n2. Running init.sh...")
            subprocess.run(["bash", str(self.init_script)])

        # Step 3: Check status
        print("\n3. Current status:")
        self.status()

        # Step 4: Suggest next work
        print("\n4. Recommended next action:")
        self.next_feature()

        print("\n=== Agent Session Ready ===")
        print("Follow the prompts and remember: ONE feature at a time!")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nCommands: init, status, next, complete <id> [notes], session")
        sys.exit(1)

    command = sys.argv[1]
    harness = Harness()

    if command == "init":
        harness.init()
    elif command == "status":
        harness.status()
    elif command == "next":
        harness.next_feature()
    elif command == "complete":
        if len(sys.argv) < 3:
            print("Usage: python harness.py complete <feature_id> [notes]")
            sys.exit(1)
        notes = " ".join(sys.argv[3:]) if len(sys.argv) > 3 else ""
        harness.complete_feature(sys.argv[2], notes)
    elif command == "session":
        harness.agent_session()
    else:
        print(f"Unknown command: {command}")
        print("Commands: init, status, next, complete, session")


if __name__ == "__main__":
    main()
