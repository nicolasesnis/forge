import pandas as pd
import plotly.graph_objects as go

# Quest Completion Rates
def quest_completion_rates(data):
    quest_data = data[data['event_type'] == 'progression']
    quest_completion = quest_data.groupby('progression_02').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=quest_completion['progression_02'],
        y=quest_completion['count'],
        text=quest_completion['count'],
        textposition='auto',
        marker_color='rgb(99, 110, 250)'
    ))

    fig.update_layout(
        title="Quest Completion Rates",
        xaxis_title="Quest Stage",
        yaxis_title="Number of Completions",
        template='plotly_white'
    )
    explanation = (
        "This chart highlights the completion rates of various quests or levels. "
        "Low completion rates indicate potential bottlenecks where players struggle or lose interest."
    )
    recommendation = (
        "Revise rewards for underperforming quests or add hints to improve player success rates. "
        "Monitor completion rates after adjustments to ensure player engagement."
    )
    return fig, explanation, recommendation

# Resource Balancing
def resource_balancing(data):
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
        title="Resource Usage Trends",
        xaxis_title="Resource Type",
        yaxis_title="Usage Count",
        template='plotly_white'
    )
    explanation = (
        "This visualization shows the frequency of resource usage, identifying the most "
        "depleted resources and imbalances in the game economy."
    )
    recommendation = (
        "Introduce challenges or quests to replenish highly consumed resources. Ensure resource "
        "availability aligns with gameplay requirements to maintain balance."
    )
    return fig, explanation, recommendation

# Progression Pathways
def progression_pathways(data):
    progression_data = data[data['event_type'] == 'progression']
    pathway_counts = progression_data.groupby('progression_01').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=pathway_counts['progression_01'],
        y=pathway_counts['count'],
        text=pathway_counts['count'],
        textposition='auto',
        marker_color='rgb(255, 127, 80)'
    ))

    fig.update_layout(
        title="Progression Pathways",
        xaxis_title="Progression Path",
        yaxis_title="Number of Players",
        template='plotly_white'
    )
    explanation = (
        "This chart compares player activity across different progression paths, highlighting "
        "player preferences for linear or open-world gameplay."
    )
    recommendation = (
        "Optimize content distribution across paths. For example, enhance popular paths with new "
        "challenges while making lesser-used paths more engaging."
    )
    return fig, explanation, recommendation

# Retention Strategy
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
    recommendation = "Expand the game world with side quests tied to lore and high-value rewards to keep players engaged."
    return fig, explanation, recommendation


def vertical_funcs():
    return {
        "Quest Completion Rates": quest_completion_rates,
        "Resource Balancing": resource_balancing,
        "Progression Pathways": progression_pathways,
        "Retention Strategy": retention_strategy
    }
