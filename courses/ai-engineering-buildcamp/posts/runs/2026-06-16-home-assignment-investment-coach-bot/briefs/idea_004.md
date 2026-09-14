# idea_004: Evaluate both the answer and the trajectory

Angle: Agent evals should check both final output and the path the agent took to produce it.

Source moments:
- 01:45:18-01:47:27: Eval scenarios include input, expected output, actual output, a judge, and tool-call trajectory.
- 01:49:32-01:51:38: The README should be transparent about scenarios, limitations, tests, evals, and generated code.

Post notes:
- Explain "trajectory" simply: the sequence of tool calls before the answer.
- Keep this practical and not research-heavy.
- Show why output-only evals can miss the wrong tool path.
