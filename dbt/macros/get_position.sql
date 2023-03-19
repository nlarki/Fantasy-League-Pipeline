 {#
    This macro returns the position of a player dependant on the value of element type 
#}

{% macro get_position(element_type) -%}

    case {{ element_type }}
        when 1 then 'GoalKeeper'
        when 2 then 'Defender'
        when 3 then 'Midfield'
        when 4 then 'Forward'
    end

{%- endmacro %}