from bot.auto.auto_bot import AutoBot
from bot.auto.base.definitions import Utils

if __name__ == '__main__':
    auto = AutoBot()
    utils = Utils()
    
    driver = auto.open_browser()
    driver = auto.open_page(driver)
    
    user = utils.USER_TEXT
    password = utils.PASS_TEXT
    
    # Insira as credenciais de login
    auto.type_credentials(driver, user, password)
    
    # Faz as quests diárias
    # auto.daily_quests(driver)
    
    auto.end(driver)
    