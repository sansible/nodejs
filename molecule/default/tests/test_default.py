import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nodejs_version(host):
    codename = host.system_info.codename
    if codename == 'trusty':
        assert 'v4.' in host.check_output('node --version')
    elif codename == 'xenial':
        assert 'v7.' in host.check_output('node --version')
    elif codename == 'bionic':
        assert 'v10.' in host.check_output('node --version')


def test_npm_packes(host):
    codename = host.system_info.codename

    if codename == 'trusty':
        assert host.file('/usr/lib/node_modules/lorem-ipsum/').is_directory
        assert host.file('/root/.npm-local/node_modules/debug/').is_directory
    elif codename == 'xenial' or codename == 'bionic':
        assert host.file(
            '/home/nodejs_test/.npm-global/lib/node_modules/lorem-ipsum/'
        ).is_directory
        assert host.file(
            '/home/nodejs_test/.npm-local/node_modules/debug/'
        ).is_directory


def test_npm_prefix(host):
    codename = host.system_info.codename
    if codename == 'xenial' or codename == 'bionic':
        assert host.file(
            '/home/nodejs_test/.npmrc'
        ).contains('prefix=/home/nodejs_test/.npm-global')
