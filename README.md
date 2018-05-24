pngbot
========
pngbot is a bot designed to combine two png images in one so that it appears as the 1st image in preview and the 2nd in  fullsize view.  This is possible due to the fact that image viewers usually change the background color between white (or some shade of white) for thumbnail to black in fullsize view states. I've observed that it works on twitter, tumblr, and also on iPhones!</br>
examples:</br>
<ul>
   <li>http://twitter.com/pngbot</li>
   <li>http://pngbot.tumblr.com</li>
</ul>
I first encountered this effect via twitter user @taki_bump, but as of 2018, the account seems to have been deleted or renamed?</br>
ex:</br>
<a href="https://stevecvar.com/wp-content/uploads/2018/05/b2mymo2efbnpkfqvcrib.png" target="_new"><img title="taki_bump example" src="https://stevecvar.com/wp-content/uploads/2018/05/b2mymo2efbnpkfqvcrib.png" width="250">  Click to view alternate Image</a></br>

<b>Operation:</b> </br>
<ul>
	<li>First it checks for new mentions and downloads the image attachments to the working directory as png0.png and png1.png.</li>
	<li>Next it will call the shell script to do the imagemagick conversion and composite commands. If the mention provides only one image, it uses default.png as the 1st image.</li>
	<li>Mentions are logged to a file called mentionlog.txt in the working directory.</li> 
</ul>

<b>APIs/ Prerequisites:</b> </br>
<ul>
	<li>Twitter (tweepy) https://github.com/tweepy/tweepy</li>
	<li>Tumblr (pytumblr) https://github.com/tumblr/pytumblr</li> 
	<li>Python - Tested with version: 2.7.5</li>
	<li>ImageMagick - Tested with version: 6.7.8.9-10</li>
</ul>
