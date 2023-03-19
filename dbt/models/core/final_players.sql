{{ config(materialized='table') }}

select * from {{ ref('stg_fpl_players')}}