import json

# Function to load data
def load_data(filename):
    with open(filename ,"r") as f:
        return json.load(f)
    
# Function to clean and structure the data
def clean_data(data):
    #removing users without names
    data['users'] = [user for user in data['users'] if user['name'].strip()]
    
    # Now to remove duplicate friends
    for user in data['users']:
        user['friends'] = list(set(user['friends']))
        
    #to remove inactive users
    data['users'] = [user for user in data['users'] if user['friends'] or user['liked_pages']]

    #Removing duplicate pages
    unique_pages = {}
    for page in data['pages']:
        unique_pages[page['id']] = page
    data['pages'] = list(unique_pages.values())
    return data

# function to implement PEOPLE USER MAY KNOW feature
def people_user_may_know(user_id, data):
    user_friends = {}
    for user in data['users']:
        user_friends[user['id']] = set(user['friends'])

    if user_id not in user_friends:
        return []

    direct_friends = user_friends[user_id]
    suggestions = {}
    for friend in direct_friends:
        for mutual in user_friends[friend]:
            if mutual != user_id and mutual not in direct_friends:
                #count mutual friends
                suggestions[mutual] = suggestions.get(mutual, 0) + 1
                sorted_suggestions = sorted(suggestions.items(), key = lambda x:x[1], reverse = True)
    return [user_id for user_id, mutual_count in sorted_suggestions]

# function to implement the PAGES USER MAY KNOW feature
def pages_user_might_like(user_id, data):
    #first we use a dictionary to store user interactions
    user_pages = {}
    for user in data['users']:
        user_pages[user['id']] = set(user['liked_pages'])
    #If the user is not found
    if user_id not in user_pages:
        return []

    user_liked_pages = user_pages[user_id]
    page_suggestions = {}
    for other_user, pages in user_pages.items():
        if other_user != user_id:
            shared_pages = user_liked_pages.intersection(pages)
        for page in pages:
            if page not in user_liked_pages:
                page_suggestions[page] = page_suggestions.get(page, 0) + len(shared_pages)

        sorted_pages = sorted(page_suggestions.items(), key = lambda x:x[1], reverse = True)

    return [page_id for page_id, _ in sorted_pages]

if __name__ == "__main__":
    data = load_data("data.json")
    cleaned_data = clean_data(data)
    
    # Test User ID
    test_user_id = 1
    
    print(f"People user {test_user_id} may know:")
    print(people_user_may_know(test_user_id, cleaned_data))
    
    print("\nPages user might like:")
    print(pages_user_might_like(test_user_id, cleaned_data))