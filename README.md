pngbot
========
pngbot is a bot designed to combine two png images so that they appear differently when expanded.  this is a "quirk" which surfaces due to the fact that most image viewers change the background color between thumbnail and fullsize view states. I've observed that it works on twitter, tumblr, and also on iphones!</br>
examples:</br>
<ul>
   <li>http://twitter.com/pngbot</li>
   <li>http://pngbot.tumblr.com</li>
</ul>
i first encountered this effect via twitter user <a href="http://twitter.com/taki_bump">@taki_bump</a></br>
ex: <a href="https://twitter.com/taki_bump/status/376313959969599488/photo/1"><img title="example" src="https://pbs.twimg.com/media/BTjvjYRCMAAXOYV.png:small" width="250"> </a>
i only managed to replicate the effect after lots of coffee, trial and error with photoshop layers, and many different imagemagick options...</br>

<b>Operation:</b> </br>
<ul>
	<li>first it will check for new mentions and download the image attachments to the working directory as png0.png and png1.png.</li>
	<li>next it will call the shell script to do the imagemagick conversion and composite commands. if the mention provides only one image, it uses default.png as the 1st image.</li>
	<li>mentions are logged to a file called mentionlog.txt in the working directory.</li> 
</ul>

<b>APIs/ Prerequisites:</b> </br>
<ul>
	<li>Twitter (tweepy) https://github.com/tweepy/tweepy</li>
	<li>Tumblr (pytumblr) https://github.com/tumblr/pytumblr</li>
	<li>Python - Tested with version: 2.7.5</li>
	<li>ImageMagick - Tested with version: 6.7.8.9-10</li>
</ul>
</br>

<b>Scheduling via Cron:</b> </br>
        `*/5 * * * * * your-username python /path-to-your-script/pngbot.py >> /path-to-your-script/pngbot.log 2>&1` </br>
<b> To Do:</b>
<ul>
	<li> get conversion and composite commands working with wand or some other imagemagick python wrapper so I don't need to use a shell script.  :)</li>
</ul>
