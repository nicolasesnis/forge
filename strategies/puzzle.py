import pandas as pd
import plotly.graph_objects as go

# Level Completion Trends
def level_completion_trends(data):
    level_data = data[data['event_type'] == 'progression']
    completion_data = level_data.groupby('progression_02').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=completion_data['progression_02'],
        y=completion_data['count'],
        text=completion_data['count'],
        textposition='auto',
        marker_color='rgb(99, 110, 250)'
    ))

    fig.update_layout(
        title="Level Completion Trends",
        xaxis_title="Level",
        yaxis_title="Number of Completions",
        template='plotly_white'
    )
    explanation = (
        "Identify levels with unusually high fail rates and fine-tune difficulty. "
        "For example, high failure rates in 'level_3' might indicate overly complex mechanics."
    )
    recommendation = "Adjust level difficulty or provide additional hints for levels with high fail rates."
    return fig, explanation, recommendation

# Hint Usage
def hint_usage(data):
    hint_data = data[data['event_type'] == 'hint']
    hint_counts = hint_data.groupby('progression_02').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=hint_counts['progression_02'],
        y=hint_counts['count'],
        text=hint_counts['count'],
        textposition='auto',
        marker_color='rgb(0, 204, 150)'
    ))

    fig.update_layout(
        title="Hint Usage Trends",
        xaxis_title="Level",
        yaxis_title="Number of Hints Used",
        template='plotly_white'
    )
    explanation = (
        "Track how often hints are used and create a reward system for solving puzzles without hints. "
        "For instance, levels with excessive hint usage might need clearer instructions or design tweaks."
    )
    recommendation = "Encourage players to minimize hint usage by introducing rewards for hint-free completions."
    return fig, explanation, recommendation

# Session Gaps
def session_gaps(data):
    session_data = data.groupby('session_id').agg({'client_ts': ['min', 'max']}).reset_index()
    session_data.columns = ['session_id', 'min_ts', 'max_ts']  # Rename columns for clarity
    session_data['gap'] = session_data['max_ts'] - session_data['min_ts']
    session_data['gap_category'] = session_data['gap'].apply(
        lambda x: 'Short' if x < 300 else 'Long' if x > 1200 else 'Medium'
    )
    gap_counts = session_data['gap_category'].value_counts().reset_index()
    gap_counts.columns = ['category', 'count']  # Rename columns explicitly

    fig = go.Figure()
    fig.add_trace(go.Pie(
        labels=gap_counts['category'],  # Use the renamed column
        values=gap_counts['count'],  # Use the renamed column
        hole=0.4,
        textinfo='percent+label'
    ))

    fig.update_layout(
        title="Session Gaps",
        template='plotly_white'
    )
    explanation = (
        "This chart categorizes session gaps into short, medium, and long periods. "
        "It helps identify players who may be at risk of churning due to extended inactivity."
    )
    recommendation = (
        "Send re-engagement emails or notifications to players with long gaps. "
        "Provide incentives like skip tokens or hints to bring them back."
    )
    return fig, explanation, recommendation


# Retention Strategy
def retention_strategy(data):
    retention_data = data.groupby('session_id').agg({'session_length': 'sum'}).reset_index()
    retention_data['category'] = retention_data['session_length'].apply(
        lambda x: 'Short' if x < 300 else 'Long' if x > 1200 else 'Medium'
    )
    category_counts = retention_data['category'].value_counts().reset_index()
    category_counts.columns = ['category', 'count']

    fig = go.Figure()
    fig.add_trace(go.Pie(
        labels=category_counts['category'],
        values=category_counts['count'],
        hole=0.4,
        textinfo='percent+label'
    ))

    fig.update_layout(
        title="Retention Strategy Insights",
        template='plotly_white'
    )
    explanation = (
        "Implement streak-based rewards to motivate users to solve puzzles daily. "
        "For instance, increasing rewards for consecutive daily logins can enhance retention."
    )
    recommendation = "Design daily puzzle challenges with increasing rewards for maintaining streaks."
    return fig, explanation, recommendation


def vertical_funcs():
    return {
        "Level Completion Trends": level_completion_trends,
        "Hint Usage": hint_usage,
        "Session Gaps": session_gaps,
        "Retention Strategy": retention_strategy
    }
