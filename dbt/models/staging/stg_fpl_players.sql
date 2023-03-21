{{ config(materialized='table') }}

select 
    cast(first_name as string) as first_name,
    cast(second_name as string) as second_name,
    cast(goals_scored as integer) as goals_scored,
    cast(assists as integer) as assists,
    cast(total_points as integer) as total_points,
    cast(minutes as integer) as minutes,
    cast(goals_conceded as integer) as goals_conceded,
    cast(creativity as decimal) as creativity,
    cast(influence as decimal) as influence,
    cast(threat as decimal) as threat,
    cast(bonus as decimal) as bonus,
    cast(bps as integer) as bps,
    cast(ict_index as decimal) as ict_index,
    cast(clean_sheets as integer) as clean_sheets,
    cast(red_cards as integer) as red_cards,
    cast(yellow_cards as integer) as yellow_cards,
    cast(selected_by_percent as decimal) as selected_by_percent,
    cast(cost as decimal) as cost,
    cast(element_type as integer) as element_type,
    {{ get_position('element_type') }} as player_position,
    cast(Season as string) as Season,
    cast(team as string) as team


from {{ source('staging', 'players_all') }}
