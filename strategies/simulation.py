import pandas as pd
import plotly.graph_objects as go

# Build Completion Rates
def build_completion_rates(data):
    build_data = data[data['event_type'] == 'progression']
    build_counts = build_data.groupby('progression_02').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=build_counts['progression_02'],
        y=build_counts['count'],
        text=build_counts['count'],
        textposition='auto',
        marker_color='rgb(99, 110, 250)'
    ))

    fig.update_layout(
        title="Build Completion Rates",
        xaxis_title="Build Type",
        yaxis_title="Number of Completions",
        template='plotly_white'
    )
    explanation = "Analyze the average time to complete builds or upgrades and optimize pacing."
    recommendation = "Adjust build timers and offer boosts for frequently incomplete builds to improve engagement."
    return fig, explanation, recommendation

# Resource Consumption Trends
def resource_consumption_trends(data):
    resource_data = data[data['event_type'] == 'resource']
    resource_usage = resource_data.groupby('currency').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=resource_usage['currency'],
        y=resource_usage['count'],
        text=resource_usage['count'],
        textposition='auto',
        marker_color='rgb(0, 204, 150)'
    ))

    fig.update_layout(
        title="Resource Consumption Trends",
        xaxis_title="Resource Type",
        yaxis_title="Usage Count",
        template='plotly_white'
    )
    explanation = "Study which resources are used most frequently and ensure a balanced acquisition rate."
    recommendation = "Increase availability or rewards for high-demand resources to maintain player satisfaction."
    return fig, explanation, recommendation

# Session Diversity
def session_diversity(data):
    session_data = data.groupby('session_id').size().reset_index(name='session_length')
    session_data['category'] = session_data['session_length'].apply(
        lambda x: 'Short' if x < 300 else 'Long' if x > 1200 else 'Medium'
    )
    category_counts = session_data['category'].value_counts().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Pie(
        labels=category_counts['index'],
        values=category_counts['count'],
        hole=0.4,
        textinfo='percent+label'
    ))

    fig.update_layout(
        title="Session Diversity",
        template='plotly_white'
    )
    explanation = "Look at user behaviors to identify repetitive actions and add variety to gameplay loops."
    recommendation = "Introduce new gameplay elements or surprises to reduce repetition and enhance engagement."
    return fig, explanation, recommendation

# Retention Strategy
def retention_strategy(data):
    retention_data = data.groupby('session_id').size().reset_index(name='session_length')
    retention_data['category'] = retention_data['session_length'].apply(
        lambda x: 'Short' if x < 300 else 'Long' if x > 1200 else 'Medium'
    )
    category_counts = retention_data['category'].value_counts().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Pie(
        labels=category_counts['index'],
        values=category_counts['count'],
        hole=0.4,
        textinfo='percent+label'
    ))

    fig.update_layout(
        title="Retention Strategy Insights",
        template='plotly_white'
    )
    explanation = "Add time-limited scenarios or challenges that organically push players to explore different game mechanics."
    recommendation = "Create dynamic events or seasonal content to maintain player interest and retention."
    return fig, explanation, recommendation


def vertical_funcs():
    return {
        "Build Completion Rates": build_completion_rates,
        "Resource Consumption Trends": resource_consumption_trends,
        "Session Diversity": session_diversity,
        "Retention Strategy": retention_strategy
    }
