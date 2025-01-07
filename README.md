
# Customer Preferences Dashboard 🍔

An interactive **Streamlit** dashboard that visualizes customer data to explore behavior, preferences, and delivery feedback. Key features include insights into customer demographics, meal preferences, delivery concerns, and more.

## Features

- **Overview**: Quick dataset summary and key metrics (Total Customers, Orders, Avg Order Value).
- **Customer Demographics**: Gender and marital status distribution.
- **Meal Preferences**: Popular meal categories and ordering mediums.
- **Delivery Concerns**: Heatmaps of delivery issues.
- **Ratings & Reviews**: Delivery and restaurant ratings distribution.
- **Age Distribution**: Age vs. gender analysis.
- **Order Value vs Rating**: Relationship between order value and delivery ratings.
- **Meal Category Impact**: Meal category vs. order value analysis.
- **Health Concerns**: Impact of health concerns on order values.
- **Delivery Time Analysis**: Delivery time distribution.
- **Family Size**: Family size vs. number of orders.
- **Occupation Analysis**: Occupation vs. preferences.
- **Delivery Time vs Rating**: Delivery time vs. rating visualization.

## Quick Start

1. **Clone the repo**:
   ```bash
   git clone https://github.com/yourusername/customer-preferences-dashboard.git
   cd customer-preferences-dashboard
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**:
   ```bash
   streamlit run app.py
   ```

5. **View the app** in your browser at the provided local URL.

## Requirements

- **streamlit**
- **pandas**
- **plotly**
- **seaborn**
- **matplotlib**

## Dataset

Ensure your `customer_data.csv` follows the required format with columns like `Gender`, `Marital Status`, `Order Value`, `Delivery Rating`, etc.
