# execute killmenow command
exec { 'killmenow':
	command  => '/usr/bin/pkill killmenow',
	provider => 'shell',
	returns  => [0, 1]
}
