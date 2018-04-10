import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nodejs_version(host):
    assert 'v4.' in host.run('node --version').stdout


def test_npm_packes(host):
    npm_packages = host.run('npm ls -g --depth=0 -p').stdout
    assert '/async' in npm_packages
    assert '/debug' in npm_packages
