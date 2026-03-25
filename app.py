from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Cities with coordinates
cities = {
    "Delhi": (28.7041, 77.1025),
    "Mumbai": (19.0760, 72.8777),
    "Chennai": (13.0827, 80.2707),
    "Kolkata": (22.5726, 88.3639),
    "Hyderabad": (17.3850, 78.4867),
    "Bangalore": (12.9716, 77.5946)
}

# Distance calculation
def distance(c1, c2):
    lat1, lon1 = cities[c1]
    lat2, lon2 = cities[c2]

    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    return round(R * c, 2)

# AI recommendation
def recommend_transport(dist, urgency, weight, within_city):
    if within_city == "yes":
        return "Bike 🏍", "Best for local delivery"

    if urgency == "high":
        return "Flight ✈️", "Fastest option"

    if dist > 1200:
        return "Flight ✈️", "Long distance"

    if weight > 1000:
        return "Train 🚆", "Best for heavy goods"

    return "Truck 🚚", "Cost-effective option"

# Cost calculation
def calculate_options(dist, weight):
    return {
        "Bike 🏍": round(dist * 2 + weight * 0.2, 2),
        "Truck 🚚": round(dist * 5 + weight * 0.5, 2),
        "Train 🚆": round(dist * 3 + weight * 0.4, 2),
        "Flight ✈️": round(dist * 10 + weight * 0.8, 2)
    }

# Home page
@app.route('/')
def index():
    return render_template("index.html", cities=cities.keys())

# Process multiple deliveries
@app.route('/choose', methods=['POST'])
def choose():
    start = request.form['start']

    orders = []

    # Loop through dynamic inputs (max 3 deliveries)
    for i in range(3):
        product = request.form.get(f'product{i}')
        city = request.form.get(f'city{i}')
        weight = request.form.get(f'weight{i}')
        priority = request.form.get(f'priority{i}')

        if product and city and weight:
            weight = float(weight)
            city = city.title()

            if city in cities:
                dist = distance(start, city)

                # AI decision
                rec, reason = recommend_transport(dist, priority, weight, "no")

                options = calculate_options(dist, weight)

                orders.append({
                    "product": product,
                    "city": city,
                    "distance": dist,
                    "recommended": rec,
                    "reason": reason,
                    "options": options
                })

    return render_template("choose.html", orders=orders, start=start)

# Final selection + map
@app.route('/result', methods=['POST'])
def result():
    count = int(request.form.get('count', 0))

    selections = []
    total_cost = 0

    for i in range(count):
        data = request.form.get(f'transport{i}')
        city = request.form.get(f'city{i}')
        product = request.form.get(f'product{i}')

        # 🔥 SAFE CHECK
        if not data:
            continue

        transport, cost = data.split('|')
        cost = float(cost)

        total_cost += cost

        selections.append({
            "product": product,
            "city": city,
            "transport": transport,
            "cost": cost
        })

    # 🔥 IF NOTHING SELECTED
    if not selections:
        return "Error: No selections received"

    # Route for map
    route = ["Delhi"] + [s["city"] for s in selections]

    return render_template(
        "result.html",
        selections=selections,
        total_cost=round(total_cost, 2),
        route=route
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)