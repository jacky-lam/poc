application/use_cases:

Contains specific application workflows (“Use Cases”). For example, complete_assignment_use_case.py implements the logic:

1. Mark an assignment as “complete.”
2. Check if the experiment is now fully complete.
3. Update the experiment status accordingly.

This orchestrates multiple domain entities (e.g., fetch the assignment, fetch other assignments in the same experiment, fetch experiment, then apply domain methods).
