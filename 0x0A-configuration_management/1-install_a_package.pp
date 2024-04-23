# install a specific version of flask (2.1.0)
exec { 'install_flask_2.1.0':
	command => 'pip3 install Flask==2.1.0',
	path	=> ['/usr/local/bin', '/usr/bin'],
}
