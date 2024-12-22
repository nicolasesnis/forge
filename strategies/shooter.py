import pandas as pd
import plotly.graph_objects as go

# Kill-to-Death Ratios
def kill_to_death_ratios(data):
    if 'kills' not in data.columns or 'deaths' not in data.columns:
        raise KeyError("Columns 'kills' and 'deaths' are missing. Ensure the dataset includes these columns.")

    performance_data = data[data['event_type'] == 'combat']
    kd_data = performance_data.groupby('user_id').agg({'kills': 'sum', 'deaths': 'sum'}).reset_index()
    kd_data['kd_ratio'] = kd_data['kills'] / (kd_data['deaths'] + 1)  # Avoid division by zero

    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=kd_data['kd_ratio'],
        nbinsx=20,
        marker_color='rgb(99, 110, 250)'
    ))

    fig.update_layout(
        title="Kill-to-Death Ratios",
        xaxis_title="K/D Ratio",
        yaxis_title="Frequency",
        template='plotly_white'
    )
    explanation = "Study player performance metrics to spot patterns in frustrating mechanics."
    recommendation = "Provide tutorials or balancing adjustments for players with significantly low K/D ratios."
    return fig, explanation, recommendation

# Weapon Usage Analysis
def weapon_usage_analysis(data):
    weapon_data = data[data['event_type'] == 'combat']
    weapon_counts = weapon_data.groupby('weapon_id').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=weapon_counts['weapon_id'],
        y=weapon_counts['count'],
        text=weapon_counts['count'],
        textposition='auto',
        marker_color='rgb(0, 204, 150)'
    ))

    fig.update_layout(
        title="Weapon Usage Analysis",
        xaxis_title="Weapon ID",
        yaxis_title="Usage Count",
        template='plotly_white'
    )
    explanation = "Identify frequently used weapons to create new gameplay challenges or weapon upgrades."
    recommendation = "Introduce upgrades or challenges for the most popular weapons to keep players engaged."
    return fig, explanation, recommendation

# Map Engagement
def map_engagement(data):
    map_data = data[data['event_type'] == 'progression']
    map_counts = map_data.groupby('map_id').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=map_counts['map_id'],
        y=map_counts['count'],
        text=map_counts['count'],
        textposition='auto',
        marker_color='rgb(255, 127, 80)'
    ))

    fig.update_layout(
        title="Map Engagement",
        xaxis_title="Map ID",
        yaxis_title="Number of Interactions",
        template='plotly_white'
    )
    explanation = "Determine which maps or game modes are most engaging and create variations."
    recommendation = "Expand or refine popular maps and game modes to maintain player interest."
    return fig, explanation, recommendation

# Retention Strategy
def retention_strategy(data):
    retention_data = data.groupby('session_id').size().reset_index(name='session_length')
    retention_data['category'] = retention_data['session_length'].apply(
        lambda x: 'Short' if x < 300 else 'Long' if x > 1200 else 'Medium'
    )
    category_counts = retention_data['category'].value_counts().reset_index()

    fig = go.Figure()
    fig.add_trace(go.Pie(
        labels=category_counts['index'],
        values=category_counts['category'],
        hole=0.4,
        textinfo='percent+label'
    ))

    fig.update_layout(
        title="Retention Strategy Insights",
        template='plotly_white'
    )
    explanation = "Offer periodic weapon unlocks or map expansions based on player preferences."
    recommendation = "Introduce timed challenges and unlocks tied to popular weapons or maps to boost retention."
    return fig, explanation, recommendation


def vertical_funcs():
    return {
        "Kill-to-Death Ratios": kill_to_death_ratios,
        "Weapon Usage Analysis": weapon_usage_analysis,
        "Map Engagement": map_engagement,
        "Retention Strategy": retention_strategy
    }
