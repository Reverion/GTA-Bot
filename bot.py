import discord
from discord.ext import commands
import asyncio
import time


description = "Nothing special"
bot = commands.Bot(command_prefix='**', description=description)


@bot.event
async def on_ready():
    print("Bot is launched, ")


#!aw @user nickname IGN




@bot.command()
async def awpc(member: discord.Member, tr_nick, IGN):
            
            #translates and sets the nick
            
            dict = str.maketrans("qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM", "qʷᵉʳᵗʸᵘⁱᵒᵖᵃˢᵈᶠᵍʰʲᵏˡᶻˣᶜᵛᵇⁿᵐ¹²³⁴⁵⁶⁷⁸⁹⁰Qᵂᴱᴿᵀʸᵁᴵᴼᴾᴬˢᴰᶠᴳᴴᴶᴷᴸᶻˣᶜⱽᴮᴺᴹ")
            value= tr_nick
            nick_nick = value.translate(dict)
            print(nick_nick)
            nickname= "%s (%s)" % (nick_nick, IGN)
            pc = discord.utils.get(member.server.roles, name="PC")
            verified = discord.utils.get(member.server.roles, name="Verified")
            agent = discord.utils.get(member.server.roles, name = "Agent")
            unverified = discord.utils.get(member.server.roles, name = "Unverified")

            await bot.remove_roles(member, unverified)
            await bot.change_nickname(member, "%s" % (nickname))
            await bot.add_roles(member, pc) #verified
            await bot.add_roles(member, verified) #verified
            await bot.add_roles(member, agent) #Agent

            general_chat = discord.utils.get(member.server.channels, name = "general-chat")

            await bot.send_message(general_chat, "Hello {}!, welcome in. Send requests in <#272479360563544075> or in <#387362971585871882> using `@everyone`to find people to play with.\nIf there are any problems, feel free to DM <@389760103462600705> and the message will automatically be forwarded to Staff.".format(member.mention))                                                                


@bot.command()
async def awps4(member: discord.Member, tr_nick, IGN):
            
            #translates and sets the nick
            
            dict = str.maketrans("qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM", "qʷᵉʳᵗʸᵘⁱᵒᵖᵃˢᵈᶠᵍʰʲᵏˡᶻˣᶜᵛᵇⁿᵐ¹²³⁴⁵⁶⁷⁸⁹⁰Qᵂᴱᴿᵀʸᵁᴵᴼᴾᴬˢᴰᶠᴳᴴᴶᴷᴸᶻˣᶜⱽᴮᴺᴹ")
            value= tr_nick
            nick_nick = value.translate(dict)
            print(nick_nick)
            nickname= "%s (%s)" % (nick_nick, IGN)
            ps4 = discord.utils.get(member.server.roles, name="PS4")
            verified = discord.utils.get(member.server.roles, name="Verified")
            agent = discord.utils.get(member.server.roles, name = "Agent")
            unverified = discord.utils.get(member.server.roles, name = "Unverified")

            await bot.remove_roles(member, unverified)
            await bot.change_nickname(member, "%s" % (nickname))
            await bot.add_roles(member, ps4) #verified
            await bot.add_roles(member, verified) #verified
            await bot.add_roles(member, agent) #Agent

            general_chat = discord.utils.get(member.server.channels, name = "general-chat")

            await bot.send_message(general_chat, "Hello {}!, welcome in. Send requests in <#422480850009980928> or in <#422481018407354376> using `@everyone`to find people to play with.\nIf there are any problems, feel free to DM <@389760103462600705> and the message will automatically be forwarded to Staff.".format(member.mention))                                                                

@bot.command()
async def awxb1(member: discord.Member, tr_nick, IGN):
            
            #translates and sets the nick
            
            dict = str.maketrans("qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM", "qʷᵉʳᵗʸᵘⁱᵒᵖᵃˢᵈᶠᵍʰʲᵏˡᶻˣᶜᵛᵇⁿᵐ¹²³⁴⁵⁶⁷⁸⁹⁰Qᵂᴱᴿᵀʸᵁᴵᴼᴾᴬˢᴰᶠᴳᴴᴶᴷᴸᶻˣᶜⱽᴮᴺᴹ")
            value= tr_nick
            nick_nick = value.translate(dict)
            print(nick_nick)
            nickname= "%s (%s)" % (nick_nick, IGN)
            xb1 = discord.utils.get(member.server.roles, name="XB1")
            verified = discord.utils.get(member.server.roles, name="Verified")
            agent = discord.utils.get(member.server.roles, name = "Agent")
            unverified = discord.utils.get(member.server.roles, name = "Unverified")

            await bot.remove_roles(member, unverified)
            await bot.change_nickname(member, "%s" % (nickname))
            await bot.add_roles(member, xb1) #verified
            await bot.add_roles(member, verified) #verified
            await bot.add_roles(member, agent) #Agent

            general_chat = discord.utils.get(member.server.channels, name = "general-chat")

            await bot.send_message(general_chat, "Hello {}!, welcome in. Send requests in <#422481305440354306> or in <#422481432951128064> using `@everyone`to find people to play with.\nIf there are any problems, feel free to DM <@389760103462600705> and the message will automatically be forwarded to Staff.".format(member.mention))                                                                

bot.run('NDAwNjkzMTMyNjMyNzg0ODk2.DhbfHQ.7muO_FNdk3S-FE_t0YjdiMQryLI')