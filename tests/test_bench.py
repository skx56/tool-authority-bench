import unittest

from bench import judge, run, safe_agent, unsafe_agent


class ToolAuthorityTest(unittest.TestCase):
    def test_safe_agent_passes(self) -> None:
        ok, reason = judge(run(safe_agent))
        self.assertTrue(ok, reason)

    def test_unsafe_agent_fails(self) -> None:
        ok, reason = judge(run(unsafe_agent))
        self.assertFalse(ok, reason)
        self.assertIn("send", reason)


if __name__ == "__main__":
    unittest.main()
