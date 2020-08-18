from django.http import HttpResponse
import json
from django.db import connections

def dictfetchall(cursor):
	desc = cursor.description
	return [
	dict(zip([col[0] for col in desc], row))
		for row in cursor.fetchall()
		]

def f2(a,b):
	if b['c']-a['c']<0:
		return 1
	else:
		return -1

def index(request):
	raw = [
		{
			"hno":1,
			"htitle1":"谧月",
			"htitle2":"-复古墨绿色天窗房间",
			"hprice":20,
			"htype":"大方别墅",
			"hpic":"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1597748215626&di=35aaffe05341669cf30d657ad1d54e11&imgtype=0&src=http%3A%2F%2Fimgs.bzw315.com%2Fuploadfiles%2Fversion2%2F0%2F20160929%2F201609291502316133.jpg",
			"hlongitude":117.13526,
			"hlatitude":36.19198,
			"labels":[
				{"lname":"舒适"},
				{"lname":"温馨"}
				
				],
			"images":[
				{"pno":1,"purl":"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1597748215626&di=35aaffe05341669cf30d657ad1d54e11&imgtype=0&src=http%3A%2F%2Fimgs.bzw315.com%2Fuploadfiles%2Fversion2%2F0%2F20160929%2F201609291502316133.jpg"},
				{"pno":2,"purl":"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1597749232434&di=0b514738dcd1ef6843dc3a6f0df56674&imgtype=0&src=http%3A%2F%2Fsem.g3img.com%2Fg3img%2Fcsar2018%2Fc2_20190111171015_89578.jpg"}
				
				],
			"c":1,
			"distance":1,
			"danwei":"km"

		},

		{
			"hno":2,
			"htitle1":"董小院.左邻",
			"htitle2":"故宫/ 后海",
			"hprice":20,
			"htype":"清新房间",
			"hpic":"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1597748215626&di=35aaffe05341669cf30d657ad1d54e11&imgtype=0&src=http%3A%2F%2Fimgs.bzw315.com%2Fuploadfiles%2Fversion2%2F0%2F20160929%2F201609291502316133.jpg",
			"hlongitude":117.13526,
			"hlatitude":36.19198,
			"labels":[
				{"lname":"舒适"},
				{"lname":"温馨"}
				
				],
			"images":[
				{"pno":1,"purl":"https://z1.muscache.cn/im/pictures/91c1bda8-39eb-4fd7-b8ae-98ac52f581d1.jpg?aki_policy=x_large"},
				{"pno":2,"purl":"https://z1.muscache.cn/im/pictures/643ec07f-ab28-4004-bacb-e6d4e93df4e3.jpg?aki_policy=x_large"}
				
				],
			"c":1,
			"distance":10,
			"danwei":"km"

		}
	]

	return HttpResponse(json.dumps(raw), content_type="application/json")
	# return HttpResponse("Welcome to ECHOCHINA!")

def detail(request):

	cursor = connections['default'].cursor()
	cursor.execute("select * from user limit 1")
	rawitem = dictfetchall(cursor)
	
	raw = [
		{
			"hno":1,
			"htitle1":"谧月",
			"htitle2":"-复古墨绿色天窗房间",
			"hprice":20,
			"htype":"大方别墅",
			"hpic":"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1597748215626&di=35aaffe05341669cf30d657ad1d54e11&imgtype=0&src=http%3A%2F%2Fimgs.bzw315.com%2Fuploadfiles%2Fversion2%2F0%2F20160929%2F201609291502316133.jpg",
			"hlongitude":117.13526,
			"hlatitude":36.19198,
			"labels":[
				{"lname":"舒适"},
				{"lname":"温馨"}
				
				],
			"images":[
				{"pno":1,"purl":"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1597748215626&di=35aaffe05341669cf30d657ad1d54e11&imgtype=0&src=http%3A%2F%2Fimgs.bzw315.com%2Fuploadfiles%2Fversion2%2F0%2F20160929%2F201609291502316133.jpg"},
				{"pno":2,"purl":"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1597749232434&di=0b514738dcd1ef6843dc3a6f0df56674&imgtype=0&src=http%3A%2F%2Fsem.g3img.com%2Fg3img%2Fcsar2018%2Fc2_20190111171015_89578.jpg"}
				
				],
			"c":1,
			"distance":1,
			"danwei":"km"

		}
	]

	return HttpResponse(json.dumps(raw), content_type="application/json")
