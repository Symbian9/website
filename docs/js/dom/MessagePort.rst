MessagePort - передает асинхронные сообщения
========================================================

.. py:class:: MessagePort()

    Наследник :py:class:`EventTarget`

    .. py:attribute:: onmessage
        
        Это свой­ст­во оп­ре­де­ля­ет об­ра­бот­чик со­бы­тий «message». Со­бы­тия «message» ге­не­ри­ру­ют­ся в объ­ек­те MessagePort. Они не всплы­ва­ют, и для них не пре­ду­смат­ри­ва­ет­ся дей­ст­вий по умол­ча­нию. Об­ра­ти­те вни­ма­ние, что при ус­та­нов­ке это­го свой­ст­ва вы­зы­ва­ет­ся ме­тод start(), ко­то­рый за­пус­ка­ет ме­ха­низм воз­бу­ж­де­ния со­бы­тий «messa­ge».


    .. py:function:: close()
        
        От­клю­ча­ет дан­ный объ­ект MessagePort от пор­та, к ко­то­ро­му он был под­клю­чен (ес­ли та­ко­вой име­ет­ся). По­сле­дую­щие вы­зо­вы ме­то­да postMessage() не бу­дут иметь ни­ка­ко­го эф­фек­та, и в бу­ду­щем со­об­ще­ния «message» при­хо­дить не бу­дут.


    .. py:function:: postMessage(any message, [MessagePort[] ports])
        
        От­прав­ля­ет ко­пию со­об­ще­ния message че­рез порт и пе­ре­да­ет его в фор­ме со­бы­тия «message» пор­ту, с ко­то­рым со­единeн дан­ный порт. Ес­ли ука­зан ар­гу­мент ports, его зна­че­ние так­же бу­дет дос­тав­ле­но вме­сте с со­бы­ти­ем «message». Ар­гу­мент message мо­жет иметь лю­бое зна­че­ние, со­вмес­ти­мое с ал­го­рит­мом струк­ту­ри­ро­ван­но­го ко­ пи­ро­ва­ния.


    .. py:function:: start()
        
        За­пус­ка­ет ме­ха­низм воз­бу­ж­де­ния со­бы­тий «message» в  объ­ек­те MessagePort. До вы­зо­ва это­го ме­то­да все дан­ные, от­прав­ляе­мые че­рез порт, бу­дут со­хра­нять­ся в бу­фе­ре. По­доб­ная за­держ­ка со­бы­тий по­зво­ля­ет сце­на­ри­ям за­ре­ги­ст­ри­ро­вать все об­ра­бот­чи­ки со­бы­тий до то­го, как бу­дет от­прав­ле­но хоть од­но со­об­ще­ние. Имей­те, од­на­ко, в ви­ду, что вы­зы­вать этот ме­тод не­об­хо­ди­мо толь­ко при ис­поль­зо­ва­нии ме­то­да addEventListener() ин­тер­фей­са EventTarget. Ес­ли сце­на­рий ре­ги­ст­ри­ру­ет об­ра­бот­чик по­сред­ст­вом свой­ст­ва onmessage, ме­тод start() бу­дет вы­зван не­яв­но.