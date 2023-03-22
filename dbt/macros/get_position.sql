 {#
    This macro returns the position of a player dependant on the value of element type 
#}

{% macro get_position(element_type) -%}

    case {{ element_type }}
        when 1 then 'GK'
        when 2 then 'DEF'
        when 3 then 'MID'
        when 4 then 'FWD'
    end

{%- endmacro %}