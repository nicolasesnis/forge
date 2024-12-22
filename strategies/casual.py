import pandas as pd
import plotly.graph_objects as go

# Session Timing Patterns
def session_timing_patterns(data):
    # Calculate average playtime per session
    timing_data = data.groupby('session_id').agg({'client_ts': 'mean'}).reset_index()
    timing_data['hour'] = pd.to_datetime(timing_data['client_ts'], unit='s').dt.hour
    hourly_counts = timing_data['hour'].value_counts().sort_index().reset_index()
    hourly_counts.columns = ['hour', 'count']

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=hourly_counts['hour'],
        y=hourly_counts['count'],
        text=hourly_counts['count'],
        textposition='auto',
        marker_color='rgb(99, 110, 250)'
    ))

    fig.update_layout(
        title="Session Timing Patterns",
        xaxis_title="Hour of Day",
        yaxis_title="Number of Sessions",
        template='plotly_white'
    )
    explanation = (
        "Analyze peak playtimes to schedule in-game events or reminders that align with user activity. "
        "For example, most users might play between 6 PM and 9 PM, indicating an optimal time for push notifications."
    )
    recommendation = "Schedule in-game events during peak play hours to maximize engagement."
    return fig, explanation, recommendation

# Ad Interaction Behavior
def ad_interaction_behavior(data):
    ad_data = data[data['event_type'] == 'ad']
    interaction_data = ad_data.groupby('ad_placement').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=interaction_data['ad_placement'],
        y=interaction_data['count'],
        text=interaction_data['count'],
        textposition='auto',
        marker_color='rgb(0, 204, 150)'
    ))

    fig.update_layout(
        title="Ad Interaction Behavior",
        xaxis_title="Ad Placement",
        yaxis_title="Number of Interactions",
        template='plotly_white'
    )
    explanation = (
        "Study which ad placements (e.g., pre_game, post_game) drive higher engagement and fewer drop-offs. "
        "For instance, ads shown after level completions might perform better since users are less engaged in gameplay."
    )
    recommendation = "Optimize ad placements to minimize interruptions and maximize engagement."
    return fig, explanation, recommendation

# Resource Usage
def resource_usage(data):
    resource_data = data[data['event_type'] == 'resource']
    resource_counts = resource_data.groupby('currency').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=resource_counts['currency'],
        y=resource_counts['count'],
        text=resource_counts['count'],
        textposition='auto',
        marker_color='rgb(255, 127, 80)'
    ))

    fig.update_layout(
        title="Resource Usage Trends",
        xaxis_title="Resource Type",
        yaxis_title="Usage Count",
        template='plotly_white'
    )
    explanation = (
        "This chart shows the most frequently consumed resources, like coins or gems, allowing for balanced game design. "
        "For instance, heavily used resources can be tied to daily rewards or special events."
    )
    recommendation = "Introduce challenges or events that reward commonly consumed resources to maintain engagement."
    return fig, explanation, recommendation

# Retention Strategy
def retention_strategy(data):
    # Calculate session lengths using session start and end timestamps
    session_times = data.pivot_table(index='session_id', columns='event_type', values='client_ts', aggfunc='first')
    session_times['session_length'] = session_times['session_end'] - session_times['session_start']
    session_times['category'] = session_times['session_length'].apply(
        lambda x: 'Short' if x < 300 else 'Long' if x > 1200 else 'Medium'
    )
    category_counts = session_times['category'].value_counts().reset_index()
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
        "Categorize player sessions by length to identify trends in engagement. "
        "Short sessions indicate casual play, while long sessions may suggest deeper engagement or potential burnout."
    )
    recommendation = (
        "Encourage medium-length sessions through targeted incentives and provide soft nudges for breaks during long sessions."
    )
    return fig, explanation, recommendation


def vertical_funcs():
    return {
        "Session Timing Patterns": session_timing_patterns,
        "Ad Interaction Behavior": ad_interaction_behavior,
        "Resource Usage": resource_usage,
        "Retention Strategy": retention_strategy
    }
