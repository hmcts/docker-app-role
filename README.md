Role Name
=========

An Ansible role for installing applications in Docker environment using `docker-compose.yml` files.

Requirements
------------

This role requires the following tools to be installed and available in the system PATH:

- [docker-machine](https://docs.docker.com/machine/)
- [docker-compose](https://docs.docker.com/compose/)

Role Variables
--------------

Applications are defined as a list in the `docker_apps` variable.

```yaml
  docker_apps:
    - name: sample-application
```

By convention role expects application `docker-compose.yml` file to be in `templates/{{ docker_app.name }}` directory.

For example sample application declarted above will use `templates/sample-application/docker-compose.yml` for application deployment.

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
  - hosts: servers
    roles:
      - { role: devops.docker-app, docker_apps: [name: sample-application] }
```

Tests
---------------

Tests are run using [molecule](https://github.com/metacloud/molecule) and [docker](https://www.docker.com).

```bash
$ molecule test
```

License
-------

MIT

Author Information
------------------

HMCTS CMC Team