def get_starts_urls():

    urls = []
    provinceId = []
    cityId = {}
    for id in range(1,10):
        prov = '1010'+str(id)+'000'
        provinceId.append(prov)
    for id in range(10,34):
        prov = '101'+str(id)+'000'
        provinceId.append(prov)
    for prov in provinceId:
        citylist = []
        for id in range(1,4):
            cid = prov[:-1] + str(id)
            citylist.append(cid)
        for id in range(10,100):
            cid = prov[:-2] + str(id)
            citylist.append(cid)

        cityId[prov] = citylist

    for prov in provinceId:
        for cid in cityId[prov]:
            for page in range(1,4):
                url = 'http://search.zhenai.com/v2/search/getPinterestData.do?sex=1&agebegin=18&ageend=30&workcityprovince={}&workcitycity={}' \
                    '&info=&h1=-1&h2=-1&salaryBegin=-1&salaryEnd=-1&occupation=-1&h=-1&c=-1&workcityprovince1=-1&workcitycity1=-1&constellation=-1' \
                    '&animals=-1&stock=-1&belief=-1&lvBegin=-1&lvEnd=-1&condition=66&orderby=hpf&hotIndex=&online=&currentpage={}' \
                    '&topSearch=false'.format(prov, cid, page)
                urls.append(url)
    return urls
