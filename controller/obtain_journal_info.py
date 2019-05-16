from scrapy import aiche, Applied_Mechanics, china_OE

def obtain_journal_info(joural_name):
    get_func = {
        "AICHE_JOURNAL": aiche.obtain_info,
        "Applied_Mechanics": Applied_Mechanics.obtain_info,
        "China_OE": china_OE.obtain_info
    }

    try:
        get_func[joural_name]()
    except KeyError:
        pass


if __name__ == '__main__':
    obtain_journal_info("Applied_Mechanics")