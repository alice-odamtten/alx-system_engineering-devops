# using Puppet to make changes to our configuration file
file_line{'Set alias name':
  path => '/etc/ssh/ssh_config',
  line => 'Host 100.25.12.128
    HostName 100.25.12.128
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
}
