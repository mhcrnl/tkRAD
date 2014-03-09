#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    tkRAD - tkinter Rapid Application Development library

    (c) 2013+ Raphaël SEBAN <motus@laposte.net>

    This program is free software: you can redistribute it and/or
    modify it under the terms of the GNU General Public License as
    published by the Free Software Foundation, either version 3 of
    the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
    General Public License for more details.

    You should have received a copy of the GNU General Public
    License along with this program.

    If not, see: http://www.gnu.org/licenses/
"""



# ========================= STANDALONE MODULE ==========================



# unique instance pointer

# module private var init

__queue = None



# service getter

def get_deferred_trigger_queue (*args, **kw):
    r"""
        gets a unique application-wide instance of the deferred
        trigger queue;

        always return the queue unique instance pointer;
    """

    global __queue

    if not isinstance(__queue, DeferredTriggerQueue):

        __queue = DeferredTriggerQueue(*args, **kw)

    # end if

    return __queue

# end def



# alias shortcut for get_deferred_trigger_queue()

get_dt_queue = get_deferred_trigger_queue



# class def

class DeferredTriggerQueue:
    r"""
        /!\ this module is *STANDALONE* /!\

        you can pick it up *as is* and use it in your own project;

        Generic Queue for deferred triggers;

    """



    def __init__ (self, *args, **kw):
        r"""
            class constructor inits;
        """

        # member inits

        self.__queue = dict(*args, **kw)

    # end def



    def clear (self, section = None):
        r"""
            clears all buffered triggers without calling them as in
            flush() or flush_all();

            if @section is set, clears only mentioned section;

            no return value (void);
        """

        # param controls

        if section:

            # clear only mentioned section

            self.__queue.pop(section, None)

        else:

            # clear all in queue

            self.__queue.clear()

        # end if

    # end def



    def defer (self, section, callback, *args, **kw):
        r"""
            registers a new callable @callback into @section with
            additional @args and @kw;

            no return value (void);
        """

        # get section buffer

        _buffer = self.__queue.setdefault(section, list())

        # register new callable into buffer

        _buffer.append(QueueItem(callback, *args, **kw))

        # update section data

        self.__queue[section] = _buffer

    # end def



    def get_queue (self):
        r"""
            returns deferred triggers queue (shallow copy);
        """

        # clear all in queue

        return self.__queue.copy()

    # end def




# end class DeferredTriggerQueue



# class subcomponent def

class QueueItem:
    r"""
        DeferredTriggerQueue subcomponent class def;

        Stores callback with its additional *args and **kw;
    """



    def __init__ (self, callback, *args, **kw):
        r"""
            class constructor inits;
        """

        self.callback = callback

        self.arguments = args

        self.keywords = kw

    # end def



    def call (self, *args, **kw):
        r"""
            calls callback with additional new *args and **kw, if
            callback is a callable object, otherwise does nothing;

            no return value (void);
        """

        # member controls

        if callable(self.callback):

            # update extra arguments

            _args = self.arguments.copy().extend(args)

            # update extra keywords

            _kw = self.keywords.copy()

            _kw.update(kw)

            # call callback with new arguments and keywords

            self.callback(*_args, **_kw)

        # end if

    # end def


# end class QueueItem
