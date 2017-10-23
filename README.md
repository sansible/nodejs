# nodejsjs

Master: [![Build Status](https://travis-ci.org/sansible/nodejs.svg?branch=master)](https://travis-ci.org/sansible/nodejs)  
Develop: [![Build Status](https://travis-ci.org/sansible/nodejs.svg?branch=develop)](https://travis-ci.org/sansible/nodejs)

* [ansible.cfg](#ansible-cfg)
* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)
* [Development & Testing](#development---testing)

This role installs and configures nodejs from NodeSource on Debian based systems.




## ansible.cfg

This role is designed to work with merge "hash_behaviour". Make sure your
ansible.cfg contains these settings

```INI
[defaults]
hash_behaviour = merge
```




## Installation and Dependencies

To install this role run `ansible-galaxy install sansible.nodejs`
or add this to your `roles.yml`

```YAML
- name: sansible.nodejs
  version: v1.0
```

and run `ansible-galaxy install -p ./roles -r roles.yml`




## Tags

This role uses two tags: **build** and **configure**

* `build` - Installs nodejs.
* `configure` - does nothing (for now).




## Examples

Simply install latest LTS version.

```YAML
- name: Install Node.js
  hosts: sandbox

  pre_tasks:
    - name: Update apt
      become: yes
      apt:
        cache_valid_time: 1800
        update_cache: yes
      tags:
        - build

  roles:
    - role: sansible.nodejs
      nodejs:
        version: 4
```

Install latest LTS version, latest lorem-ipsum and v0.15.3 of forever NPMs.
NPM installation accepts the same arguments as the [Ansible npm module](http://docs.ansible.com/ansible/latest/npm_module.html),
with the exception that `global` is set to `yes` by default.

```YAML
- name: Install Node.js
  hosts: sandbox

  pre_tasks:
    - name: Update apt
      become: yes
      apt:
        cache_valid_time: 1800
        update_cache: yes
      tags:
        - build

  roles:
    - role: sansible.nodejs
      nodejs:
        version: 4
        npms:
          - name: lorem-ipsum
          - name: forever
            version: '0.15.3'
```

When using this role you may encounter permission issues when running 
commands such as NPM as a non-root user (see
[fixing npm permissions](https://docs.npmjs.com/getting-started/fixing-npm-permissions) 
for more information). To fix permissions for a particular user you can 
pass in their name like so:

```YAML
- name: Install Node.js
  hosts: sandbox

  pre_tasks:
    - name: Update apt
      become: yes
      apt:
        cache_valid_time: 1800
        update_cache: yes
      tags:
        - build

  roles:
    - role: sansible.nodejs
      nodejs:
        version: 4
        workspace_user: some_user
```




## Development & Testing

If you want to work on this role, please start with running
`make watch`. This will re-provision vagrant box on any file changes.
