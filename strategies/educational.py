import pandas as pd
import plotly.graph_objects as go

# Challenge Completion Rates
def challenge_completion_rates(data):
    challenge_data = data[data['event_type'] == 'challenge']
    completion_data = challenge_data.groupby('progression_01').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=completion_data['progression_01'],
        y=completion_data['count'],
        text=completion_data['count'],
        textposition='auto',
        marker_color='rgb(99, 110, 250)'
    ))

    fig.update_layout(
        title="Challenge Completion Rates",
        xaxis_title="Challenge ID",
        yaxis_title="Number of Completions",
        template='plotly_white'
    )
    explanation = (
        "Identify challenges or lessons with high completion rates to design future content effectively. "
        "For instance, if a math challenge has high engagement, replicate its structure for other topics."
    )
    recommendation = "Simplify or enhance frequently failed challenges to make them more engaging."
    return fig, explanation, recommendation

# Session Patterns by Age Group
def session_patterns_by_age_group(data):
    age_group_data = data.groupby(['age_group', 'session_id']).size().reset_index(name='count')
    age_group_counts = age_group_data.groupby('age_group')['count'].sum().reset_index()

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=age_group_counts['age_group'],
        y=age_group_counts['count'],
        text=age_group_counts['count'],
        textposition='auto',
        marker_color='rgb(0, 204, 150)'
    ))

    fig.update_layout(
        title="Session Patterns by Age Group",
        xaxis_title="Age Group",
        yaxis_title="Number of Sessions",
        template='plotly_white'
    )
    explanation = (
        "Analyze how different demographics engage with the content to design age-appropriate features. "
        "For instance, younger users might prefer interactive elements, while older users may focus on detailed lessons."
    )
    recommendation = "Design content to align with the preferences of each age group for higher engagement."
    return fig, explanation, recommendation

# Topic Popularity
def topic_popularity(data):
    topic_data = data[data['event_type'] == 'topic']
    topic_counts = topic_data.groupby('progression_02').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=topic_counts['progression_02'],
        y=topic_counts['count'],
        text=topic_counts['count'],
        textposition='auto',
        marker_color='rgb(255, 127, 80)'
    ))

    fig.update_layout(
        title="Topic Popularity",
        xaxis_title="Topic ID",
        yaxis_title="Number of Interactions",
        template='plotly_white'
    )
    explanation = (
        "Identify the most revisited topics to prioritize future updates. "
        "For example, history topics with high engagement could be expanded with quizzes or interactive timelines."
    )
    recommendation = "Add depth to popular topics to maintain user interest."
    return fig, explanation, recommendation

# Retention Strategy
def retention_strategy(data):
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
        "Analyze session length categories to understand user retention patterns. "
        "For example, short sessions may indicate casual play habits, while long sessions suggest deeper engagement."
    )
    recommendation = "Develop competitive challenges and incentives to motivate retention."
    return fig, explanation, recommendation


def vertical_funcs():
    return {
        "Challenge Completion Rates": challenge_completion_rates,
        "Session Patterns by Age Group": session_patterns_by_age_group,
        "Topic Popularity": topic_popularity,
        "Retention Strategy": retention_strategy
    }
