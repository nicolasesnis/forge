import pandas as pd
import plotly.graph_objects as go

# 1. Storyline Drop-offs
def storyline_dropoffs(data):
    narrative_data = data[data['event_type'] == 'progression']
    dropoff_data = narrative_data.groupby('progression_02').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=dropoff_data['progression_02'],
        y=dropoff_data['count'],
        text=dropoff_data['count'],
        textposition='auto',
        marker_color='rgb(99, 110, 250)'
    ))

    fig.update_layout(
        title="Storyline Drop-offs",
        xaxis_title="Narrative Stage",
        yaxis_title="Number of Drop-offs",
        template='plotly_white'
    )
    explanation = (
        "This chart shows where players are dropping off in the narrative. "
        "It helps identify stages or levels that need balancing or enhanced storytelling elements."
    )
    recommendation = "Focus on reworking or enhancing narrative elements at stages with significant drop-offs."
    return fig, explanation, recommendation

# 2. Resource Usage Analysis
def resource_usage(data):
    resource_data = data[data['event_type'] == 'resource']
    usage_data = resource_data.groupby('currency').agg({'amount': 'sum'}).reset_index()

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=usage_data['currency'],
        y=usage_data['amount'],
        text=usage_data['amount'],
        textposition='auto',
        marker_color='rgb(0, 204, 150)'
    ))

    fig.update_layout(
        title="Resource Usage Trends",
        xaxis_title="Resource Type",
        yaxis_title="Total Amount Used",
        template='plotly_white'
    )
    explanation = (
        "This chart highlights which in-game resources are being used the most by players. "
        "It provides insights into resource balancing and opportunities for creating rewarding systems."
    )
    recommendation = "Introduce quests or events rewarding highly consumed resources to maintain player satisfaction."
    return fig, explanation, recommendation

# 3. Retention Strategy
def retention_strategy(data):
    # Group sessions and calculate the number of events per session
    session_data = data.groupby('session_id').size().reset_index(name='events_per_session')
    
    # Categorize sessions based on the number of events
    session_data['category'] = session_data['events_per_session'].apply(
        lambda x: 'Short' if x < 5 else 'Long' if x > 15 else 'Medium'
    )
    
    # Count the occurrences of each category
    category_counts = session_data['category'].value_counts().reset_index()
    category_counts.columns = ['category', 'count']  # Rename columns for clarity

    # Create the Pie chart
    fig = go.Figure()
    fig.add_trace(go.Pie(
        labels=category_counts['category'],  # Use the renamed column 'category'
        values=category_counts['count'],    # Use the renamed column 'count'
        hole=0.4,
        textinfo='percent+label'
    ))

    fig.update_layout(
        title="Retention Strategy Insights",
        template='plotly_white'
    )

    explanation = (
        "Categorize player sessions by length to identify trends in engagement. "
        "Short sessions might indicate casual play habits, while long ones could lead to potential burnout. "
        "Tailor rewards for medium-length sessions and provide soft nudges for breaks during extended play to enhance overall retention."
    )
    recommendation = (
        "Introduce rewards for medium-length sessions to sustain player engagement. "
        "For longer sessions, implement optional breaks or incentives for session continuity."
    )
    
    return fig, explanation, recommendation



# Vertical Functions
def vertical_funcs():
    return {
        "Storyline Drop-offs": storyline_dropoffs,
        "Resource Usage": resource_usage,
        "Retention Strategy": retention_strategy
    }
