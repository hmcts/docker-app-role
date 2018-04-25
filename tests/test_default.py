from setup import inventory

testinfra_hosts = inventory.get_hosts('all')


def test_application_directory_exists(File):
    f = File('/opt/registry')

    assert f.exists
    assert f.is_directory
    assert f.user == 'root'
    assert f.group == 'docker'


def test_application_file_exixts(File):
    f = File('/opt/registry/docker-compose.yml')

    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'docker'


def test_application_is_started(Command):
    cmd = Command('pgrep -f registry')

    assert cmd.rc == 0
