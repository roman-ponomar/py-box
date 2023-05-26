def main_one_day():
    #InsertIntegrationActivities(18)
    dt = date.today()
    ads_list_ids = 0
    try:
        print("Обновление данных справочника Dolphin... ")
        print("Обновление данных начато в ", datetime.now())
        ads_list_ids = transform_data()
        print("Обновление данных закончено в ", datetime.now())
    except:
        err_handle("Произошла ошибка при обновлении данных справочника Dolphin!")
