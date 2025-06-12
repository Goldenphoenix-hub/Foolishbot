import discord
from discord.ext import commands
from discord import app_commands
from discord.utils import get
from typing import Optional
import io

GUILD_IDS = [1290714708730712106, 1358497613485310005, 1356321215618220305, 1348990547615940690, 1349464333532528790, 1373704213053571264, 1373195401896788008]

# role‑ID ➜ {allowed user IDs}
ROLE_ACCESS = { 
    1290733713964925019: {1312471992389206018}, # Owner role
    1363653146563580034: {1354100267393482772, 1276602447925739521}, # chair people
    1356753306386567308: {1354100267393482772}, # chair man
    1356032178877759627: {1276602447925739521}, # chairwoman 
    1335763236011638834: {1192374383755407393},  # president
    1333395781947887698: {779295531112464405}, # vice president 
    1346554165849100289: {1192374383755407393, 779295531112464405}, # presidential team
    1311574266885701682: {},  # operational director
    1299777331715637409: {1036573579808092180, 1354100267393482772, 1312471992389206018, 1036573579808092180}, # devs
    1313531037095297166: {1336769001887633569, 1282740411135426563, 860043493094326292, 1354100267393482772, 1276602447925739521, 1192374383755407393, 779295531112464405}, # admin team
    1358891828014878890: {1312471992389206018, 1276602447925739521}, # admin overseer
    1361294682583470260: {779295531112464405, 679290754568421377}, # mod overseer
    1297287851268116555: {}, # senior admin
    1297287926622720071: {1336769001887633569, 860043493094326292}, # junior admin
    1331866194004938782: {1282740411135426563}, # interim Admin
    1346723934254534727: {1346723934254534727, 1312471992389206018}, # announcement approval
    1334959548703707166: {779295531112464405, 1276602447925739521}, # quota checkers
    1347569405273313331: {1312471992389206018, 779295531112464405}, # ticket trainers
    1313546443193319505: {1055875824101896222, 1336769001887633569}, # LOA
    1297288808454426634: {1055875824101896222}, # mod lead
    1311378279751618580: {1311353523316985937}, # mod co lead
    1340695921742319717: {1334384035807494204}, # senior mod
    1333397172288229406: {1055875824101896222, 779295531112464405, 1311353523316985937}, # mod leadership
    1328069102350110733: {1311353523316985937}, # mod star
    1311350165138833458: {}, # normal mod
    1340695642468651130: {}, # junior mod
    1311573952287473694: {1282740411135426563, 1055875824101896222, 1311353523316985937}, # mod team
    1315700239088222208: {}, # mod trials
    1304877602321727659: {1312471992389206018, 1055875824101896222, 779295531112464405, 1336769001887633569, 1276602447925739521}, # ticket support team
    1367134751722569768: {}, # suspended staff
    1363249606019776653: {1282740411135426563, 1055875824101896222, 779295531112464405}, # all mod perms
    1305219781284073483: {1036573579808092180, 1055875824101896222, 779295531112464405, 1276602447925739521}, # PR leadership
    1296158413931413604: {1336769001887633569}, # PR team
    1317561292256444517: {860043493094326292, 1312824117577388143}, # honorary admins
    1333875013903843482: {1036573579808092180}, #honarary mods
    1290737031722303605: {814792284045705246, 1068731653108793444, 458421553600790530, 1129853005609570364, 1312824117577388143, 761569716829290536, 779295531112464405, 1336769001887633569, 1091362759729487872, 881427983800352768, 1344516109637779543, 1186619552818286662, 679290754568421377, 1248931833345867837}, # lords
    1323615700505591860: {732468984561270834, 780523683575103488, 1256668398457323522, 796003035926888450, 1158122107138494636}, #alliance representatives
    1334899110125375489: {1036573579808092180, 1312471992389206018, 779295531112464405, 1276602447925739521}, # song perms
    1331866687951208458: {1312471992389206018, 779295531112464405, 1276602447925739521}, # role perms
    1344201090127888405: {761569716829290536, 779295531112464405, 1276602447925739521}, # mega private room access
    1355915035876003952: {1036573579808092180, 779295531112464405}, # image perms
    1318585821426618418: {}, # mod trial perms
    1346516507261276322: {}, # ticket blacklisted users
    1373021414499815607: {1354100267393482772, 1312471992389206018, 1248931833345867837}, # jenny's role

    # Appeals Server Roles
    1356326027005001738: {1312471992389206018}, # founder
    1363308264749531176: {1248931833345867837, 1276602447925739521}, # chairpeople
    1356326247650562282: {1192374383755407393, 779295531112464405}, # presidensial team
    1356326087956889772: {1248931833345867837, 1312471992389206018, 779295531112464405}, # appeals Overseer
    1356326315023794190: {860043493094326292}, # admin team in server
    1356326149831262420: {1356326149831262420}, # appeals lead
    1356326529893929087: {860043493094326292}, # appeals officer
    1356326589612429513: {860043493094326292, 1312471992389206018, 1192374383755407393, 1276602447925739521, 779295531112464405, 679290754568421377}, # staff access 
    1364345985949503609: {1336769001887633569}, # Leave of Absence 

    # public relations server
    1349068660077232259: {1349068660077232259}, # founder
    1367903788513497241: {1349068660077232259}, # owner
    1366280692631081010: {1248931833345867837, 1276602447925739521}, # chairpeople
    1367903792733093910: {1192374383755407393}, # president
    1367903798835679252: {779295531112464405}, # vice president 
    1367903802677792958: {}, # operational director
    1349015322354647070: {1312471992389206018, 779295531112464405}, # overseer of pr
    1349015566710607903: {1036573579808092180, 1055875824101896222, 779295531112464405, 1276602447925739521}, # admin team perm
    1349016881096429629: {1055875824101896222}, # head of pr
    1349016961639780392: {1276602447925739521}, # co head
    1375546426993410201: {779295531112464405}, # coordinator
    1349021855759204415: {1036573579808092180}, # lead of pr 
    1349022209410072626: {1312471992389206018}, # senior staff of pr
    1349385562569703525: {1055875824101896222, 779295531112464405, 1036573579808092180}, # quota checkers of pr
    1349021757050191922: {1036573579808092180, 1055875824101896222, 779295531112464405, 1276602447925739521, 1312471992389206018}, # leadership of pr
    1362471309224710417: {779295531112464405, 1312471992389206018, 1055875824101896222, 1036573579808092180}, # pr pr manager
    1349022618136612864: {779295531112464405, 1192374383755407393}, # presidential team role
    1367903806901194843: {1336769001887633569, 860043493094326292}, # admin team role
    1349022112546947115: {}, # pr staff role
    1349022624486785024: {1336769001887633569}, # pr junior staff
    1349022675154243606: {860043493094326292}, # pr interns
    1349022857744748594: {1336769001887633569}, # leave of absence
    1349033741581811732: {1312471992389206018}, # allince dep lead
    1349033676758843453: {1036573579808092180}, # engagement dep lead
    1360254951644729415: {1248931833345867837}, # co lead of engagement dep
    1349034760768589834: {1055875824101896222, 779295531112464405, 1276602447925739521}, # alliance dep leadership 
    1349034694796120217: {1248931833345867837, 1276602447925739521, 779295531112464405, 1055875824101896222, 1036573579808092180}, # engagement dep leadership
    1367903814493011969: {1055875824101896222}, # moderation team 
    1367903816292503808: {}, # suspended staff

    # alliance server
    1349465596630269982: {1312471992389206018}, # owner
    1363306837230878817: {1276602447925739521, 1248931833345867837}, # chairpeople
    1349465493991456851: {1192374383755407393, 779295531112464405}, # presidential Team
    1349465069309657220: {1336769001887633569, 860043493094326292}, # admins
    1349466239029743768: {1312471992389206018, 779295531112464405}, # pr overseer
    1349480549605179543: {1312471992389206018}, # alli lead
    1349464961453264967: {1312471992389206018, 1276602447925739521, 1055875824101896222}, # pr leadership
    1349465450282483713: {1312471992389206018}, # pr team mem
    1349465273949749452: {780523683575103488, 1256668398457323522, 796003035926888450, 1158122107138494636}, # business partner
    1349467539994050681: {1336769001887633569}, # LOA
    1357410099211010200: {1158122107138494636}, # maus pr
    1349764853228638239: {1256668398457323522}, # plug pr
    1349764969130102805: {780523683575103488}, # stellar pr
    1349768036004925512: {796003035926888450}, # gaming challanges

    # Staff Server
    1358497995984994316: {1312471992389206018}, # owner 
    1358499013065965655: {1276602447925739521, 1248931833345867837}, # chairpeople
    1363625775055634494: {1276602447925739521}, # chairwoman
    1363625921961136320: {1248931833345867837}, # chairman
    1358498745032904806: {1192374383755407393}, # president
    1358498702213517562: {779295531112464405}, # vice president
    1358501112151277780: {1192374383755407393, 779295531112464405}, # presidential Team
    1358498562782138552: {}, # operational Director 
    1358498351896727895: {}, # senior admin 
    1376343548244529232: {}, # admin 
    1358498294057271306: {860043493094326292, 1336769001887633569}, # junior admin 
    1358498484608696351: {}, # interim admin
    1358498251900194967: {860043493094326292, 1336769001887633569}, # admin team role
    1358500073830486229: {1248931833345867837, 779295531112464405}, # mod overseer
    1358498175047962934: {1055875824101896222}, # mod lead
    1358498213476434121: {1311353523316985937}, # mod co lead
    1358498101094256911: {1311353523316985937, 1055875824101896222}, # mod leadership 
    1358500220756824074: {}, # mod of the week
    1358500328592380025: {1311353523316985937}, # active mod 
    1358498078214066437: {1334384035807494204}, # Senior mod
    1358498053912395947: {}, # normal mod
    1358498016281104477: {}, # junior mod
    1358497956935766057: {}, # trial mod
    1358499412376027317: {}, # mod team role
    1367905752832016405: {}, # suspeneded staff
    1367905788508504084: {1336769001887633569}, # lOA

    # test server IDs
    1373710145808367667: {1248931833345867837, 1312471992389206018}, # admin role 
    1373710305632321606: {888373650032570401, 1248931833345867837, 1036573579808092180, 1363185128716767424, 860043493094326292, 779295531112464405, 1311353523316985937, 1091362759729487872, 458421553600790530}, # tester access 
    1373710888812679301: {1248931833345867837, 1036573579808092180, 1363185128716767424, 860043493094326292, 779295531112464405, 1311353523316985937, 1091362759729487872, 888373650032570401, 458421553600790530}, # server chat access
    }


VERIFIED_ROLE_IDS = [1327734787942781052, 1358497908122587427, 1377411110369497108, 1349019490402304072, 1349465119402491956, 1373967235885961338] 

UNVERIFIED_ROLE_IDS = [1327734833761226953, 1358499933832872237, 1377411212807110827, 1349019466658217994, 1349465160187772959, 1373961608400732185]

# IDs allowed to use /update
UPDATE_ALLOWED_USERS = {
    1248931833345867837, 1312471992389206018, 1168481552460693574, 458421553600790530}

ALLOWED_ROLE_IDS = [1373710145808367667, 1373710305632321606, 1373021414499815607]
EXEMPT_COMMANDS = {"troll_ansh", "troll_squid"}

TICKET_OPTIONS = {
    "admin": {
        "label": "Contact an administrator",
        "emoji": "🔧",
        "description": "Click to contact an admin",
        "category_id": 1382364374630662324,
        "handler_ids": [1373710145808367667],  # Admin/Support roles
        "transcript_channel_id": 1382364557959499936,
    },
    "support": {
        "label": "Contact support team",
        "emoji": "🛠",
        "description": "Click to contact support",
        "category_id": 1382364374630662324,
        "handler_ids": [1373710145808367667],
        "transcript_channel_id": 1382364557959499936,
    },
    "other": {
        "label": "Other questions/Not listed above",
        "emoji": "❓",
        "description": "For general or unlisted inquiries",
        "category_id": 1382364374630662324,
        "handler_ids": [1373710145808367667],
        "transcript_channel_id": 1382364557959499936,
    },
}

intents = discord.Intents.default()
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="/", intents=intents)

# ───── Global Permission Check ─────
@bot.tree.interaction_check
async def global_interaction_check(interaction: discord.Interaction) -> bool:
    if interaction.command and interaction.command.name in EXEMPT_COMMANDS:
        return True
    return any(role.id in ALLOWED_ROLE_IDS for role in interaction.user.roles)

def get_serverlinks_embed(user: str) -> discord.Embed:
    embed = discord.Embed(
        title="Foolish Staff Server Invitation",
        description=(
            f"Greetings, {user}\n\n"
            "Welcome to the foolish server staff Department!\n\n"
            "Please use the below links to join our staff server."
        ),
        color=discord.Color.purple()
    )
    embed.add_field(
        name="Staff Server",
        value="[Invitation To Staff Server](https://discord.gg/6ZSHtD6bzK)",
        inline=False
    )
    embed.set_footer(text="Foolish Server")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1368600512999456788/1369018107896791061/Capture.PNG")
    return embed

# ----- The Moderation server embed -----

def get_moderationserver_embed(user: str) -> discord.Embed:
    embed = discord.Embed(
        title="Foolish Moderation Server Invitation",
        description=(
            f"Greetings, {user}\n\n"
            "Welcome to the foolish server Moderation Department!\n\n"
            "Please use the below links to join our moderation server."
        ),
        color=discord.Color.purple()
    )
    embed.add_field(
        name="Moderation Department Server",
        value="[Invitation To Moderation Department Server](https://discord.gg/q6f54bUFWX)",
        inline=False
    )
    embed.set_footer(text="Foolish Server")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1368600512999456788/1369018107896791061/Capture.PNG")
    return embed

# ------ Public Relations Department Embed ------

def get_publicrelationsdepartmentserver_embed(user: str) -> discord.Embed:
    embed = discord.Embed(
        title="Foolish Public Relations Department Invitation",
        description=(
            f"Greetings, {user}\n\n"
            "Welcome to the foolish server Public Relations Department!\n\n"
            "Please use the below links to join our Public Relations department server and public relations sub-department server."
        ),
        color=discord.Color.purple()
    )
    embed.add_field(
        name="Public Relations Department Server",
        value="[Invitation To Public Relations Department Server](https://discord.gg/AwUS9fCHsz)",
        inline=False
    )
    embed.add_field(
        name="Public Relations Sub-Department Alliance Server",
        value="[Invitation To Sub-Department Server](https://discord.gg/nPxxRPtv6X)",
        inline=False
    )
    embed.set_footer(text="Foolish Server")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1368600512999456788/1369018107896791061/Capture.PNG")
    return embed

# ------ Embed command for appeal server ------

def get_appealsserver_embed(user: str) -> discord.Embed:
    embed = discord.Embed(
        title="Foolish Appeals Server Invitation",
        description=(
            f"Greetings, {user}\n\n"
            "Need to appeal a punishment? No worries—just hop into our Appeals Server using the link below.\n\n"
            "Please use the below links to join our appeals server."
        ),
        color=discord.Color.purple()
    )
    embed.add_field(
        name="Appeals Server",
        value="[Invitation To Appeals Server](https://discord.gg/CZBWTmGzuV)",
        inline=False
    )
    embed.set_footer(text="Foolish Server")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1368600512999456788/1369018107896791061/Capture.PNG")
    return embed



# ───── Information Embed Function ─────

def get_information_embeds() -> list[discord.Embed]:
    embed1 = discord.Embed(
        title="Foolish People",
        description="Created by <@1312471992389206018>",
        color=discord.Color.purple()
    )
    embed1.set_thumbnail(url="https://cdn.discordapp.com/attachments/1368600512999456788/1369018107896791061/Capture.PNG")

    embed2 = discord.Embed(
        title="About Us",
        color=discord.Color.purple()
    )
    embed2.add_field(name="Events", value="Regularly held to keep the community active and entertained.", inline=False)
    embed2.add_field(name="Promotions", value="Earned through dedication, talent, and hard work.", inline=False)
    embed2.add_field(name="Reputation", value="Known for a positive atmosphere and friendly behaviour.", inline=False)
    embed2.add_field(name="Satisfaction", value="Ensuring members feel valued is our top priority.", inline=False)
    embed2.add_field(name="Community Engagement", value="Fun events, engaging discussions, and spotlight opportunities.", inline=False)
    embed2.add_field(name="Growth Opportunities", value="No shortcuts—just real recognition for your contributions.", inline=False)
    embed2.add_field(
        name="Partnerships",
        value=(
            "**Current Partners:**\n"
            "- **[Plug](https://discord.gg/C2JMn6nbBW)** ➜ <@1256668398457323522>\n"            
            "- **[Stellar City](https://discord.gg/stellar-city)** ➜ <@780523683575103488>\n"
            "Interested? Check the [Affiliation Requirement Guide](https://docs.google.com/document/d/1XbKyQGN6A7IXaCr4HBYteQIS9ROAuoMm5ZtXxbuE-Ug/edit?usp=drivesdk) and open a ticket!"
        ),
        inline=False
    )

    embed3 = discord.Embed(
        title="Foolish People Structure",
        color=discord.Color.purple()
    )
    embed3.add_field(name="◦ Ownership", value="<@1312471992389206018>", inline=False)
    embed3.add_field(name="◦ Server Chairpeople", value="<@1354100267393482772>\n<@1276602447925739521>", inline=False)
    embed3.add_field(name="◦ Presidential Team", value="<@679290754568421377>\n<@1192374383755407393>\n<@779295531112464405> ➜ <@&1311574266885701682>", inline=False)
    embed3.add_field(name="◦ Administration Team", value="<@1336769001887633569> ➜ <@&1297287851268116555>\n", inline=False)
    embed3.add_field(name="◦ Public Relations Department Leadership", value="<@1036573579808092180>\n<@1276602447925739521>\n <@1036573579808092180>", inline=False)
    embed3.add_field(name="◦ Moderation Department", value="<@1282740411135426563> ➜ <@&1297288808454426634>\n<@1055875824101896222> ➜ <@&1311378279751618580>", inline=False)
    embed4 = discord.Embed(
        title="Why Join Us?",
        description=(
            "➜ Be part of a group that genuinely values hard work.\n"
            "➜ Experience a disciplined yet fun environment.\n"
            "➜ Join a reputation-driven community that cares about its people."
        ),
        color=discord.Color.purple()
    )
    embed4.set_footer(text="Foolish Server")

    return [embed1, embed2, embed3, embed4]


# ------ Support Team Ticket Greeting Embed ------
def get_support_ticket_embed(user: str) -> discord.Embed:
    embed = discord.Embed(
        title=" Foolish People Support Ticket",
        description=(
            f"Greetings, {user}\n\n"
            "Thank you for reaching out to the Foolish People Support Team.\n\n"
            "Please provide any relevant details or information regarding your issue so we can offer the most accurate and efficient support possible.\n\n"
            "We appreciate your patience and will do our best to resolve your concern promptly.\n\n"
            "— Support Team | Foolish People"
        ),
        color=discord.Color.purple()
    )
    embed.set_footer(text="Foolish Server")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1368600512999456788/1369018107896791061/Capture.PNG")
    return embed

# ------ Administration Team Ticket Greeting Embed ------
def get_admin_ticket_embed(user: str) -> discord.Embed:
    embed = discord.Embed(
        title="Administration Support Ticket",
        description=(
            f"Greetings, {user}\n\n"
            "Your ticket has been claimed by a member of the Administration Team.\n\n"
            "Kindly provide any additional information or clarification related to your request so we can proceed with the appropriate support or action.\n\n"
            "Thank you for your patience.\n\n"
            "— Administration Team | Foolish People"
        ),
        color=discord.Color.purple()
    )
    embed.set_footer(text="Foolish Server")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1368600512999456788/1369018107896791061/Capture.PNG")
    return embed

# ------ Presidential Team Ticket Greeting Embed ------
def get_presidential_ticket_embed(user: str) -> discord.Embed:
    embed = discord.Embed(
        title="Presidential Team Support Ticket",
        description=(
            f"Greetings, {user}\n\n"
            "Thank you for contacting the Presidential Team of the Foolish People server. Your ticket has been received and claimed.\n\n"
            "Please share all relevant details to help us proceed effectively. We appreciate your cooperation and will work to assist you as efficiently as possible.\n\n"
            "— Presidential Team | Foolish People"
        ),
        color=discord.Color.purple()
    )
    embed.set_footer(text="Foolish Server")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1368600512999456788/1369018107896791061/Capture.PNG")
    return embed

# ---- Rules Embeds ----

def get_rules_embeds() -> list[discord.Embed]:
    embed1 = discord.Embed(
        title="Foolish People Rule-Book",
        description="",
        color=discord.Color.purple()
    )

    embed2 = discord.Embed(
        title="__Rule #1 - Harassment__",
        description=(
            "> - Do not spread any negativity within the server.\n"
            "> - Do not start or continue any drama within the server.\n"
            "> - Do not be disrespectful or rude to anyone.\n"
            "> - Do not harass, or join in on the harassment of, another user.\n"
            "> - Do not endorse or joke about self-harm or mental health issues.\n"
            "> - Do not engage in hate speech of any kind (e.g. racism, sexism, homophobia, etc).\n"
            "> - Do not threaten anyone.\n"
            "> - Do not spam.\n"
            "> - Do not try to mass mention users.\n"
        ),
        color=discord.Color.purple()
    )
    

    embed3 = discord.Embed(
        title="__Rule #2 - Content & Behavior__",
        description=(
            "> - Do not post unsafe items (e.g. malicious websites, pirated software, etc).\n"
            "> - Do not post any link or file that crashes Discord.\n"
            "> - Do not DDoS or threaten to DDoS other users\n"
            "> - Do not post any kind of NSFW content.\n"
        ),
        color=discord.Color.purple()
    )

    embed4 = discord.Embed(
        title="__Rule #3 - Profile__",
        description=(
            "> - Do not use special characters, punctuation, or symbols in your name.\n"
            "> - Do not display NSFW images in your profile picture.\n"
            "> - Do not attempt to draw any attention to advertisements you may have in your discord profile.\n"
            "> - Do not fake your age for any purpose.\n"
        ),
        color=discord.Color.purple()
    ) 

    embed5 = discord.Embed(
        title="Rule #4 - Staff & Punishments",
        description=(
            "> - Do not evade any punishment (e.g. ban, mute, etc).\n"
            "> - Do not exploit loopholes to get around the rules.\n"
            "> - Do not ping support members for no reason.\n"
            "> - Do not disrespect staff members.\n"
            "> - Do not impersonate staff members.\n"
            "> - Do not falsely report users.\n"
            "> - Do not join discord on multiple accounts.\n"
        ),
        color=discord.Color.purple()
    )

    embed6 = discord.Embed(
        title="Rule #5 - Discord TOS",
        description=(
            "> - You need to be at least 13 years old to use discord.\n"
            "> - breaking the law / admitting to crime = reported to the authorities.\n"
        ),
        color=discord.Color.purple()
    )
    embed6.set_footer(text="Foolish Server")
    
    return [embed1, embed2, embed3, embed4, embed5, embed6] 

# ─── Verification Embed ───────────────────────────────────────────────────────
def verification_embed():
    embed = discord.Embed(
        title="Note",
        description=(
            "Welcome to **𝐅𝐨𝐨𝐥𝐢𝐬𝐡 𝐏𝐞𝐨𝐩𝐥𝐞 [𝐑𝐄𝐕𝐀𝐌𝐏𝐈𝐍𝐆]!** Execute the command `/link` to sync your role and gain access to the rest of the server, execute command `/verify`."
        ),
        color=discord.Color.purple()
    )
    embed.set_footer(text="Foolish Server")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/1368600512999456788/1369018107896791061/Capture.PNG"
    )
    return embed


# logging command 
TICKET_LOG_CHANNEL_IDS = {1380315959637573783}

class TicketLogger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.guilds(*[discord.Object(id=guild_id) for guild_id in GUILD_IDS])
    @app_commands.command(name="log-ticket", description="Log a ticket with all necessary information.")
    @app_commands.describe(
        user="User involved in the ticket",
        ticket_number="Ticket number",
        reason="Reason for opening the ticket",
        rank="Rank the user got",
        additional_info="Any extra information"
    )
    async def log_ticket(
        self,
        interaction: discord.Interaction,
        user: str,
        ticket_number: str,
        reason: str,
        rank: str,
        additional_info: str = "N/A"
    ):
        # ✅ Check permission BEFORE doing anything
        if not any(role.id in ALLOWED_ROLE_IDS for role in interaction.user.roles):
            await interaction.response.send_message("❌ You don't have permission to use this command.", ephemeral=True)
            return  # ⛔ Stop execution here

        # 🧾 Create the embed
        embed = discord.Embed(
            title=f"Ticket Log - {ticket_number}",
            color=discord.Color.purple()
        )
        embed.add_field(name="**User:**", value=user, inline=False)
        embed.add_field(name="**Reason for Opening:**", value=reason, inline=False)
        embed.add_field(name="**Rank they got:**", value=rank, inline=False)
        embed.add_field(name="**Additional Information:**", value=additional_info, inline=False)

        successful_logs = 0

        # 🔁 Loop through the allowed log channels
        for channel_id in TICKET_LOG_CHANNEL_IDS:
            channel = interaction.guild.get_channel(channel_id)
            if channel:
                try:
                    await channel.send(embed=embed)
                    successful_logs += 1
                except Exception as e:
                    print(f"Failed to send to channel {channel_id}: {e}")

        # ✅ Respond to user
        if successful_logs > 0:
            await interaction.response.send_message("Ticket logged successfully to all configured channels!", ephemeral=True)
        else:
            await interaction.response.send_message("Failed to log the ticket", ephemeral=True)




# ───── Cogs ─────
class StaffServerInviteLink(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="staffserverinvitation", description="Sends the staff server invite link")
    @app_commands.describe(user="The name or nickname you want to use in the embed")
    @app_commands.guilds(*[discord.Object(id=guild_id) for guild_id in GUILD_IDS])
    async def serverlinks(self, interaction: discord.Interaction, user: str):
        if not any(role.id in ALLOWED_ROLE_IDS for role in interaction.user.roles):
            await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)
            return
        await interaction.response.send_message(embed=get_serverlinks_embed(user))

        


class moderationserver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="moderationserver", description="Sends the moderation server invite link")
    @app_commands.describe(user="The name or nickname you want to use in the embed")
    @app_commands.guilds(*[discord.Object(id=guild_id) for guild_id in GUILD_IDS])
    async def moderationserver(self, interaction: discord.Interaction, user: str):
        if not any(role.id in ALLOWED_ROLE_IDS for role in interaction.user.roles):
                await interaction.response.send_message("🚫 You don't have permission to use this command.", ephemeral=True)
                return
        await interaction.response.send_message(embed=get_moderationserver_embed(user))

class publicrelationsdepartmentserver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="publicrelationserver", description="Sends the public relations department server invite link")
    @app_commands.describe(user="The name or nickname you want to use in the embed")
    @app_commands.guilds(*[discord.Object(id=guild_id) for guild_id in GUILD_IDS])
    async def publicrelationsdepartmentserver(self, interaction: discord.Interaction, user: str):
        if not any(role.id in ALLOWED_ROLE_IDS for role in interaction.user.roles):
                await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)
                return
        await interaction.response.send_message(embed=get_publicrelationsdepartmentserver_embed(user))

class appealsserver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="appealsserver", description="Sends the appeals server invite link")
    @app_commands.describe(user="The name or nickname you want to use in the embed")
    @app_commands.guilds(*[discord.Object(id=guild_id) for guild_id in GUILD_IDS])
    async def appealsserver(self, interaction: discord.Interaction, user: str):
        if not any(role.id in ALLOWED_ROLE_IDS for role in interaction.user.roles):
                await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)
                return
        await interaction.response.send_message(embed=get_appealsserver_embed(user))

class MediaCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @app_commands.command(name="troll_squid", description="Sends squid head pat")
    @app_commands.guilds(*[discord.Object(id=guild_id) for guild_id in GUILD_IDS])
    async def troll_squid(self, interaction: discord.Interaction):
        await interaction.response.send_message(content="https://cdn.discordapp.com/attachments/1368264384576622592/1375425784776233112/f0bb1d57-d21b-4fd7-b6cd-efbd37961146.png?ex=6831a495&is=68305315&hm=d97927a6eb77eadca6dd8a12b92fa6414f7f9b3d1e58717e3b56a181dc0f7cd7&")

    @app_commands.command(name="troll_ansh", description="Sends ansh head pat")
    @app_commands.guilds(*[discord.Object(id=guild_id) for guild_id in GUILD_IDS])
    async def troll_ansh(self, interaction: discord.Interaction):
        await interaction.response.send_message(content="https://cdn.discordapp.com/attachments/1324066685803823164/1373026727370166292/e464087e-3685-4907-a648-d17a1915cf55.gif")

class MessageRepeater(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="say", description="The bot will repeat what you say.")
    @app_commands.describe(text="Type the message you want the bot to send")
    @app_commands.guilds(*[discord.Object(id=guild_id) for guild_id in GUILD_IDS])
    async def say_anything(self, interaction: discord.Interaction, text: str):
        if not any(role.id in ALLOWED_ROLE_IDS for role in interaction.user.roles):
                await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)
                return
        await interaction.response.send_message(f"{text}")

class InformationEmbeds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="information", description="Sends an informational embed about Foolish Server")
    @app_commands.guilds(*[discord.Object(id=guild_id) for guild_id in GUILD_IDS])
    async def information(self, interaction: discord.Interaction):
        if not any(role.id in ALLOWED_ROLE_IDS for role in interaction.user.roles):
                await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)
                return
        embeds = get_information_embeds()
        for embed in embeds:
            await interaction.channel.send(embed=embed)
        await interaction.response.send_message("Information sent!", ephemeral=True)

class SupportTeamTicketGreeting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="support_ticket", description="Sends the support team ticket greeting")
    @app_commands.describe(user="The name or nickname you want to use in the embed")
    @app_commands.guilds(*[discord.Object(id=guild_id) for guild_id in GUILD_IDS])
    async def support_ticket(self, interaction: discord.Interaction, user: str):
        if not any(role.id in ALLOWED_ROLE_IDS for role in interaction.user.roles):
                await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)
                return
        await interaction.response.send_message(embed=get_support_ticket_embed(user))


class AdminTeamTicketGreeting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="admin_ticket", description="Sends the administration team ticket greeting")
    @app_commands.describe(user="The name or nickname you want to use in the embed")
    @app_commands.guilds(*[discord.Object(id=guild_id) for guild_id in GUILD_IDS])
    async def admin_ticket(self, interaction: discord.Interaction, user: str):
        if not any(role.id in ALLOWED_ROLE_IDS for role in interaction.user.roles):
                await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)
                return
        await interaction.response.send_message(embed=get_admin_ticket_embed(user))


class PresidentialTeamTicketGreeting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="presidential_ticket", description="Sends the presidential team ticket greeting")
    @app_commands.describe(user="The name or nickname you want to use in the embed")
    @app_commands.guilds(*[discord.Object(id=guild_id) for guild_id in GUILD_IDS])
    async def presidential_ticket(self, interaction: discord.Interaction, user: str):
        if not any(role.id in ALLOWED_ROLE_IDS for role in interaction.user.roles):
                await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)
                return
        await interaction.response.send_message(embed=get_presidential_ticket_embed(user))

class RulesEmbed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="rules", description="Sends an rules embed of Foolish Server")
    @app_commands.guilds(*[discord.Object(id=guild_id) for guild_id in GUILD_IDS])
    async def rules(self, interaction: discord.Interaction):
        if not any(role.id in ALLOWED_ROLE_IDS for role in interaction.user.roles):
                await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)
                return
        embeds = get_rules_embeds()
        for embed in embeds:
         await interaction.channel.send(embed=embed)
        await interaction.response.send_message("Rules embed sent!", ephemeral=True)

        # ─── Role-sync Cog ────────────────────────────────────────────────────────────
class VerifyRoles(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="verification_note", description="Sends the verification info embed.")
    @app_commands.guilds(*[discord.Object(id=g) for g in GUILD_IDS])
    async def send_verification_embed(self, interaction: discord.Interaction):
        if interaction.user.id not in UPDATE_ALLOWED_USERS:
            await interaction.response.send_message("You’re not allowed to use this command.", ephemeral=True)
            return
        embed = verification_embed()
        await interaction.response.send_message(embed=embed)
        
        

    @app_commands.command(name="verify", description="Get verified to access the full server.")
    @app_commands.guilds(*[discord.Object(id=g) for g in GUILD_IDS])
    async def Verify(self, interaction: discord.Interaction):
            verified_roles = [interaction.guild.get_role(rid) for rid in VERIFIED_ROLE_IDS if interaction.guild.get_role(rid)]
            unverified_roles = [interaction.guild.get_role(rid) for rid in UNVERIFIED_ROLE_IDS if interaction.guild.get_role(rid)]

            if verified_roles and unverified_roles:
                await interaction.user.add_roles(*verified_roles, reason="User verified")
                await interaction.user.remove_roles(*unverified_roles, reason="User verified")

                role_mentions = ', '.join([role.mention for role in verified_roles])
                await interaction.response.send_message(
                    f"You have been verified!",
                    ephemeral=True
                )
            else:
                await interaction.response.send_message(
                    "Verification roles are not configured properly.",
                    ephemeral=True
                )


    # Returns an embed after syncing roles
    async def _sync_roles(self, member: discord.Member) -> discord.Embed:
        guild = member.guild
        current_ids = {r.id for r in member.roles}
        add, remove = [], []

        for role_id, whitelist in ROLE_ACCESS.items():
            role = guild.get_role(role_id)
            if not role:
                continue
            should_have = member.id in whitelist
            has_role = role_id in current_ids
            if should_have and not has_role:
                add.append(role)
            if not should_have and has_role:
                remove.append(role)

        if add or remove:
            new_roles = [r for r in member.roles if r not in remove] + add
            await member.edit(roles=new_roles, reason="Role sync")

        embed = discord.Embed(
            title=f"Role Sync: {member.display_name}",
            color=discord.Color.green()
        )

        if add:
            embed.add_field(name="Added Roles", value="\n".join(r.mention for r in add), inline=False)
        if remove:
            embed.add_field(name="Removed Roles", value="\n".join(r.mention for r in remove), inline=False)
        if not add and not remove:
            embed.description = "No changes were needed."

        return embed

    # ── /link (self-service verify) ───────────────────────────────────────────
    @app_commands.command(name="link", description="Sync your roles with the server allow-list.")
    @app_commands.guilds(*[discord.Object(id=g) for g in GUILD_IDS])
    async def verify(self, interaction: discord.Interaction):
        embed = await self._sync_roles(interaction.user)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    # ── /update (staff-only) ─────────────────────────────────────────────────
    @app_commands.command(name="update", description="Sync roles for another member.")
    @app_commands.describe(member="The user to be updated")
    @app_commands.guilds(*[discord.Object(id=g) for g in GUILD_IDS])
    async def update_user(self, interaction: discord.Interaction, member: discord.Member):
        if interaction.user.id not in UPDATE_ALLOWED_USERS:
            await interaction.response.send_message(
                "You’re not allowed to use this command.", ephemeral=True
            )
            return

        embed = await self._sync_roles(member)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    # ── /update_all (staff-only) ─────────────────────────────────────────────
    @app_commands.command(name="update_all", description="Sync roles for all members in the server.")
    @app_commands.guilds(*[discord.Object(id=g) for g in GUILD_IDS])
    async def update_all_users(self, interaction: discord.Interaction):
        if interaction.user.id not in UPDATE_ALLOWED_USERS:
            await interaction.response.send_message(
                "You’re not allowed to use this command.", ephemeral=True
            )
            return

        await interaction.response.send_message(
            "Syncing all members. This may take a moment...", ephemeral=True
        )

        guild = interaction.guild
        updated_members = []
        unchanged_count = 0

        for member in guild.members:
            embed = await self._sync_roles(member)
            if embed.fields or (embed.description and "No changes" not in embed.description):
                summary = ""
                for field in embed.fields:
                    summary += f"**{field.name}:** {field.value}\n"
                updated_members.append((member.display_name, summary.strip()))
            else:
                unchanged_count += 1

        if not updated_members:
            await interaction.followup.send("No changes needed for any member.", ephemeral=True)
            return

        full_summary = discord.Embed(
            title="Bulk Role Sync Complete",
            description=f"**Members Updated:** {len(updated_members)}\n**No Changes:** {unchanged_count}",
            color=discord.Color.blurple()
        )

        for name, changes in updated_members[:20]:  # Cap to avoid embed limits
            full_summary.add_field(name=name, value=changes, inline=False)

        if len(updated_members) > 20:
            full_summary.add_field(
                name="Note",
                value=f"...and {len(updated_members) - 20} more members were updated.",
                inline=False
            )

        full_summary.set_footer(text="Sync completed for all members.")
        await interaction.followup.send(embed=full_summary, ephemeral=True)

panel_sent = False

# ID of the channel where the panel should be sent
PANEL_CHANNEL_ID = 1382501358263079096  # ⬅️ Replace with your panel channel ID
@bot.tree.interaction_check
@bot.tree.command(name="panel", description="Show the ticket panel (one-time setup)")
@app_commands.guilds(*[discord.Object(id=g) for g in GUILD_IDS])
async def panel(inter: discord.Interaction):
    global panel_sent

    if panel_sent:
        await inter.response.send_message("⚠️ The panel has already been sent.", ephemeral=True)
        return

    if inter.channel.id != PANEL_CHANNEL_ID:
        await inter.response.send_message("❌ You can only use this command in the designated panel channel.", ephemeral=True)
        return

    embed = discord.Embed(
        title="🎫 Create a Ticket",
        description="Select a topic from the dropdown menu below to open a ticket.",
        color=discord.Color.blurple()
    )

    await inter.response.send_message(embed=embed, view=TicketDropdown(), ephemeral=False)

    # Mark the panel as sent so it doesn't run again
    panel_sent = True


# View for dropdown
class TicketDropdown(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(TicketTypeSelect())

# Dropdown select
class TicketTypeSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label=opt["label"],
                description=opt["description"],
                emoji=opt["emoji"],
                value=key
            ) for key, opt in TICKET_OPTIONS.items()
        ]
        super().__init__(placeholder="Select a topic", options=options, custom_id="ticket_select")

    async def callback(self, inter: discord.Interaction):
        await create_ticket(inter, self.values[0])


TICKET_ALLOWED_ROLES = {1373967235885961338}
# Create ticket logic
async def create_ticket(inter: discord.Interaction, topic_key: str):
    user_roles = [role.id for role in inter.user.roles]
    if not any(role_id in TICKET_ALLOWED_ROLES for role_id in user_roles):
        await inter.response.send_message("🚫 You are not allowed to create a ticket.", ephemeral=True)
        return
    config = TICKET_OPTIONS[topic_key]
    user = inter.user
    guild = inter.guild
    category = guild.get_channel(config["category_id"])
    name = f"{user.name}-{config['label']}"

    if get(category.text_channels, name=name):
        await inter.response.send_message(f"You already have a ticket: {name}", ephemeral=True)
        return

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(view_channel=False),
        user: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True),
        guild.me: discord.PermissionOverwrite(view_channel=True)
    }

    # Add handler roles
    handler_mentions = []
    for handler_id in config["handler_ids"]:
        handler = guild.get_role(handler_id)
        if handler:
            overwrites[handler] = discord.PermissionOverwrite(view_channel=True)
            handler_mentions.append(handler.mention)

    chan = await category.create_text_channel(name=name, overwrites=overwrites)

    # Create embed
    embed = discord.Embed(
        title=f"🎫 {config['label']}",
        description=(
            f"Ticket Created By: {user.mention}\n\n"
            f"Please explain why you opened this ticket below.\n"
            f"A member of the support team will assist you shortly.\n\n"
            f"-# Do not ping any!"
        ),
        color=discord.Color.green()
    )

    # Send ticket message tagging both user and handlers
    mentions = " ".join(handler_mentions + [user.mention])
    await chan.send(content=mentions, embed=embed)
    await inter.response.send_message(f"🎟 Ticket created: {chan.mention}", ephemeral=True)


# Close ticket with transcript
@bot.tree.interaction_check
@bot.tree.command(name="close", description="Close the ticket and send transcript")
@app_commands.describe(
    user_id="User ID of the ticket creator",
    reason="Reason for ticket",
    notes="Additional notes"
)
@app_commands.guilds(*[discord.Object(id=g) for g in GUILD_IDS])
async def close_cmd(inter: discord.Interaction, user_id: str, reason: str, notes: Optional[str] = None):
    chan = inter.channel
    notes = notes or "N/A"

    await inter.response.send_message("📄 Generating transcript and closing ticket...", ephemeral=True)

    buffer = io.StringIO()
    buffer.write(f"USER ID: {user_id}\nREASON: {reason}\nNOTES: {notes}\n")
    buffer.write("-" * 40 + "\n")

    async for msg in chan.history(limit=None, oldest_first=True):
        timestamp = msg.created_at.strftime("%Y-%m-%d %H:%M:%S")
        buffer.write(f"[{timestamp}] {msg.author.display_name} ({msg.author.id}): {msg.clean_content}\n")

    buffer.seek(0)
    transcript = discord.File(io.BytesIO(buffer.read().encode()), filename=f"{chan.name}_transcript.txt")

    # Try to find correct transcript channel
    transcript_sent = False
    for config in TICKET_OPTIONS.values():
        category = inter.guild.get_channel(config["category_id"])
        if chan.category_id == category.id:
            log_channel = inter.guild.get_channel(config["transcript_channel_id"])
            if log_channel:
                await log_channel.send(content=f"Transcript from {chan.name}", file=transcript)
                transcript_sent = True
                break

    if not transcript_sent:
        await inter.followup.send("⚠️ Could not find matching transcript channel.", ephemeral=True)

    await chan.delete(reason="Ticket closed by staff")

# Add user
@bot.tree.interaction_check
@bot.tree.command(name="add", description="Add a user to this ticket")
@app_commands.describe(member="User to add")
@app_commands.guilds(*[discord.Object(id=g) for g in GUILD_IDS])
async def add_cmd(inter: discord.Interaction, member: discord.Member):
    await inter.channel.set_permissions(member, view_channel=True, send_messages=True)
    await inter.response.send_message(f"{member.mention} added to the ticket.", ephemeral=True)

# Rename ticket
@bot.tree.interaction_check
@bot.tree.command(name="rename", description="Rename this ticket")
@app_commands.describe(new_name="New name")
@app_commands.guilds(*[discord.Object(id=g) for g in GUILD_IDS])
async def rename_cmd(inter: discord.Interaction, new_name: str):
    await inter.channel.edit(name=new_name)
    await inter.response.send_message(f"Renamed channel to `{new_name}`", ephemeral=True)

# Helper for reopening tickets
def get_ticket_category(guild: discord.Guild):
    # Default to first category in the options
    first_key = list(TICKET_OPTIONS.keys())[0]
    return guild.get_channel(TICKET_OPTIONS[first_key]["category_id"])

# Reopen command
@bot.tree.interaction_check
@bot.tree.command(name="reopen", description="Reopen a ticket for a user")
@app_commands.describe(
    user="The user to reopen the ticket for",
    original_reason="Reason the ticket was originally opened",
    notes="Any notes about why it's being reopened"
)
@app_commands.guilds(*[discord.Object(id=g) for g in GUILD_IDS])
async def reopen_cmd(inter: discord.Interaction, user: discord.Member, original_reason: str, notes: Optional[str] = None):
    guild = inter.guild
    cat = get_ticket_category(guild)
    name = f"{user.name}-{user.discriminator}-reopened"

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(view_channel=False),
        user: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True),
        guild.me: discord.PermissionOverwrite(view_channel=True)
    }

    for config in TICKET_OPTIONS.values():
        for handler_id in config["handler_ids"]:
            role = guild.get_role(handler_id)
            if role:
                overwrites[role] = discord.PermissionOverwrite(view_channel=True)

    chan = await cat.create_text_channel(name=name, overwrites=overwrites)
    embed = discord.Embed(
        title="🔄 Ticket Reopened",
        description=(
            f"{user.mention} your ticket has been reopened!\n"
            f"**Original Reason:** {original_reason}\n"
            f"**Notes:** {notes or 'N/A'}"
        ),
        color=discord.Color.orange()
    )
    await chan.send(embed=embed)
    await inter.response.send_message(f"Reopened ticket: {chan.mention}", ephemeral=True)        

    
        # bot funstions cogs

        # ───── Events ─────
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(type=discord.ActivityType.watching, name="Foolish Server Activities")
    )

    try:
        await bot.add_cog(StaffServerInviteLink(bot))
        await bot.add_cog(MediaCommands(bot))
        await bot.add_cog(MessageRepeater(bot))
        await bot.add_cog(moderationserver(bot))
        await bot.add_cog(publicrelationsdepartmentserver(bot))
        await bot.add_cog(appealsserver(bot))
        await bot.add_cog(InformationEmbeds(bot))
        await bot.add_cog(SupportTeamTicketGreeting(bot))
        await bot.add_cog(AdminTeamTicketGreeting(bot))
        await bot.add_cog(PresidentialTeamTicketGreeting(bot))
        await bot.add_cog(RulesEmbed(bot))
        await bot.add_cog(VerifyRoles(bot))
        await bot.add_cog(TicketLogger(bot))

        
        total_synced = 0
        for gid in GUILD_IDS:
            synced = await bot.tree.sync(guild=discord.Object(id=gid))
            print(f"🔁 Synced {len(synced)} command(s) to guild {gid}")
            total_synced += len(synced)

        print(f"✅ Total synced commands: {total_synced}")
    except Exception as e:
        print(f"❌ Error syncing commands: {e}")

# ───── Run the Bot ─────
TOKEN = "MTM3NjMzNDgxODk0OTg1NzQxMg.GqoGQ-.6RKgSwzHejN4Le1fXXEv8EexXGBJED1NOh9dhk"
bot.run(TOKEN)