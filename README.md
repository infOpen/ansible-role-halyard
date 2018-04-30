# halyard

[![Build Status](https://img.shields.io/travis/infOpen/ansible-role-halyard/master.svg?label=travis_master)](https://travis-ci.org/infOpen/ansible-role-halyard)
[![Build Status](https://img.shields.io/travis/infOpen/ansible-role-halyard/develop.svg?label=travis_develop)](https://travis-ci.org/infOpen/ansible-role-halyard)
[![Updates](https://pyup.io/repos/github/infOpen/ansible-role-halyard/shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-halyard/)
[![Python 3](https://pyup.io/repos/github/infOpen/ansible-role-halyard/python-3-shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-halyard/)
[![Ansible Role](https://img.shields.io/ansible/role/25377.svg)](https://galaxy.ansible.com/infOpen/halyard/)

Install halyard package.

## Requirements

This role requires Ansible 2.2 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Trusty
- Ubuntu Xenial

and use:
- Ansible 2.2.x
- Ansible 2.3.x
- Ansible 2.4.x
- Ansible 2.5.x

### Running tests

#### Using Docker driver

```
$ tox
```

## Role Variables

### Default role variables

``` yaml
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infOpen.halyard }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
