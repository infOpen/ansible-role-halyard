"""
Role tests
"""

import os
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_user(host):
    """
    Ensure halyard user exists
    """

    user = host.user('halyard')

    assert user.home == '/var/lib/halyard'
    assert user.group == 'halyard'


def test_cli(host):
    """
    Ensure Halyard is installed and available
    """

    assert host.run_expect([0], 'hal --ready')
