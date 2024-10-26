def searchFor(searchPhrase, catListings):
    '''
        searchFor searches for a searchPhrase inside a catListings

        returns: listof the objects that match in a desired order
    '''
    #output lists
    prio = {'prio1': [], 'prio2': [], 'prio3': [], 'prio4': []}
    #They are filtered by priority, so the higher priority is put first on a list.
    searchPhrase = searchPhrase.lower()
    for listing in catListings:
        if searchPhrase == listing.product_name.lower():
            prio['prio1'].append(listing)
        elif searchPhrase in listing.product_name.lower():
            prio['prio2'].append(listing)
        elif searchPhrase in listing.location.lower():
            prio['prio3'].append(listing)
        elif searchPhrase in listing.description.lower():
            prio['prio4'].append(listing)

    res = []
    res.extend(prio['prio1'])
    res.extend(prio['prio2'])
    res.extend(prio['prio3'])
    res.extend(prio['prio4'])
    return res
 # returns list of lists of listings instead of a list of listings? 

def advancedSearch(catListings, productPhrase, locationPhrase = None):
    '''
    advancedSearch returns the prefered listing based on advanced search
    '''

    #checking if advanced search is even required
    if not locationPhrase:
        return searchFor(productPhrase, catListings)
    
    productPhrase = productPhrase.lower()
    locationPhrase = locationPhrase.lower()
    prio = {'prio1': [], 'prio2': [], 'prio3': []}
    #They are filtered by priority, so the higher priority is put first on a list.
    for listing in catListings:
        if productPhrase == listing.product_name.lower() and locationPhrase == listing.location.lower():
            prio['prio1'].append(listing)
        elif productPhrase in listing.product_name.lower() and locationPhrase in listing.location.lower():
            prio['prio2'].append(listing)
        elif productPhrase in listing.description.lower() or locationPhrase in listing.description.lower():
            prio['prio3'].append(listing)
    
    res = []
    res.extend(prio['prio1'])
    res.extend(prio['prio2'])
    res.extend(prio['prio3'])
    return res
