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

To simply install latest LTS version:

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




## Development & Testing

If you want to work on this role, please start with running
`make watch`. This will re-provision vagrant box on any file changes.
