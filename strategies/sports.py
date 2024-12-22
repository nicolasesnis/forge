import pandas as pd
import plotly.graph_objects as go

# Match Participation Trends
def match_participation_trends(data):
    if "match_phase" not in data.columns:
        raise KeyError("Column 'match_phase' is missing. Ensure the dataset includes this column.")

    match_data = data[data['event_type'] == 'progression']
    dropoff_data = match_data.groupby('match_phase').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=dropoff_data['match_phase'],
        y=dropoff_data['count'],
        text=dropoff_data['count'],
        textposition='auto',
        marker_color='rgb(99, 110, 250)'
    ))

    fig.update_layout(
        title="Match Participation Trends",
        xaxis_title="Match Phase",
        yaxis_title="Number of Users",
        template='plotly_white'
    )
    explanation = "Examine drop-off points in match sessions to identify frustrating mechanics or features."
    recommendation = "Refine pacing or rules at phases with significant drop-offs, such as overtime."
    return fig, explanation, recommendation

# In-game Tournaments
def in_game_tournaments(data):
    tournament_data = data[data['event_type'] == 'progression']
    tournament_counts = tournament_data.groupby('match_phase').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=tournament_counts['match_phase'],
        y=tournament_counts['count'],
        text=tournament_counts['count'],
        textposition='auto',
        marker_color='rgb(0, 204, 150)'
    ))

    fig.update_layout(
        title="In-game Tournament Participation",
        xaxis_title="Tournament Stage",
        yaxis_title="Number of Participants",
        template='plotly_white'
    )
    explanation = "Assess participation in events or leagues and correlate with player retention."
    recommendation = "Introduce better rewards or accessibility options to increase tournament participation."
    return fig, explanation, recommendation

# Customization Usage
def customization_usage(data):
    customization_data = data[data['event_type'] == 'customization']
    customization_counts = customization_data.groupby('customization_type').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=customization_counts['customization_type'],
        y=customization_counts['count'],
        text=customization_counts['count'],
        textposition='auto',
        marker_color='rgb(0, 204, 150)'
    ))

    fig.update_layout(
        title="Customization Usage",
        xaxis_title="Customization Type",
        yaxis_title="Number of Selections",
        template='plotly_white'
    )
    explanation = (
        "This chart tracks how often players use various customization features, such as avatars, teams, or jerseys. "
        "Frequent usage indicates strong interest in certain customization types."
    )
    recommendation = (
        "Focus on expanding popular customization options and introducing themed variations to maintain engagement. "
        "For example, add seasonal or event-specific customization items."
    )
    return fig, explanation, recommendation

# Retention Strategy
def retention_strategy(data):
    retention_data = data.groupby('session_id').size().reset_index(name='session_length')
    retention_data['category'] = retention_data['session_length'].apply(
        lambda x: 'Short' if x < 300 else 'Long' if x > 1200 else 'Medium'
    )
    category_counts = retention_data['category'].value_counts().reset_index()
    category_counts.columns = ['category', 'count']  # Rename columns for clarity

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
    explanation = "Introduce regular tournaments with leaderboards and low entry barriers to foster competition."
    recommendation = "Develop more accessible tournaments and highlight leaderboard rewards to keep players engaged."
    return fig, explanation, recommendation


def vertical_funcs():
    return {
        "Match Participation Trends": match_participation_trends,
        "In-game Tournaments": in_game_tournaments,
        "Customization Usage": customization_usage,
        "Retention Strategy": retention_strategy
    }
