#config server

package { 'nginx':
  ensure => present,
}
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx_config/nginx.conf.erb'),
  require => Package['nginx'],
  notify => Service['nginx'],
}
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}
file { '/var/www/html/404.html':
  ensure  => file,
  content => 'Ceci n'est pas une page',
  require => Package['nginx'],
}
nginx::resource::location { 'redirect_me':
  location    => '/redirect_me',
  ensure      => present,
  server      => 'default',
  server_name => '_',
  rewrite     => 'permanent / http://google.com/', 
  require     => Package['nginx'],
  notify      => Service['nginx'],
}
