ProgressEvent - событие продолжения загрузки, выгрузки или чтения файла
=======================================================================

.. py:class:: ProgressEvent()

    Наследник :py:class:`Event`


    .. py:attribute:: lengthComputable
        
        Име­ет зна­че­ние true, ес­ли из­вест­но об­щее ко­ли­че­ст­во бай­тов, пред­на­зна­чен­ных для пе­ре­да­чи, и false – в про­тив­ном слу­чае. 


    .. py:attribute:: loaded
        
        Ко­ли­че­ст­во уже пе­ре­дан­ных бай­тов.


    .. py:attribute:: total
        
        Об­щее ко­ли­че­ст­во бай­тов, пред­на­зна­чен­ных для пе­ре­да­чи, ес­ли из­вест­но, и  0 – в  про­тив­ном слу­чае. Эту ин­фор­ма­цию мож­но по­лу­чить, на­при­мер, из свой­ст­ва size объ­ек­та Blob или из за­го­лов­ка Content-Length, воз­вра­щае­мо­го веб-сер­ве­ром.