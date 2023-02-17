import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "21119132"))
    API_HASH = os.environ.get("API_HASH", "c0a90d0ba66e6bdea356894a55f4856e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5613698470:AAGSRWiGDSS6EZSX-STpbTbbb-NqP4VNOSg")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1sBuzEwZTqGvfB-D-STC3yGYYDffP7fLwujNpx84i8TraXQkud7OcTadRTzwNYvMzVvtoJWbECGDhnthIYkYzING_d4qxB2UDHenKtWHwP0O9bbwMwqsoVQZ_Qqq1m7MObuzkUJ95v5bUijptw2_YF4rxd67DkMPZhz3imBDpkxZR6bi9mBK7dovLhyewkYddbnwoOzR5Wer2NbzeswA28y1c4gRfyOFsN_QK3aSxjM-WXIeMSBVJXR3PDXkb0JCOotLi2_MRVmnENb79-xaWLbofdpWG1GdMPCpn-8DL8ECByTej05g4fdQHav2ki8tatzogL-6e3BxATAdwiEqvuZCOk=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Abdcmusicbot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5968970670")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
