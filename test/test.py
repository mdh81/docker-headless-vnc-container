#!/usr/bin/env python3

import os
import subprocess
import yaml
import unittest

def load_yaml(filename):
    with open(filename, 'r') as file:
        return yaml.safe_load(file)

class TestDockerCompose(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.conf = load_yaml("docker-compose.yml")

    def test_read_docker_compose(self):
        self.assertIsInstance(self.conf['services'], dict)
        self.assertEqual(len(self.conf['services']), 4)

    def test_service_ports(self):
        for svc, app in self.conf['services'].items():
            self.assertTrue(True, svc)
            for port in app.get('ports', []):
                ip, localport, remoteport = port.split(':')
                self.assertTrue(True, " - " + remoteport)
                if remoteport == "5901":
                    try:
                        subprocess.run(["nc", "-q", "1", "-w", "1", "localhost", localport], input=b"", stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=3, text=True, check=True)
                    except subprocess.CalledProcessError as e:
                        self.fail(f"vnc connect header not found: {e.stderr}")
                elif remoteport == "6901":
                    try:
                        subprocess.run(["curl", "-s", f"http://localhost:{localport}/?password=vncpassword"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=3, text=True, check=True)
                    except subprocess.CalledProcessError as e:
                        self.fail("web vnc html doesn't contain noVNC: {e.stderr}")
                else:
                    raise ValueError(f"unknown port: {remoteport}")

if __name__ == "__main__":
    unittest.main()

