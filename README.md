# ShopFind — E-Commerce Product Search Engine

A responsive sample e-commerce product search app built with **Python Flask**, HTML, CSS, and JavaScript.

## Features
- Keyword search across product names, brands, categories, and descriptions
- Search suggestions / autocomplete
- Category and brand filters
- Minimum and maximum price filters (INR)
- Minimum customer rating filter
- Sorting by relevance, price, rating, and name
- Responsive product grid and no-results state
- Sample catalog with 12 products
- JSON endpoints for products and suggestions

## Requirements
- Python 3.9 or newer
- Internet connection for Google Fonts and remote sample product images (optional; app logic works without them)

## Setup

### Windows
1. Extract the ZIP file.
2. Open Command Prompt or PowerShell inside the extracted `ecommerce_product_search_engine` folder.
3. Create a virtual environment:
   ```bash
   py -m venv .venv
   .venv\\Scripts\\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the app:
   ```bash
   python app.py
   ```
6. Open `http://127.0.0.1:5000` in your browser.

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Then open `http://127.0.0.1:5000`.

## API endpoints
- `GET /api/products?q=headphones&category=Electronics&sort=price_asc`
- `GET /api/suggestions?q=hea`

Supported product query parameters:
`q`, `category`, `brand`, `min_price`, `max_price`, `min_rating`, `sort`.

## Project structure
```text
ecommerce_product_search_engine/
├── app.py
├── products.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── app.js
    └── style.css
```

## Notes
- This is a learning/demo project. The catalog is stored in `products.py` rather than a database.
- Search uses simple all-terms matching and a basic relevance score. It is not a production search engine.
- Product detail buttons show a basic detail popup; there is no cart, checkout, login, or payment integration.
- For a production version, consider adding a database, pagination, typo-tolerant search (e.g. Elasticsearch), authentication, and tests.
