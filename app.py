from flask import Flask, render_template, request, jsonify
from products import PRODUCTS

app = Flask(__name__)

def search_products(query="", category="", brand="", min_price=None, max_price=None,
                    min_rating=None, sort="relevance"):
    q = query.strip().lower()
    results = []
    for p in PRODUCTS:
        searchable = f"{p['name']} {p['brand']} {p['category']} {p['description']}".lower()
        if q and not all(term in searchable for term in q.split()):
            continue
        if category and p["category"] != category:
            continue
        if brand and p["brand"] != brand:
            continue
        if min_price is not None and p["price"] < min_price:
            continue
        if max_price is not None and p["price"] > max_price:
            continue
        if min_rating is not None and p["rating"] < min_rating:
            continue
        item = dict(p)
        # Simple relevance score: exact name matches rank ahead of broader matches.
        item["relevance"] = 2 if q and q in p["name"].lower() else (1 if q else 0)
        results.append(item)

    if sort == "price_asc":
        results.sort(key=lambda p: p["price"])
    elif sort == "price_desc":
        results.sort(key=lambda p: p["price"], reverse=True)
    elif sort == "rating":
        results.sort(key=lambda p: p["rating"], reverse=True)
    elif sort == "name":
        results.sort(key=lambda p: p["name"].lower())
    else:
        results.sort(key=lambda p: (p["relevance"], p["rating"]), reverse=True)
    return results

@app.route("/")
def index():
    categories = sorted({p["category"] for p in PRODUCTS})
    brands = sorted({p["brand"] for p in PRODUCTS})
    return render_template("index.html", categories=categories, brands=brands)

@app.route("/api/products")
def api_products():
    def number_arg(key):
        value = request.args.get(key, "").strip()
        if not value:
            return None
        try:
            return float(value)
        except ValueError:
            return None

    products = search_products(
        query=request.args.get("q", ""),
        category=request.args.get("category", ""),
        brand=request.args.get("brand", ""),
        min_price=number_arg("min_price"),
        max_price=number_arg("max_price"),
        min_rating=number_arg("min_rating"),
        sort=request.args.get("sort", "relevance")
    )
    return jsonify({"count": len(products), "products": products})

@app.route("/api/suggestions")
def suggestions():
    q = request.args.get("q", "").strip().lower()
    if len(q) < 2:
        return jsonify([])
    matches = []
    for p in PRODUCTS:
        if q in p["name"].lower() or q in p["brand"].lower():
            if p["name"] not in matches:
                matches.append(p["name"])
        if len(matches) >= 6:
            break
    return jsonify(matches)

if __name__ == "__main__":
    app.run(debug=True)
