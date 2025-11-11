import math
import time
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.script import Translation
from pyrogram import enums

# Configuration
SHOW_PROGRESS = True
UPDATE_INTERVAL = 5  # Update every 5 seconds


async def progress_for_pyrogram(current, total, ud_type, message, start):
    """
    Progress function that works for both download and upload
    """
    if not SHOW_PROGRESS:
        return
    
    now = time.time()
    diff = now - start
    
    # Update at start, intervals, or completion
    if diff < 1 or round(diff % UPDATE_INTERVAL) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff if diff > 0 else 0
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000 if speed > 0 else 0
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        # Optimized progress bar generation
        filled = math.floor(percentage / 10)
        progress = f"┏━━━━✦[{'▣' * filled}{'▢' * (10 - filled)}]✦━━━━"

        tmp = progress + Translation.PROGRESS.format(
            round(percentage, 2),
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            estimated_total_time if estimated_total_time else "0 s"
        )
        
        try:
            # Try to edit as text first (for downloads), then as caption (for uploads)
            text_content = Translation.PROGRES.format(ud_type, tmp)
            
            try:
                # For regular messages (downloads)
                await message.edit_text(
                    text=text_content,
                    parse_mode=enums.ParseMode.MARKDOWN,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton('⛔ Cancel', callback_data=f"cancel_download+{message.id}")]
                    ])
                )
            except AttributeError:
                # For media messages (uploads) - use edit_caption
                await message.edit_caption(
                    caption=text_content,
                    parse_mode=enums.ParseMode.MARKDOWN,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton('⛔ Cancel', callback_data=f"cancel_download+{message.id}")]
                    ])
                )
        except Exception as e:
            # Silent fail for flood wait or other errors
            pass


def humanbytes(size):
    """Convert bytes to human readable format"""
    if not size:
        return "0 B"
    
    power = 1024
    n = 0
    units = {0: 'B', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
    
    while size >= power and n < 4:
        size /= power
        n += 1
    
    return f"{size:.2f} {units[n]}"


def TimeFormatter(milliseconds: int) -> str:
    """Format milliseconds to human readable time"""
    if not milliseconds:
        return "0s"
    
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    
    parts = []
    if days:
        parts.append(f"{days}d")
    if hours:
        parts.append(f"{hours}h")
    if minutes:
        parts.append(f"{minutes}m")
    if seconds:
        parts.append(f"{seconds}s")
    if milliseconds and not parts:  # Only show ms if no larger units
        parts.append(f"{milliseconds}ms")
    
    return ", ".join(parts) if parts else "0s"


# Toggle and configuration functions
def toggle_progress(show: bool):
    """Enable or disable progress bar display"""
    global SHOW_PROGRESS
    SHOW_PROGRESS = show
    return f"Progress bar {'enabled' if show else 'disabled'}"


def set_update_interval(seconds: int):
    """Set how often the progress bar updates (minimum 1 second)"""
    global UPDATE_INTERVAL
    UPDATE_INTERVAL = max(1, seconds)
    return f"Update interval set to {UPDATE_INTERVAL} seconds"
