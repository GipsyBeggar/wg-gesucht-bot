import os
from wg_gesucht.crawler import WgGesuchtCrawler


login_info={
    "email": "youremail@email.id",
    "password": "password",
    "phone": "phone number is optional, empty this if no number"
}

ad_links_folder= "absolute dir path where this script will store links it has applied for"
offline_ad_folder= "absolute dir path where this script will store ads which are pulled away form wg-gesucht"
logs_folder= "absolute dir path where this script will store logs"
email_template_name="in wg gesucht you can save an email template with a name state that template name here"


def checkDir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
def start():
    checkDir(ad_links_folder)
    checkDir(offline_ad_folder)
    checkDir(logs_folder)

    crawler = WgGesuchtCrawler(login_info, ad_links_folder, offline_ad_folder, logs_folder, email_template_name)
    crawler.sign_in()
    crawler.search() #this will start searching and applying automatically

def main():
    start()


if __name__ == '__main__':
    main()    