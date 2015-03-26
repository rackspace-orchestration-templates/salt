from fabric.api import env, task
from envassert import detect, package, port, process, service
from hot.utils.test import get_artifacts


@task
def check_master():
    env.platform_family = detect.detect()

    packages = [
        'salt-master',
        'salt-cloud'
    ]

    for pkg in packages:
        assert package.installed(pkg), 'package %s not installed' % pkg

    port_services = [
        (4505, 'python'),
        (4506, 'python')
    ]

    for prt in port_services:
        assert port.is_listening(prt[0]), 'port %i/%s is not listening' % prt

    assert process.is_up("salt-master"), "salt-master process is not up"
    assert service.is_enabled("salt-master"), "salt-master is not enabled"


@task
def artifacts():
    env.platform_family = detect.detect()
    get_artifacts()
