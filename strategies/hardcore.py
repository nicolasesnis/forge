import pandas as pd
import plotly.graph_objects as go

# Skill vs Progression Analysis
def skill_vs_progression_analysis(data):
    skill_data = data.groupby('progression_01').agg({'score': 'mean'}).reset_index()

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=skill_data['progression_01'],
        y=skill_data['score'],
        text=skill_data['score'].round(2),
        textposition='auto',
        marker_color='rgb(255, 127, 80)'
    ))

    fig.update_layout(
        title="Skill vs Progression Analysis",
        xaxis_title="Progression Stage",
        yaxis_title="Average Score",
        template='plotly_white'
    )
    explanation = (
        "Assess the correlation between user progression (e.g., levels completed) and scores to identify users struggling to advance. "
        "For instance, lower scores in early levels might indicate poorly explained mechanics or a steep learning curve."
    )
    recommendation = "Provide targeted support in stages where average scores are low, such as additional tutorials or power-ups."
    return fig, explanation, recommendation

# Social Dynamics
def social_dynamics(data):
    social_data = data[data['event_type'] == 'guild_interaction']
    participation = social_data.groupby('session_id').size().reset_index(name='interactions')

    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=participation['interactions'],
        nbinsx=20,
        marker_color='rgb(60, 179, 113)'
    ))

    fig.update_layout(
        title="Social Dynamics: Interaction Distribution",
        xaxis_title="Number of Interactions per Session",
        yaxis_title="Frequency",
        template='plotly_white'
    )
    explanation = (
        "Analyze multiplayer or guild participation to identify players who are not engaging with social features. "
        "For instance, users with zero interactions may need incentives to join guilds or participate in cooperative play."
    )
    recommendation = "Encourage social interaction through exclusive rewards or guild-specific challenges."
    return fig, explanation, recommendation

# Transaction Analysis
def transaction_analysis(data):
    transaction_data = data[data['event_type'] == 'business']
    transaction_counts = transaction_data.groupby('item_type').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=transaction_counts['item_type'],
        y=transaction_counts['count'],
        text=transaction_counts['count'],
        textposition='auto',
        marker_color='rgb(255, 215, 0)'
    ))

    fig.update_layout(
        title="Transaction Analysis",
        xaxis_title="Item Type",
        yaxis_title="Number of Transactions",
        template='plotly_white'
    )
    explanation = (
        "Analyze the popularity of different in-game purchases, such as consumables vs non-consumables. "
        "For instance, a high frequency of consumable purchases might suggest opportunities for bundling or discounts."
    )
    recommendation = "Optimize in-game store offerings based on the most popular item types."
    return fig, explanation, recommendation

# Retention Strategy
def retention_strategy(data):
    session_data = data.groupby('session_id').agg({'session_length': 'sum'}).reset_index()
    session_data['category'] = session_data['session_length'].apply(
        lambda x: 'Short' if x < 300 else 'Long' if x > 1200 else 'Medium'
    )
    category_counts = session_data['category'].value_counts().reset_index()
    category_counts.columns = ['category', 'count']

    fig = go.Figure()
    fig.add_trace(go.Pie(
        labels=category_counts['category'],
        values=category_counts['count'],
        hole=0.4,
        textinfo='percent+label'
    ))

    fig.update_layout(
        title="Retention Strategy: Session Length Distribution",
        template='plotly_white'
    )
    explanation = (
        "Analyze session lengths to identify engagement trends. Short sessions may indicate casual play habits, "
        "while long sessions could suggest deeper engagement or potential burnout risks."
    )
    recommendation = "Introduce cooldown mechanics or breaks during extended sessions to improve retention."
    return fig, explanation, recommendation


def vertical_funcs():
    return {
        "Skill vs Progression Analysis": skill_vs_progression_analysis,
        "Social Dynamics": social_dynamics,
        "Transaction Analysis": transaction_analysis,
        "Retention Strategy": retention_strategy
    }
