// Packages

const Discord = require('discord.js');
const config = require('./config.json');
const { prefix, token } = require('./config.json');
const client = new Discord.Client();


// On Start
client.once('ready', () => {
	console.log('Ready!');
});


// Commands
client.on('message', message => {
	if (message.content === `${prefix}ping`) {
		message.channel.send('Pong.');
	} else if (message.content === `${prefix}beep`) {
		message.channel.send('Boop.');
	} else if (message.content === `${prefix}server`)
		message.channel.send(`This sever's name is: **${message.guild.name}**`);
});


// Token
client.login(token);