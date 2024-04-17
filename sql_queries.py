# Вывести топ 5 самых коротких по длительности перелетов.
# Duration - разница между scheduled_arrival и scheduled_departure.
# В ответе должно быть 2 колонки [flight_no, duration]
TASK_1_QUERY = """ SELECT flight_no, (flights.scheduled_arrival - flights.scheduled_departure) as duration FROM flights ORDER BY duration LIMIT 5;
"""
#  flight_no | duration
# -----------+----------
#  PG0235    | 00:25:00
#  PG0234    | 00:25:00
#  PG0233    | 00:25:00
#  PG0235    | 00:25:00
#  PG0234    | 00:25:00


# Вывести топ 3 рейса по числу упоминаний в таблице flights
# количество упоминаний которых меньше 50
# В ответе должно быть 2 колонки [flight_no, count]
TASK_2_QUERY = """ SELECT flight_no, COUNT(1) FROM flights GROUP BY flight_no HAVING COUNT(1) < 50 ORDER BY COUNT(1) DESC LIMIT 3;
"""
#  flight_no | count
# -----------+-------
#  PG0260    |    27
#  PG0371    |    27
#  PG0310    |    27

# Вывести число перелетов внутри одной таймзоны
# Нужно вывести 1 значение в колонке count
TASK_3_QUERY = """ SELECT COUNT(CASE WHEN ad_dep.timezone=ad_arr.timezone THEN 1 END) FROM flights AS f LEFT JOIN airports_data AS ad_dep ON ad_dep.airport_code=f.departure_airport LEFT JOIN airports_data AS ad_arr ON ad_arr.airport_code=f.arrival_airport;
"""
#  count
# --------
#  16824
