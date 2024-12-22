import pandas as pd 
import plotly.graph_objects as go

# 1. Ad Viewing Drop-offs
def analyze_ad_viewing_dropoffs(data):
    ad_data = data[data['event_type'] == 'ad']
    dropoff_data = ad_data.groupby(['ad_placement', 'ad_action']).size().reset_index(name='count')
    
    fig = go.Figure()
    for action in dropoff_data['ad_action'].unique():
        action_data = dropoff_data[dropoff_data['ad_action'] == action]
        fig.add_trace(go.Bar(
            x=action_data['ad_placement'],
            y=action_data['count'],
            name=action,
            text=action_data['count'],
            textposition='auto'
        ))

    fig.update_layout(
        title="Ad Viewing Drop-offs by Placement and Action",
        xaxis_title="Ad Placement",
        yaxis_title="Number of Events",
        barmode='group',
        template='plotly_white',
        legend_title="Ad Action"
    )
    explanation = "This chart shows the number of ad interactions (viewed or clicked) across different ad placements. It highlights where users are most and least engaged with ads."
    recommendation = "If ads drop off significantly at certain placements, consider repositioning or reducing ad frequency at those placements to improve user experience."
    return fig, explanation, recommendation

# 2. Session Length Patterns
def analyze_session_length_patterns(data):
    session_end_data = data[data['event_type'] == 'session_end']
    session_end_data['length_category'] = session_end_data['session_length'].apply(
        lambda x: 'Short' if x < 300 else 'Long' if x > 1200 else 'Medium'
    )
    length_patterns = session_end_data.groupby('length_category').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Pie(
        labels=length_patterns['length_category'],
        values=length_patterns['count'],
        hole=0.4,
        textinfo='percent+label'
    ))

    fig.update_layout(
        title="Session Length Distribution",
        template='plotly_white'
    )
    explanation = "This chart displays the distribution of session lengths categorized as Short, Medium, or Long. It provides insights into user engagement duration."
    recommendation = "For short sessions, consider introducing quick and engaging content. For long sessions, monitor for potential burnout and add optional breaks or rewards."
    return fig, explanation, recommendation

# 3. Content Popularity
def analyze_content_popularity(data):
    progression_data = data[data['event_type'] == 'progression']
    content_popularity = progression_data.groupby('ad_placement').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=content_popularity['ad_placement'],
        y=content_popularity['count'],
        text=content_popularity['count'],
        textposition='auto',
        marker_color='rgb(99, 110, 250)'
    ))

    fig.update_layout(
        title="Content Popularity by Placement",
        xaxis_title="Placement",
        yaxis_title="Number of Events",
        template='plotly_white'
    )
    explanation = "This chart shows the frequency of user interactions with different content placements, indicating which areas are most popular."
    recommendation = "Focus on enhancing and expanding content in the most popular placements to drive further engagement."
    return fig, explanation, recommendation

# 4. Retention Strategy Insights
def retention_strategy_insights(data):
    ad_data = data[data['event_type'] == 'ad']
    most_popular_ad = ad_data['ad_placement'].value_counts().idxmax()

    fig = go.Figure()
    fig.add_trace(go.Indicator(
        mode="number+delta",
        value=ad_data['ad_placement'].value_counts().max(),
        title={"text": f"Most Popular Ad Placement: {most_popular_ad}"},
        delta={"reference": ad_data['ad_placement'].value_counts().mean()},
    ))

    fig.update_layout(
        title="Retention Strategy Insights",
        template='plotly_white'
    )
    explanation = f"This chart identifies the most popular ad placement, {most_popular_ad}, and provides the highest interaction count compared to the average across all placements."
    recommendation = "Leverage the most popular ad placement for critical in-game promotions or high-value ad campaigns to maximize engagement."
    return fig, explanation, recommendation

def vertical_funcs():
    return {"Ad Viewing Drop-offs": analyze_ad_viewing_dropoffs,
            "Session Length Patterns": analyze_session_length_patterns, 
            "Content Popularity": analyze_content_popularity,
            "Retention Strategy": retention_strategy_insights}
    