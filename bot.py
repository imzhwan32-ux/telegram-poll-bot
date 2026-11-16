import logging
from datetime import time
import pytz
from telegram.ext import ApplicationBuilder, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# PASTE YOUR TOKEN AND GROUP ID BELOW:
TOKEN = "9148374194:AAEJwmwRAfy_60XLQ_DOBPjPZF-_OVNDwLA"
GROUP_CHAT_ID = -1001234567890  # Must be your group's numeric ID (starts with -100)


async def send_daily_poll(context: ContextTypes.DEFAULT_TYPE):
  """Sends the daily 0-10 points poll to the group every morning at 7:00 AM."""
  question = "بەیانیتان باش، خاڵەکانی دوێنێتان هەڵبژێرن، بەهیوای ڕۆژێکی خۆش"

  options = [
      "0 Points",
      "1 Point",
      "2 Points",
      "3 Points",
      "4 Points",
      "5 Points",
      "6 Points",
      "7 Points",
      "8 Points",
      "9 Points",
      "10 Points (Max!)",
  ]

  try:
    await context.bot.send_poll(
        chat_id=GROUP_CHAT_ID,
        question=question,
        options=options,
        is_anonymous=False,
        allows_multiple_answers=False,
    )
  except Exception as e:
    logging.error(f"Failed to send scheduled poll: {e}")


def main():
  application = ApplicationBuilder().token(TOKEN).build()
  job_queue = application.job_queue

  # Set your local timezone (Asia/Baghdad)
  local_tz = pytz.timezone("Asia/Baghdad")

  # Schedules the poll for 7:00 AM daily
  job_queue.run_daily(
      send_daily_poll,
      time=time(hour=7, minute=0, second=0, tzinfo=local_tz),
  )

  print("Bot is running and scheduler is active...")
  application.run_polling()


if __name__ == "__main__":
  main()