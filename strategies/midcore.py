import pandas as pd
import plotly.graph_objects as go

# Progression Bottlenecks
def progression_bottlenecks(data):
    bottleneck_data = data.groupby('progression_01').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=bottleneck_data['progression_01'],
        y=bottleneck_data['count'],
        text=bottleneck_data['count'],
        textposition='auto',
        marker_color='rgb(99, 110, 250)'
    ))

    fig.update_layout(
        title="Progression Bottlenecks",
        xaxis_title="Progression Stage",
        yaxis_title="Number of Users",
        template='plotly_white'
    )
    explanation = (
        "Analyze levels or stages with high drop-off rates to adjust difficulty or provide in-game tips. "
        "For instance, high drop-offs at 'world_2' might indicate a steep difficulty curve."
    )
    recommendation = "Provide power-ups or reduce difficulty in challenging progression stages to retain players."
    return fig, explanation, recommendation

# User Segmentation
def user_segmentation(data):
    segmentation_data = data.groupby('user_id').agg({'session_id': 'count', 'amount': 'sum'}).reset_index()
    segmentation_data['activity_level'] = segmentation_data['session_id'].apply(
        lambda x: 'High' if x > 10 else 'Medium' if x > 5 else 'Low'
    )
    activity_counts = segmentation_data['activity_level'].value_counts().reset_index()

    fig = go.Figure()
    fig.add_trace(go.Pie(
        labels=activity_counts['index'],
        values=activity_counts['activity_level'],
        hole=0.4,
        textinfo='percent+label'
    ))

    fig.update_layout(
        title="User Segmentation by Activity Level",
        template='plotly_white'
    )
    explanation = (
        "Group users by their session frequency and spending habits to target less active or non-spending players. "
        "For example, dormant players with low spending might benefit from exclusive login rewards."
    )
    recommendation = "Offer personalized rewards to low-activity users to re-engage them."
    return fig, explanation, recommendation

# Transaction Trends
def transaction_trends(data):
    transaction_data = data.groupby('item_type').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=transaction_data['item_type'],
        y=transaction_data['count'],
        text=transaction_data['count'],
        textposition='auto',
        marker_color='rgb(0, 204, 150)'
    ))

    fig.update_layout(
        title="Transaction Trends",
        xaxis_title="Item Type",
        yaxis_title="Number of Transactions",
        template='plotly_white'
    )
    explanation = (
        "Analyze the popularity of consumable and non-consumable purchases. "
        "For example, a high volume of consumable sales might suggest opportunities for bundling or discounts."
    )
    recommendation = "Introduce limited-time offers for popular item types to boost sales."
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
        "Analyze session lengths to identify engagement trends. Short sessions might indicate casual play habits, "
        "while long sessions could suggest fatigue or engagement issues."
    )
    recommendation = "Introduce events or rewards targeting medium-length sessions to enhance retention."
    return fig, explanation, recommendation


def vertical_funcs():
    return {
        "Progression Bottlenecks": progression_bottlenecks,
        "User Segmentation": user_segmentation,
        "Transaction Trends": transaction_trends,
        "Retention Strategy": retention_strategy
    }
