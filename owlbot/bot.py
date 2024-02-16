# Import the necessary Discord library
import datetime
from http import HTTPStatus
import discord
from discord.ext import commands

# Initialize the Discord bot client
client = commands.Bot(command_prefix='!')

# Define the admin commands
@client.command(name="kick")
async def kick_member(ctx, member: discord.Member):
    """Kick a member from the server."""
    if ctx.author.guild_permissions.kick_members:
        await member.kick()
        await ctx.send(f"{member.name} has been kicked from the server.")
    else:
        await ctx.send("You don't have permission to kick members.")
@client.command(name="ban")
async def ban_member(ctx, member: discord.Member):
    """Ban a member from the server."""
    if ctx.author.guild_permissions.ban_members:
        await member.ban()
        await ctx.send(f"{member.name} has been banned from the server.")
    else:
        await ctx.send("You don't have permission to ban members.")
@client.command(name="unban")
async def unban_member(ctx, member_name: str):
    """Unban a member from the server."""
    if ctx.author.guild_permissions.ban_members:
        banned_users = await ctx.guild.bans()
        for ban_entry in banned_users:
            user = ban_entry.user
            if user.name == member_name:
                await ctx.guild.unban(user)
                await ctx.send(f"{member_name} has been unbanned from the server.")
                return
        await ctx.send(f"{member_name} is not banned from the server.")
    else:
        await ctx.send("You don't have permission to unban members.")
@client.command(name="mute")
async def mute_member(ctx, member: discord.Member):
    """Mute a member from sending messages."""
    if ctx.author.guild_permissions.mute_members:
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not role:
            role = await ctx.guild.create_role(name="Muted")
        await member.add_roles(role)
        await ctx.send(f"{member.name} has been muted.")
    else:
        await ctx.send("You don't have permission to mute members.")
@client.command(name="unmute")
async def unmute_member(ctx, member: discord.Member):
    """Unmute a member from sending messages."""
    if ctx.author.guild_permissions.mute_members:
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(role)
        await ctx.send(f"{member.name} has been unmuted.")
    else:
        await ctx.send("You don't have permission to unmute members.")
# Purge messages
@client.command(name="purge")
async def purge_messages(ctx, limit: int):
    """Purge a specified number of messages from the channel."""
    if ctx.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=limit)
        await ctx.send(f"Deleted {limit} messages.")
    else:
        await ctx.send("You don't have permission to purge messages.")
# Change nickname
@client.command(name="nickname")
async def change_nickname(ctx, member: discord.Member, new_nickname: str):
    """Change the nickname of a member."""
    if ctx.author.guild_permissions.manage_nicknames:
        await member.edit(nick=new_nickname)
        await ctx.send(f"{member.name}'s nickname has been changed to {new_nickname}.")
    else:
        await ctx.send("You don't have permission to change nicknames.")
# Create role
@client.command(name="createrole")
async def create_role(ctx, role_name: str):
    """Create a new role on the server."""
    if ctx.author.guild_permissions.manage_roles:
        await ctx.guild.create_role(name=role_name)
        await ctx.send(f"Created role {role_name}.")
    else:
        await ctx.send("You don't have permission to create roles.")
# Delete role
@client.command(name="deleterole")
async def delete_role(ctx, role: discord.Role):
    """Delete a role from the server."""
    if ctx.author.guild_permissions.manage_roles:
        await role.delete()
        await ctx.send(f"Deleted role {role.name}.")
    else:
        await ctx.send("You don't have permission to delete roles.")
# Assign role
@client.command(name="addrole")
async def add_role(ctx, member: discord.Member, role: discord.Role):
    """Add a role to a member."""
    if ctx.author.guild_permissions.manage_roles:
        await member.add_roles(role)
        await ctx.send(f"Added role {role.name} to {member.name}.")
    else:
        await ctx.send("You don't have permission to assign roles.")
# Remove role
@client.command(name="removerole")
async def remove_role(ctx, member: discord.Member, role: discord.Role):
    """Remove a role from a member."""
    if ctx.author.guild_permissions.manage_roles:
        await member.remove_roles(role)
        await ctx.send(f"Removed role {role.name} from {member.name}.")
    else:
        await ctx.send("You don't have permission to remove roles.")
# Lock/Unlock channel
@client.command(name="lockdown")
async def lockdown_channel(ctx):
    """Lock or unlock the current channel."""
    if ctx.author.guild_permissions.manage_channels:
        channel = ctx.channel
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False)
        }
        if channel.overwrites_for(ctx.guild.default_role).send_messages:
            await channel.edit(overwrites=overwrites)
            await ctx.send("Channel locked.")
        else:
            await channel.edit(overwrites={})
            await ctx.send("Channel unlocked.")
    else:
        await ctx.send("You don't have permission to lock/unlock channels.")
# Set slowmode
@client.command(name="slowmode")
async def set_slowmode(ctx, seconds: int):
    """Set the slowmode for the current channel."""
    if ctx.author.guild_permissions.manage_channels:
        channel = ctx.channel
        await channel.edit(slowmode_delay=seconds)
        await ctx.send(f"Slowmode set to {seconds} seconds.")
    else:
        await ctx.send("You don't have permission to set slowmode.")
# Create invite
@client.command(name="createinvite")
async def create_invite(ctx):
    """Create an invite link for the current channel."""
    if ctx.author.guild_permissions.create_instant_invite:
        invite = await ctx.channel.create_invite()
        await ctx.send(f"Invite link: {invite}")
    else:
        await ctx.send("You don't have permission to create invites.")
# Delete invite
@client.command()
async def deleteinvite(ctx, url):
    try:
        invite = await ctx.fetch_invite(url)
        await invite.delete()
        await ctx.send("Successfully deleted the given invite.")
    except Exception as e:
        print(e)
        await ctx.send("Failed to delete the invite due to an error.")
@client.command(name="inviteinfo")
async def get_invite_info(ctx, invite_code: str):
    """Get information about an invite link."""
    invite = await new_func()
    await ctx.send(f"Invite created by: {invite.inviter.name}\nInvite uses: {invite.uses}")

async def new_func():
    invite = await  (f"https://discord.gg/{HTTPStatus://discord.com/api/oauth2/authorize?client_id=1207847447444070452&permissions=8&scope=bot}")
    return invite
# Ban/Unban by ID
@client.command(name="banid")
async def ban_by_id(ctx, user_id: int):
    """Ban a user from the server by their user ID."""
    if ctx.author.guild_permissions.ban_members:
        guild = ctx.guild
        user = await guild.fetch_user(user_id)
        await guild.ban(user)
        await ctx.send(f"{user.name} has been banned from the server.")
    else:
        await ctx.send("You don't have permission to ban members.")
@client.command(name="unbanid")
async def unban_by_id(ctx, user_id: int):
    """Unban a user from the server by their user ID."""
    if ctx.author.guild_permissions.ban_members:
        guild = ctx.guild
        user = await guild.fetch_user(user_id)
        await guild.unban(user)
        await ctx.send(f"{user.name} has been unbanned from the server.")
    else:
        await ctx.send("You don't have permission to unban members.")
# Prune members
@client.command(name="prune")
async def prune_members(ctx, days: int):
    """Prune inactive members from the server."""
    if ctx.author.guild_permissions.kick_members:
        guild = ctx.guild
        inactive_members = []
        for member in guild.members:
            if member.joined_at < (datetime.datetime.now(tz=datetime.timezone.utc) - datetime.timedelta(days=days)):
                inactive_members.append(member)
        await guild.prune_members(days=days, compute_prune_count=False)
        await ctx.send(f"Pruned {len(inactive_members)} inactive members from the server.")
    else:
        await ctx.send("You don't have permission to prune members.")