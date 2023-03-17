<h2>Simple telegram bot</h2>
<h4>Codename: Charles</h4>
<img src="img/readme_terminator.jpg">
<h6>version: 0.2</h6>
<h6>status: in dev</h6>
<br>
<h6>Introduce</h6>
<p>
Simple telegram bot wich has minimum functionality.
Main feature is that bot can collect all system info about
device where he's situated (In future he's get more functions).
</p>
<h6>Update v0.2</h6>
<p>
Chatbot moved to OpenAi Chat gpt 3.5 turbo
</p>
<h6>Installing</h6>
<p>
Enviroment: Install <strong>python 3</strong> or higher and <strong>pip</strong> 
first of all you need to install Telegram bot library
   <code>pip install pytelegrambotapi</code> or like in my case <code>pip3 install pytelegrambotapi</code>
   Then go to telegram and find uset BotFather and type <code>/newbot</code>
   enter name and bot_code and that's all, bot will be created and Bot father will send you bot api.
   <strong>Get this api and set it in __project_root_/core/config on api_key field</strong>
   Also you can insert owner id. Check in /help how it works.
   And then just run execute (main.py) script by using <code>python3 your_script.py</code>
</p>