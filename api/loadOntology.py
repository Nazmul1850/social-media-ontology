from owlready2 import *

onto_path.append("/home/nazmul/Documents/GitHub/CSE400/Protege")
onto = get_ontology("http://www.semanticweb.org/user/ontologies/2022/11/Social_Influencer_V_1#")
onto.load()


def getInstagramData():
    data = onto.Instagram.instances()
    all = []
    for account in data:
        i = account.isAccountOf[0]
        try:
            name = str(i).split('.')[1]
        except:
            name = ""
        try:
            accountName = str(account).split('.')[1]
        except:
            accountName = ""
        try:
            level = account.hasInfluenceLevel[0]
            level = str(level).split('.')[1]
        except:
            level = ""
        accountTypes = account.is_a
        accountType = ""
        for acc in accountTypes:
            acName = str(acc).split('.')[1]
            if acName != "Influencer":
                accountType = acName
        try:
            audience = i.hasAudienceIn[0]
            audience = str(audience).split('.')[1]
        except:
            audience = ""
        try:
            follower = account.hasFollower[0]
        except:
            follower = 0
        try:
            viewers = account.hasAverageViewers[0]
        except:
            viewers = 0
        try:
            comments = account.hasAverageComments[0]
        except:
            comments = 0
        try:
            likes = account.hasAverageLikes[0]
        except:
            likes = 0

        # make a dictionary
        collection = {
            "name": name,
            "accountName": accountName,
            "accountType": accountType,
            "level": level,
            "audience": audience,
            "follower": follower,
            "viewers": viewers,
            "comments": comments,
            "likes": likes
        }
        all.append(collection)  # append the dictionary to the list
    return all


def getTiktokData():
    data = onto.TikTok.instances()
    all = []
    for account in data:
        i = account.isAccountOf[0]
        try:
            name = str(i).split('.')[1]
        except:
            name = ""
        try:
            accountName = str(account).split('.')[1]
        except:
            accountName = ""
        try:
            level = account.hasInfluenceLevel[0]
            level = str(level).split('.')[1]
        except:
            level = ""
        accountTypes = account.is_a
        accountType = ""
        for acc in accountTypes:
            acName = str(acc).split('.')[1]
            if acName != "Influencer":
                accountType = acName
        try:
            audience = i.hasAudienceIn[0]
            audience = str(audience).split('.')[1]
        except:
            audience = ""
        try:
            follower = account.hasFollower[0]
        except:
            follower = 0
        try:
            viewers = account.hasAverageViewers[0]
        except:
            viewers = 0
        try:
            comments = account.hasAverageComments[0]
        except:
            comments = 0
        try:
            likes = account.hasAverageLikes[0]
        except:
            likes = 0

        # make a dictionary
        collection = {
            "name": name,
            "accountName": accountName,
            "accountType": accountType,
            "level": level,
            "audience": audience,
            "follower": follower,
            "viewers": viewers,
            "comments": comments,
            "likes": likes
        }
        all.append(collection)  # append the dictionary to the list
    return all


def getAllInfluencer():
    indi = onto.Influencer.instances()
    allData = []
    for i in indi:
        name = str(i).split('.')[1]
        try:
            account = i.hasAccount[0]
            accountName = str(account).split('.')[1]
        except:
            account = ""
        try:
            level = account.hasInfluenceLevel[0]
            level = str(level).split('.')[1]
        except:
            level = ""
        accountTypes = account.is_a
        accountType = ""
        for acc in accountTypes:
            acName = str(acc).split('.')[1]
            if acName != "Influencer":
                accountType = acName
        try:
            audience = i.hasAudienceIn[0]
            audience = str(audience).split('.')[1]
        except:
            audience = ""
        try:
            follower = account.hasFollower[0]
        except:
            follower = 0
        try:
            viewers = account.hasAverageViewers[0]
        except:
            viewers = 0
        try:
            comments = account.hasAverageComments[0]
        except:
            comments = 0
        try:
            likes = account.hasAverageLikes[0]
        except:
            likes = 0

        # make a dictionary
        collection = {
            "name": name,
            "accountName": accountName,
            "accountType": accountType,
            "level": level,
            "audience": audience,
            "follower": follower,
            "viewers": viewers,
            "comments": comments,
            "likes": likes
        }
        allData.append(collection)  # append the dictionary to the list
    return allData


def getYoutubeData():
    data = onto.Youtube.instances()
    all = []
    for account in data:
        i = account.isAccountOf[0]
        try:
            name = str(i).split('.')[1]
        except:
            name = ""
        try:
            accountName = str(account).split('.')[1]
        except:
            accountName = ""
        try:
            level = account.hasInfluenceLevel[0]
            level = str(level).split('.')[1]
        except:
            level = ""
        accountTypes = account.is_a
        accountType = ""
        for acc in accountTypes:
            acName = str(acc).split('.')[1]
            if acName != "Influencer":
                accountType = acName
        try:
            audience = i.hasAudienceIn[0]
            audience = str(audience).split('.')[1]
        except:
            audience = ""
        try:
            follower = account.hasFollower[0]
        except:
            follower = 0
        try:
            viewers = account.hasAverageViewers[0]
        except:
            viewers = 0
        try:
            comments = account.hasAverageComments[0]
        except:
            comments = 0
        try:
            likes = account.hasAverageLikes[0]
        except:
            likes = 0

        # make a dictionary
        collection = {
            "name": name,
            "accountName": accountName,
            "accountType": accountType,
            "level": level,
            "audience": audience,
            "follower": follower,
            "viewers": viewers,
            "comments": comments,
            "likes": likes
        }
        all.append(collection)
    return all
