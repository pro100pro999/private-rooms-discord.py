#Я дал вам только кусок кода.
#Сам код бота пишите сами!

@client.event
async def on_voice_state_update(member, before, after):
    if after.channel.id == 773808458528718849: #Сюда ID вашего ГОЛОСОВОГО канала!
        for guild in client.guilds:
            mycategory=discord.utils.get(guild.categories, id= 773808378887667772 ) #Сюда ID категории,где находится ваш канал
            channel2= await guild.create_voice_channel(name=f'Room of {member.display_name}', category= mycategory)
            await channel2.set_permissions(member, connect=True, mute_members=True, move_members= True, manage_channels= True)
            await member.move_to(channel2)
            def check(x, y, z)
                return len(channel2.members)==0
            await client.wait_for('voice_state_update', check=check)
            await channel2.delete()
            
@client.command()
async def changename(ctx, *, namech = None):
    if namech is None:
        await ctx.send(embed = discord.Embed(title = f'**Ошибка в написании команды**', description = f'**:shield: Обязательно укажите имя канала :shield:**', color = 0x0c0c0c))
    else:
        voicech = ctx.author.voice.channel
        if voicech.name.endswith(f'{ctx.author.name}'):
            await voicech.edit(name = f'{namech}  ...{ctx.author.name}') #Пример: НАЗВАНИЕ ...ВАШ НИК
        else:
            await ctx.send(embed = discord.Embed(title = f'**Ошибка**', description = f'**Название твоего канала уже было изменено, или же не ты создал этот канал**', color = 0x0c0c0c))
            
@client.command()
async def changelimit(ctx, limits: int = None):
    if limits is None:
        await ctx.send(embed=discord.Embed(title=f'**Ошибка в написании команды**', description=f'**:shield: Обязательно укажите лимит канала :shield:**', color=0x0c0c0c))
    else:
        voicech = ctx.author.voice.channel
        if voicech.name.endswith(f'{ctx.author.name}'): #Если название канала оканчивается на ваш ник,то лимит изменяется 
            await voicech.edit(user_limit = limits)
        else:
            await ctx.send(embed=discord.Embed(title=f'**Ошибка**',  description=f'**Название твоего канала уже было изменено, или же не ты создал этот канал**', color=0x0c0c0c))
