from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)
import aiohttp
from bs4 import BeautifulSoup
from emoji import emojize
import os


async def obtain_results_from_query(query):
    search_string = query.replace(" ", "+")
    url = f"https://www.seventhstring.com/fbindex.html?z_srchstr={search_string}&z_bklist=2&z_dpage=Results&z_titlelen=0&cs1=1&cs2=1&cs3=1&cs5=1&re1=1&re2=1&re3=1&cs6=1&cs12=1&cs8=1&cs9=1&aeb=1&hlp=1&hl1=1&hl11=1&hl12=1&hl2=1&hl3=1&hl8=1&hl9=1&hl4=1&hl5=1&hl6=1&hl7=1&hl13=1&fm1=1&fm2=1&fm3=1&fm4=1&fm5=1&cc0=1&lg1=1&ltfk=1&wb1=1&wb2=1&wb3=1&bbeb=1&jbg=1&sb2=1&wrb=1&wrj=1&le1=1&dh1=1&dh2=1&lhb=1&pm=1&jchl=1&trhl=1&cmhl=1&kbhl=1&alhl=1&bef=1&omni=1&gs0=1&gs1=1&jb0=1&jb1=1&jb2=1&hlrb=1&hlb=1&ts1=1&ts2=1&ts3=1&belt=1&bbjs=1&ab0=1&pk0=1&pk1=1&rgm0=1&rgm1=1&md0=1&md1=1&md2=1&pdsa=1&hlrb1=1&hlrb2=1&hlrb3=1&hlrb4=1&hlrb5=1&hlrb6=1&hlvrb1=1&hlvrb2=1&hlvrb3=1&hlvrb4=1&720=1&721=1&722=1&723=1&724=1&725=1&726=1&727=1&orb1=1&orb2=1&orb3=1&ovrb=1&sch=1&rds=1"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()

    soup = BeautifulSoup(html, "html.parser")
    results = soup.find_all("p")[:-1]
    results = [
        result.text for result in results if "your search. Here" not in result.text
    ]
    results = [results[i].replace(results[i + 1], "") for i in range(len(results) - 1)]

    if len(results) < 1:
        return {}

    end_string = "\n\n\n\n\nSeventh String Home\n\n\n\n\n"
    results[-1] = results[-1].replace(end_string, "")
    results = [result.strip().split("\n") for result in results]
    results = {result[0]: result[1:] for result in results}

    return results


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "Send me any <i>jazz standard song</i> :musical_note: and "
        "I will tell you in which <b>books</b> :books: (if any) you can find it!"
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=emojize(message),
        parse_mode="html",
    )


async def query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.split()
    query = " ".join(query)
    result = await obtain_results_from_query(query)
    message = ""
    for book, songs in result.items():
        message += f":books: <b>{book}</b>:\n"
        for song in songs:
            message += f"\t\t\t\t\t:musical_note: <i>{song}</i>\n"
        message += "\n"
    if message == "":
        message = f":cross_mark: The song <i>{query}</i> was not found anywhere, sorry :loudly_crying_face:"

    await context.bot.send_message(
        chat_id=update.message.chat_id,
        text=emojize(message),
        parse_mode="html",
    )


if __name__ == "__main__":
    TOKEN = os.environ.get("BOT_TOKEN")

    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler("start", start)
    query_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), query)

    application.add_handler(start_handler)
    application.add_handler(query_handler)

    application.run_polling()
