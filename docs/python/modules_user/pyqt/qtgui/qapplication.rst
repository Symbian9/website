.. py:module:: QtGui

QApplication - приложение, с которого начинается построение интерфейса
======================================================================


.. py:class:: QApplication(*args)

    ::

        import sys

        from PyQt4.QtGui import QApplication, QWidget

        application = QApplication(sys.argv)
        
        w = QWidget()
        w.show()
        
        sys.exit(application.exec_())


    .. py:method:: argv()

        возвращает список переданных аргументов


    .. py:staticmethod:: focusWidget()

        Возвращает ссылку на компонент, находящийся в фокусе ввода.

        
    .. py:staticmethod:: desktop()

        Возвращает объект :py:class:`QtGui.QDesktopWidget`, компонент рабочего стола.