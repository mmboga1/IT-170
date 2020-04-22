import socket



domainList = ['geomobldn.org',
'posdgis.wordpress.com',
'sproke.blogspot.com',
'blog.americaview.org',
'blog.zolnai.ca',
'blog.gisuser.com',
'www.arc2earth.com',
'geospatial.blogs.com',
'billthorp.wordpress.com',
'www.azavea.com',
'boundlessgeo.com',
'www.donmeltz.com',
'www.orfeo-toolbox.org',
'blog.shoutis.org',
'bob-roberts.net',
'www.bostongis.com',
'brainoff.com',
'www.gretchenpeterson.com',
'www.directionsmag.com',
'www.disruptivegeo.com',
'pvanb.wordpress.com',
'www.edparsons.com',
'sextantegis.blogspot.com',
'www.espatial.com',
'www.evs-islands.com',
'fantomplanet.wordpress.com',
'fwarmerdam.blogspot.com',
'anitagraser.com',
'gvsigmobileonopenmoko.wordpress.com',
'www.aerometrex.com.au',
'fuzzytolerance.info',
'www.galdosinc.com',
'dmorissette.blogspot.com',
'gis-elektrika.blogspot.com',
'blog.burhum.com',
'geodatapolicy.wordpress.com',
'geodribble.blogspot.com',
'geoext.blogspot.com',
'geographika.co.uk',
'geoinformaticstutorial.blogspot.com',
'tylerickson.blogspot.com',
'geojason.info',
'geomaticblog.net',
'geopdf.blogspot.com',
'geops.de',
'geoscriptblog.blogspot.com',
'blog.geoserver.org',
'geo-solutions.blogspot.com',
'geospatialelucubrations.blogspot.com',
'epsg4253.wordpress.com',
'nyalldawson.net',
'geosprocket.blogspot.com',
'geothought.blogspot.com',
'gfoss.blogspot.com',
'www.giscloud.com',
'gismaps.wordpress.com',
'blog.rtwilson.com',
'knowwhereconsulting.co.uk',
'www.gisn8.com',
'gisnuts.com',
'geosquan.blogspot.com',
'www.how2map.com',
'bbox.me',
'blog.lidarnews.com',
'cholmes.wordpress.com',
'izwe.blogspot.com',
'spatiallyadjusted.com',
'jgrasstechtips.blogspot.com',
'kelsocartography.com',
'learondalby.blogspot.com',
'lptf.blogspot.com',
'letters-sal.blogspot.com',
'lin-ear-th-inking.blogspot.com',
'blog.lostinspatial.com',
'makingmaps.net',
'mapbutcher.com',
'mapbrief.com',
'mapfishblog.blogspot.com',
'www.mapgears.com',
'mapoholic.wordpress.com',
'mapperz.blogspot.com',
'sushantakabi.blogspot.com',
'www.web-maps.com',
'mapzlibrarian.blogspot.com',
'blog.mastermaps.com',
'jamiepopkin.blogspot.com',
'www.vicchi.org',
'mousebirdconsulting.blogspot.com',
'nathanw.net',
'njgeo.org',
'news.nsgic.org',
'oegeo.wordpress.com',
'ogleearth.com',
'www.archaeogeek.com',
'www.spatialytics.org',
'openaddresses.blogspot.com',
'blog.cleverelephant.ca',
'postgis.net',
'prioleauadv.com',
'www.jamesrichards.com',
'rexdotnet.blogspot.com',
'blog.safe.com',
'sgillies.net',
'arnulf.us',
'www.sharpgis.net',
'nosolosoftware.com',
'grimmeister.wordpress.com',
'blogs.msdn.microsoft.com',
'www.spatialexplorations.net',
'spatialintel.blogspot.com',
'spatiallaw.blogspot.com',
'gisconsultancy.com',
'www.ralphstraumann.ch',
'spatialityblog.com',
'gis.blogoverflow.com',
'thesteve0.wordpress.com',
'surveying-mapping-gis.blogspot.com',
'crschmidt.net',
'blog.delorme.com',
'evarigisconsulting.wordpress.com',
'blog.epa.gov',
'field-guide.blogspot.com',
'themapguyde.blogspot.com',
'ambergis.wordpress.com',
'kiwigis.blogspot.com',
'thes.wordpress.com',
'thinkwhere.wordpress.com',
'www.kralidis.ca',
'blog.trackprofiler.com',
'udig-news.blogspot.com',
'usingopendata.wordpress.com',
'veryspatial.com',
'viswaug.wordpress.com',
'walteis.wordpress.com',
'webmapdesign.blogspot.com',
'zekiah.com']


ipAddressList = []


for item in domainList:
    try:
        ipAddressList.append(socket.gethostbyname(item))
        
    except:
        ipAddressList.append('IP address cannot be resolved.')
        

domainName = ''

while domainName != '999':
    domainName = input('Enter the domain address(Enter 999 to exit): ')
    counter = False
    number = 0
    for item in domainList:
        if item == domainName:
            counter = True
            print(ipAddressList[number])
        number = number + 1
    if counter == False and domainName != '999':
        print("The domain name cannot be found in the local directory.")
print('You have exited the program.')    
    



            
    
    
