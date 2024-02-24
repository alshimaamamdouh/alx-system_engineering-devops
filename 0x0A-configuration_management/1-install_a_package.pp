# Install Flask using pip3

exec { 'install_flask':
command => '/usr/bin/pip3 install flask==2.1.0',
path    => '/usr/local/bin:/usr/bin',
creates => '/usr/lib/python3/dist-packages/flask',
require => Package['python3-pip'],
}
