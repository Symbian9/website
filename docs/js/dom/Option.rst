Option - HTML option
====================


.. py:class:: Option([text, value, defaultSelect, selected])

    Наследник :py:class:`Element`

    .. code-block:: js

        var o = Option(text, value, defaultSelected, selected);


    .. py:attribute:: defaultSelected
        
        Со­от­вет­ст­ву­ет HTML-ат­ри­бу­ту selected. Оп­ре­де­ля­ет на­чаль­ное зна­че­ние со­стоя­ния вы­бо­ра дан­но­го ва­ри­ан­та, а  так­же зна­че­ние, ко­то­рое бу­дет ис­поль­зо­вать­ся при сбро­се фор­мы в ис­ход­ное со­стоя­ние.


    .. py:attribute:: disabled
        
        Зна­че­ние true оз­на­ча­ет, что дан­ный эле­мент <option> не­дос­ту­пен. Ва­ри­ан­ты вы­бо­ра ста­но­вят­ся не­дос­туп­ны­ми, ес­ли они или вме­щаю­щие их эле­мен­ты <optgroup> име­ют HTML-ат­ри­бут disabled.


    .. py:attribute:: form
        
        Эле­мент <form>, ес­ли име­ет­ся, со­дер­жа­щий дан­ный эле­мент Option.


    .. py:attribute:: index
        
        Ин­декс дан­но­го эле­мен­та Option в  со­дер­жа­щем его эле­мен­те Select.


    .. py:attribute:: label
        
        Зна­че­ние HTML-ат­ри­бу­та label, ес­ли оп­ре­де­лен, ина­че – зна­че­ние свой­ст­ва text­Content (см. Node) дан­но­го эле­мен­та Option.


    .. py:attribute:: selected
        
        Име­ет зна­че­ние true, ес­ли дан­ный ва­ри­ант вы­бо­ра вы­бран в на­стоя­щее вре­мя, или false – в про­тив­ном слу­чае.


    .. py:attribute:: text
        
        Зна­че­ние свой­ст­ва textContent (см. Node) дан­но­го эле­мен­та Option, из ко­то­ро­го уда­ле­ны на­чаль­ные и  за­вер­шаю­щие про­бель­ные сим­во­лы, а  ка­ж­дые два или бо­лее смеж­ных про­бе­лов за­ме­не­ны од­ним сим­во­лом про­бе­ла.


    .. py:attribute:: value
        
        Зна­че­ние HTML-ат­ри­бу­та value, ес­ли оп­ре­де­лен, ина­че – зна­че­ние свой­ст­ва text­Content.