from . import models, database, google_api, yelp_api
import math

def get_place_info(place_name):
    res_json = google_api.find_place_requests(place_name)
    info = google_api.parse_find_place_requests(res_json)
    info = info[0]
    new_place = models.Place(
        place_id=info[0], name=info[1], address=info[2], 
        latitude=info[3], longitude=info[4])
    return new_place

def get_all_restaurants(place):
    restaurants = []
    for query in google_api.FOOD_STYLES:
        info_part = get_nearby_restaurants(place, query, food_style=True)
        restaurants.extend(info_part)
    for query in google_api.FOOD_TYPES:
        info = get_nearby_restaurants(place, query, food_type=True)
        restaurants.extend(info)
    return restaurants

def get_nearby_restaurants(place, query, food_style = False, food_type = False, lower_bound = 5):
    place_id = place.name
    lat = place.latitude
    long = place.longitude
    restaurants = []
    res_json = google_api.text_search_requests(lat, long, query)
    info_list = google_api.parse_text_search_requests(res_json, place_id, query, food_style, food_type)
    for info in info_list:
        new_restaurant = models.Restaurant(
            place_id=info[0], name=info[1], address=info[2], latitude=info[3], 
            longitude=info[4], price_level=info[5], rating=info[6], num_ratings=info[7], 
            query_place_id=info[8], food_style=info[9], food_type=info[10])
        restaurants.append(new_restaurant)
    return restaurants

def get_formatted_restaurants(place, restaurants, style_or_type, k=5):
    place_id = place.name
    if style_or_type == "style":
        st_list = [[] for x in range(len(google_api.FOOD_STYLES))]
    elif style_or_type == "type":
        st_list = [[] for x in range(len(google_api.FOOD_TYPES))]
    avg_rating = [0 for x in range(len(st_list))]
    avg_num_ratings = [0 for x in range(len(st_list))]

    for r in restaurants:
        if style_or_type == "style" and r.food_style != "null":
            pos = google_api.FOOD_STYLES.index(r.food_style)
            st_list[pos].append(r)
            avg_rating[pos] += r.rating
            avg_num_ratings[pos] += r.num_ratings
        elif style_or_type == "type" and r.food_type != "null":
            pos = google_api.FOOD_TYPES.index(r.food_type)
            st_list[pos].append(r)
            avg_rating[pos] += r.rating
            avg_num_ratings[pos] += r.num_ratings
    
    if style_or_type == "style":        
        sorted_list = [[
            st_list[x][0].food_style,
            avg_rating[x]/len(st_list[x]),
            avg_num_ratings[x]/len(st_list[x]),
            len(st_list[x])] for x in range(len(st_list)) if st_list[x] != []]
    elif style_or_type == "type":        
        sorted_list = [[
            st_list[x][0].food_type,
            avg_rating[x]/len(st_list[x]),
            avg_num_ratings[x]/len(st_list[x]),
            len(st_list[x])] for x in range(len(st_list)) if st_list[x] != []]

    return sorted_list

def get_top_k_restaurant_types(sorted_list):
    sorted_list.sort(key = lambda x: x[1])
    sorted_list.reverse()
    final_list = [models.RestaurantType(
        type=sorted_list[x][0], avg_rating='{:.2f}'.format(sorted_list[x][1]), 
        avg_num_ratings='{:.2f}'.format(sorted_list[x][2]), number=sorted_list[x][3]
        ) for x in range(5)]

    return final_list

def get_top_k_restaurants(place, restaurants, type, k=10):
    type_list = []
    for r in restaurants:
        if r.food_style == type or r.food_type == type:
            type_list.append(r)
    type_list.sort(key = lambda x: x.rating)
    type_list.reverse()
    final_list = [type_list[x] for x in range(5)]
    return final_list

def get_google_details(place_id):
    res_json = google_api.place_details_requests(place_id)
    info = google_api.parse_place_details_requests(res_json, place_id)
    info = info[0]
    gmap_detail = models.GMapDetail(
        place_id = info[0], name = info[1],
        phone = info[2], address = info[3], hours = info[4],
        price_level = None, rating = None,
        num_ratings = None,
        r1_name = info[5], r1_score = info[6], r1_text = info[7],
        r2_name = info[8], r2_score = info[9], r2_text = info[10],
        r3_name = info[11], r3_score = info[12], r3_text = info[13],
    )
    return gmap_detail

def get_yelp_details(phone):
    info = yelp_api.yelp_restaurant_search(phone)
    info = info[0]
    yelp_detail = models.YelpDetail(
        place_id = info[0], name = info[1],
        phone = info[2], url = info[3],
        price_level = info[4], rating = info[5],
        num_ratings = info[6],
        r1_name = info[7], r1_score = info[8], r1_text = info[9],
        r2_name = info[10], r2_score = info[11], r2_text = info[12],
        r3_name = info[13], r3_score = info[14], r3_text = info[15],
    )
    return yelp_detail