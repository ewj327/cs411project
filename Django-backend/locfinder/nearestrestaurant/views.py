from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from . import utils, google_api

selected_place = None
all_restaurants = None
selected_restaurants = None

def index(request):
    global selected_place
    if request.method == "POST" :
        place_name = request.POST.get("place")
        place = utils.get_place_info(place_name)
        selected_place = place
        return redirect('place', placename = place.name)
    else:
        return render(request, 'nearestrestaurant/index.html')

def place(request, placename):
    global selected_place, all_restaurants
    if request.method == "POST" :
        query = request.POST.get("query")
        return redirect('rst_type', typename = query)
    restaurants = utils.get_all_restaurants(selected_place)
    all_restaurants = restaurants
    formatted_styles = utils.get_formatted_restaurants(selected_place, restaurants, "style")
    top_k_styles = utils.get_top_k_restaurant_types(formatted_styles)
    formatted_types = utils.get_formatted_restaurants(selected_place, restaurants, "type")
    top_k_types = utils.get_top_k_restaurant_types(formatted_types)
    rst_cls = ["Type" , "Average Rating", "Average Number of Ratings", "# of Restaurants"]
    return render(request, 'nearestrestaurant/place.html', 
    { 'place' : placename, 'restaurant_class' : rst_cls,
    'food_styles' : top_k_styles, 'food_types' : top_k_types })


def rst_type(request, typename):
    global selected_place, all_restaurants, selected_restaurants
    if selected_place == None:
        return redirect('index')
    top_k_restaurants = utils.get_top_k_restaurants(selected_place, all_restaurants, typename)
    selected_restaurants = top_k_restaurants
    rst_cls = ["Name", "Rating", "Number of Ratings", "Price Level", "Address"]
    return render(request, 'nearestrestaurant/restaurant_type.html', 
        {'restaurant_type' : typename, 'restaurant_class' : rst_cls,
        'restaurants' : top_k_restaurants})

def restaurant(request, restname):
    global selected_place, selected_restaurants
    if selected_place == None:
        return redirect('index')
    else:
        for r in selected_restaurants:
            if restname == r.name:
                place_id = r.place_id
                break
        gmapdetail = utils.get_google_details(place_id)
        gmapdetail.rating = r.rating
        gmapdetail.num_ratings = r.num_ratings
        gmapdetail.price_level = r.price_level
        yelpdetail = utils.get_yelp_details(gmapdetail.phone)
        processed_hours = gmapdetail.hours.split(';')

    return render(request, 'nearestrestaurant/restaurant.html',
    {'restaurant_name' : restname, 
    'restaurant_gmap_detail' : gmapdetail,
    'restaurant_yelp_detail' : yelpdetail,
    'processed_hours' : processed_hours,}
    )
    