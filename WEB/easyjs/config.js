var config = {};

config.secret_password = "x"

// Debug session_keys
config.session_keys = [ 
	`REAL_PASSWORD_C4n0t_GU3SS${Math.random()}`,
	`REAL_PASSWORD_C4n0t_GU3SS${Math.random()}`, 
	`REAL_PASSWORD_C4n0t_GU3SS${Math.random()}` 
];


module.exports = config;
