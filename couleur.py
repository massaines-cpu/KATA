color_data = [{
  "time_start": "1:38:01",
  "time_end": "18:48:05",
  "color": "#640c0b"
}, {
  "time_start": "7:50:25",
  "time_end": "10:41:37",
  "color": "#a61276"
}, {
  "time_start": "0:47:40",
  "time_end": "11:05:24",
  "color": "#922553"
}, {
  "time_start": "7:22:26",
  "time_end": "9:08:07",
  "color": "#8af9f7"
}, {
  "time_start": "0:05:20",
  "time_end": "12:06:49",
  "color": "#1fc771"
}, {
  "time_start": "4:32:28",
  "time_end": "11:02:06",
  "color": "#d7718e"
}, {
  "time_start": "6:00:10",
  "time_end": "9:53:21",
  "color": "#27f414"
}, {
  "time_start": "0:04:30",
  "time_end": "9:25:44",
  "color": "#7e79b6"
}, {
  "time_start": "0:24:42",
  "time_end": "12:27:28",
  "color": "#6eb31b"
}, {
  "time_start": "7:06:52",
  "time_end": "22:36:25",
  "color": "#a03827"
}]

# Afficher les couleurs de la durée la plus courte à la durée la plus longue. (On a le droit d’utiliser pandas…)
from datetime import datetime

def calcul_duree(dictionnaire):
    start = datetime.strptime(dictionnaire['time_start'], '%H:%M:%S')
    end = datetime.strptime(dictionnaire['time_end'], '%H:%M:%S')
    calcul = end - start
    return calcul

color_data.sort(key=calcul_duree)

print(color_data)


