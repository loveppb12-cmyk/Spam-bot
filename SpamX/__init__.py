# fix_pyrogram.py
import asyncio
import sys

def fix_pyrogram_event_loop():
    """Fix Pyrogram's event loop issue in Python 3.10+"""
    # Method 1: Try to get existing loop
    try:
        loop = asyncio.get_event_loop()
        return loop
    except RuntimeError:
        pass
    
    # Method 2: Create new loop for main thread
    if sys.platform == "win32":
        # Windows needs special handling
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop

# Apply fix immediately
fix_pyrogram_event_loop()
