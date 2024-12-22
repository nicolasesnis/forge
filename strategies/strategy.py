import pandas as pd
import plotly.graph_objects as go

# Battle Success Rates
def battle_success_rates(data):
    battle_data = data[data['event_type'] == 'progression']
    success_data = battle_data.groupby('progression_02').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=success_data['progression_02'],
        y=success_data['count'],
        text=success_data['count'],
        textposition='auto',
        marker_color='rgb(99, 110, 250)'
    ))

    fig.update_layout(
        title="Battle Success Rates",
        xaxis_title="Battle Stage",
        yaxis_title="Number of Successes",
        template='plotly_white'
    )
    explanation = "Analyze the win/loss ratio across levels to identify overly difficult battles."
    recommendation = "Adjust difficulty or provide additional tools for stages with disproportionately low success rates."
    return fig, explanation, recommendation

# Resource Scarcity Impact
def resource_scarcity_impact(data):
    resource_data = data[data['event_type'] == 'resource']
    scarcity_data = resource_data.groupby('currency').size().reset_index(name='count')

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=scarcity_data['currency'],
        y=scarcity_data['count'],
        text=scarcity_data['count'],
        textposition='auto',
        marker_color='rgb(0, 204, 150)'
    ))

    fig.update_layout(
        title="Resource Scarcity Impact",
        xaxis_title="Resource Type",
        yaxis_title="Usage Count",
        template='plotly_white'
    )
    explanation = "Study the impact of resource scarcity on user drop-offs."
    recommendation = "Provide alternative acquisition methods for scarce resources to reduce drop-offs."
    return fig, explanation, recommendation

# Group Play Dynamics
def group_play_dynamics(data):
    session_counts = data.groupby('session_id').size().reset_index(name='group_activity')

    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=session_counts['group_activity'],
        nbinsx=20,
        marker_color='rgb(255, 127, 80)'
    ))

    fig.update_layout(
        title="Group Play Dynamics",
        xaxis_title="Number of Group Activities per Session",
        yaxis_title="Frequency",
        template='plotly_white'
    )
    explanation = "Examine participation in alliances or group missions to encourage cooperative strategies."
    recommendation = "Introduce rewards for group participation and highlight cooperative gameplay opportunities."
    return fig, explanation, recommendation

# Retention Strategy
def retention_strategy(data):
    retention_data = data.groupby('session_id').size().reset_index(name='session_length')
    retention_data['category'] = retention_data['session_length'].apply(
        lambda x: 'Short' if x < 300 else 'Long' if x > 1200 else 'Medium'
    )
    category_counts = retention_data['category'].value_counts().reset_index()

    fig = go.Figure()
    fig.add_trace(go.Pie(
        labels=category_counts['index'],
        values=category_counts['category'],
        hole=0.4,
        textinfo='percent+label'
    ))

    fig.update_layout(
        title="Retention Strategy Insights",
        template='plotly_white'
    )
    explanation = "Introduce team-based rewards or collaborative missions to encourage sustained engagement."
    recommendation = "Develop cooperative missions with compelling rewards to promote teamwork and engagement."
    return fig, explanation, recommendation

def vertical_funcs():
    return {
        "Battle Success Rates": battle_success_rates,
        "Resource Scarcity Impact": resource_scarcity_impact,
        "Group Play Dynamics": group_play_dynamics,
        "Retention Strategy": retention_strategy
    }
