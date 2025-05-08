import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Customer Preferences Dashboard",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Display Logo on All Pages
st.sidebar.image("pic1.jpeg", width=200)  # Adjust the path as needed
# Load Data with Caching
@st.cache_data
def load_data():
    data = pd.read_csv("customer_data.csv")
    # Standardize column names
    data.columns = data.columns.str.strip().str.replace(' +', ' ', regex=True).str.title()
    return data

data = load_data()

# Sidebar for Navigation
st.sidebar.title("Dashboard Navigation")
options = [
    "Overview",
    "Customer Demographics",
    "Meal Preferences",
    "Delivery Concerns",
    "Ratings and Reviews",
    "Age Distribution",
    "Order Value vs Delivery Rating",
    "Meal Category vs Order Value",
    "Health Concern Impact",
    "Delivery Time Analysis",
    "Family Size vs No. of Orders",
    "Influence of Rating",
    "Occupation Analysis",
    "Delivery Time vs Rating",
    "Marital Status and Preferences"
]
selection = st.sidebar.radio("Choose an option:", options)

# Title
st.title("🍔 Customer Preferences Dashboard")
st.markdown("Analyze customer behavior, meal preferences, delivery feedback, and more.")

# Dashboard Sections
if selection == "Overview":
    st.header("🕰️ Dataset Overview")
    st.write("A quick summary of the dataset.")

    total_customers = data.shape[0]
    total_orders = data['No. Of Orders Placed'].sum()
    avg_order_value = data['Order Value'].mean()
    avg_delivery_rating = data['Delivery Rating'].mean()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("👥 Total Customers", total_customers)
    col2.metric("📦 Total Orders", total_orders)
    col3.metric("💰 Avg Order Value", f"${avg_order_value:.2f}")
    col4.metric("⭐ Avg Delivery Rating", f"{avg_delivery_rating:.2f}/5")

    st.subheader("Dataset Sample")
    st.write(data.head())

elif selection == "Customer Demographics":
    st.header("👥 Customer Demographics")
    gender_dist = data['Gender'].value_counts()
    marital_status_dist = data['Marital Status'].value_counts()

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Gender Distribution")
        fig = px.pie(
            names=gender_dist.index,
            values=gender_dist.values,
            title="Gender Distribution",
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        st.plotly_chart(fig)
    with col2:
        st.subheader("Marital Status Distribution")
        fig = px.sunburst(
            data, 
            path=['Marital Status'], 
            values='No. Of Orders Placed',
            title="Marital Status Distribution",
            color='No. Of Orders Placed',
            color_continuous_scale='Viridis'
        )
        st.plotly_chart(fig)

elif selection == "Meal Preferences":
    st.header("🍲 Frequently Ordered Meals")
    meal_categories = data['Frequently Ordered Meal Category'].value_counts()
    preferred_medium = data['Frequently Used Medium'].value_counts()

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Meal Categories")
        grouped_data = data.groupby('Frequently Ordered Meal Category')['Order Value'].sum().reset_index()
        fig = px.treemap(
            grouped_data,
            path=['Frequently Ordered Meal Category'],
            values='Order Value',
            title="Popular Meal Categories",
            color='Order Value',
            color_continuous_scale='Blues'
        )
        st.plotly_chart(fig)
    with col2:
        st.subheader("Ordering Mediums")
        fig = px.funnel(
            preferred_medium,
            y=preferred_medium.index,
            x=preferred_medium.values,
            title="Popular Ordering Mediums",
            color_discrete_sequence=px.colors.cyclical.IceFire
        )
        st.plotly_chart(fig)

elif selection == "Delivery Concerns":
    st.header("🚚 Delivery Concerns")

    concern_columns = ['Health Concern', 'Late Delivery', 'Poor Hygiene', 'Bad Past Experience']
    concern_mapping = {
        "Yes": 1,
        "No": 0,
        "Neutral": 0,
        "Strongly agree": 2,
        "Agree": 1,
        "Disagree": -1,
        "Strongly disagree": -2
    }
    data[concern_columns] = data[concern_columns].replace(concern_mapping).fillna(0).astype(int)

    concerns = data[concern_columns].sum()

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(pd.DataFrame(concerns).T, annot=True, fmt="d", cmap="YlGnBu", ax=ax)
    ax.set_title("Delivery Concerns Heatmap")
    st.pyplot(fig)

elif selection == "Ratings and Reviews":
    st.header("⭐ Ratings and Reviews")
    delivery_ratings = data['Delivery Rating'].value_counts()
    restaurant_ratings = data['Restaurnat Rating'].value_counts()

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Delivery Ratings")
        fig = px.line(
            delivery_ratings, 
            x=delivery_ratings.index, 
            y=delivery_ratings.values,
            title="Delivery Ratings Distribution",
            markers=True,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig)
    with col2:
        st.subheader("Restaurant Ratings")
        fig = px.area(
            restaurant_ratings,
            x=restaurant_ratings.index, 
            y=restaurant_ratings.values,
            title="Restaurant Ratings Distribution",
            color_discrete_sequence=px.colors.qualitative.G10
        )
        st.plotly_chart(fig)

elif selection == "Age Distribution":
    st.header("👶 Age Distribution")
    fig = px.box(
        data, 
        x="Age", 
        color="Gender",
        title="Age Distribution by Gender",
        color_discrete_sequence=px.colors.qualitative.Dark24
    )
    st.plotly_chart(fig)

elif selection == "Order Value vs Delivery Rating":
    st.header("💰 Order Value vs Delivery Rating")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(
        pd.crosstab(data['Delivery Rating'], data['Order Value'], normalize='index'),
        cmap="coolwarm",
        annot=False
    )
    ax.set_title("Heatmap of Order Value by Delivery Rating")
    st.pyplot(fig)

elif selection == "Meal Category vs Order Value":
    st.header("🍽️ Meal Category vs Order Value")
    fig = px.violin(
        data, 
        x="Frequently Ordered Meal Category", 
        y="Order Value", 
        title="Meal Category vs Order Value",
        box=True,
        color="Frequently Ordered Meal Category",
        color_discrete_sequence=px.colors.sequential.Plasma
    )
    st.plotly_chart(fig)

elif selection == "Health Concern Impact":
    st.header("🏥 Health Concern Impact")
    health_impact = data.groupby('Health Concern')['Order Value'].mean()
    fig = px.bar(
        health_impact,
        x=health_impact.index, 
        y=health_impact.values,
        title="Impact of Health Concern on Order Value",
        labels={'x': 'Health Concern', 'y': 'Average Order Value'},
        color=health_impact.index,
        color_continuous_scale="Inferno"
    )
    st.plotly_chart(fig)

elif selection == "Delivery Time Analysis":
    st.header("⏰ Delivery Time Analysis")
    delivery_time_dist = data['Delivery Time'].value_counts()
    fig = px.line(
        delivery_time_dist,
        x=delivery_time_dist.index,
        y=delivery_time_dist.values,
        title="Delivery Time Frequency",
        markers=True,
        color_discrete_sequence=['#00CC96']
    )
    st.plotly_chart(fig)

elif selection == "Family Size vs No. of Orders":
    st.header("👪 Family Size vs No. of Orders")
    fig = px.density_heatmap(
        data,
        x="Family Size",
        y="No. Of Orders Placed",
        title="Family Size vs No. of Orders",
        color_continuous_scale="Cividis"
    )
    st.plotly_chart(fig)

elif selection == "Influence of Rating":
    st.header("⭐ Influence of Ratings")
    ratings_data = data.groupby('Restaurnat Rating')[['No. Of Orders Placed', 'Delivery Rating']].mean().reset_index()
    fig = px.line(
        ratings_data,
        x="Restaurnat Rating",
        y=["No. Of Orders Placed", "Delivery Rating"],
        title="Influence of Ratings on Orders and Delivery",
        labels={"value": "Average Value", "variable": "Metric"},
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig)

elif selection == "Occupation Analysis":
    st.header("💼 Occupation Analysis")
    occupation_dist = data['Occupation'].value_counts()
    fig = px.pie(
        occupation_dist, 
        names=occupation_dist.index, 
        values=occupation_dist.values,
        title="Occupation Distribution",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig)

elif selection == "Delivery Time vs Rating":
    st.header("🚚 Delivery Time vs Rating")
    fig = px.strip(
        data,
        x="Delivery Time",
        y="Delivery Rating",
        color="Gender",
        title="Delivery Time vs Delivery Rating",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig)

elif selection == "Marital Status and Preferences":
    st.header("💍 Marital Status and Meal Preferences")
    marital_status_pref = pd.crosstab(data['Marital Status'], data['Frequently Ordered Meal Category'])
    fig = sns.heatmap(
        marital_status_pref,
        cmap="coolwarm",
        annot=True,
        fmt="d"
    )
    plt.title("Meal Preferences by Marital Status")
    st.pyplot(fig.figure)

# Footer
st.markdown(
    """
    ---
    🚀 **Customer Preferences Dashboard** | Made By Ayesha Khan
    """
)
