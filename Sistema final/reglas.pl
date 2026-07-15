/* ================================================================
   SISTEMA EXPERTO: DIAGNOSTICO DE ENFERMEDADES DEL CHILE JALAPENO
   Enfoque: Logica de Primer Orden (Variables y Predicados)
   ================================================================ */

:- dynamic confirmado/1, descartado/1.

% --------------------------------------------------------------
% 1. BLOQUE PRINCIPAL
% --------------------------------------------------------------
iniciar :-
    borrar_memoria,
    nl, write('--- SISTEMA EXPERTO: FITOPATOLOGIA DE CHILE JALAPENO ---'), nl,
    write('Responda con "si." o "no." e incluya el punto final.'), nl, nl,

    (   enfermedad(planta_actual, Diagnostico) ->
        nl, write('>>> CONCLUSION: La planta tiene: '), write(Diagnostico), nl
    ;   
        nl, write('>>> RESULTADO: No se pudo determinar la enfermedad.'), nl
    ).

% --------------------------------------------------------------
% 2. BASE DE CONOCIMIENTOS
% --------------------------------------------------------------

% R1 - Tizon Tardio
enfermedad(Chile, 'Tizon Tardio') :-
    tiene(Chile, manchas_negras_hojas),
    tiene(Chile, tallo_con_manchas).

enfermedad(Chile, 'Tizon Tardio') :-
    tiene(Chile, punta_muerta_hoja).

% R2 - Mancha Bacteriana
enfermedad(Chile, 'Mancha Bacteriana') :-
    tiene(Chile, manchas_acuosas_hojas),
    tiene(Chile, perdida_severa_hojas).

% R3 - Mosaico Viral
enfermedad(Chile, 'Mosaico Viral') :-
    tiene(Chile, deformacion_hoja),
    tiene(Chile, patron_mosaico_amarillo).

% --------------------------------------------------------------
% 3. MOTOR DE INFERENCIA
% --------------------------------------------------------------

tiene(_, Sintoma) :-
    (   confirmado(Sintoma) -> true
    ;   descartado(Sintoma) -> fail
    ;   preguntar(Sintoma)
    ).

preguntar(Sintoma) :-
    format('¿La planta tiene ~w? (si./no.): ', [Sintoma]),
    read(Respuesta),
    (   Respuesta == si ->
        assert(confirmado(Sintoma))
    ;   
        assert(descartado(Sintoma)), fail
    ).

borrar_memoria :-
    retractall(confirmado(_)),
    retractall(descartado(_)).
