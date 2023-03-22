{{ config(materialized='table') }}


with players as (
    select * from {{ ref('stg_fpl_players')}}
),

teams as (
    select * from {{ ref('aligned_teams')}}
)

select * from players
left join teams on teams.id = players.team_code