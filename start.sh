export BOTVERSION=0.1

sudo pip install discord.py

git clone https://github.com/Jklars/ebot.git

cd ebot

export NEWVERSION=$(<version)

python3 checkver.py 0.1 $NEWVERSION

export ISNEW=$(<isnew)

if [$ISNEW == True]
    then
        cp * ..
fi

cd ..
rm ebot

python3 basic_bot.py
