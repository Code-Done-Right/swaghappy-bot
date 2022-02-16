import hikari as swagcat
import lightbulb as swaghappy
from secrets import SWAGHAPPY

intents = swagcat.Intents.ALL
swaghappy_bot = swaghappy.BotApp(
    token = SWAGHAPPY,
    intents = intents
)

@swaghappy_bot.listen(swagcat.MemberCreateEvent)
async def on_server_join(event):
    await event.member.add_role(
        942361322094465054
    )
    
swaghappy_bot.run()