import pandas as pd
import plotly.graph_objects as go

# Kill-to-Death Ratios
def kill_to_death_ratios(data):
    combat_data = data.dropna(subset=['kills', 'deaths'])
    kd_data = combat_data.groupby('user_id').agg({'kills': 'sum', 'deaths': 'sum'}).reset_index()
    kd_data['kd_ratio'] = kd_data['kills'] / (kd_data['deaths'] + 1)

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
    explanation = "This chart visualizes the Kill-to-Death (K/D) ratios of players. A low K/D ratio may indicate challenging mechanics or balance issues, especially for newer players."
    recommendation = "Consider tutorials or balancing adjustments to support players with low K/D ratios and encourage long-term engagement."
    return fig, explanation, recommendation

# Weapon Usage Analysis
def weapon_usage_analysis(data):
    combat_data = data.dropna(subset=['weapon_id'])
    weapon_counts = combat_data.groupby('weapon_id').size().reset_index(name='count')

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
        xaxis_title="Weapon",
        yaxis_title="Usage Count",
        template='plotly_white'
    )
    explanation = "This chart shows the frequency of usage for each weapon, identifying popular choices among players."
    recommendation = "Develop gameplay challenges or upgrades around the most frequently used weapons to sustain engagement."
    return fig, explanation, recommendation

# Map Engagement
def map_engagement(data):
    progression_data = data.dropna(subset=['map_id'])
    map_counts = progression_data.groupby('map_id').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=map_counts['map_id'],
        y=map_counts['count'],
        text=map_counts['count'],
        textposition='auto',
        marker_color='rgb(255, 127, 80)'
    ))

    fig.update_layout(
        title="Map Engagement Trends",
        xaxis_title="Map",
        yaxis_title="Number of Interactions",
        template='plotly_white'
    )
    explanation = "This chart identifies the most frequently played maps, which can help prioritize updates or new content."
    recommendation = "Expand or refine popular maps by adding objectives or variations to keep players engaged."
    return fig, explanation, recommendation

# Retention Strategy
def retention_strategy(data):
    retention_data = data.groupby('session_id').size().reset_index(name='session_length')
    retention_data['category'] = retention_data['session_length'].apply(
        lambda x: 'Short' if x < 300 else 'Long' if x > 1200 else 'Medium'
    )
    category_counts = retention_data['category'].value_counts().reset_index()
    category_counts.columns = ['category', 'count']  # Rename columns explicitly

    fig = go.Figure()
    fig.add_trace(go.Pie(
        labels=category_counts['category'],  # Use the renamed column
        values=category_counts['count'],  # Use the renamed column
        hole=0.4,
        textinfo='percent+label'
    ))

    fig.update_layout(
        title="Retention Strategy Insights",
        template='plotly_white'
    )
    explanation = "This chart segments session lengths into short, medium, and long categories to analyze player engagement."
    recommendation = "Offer retention incentives such as timed weapon unlocks or map-exclusive rewards to encourage returning players."
    return fig, explanation, recommendation


def vertical_funcs():
    return {
        "Kill-to-Death Ratios": kill_to_death_ratios,
        "Weapon Usage Analysis": weapon_usage_analysis,
        "Map Engagement": map_engagement,
        "Retention Strategy": retention_strategy
    }
