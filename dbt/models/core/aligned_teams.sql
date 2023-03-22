{{ config(materialized='table') }}

select 
    id,
    team
from {{ ref("teams") }}