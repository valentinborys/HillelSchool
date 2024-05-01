import unittest
import logging
from homework10  import log_event

class TestLogEvent(unittest.TestCase):

    def test_success_logging(self):
        log_event("user1", "success")
        with open('login_system.log', 'r') as f:
            last_line = f.readlines()[-1]
            self.assertTrue("Username: user1" in last_line)
            self.assertTrue("Status: success" in last_line)

    def test_expired_logging(self):
        log_event("user2", "expired")
        with open('login_system.log', 'r') as f:
            last_line = f.readlines()[-1]
            self.assertTrue("Username: user2" in last_line)
            self.assertTrue("Status: expired" in last_line)

    def test_failed_logging(self):
        log_event("user3", "failed")
        with open('login_system.log', 'r') as f:
            last_line = f.readlines()[-1]
            self.assertTrue("Username: user3" in last_line)
            self.assertTrue("Status: failed" in last_line)

if __name__ == '__main__':
    unittest.main()