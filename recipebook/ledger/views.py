from django.shortcuts import render

# Create your views here.

def recipe_list(request): 
	return render(request, "recipe_list.html") 

def recipe_1(request): 
	
    ctx = {
		"recipe_name": "Pork Sinigang",
		"ingredients": [
			["tomato", "3 pcs"],
			["onion", "1 pc"],
			["pork", "1 kg"],
			["water", "1L"],
			["sinigang mix", "1 packet"]
        ],
		"link": "/recipe/1"
    }

    return render(request, "recipe_1.html", ctx)   

def recipe_2(request): 

    ctx = {
		"recipe_name": "Pork Adobo",
		"ingredients": [
			["garlic", "1 head"],
			["onion", "1 pc"],
			["vinegar", "1/2 cup"],
			["water", "1 cup"],
            ["salt", "1 tablespoon"],
            ["whole black peppers", "1 tablespoon"],
			["pork", "1 kilo"]
        ],
		"link": "/recipe/2"
    }

    return render(request, "recipe_2.html", ctx)
