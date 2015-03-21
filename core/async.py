#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    tkRAD - tkinter Rapid Application Development library

    (c) 2013+ Raphaël SEBAN <motus@laposte.net>

    This program is free software: you can redistribute it and/or
    modify it under the terms of the GNU General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
    General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.

    If not, see: http://www.gnu.org/licenses/
"""

# ========================= STANDALONE MODULE ==========================


# lib imports
import weakref
import tkinter as TK


# private module member
__async = None


def get_async_manager ():
    """
        retrieves app-wide unique instance;
    """
    global __async
    if not isinstance(__async, AsyncTask):
        __async = AsyncTask()
    # end if
    return __async
# end def


class AsyncTask:
    """
        Asynchronous task for Tkinter GUI environment;
    """

    # locker states
    STATE_LOCKED = 1
    STATE_ATOMIC = 2


    def __init__ (self):
        """
            class constructor
        """
        # thread-ids dictionary inits
        self.tid = weakref.WeakKeyDictionary()
        # atomic lockers inits
        self.lockers = weakref.WeakKeyDictionary()
        # tkinter default root object
        self.root = TK._default_root
    # end def


    def _atomic (self, callback, *args):
        """
            ensures each callback runs in atomic mode (neither
            interrupted nor called several times);
        """
        # allowed to proceed?
        if not self.lockers.get(callback):
            # set atomic mode
            self.lockers[callback] = self.STATE_ATOMIC
            # run callback (may modify lockers)
            callback(*args)
            # locker is still in atomic mode after callback?
            if self.lockers.get(callback) == self.STATE_ATOMIC:
                # release atomic mode (and callback reference)
                self.lockers.pop(callback, None)
            # end if
        # end if
    # end def


    def clear_all (self, *args, **kw):
        """
            event handler;
            stops all pending threads and releases all registered
            lockers;
            clears up all dictionaries;
        """
        # these will clear up all dictionaries
        self.stop_all(*args, **kw)
        self.release_all(*args, **kw)
    # end def


    def lock (self, *callbacks):
        """
            stops and then locks scheduled threads, if any;
        """
        # browse list of callbacks
        for _cb in callbacks:
            # stop thread
            self.stop(_cb)
            # lock future thread calls
            self.lockers[_cb] = self.STATE_LOCKED
        # end for
    # end def


    def lock_all (self):
        """
            locks all registered callbacks;
        """
        self.lock(*self.tid.keys())
    # end def


    def release (self, *callbacks):
        """
            releases listed threads lockers, if any;
            this also frees any memory reference to @callbacks;
        """
        # browse list of callbacks
        for _cb in callbacks:
            # stop thread
            self.stop(_cb)
            # release locker (and callback reference)
            # for future thread calls
            self.lockers.pop(_cb, None)
        # end for
    # end def


    def release_all (self, *args, **kw):
        """
            event handler;
            releases all lockers;
        """
        # simply clear all dictionary
        self.lockers.clear()
    # end def


    def run_after (self, delay, callback, *args):
        """
            runs a delayed thread;
            parameter @delay is in milliseconds;
        """
        # param inits
        delay = max(1, int(delay))
        # stop previous running thread, if any
        self.stop(callback)
        # schedule new thread id for further call
        self.tid[callback] = self.root.after(
            delay, self._atomic, callback, *args
        )
    # end def


    def run_after_idle (self, callback, *args):
        """
            runs a delayed thread after mainloop enters in idle mode
            i.e. when all events are done;
        """
        # stop previous running thread, if any
        self.stop(callback)
        # schedule new thread id for further call
        self.tid[callback] = self.root.after_idle(
            self._atomic, callback, *args
        )
    # end def


    def stop (self, *callbacks):
        """
            stops scheduled threads, if any;
        """
        # browse list of callbacks
        for _cb in callbacks:
            # stop thread
            self.root.after_cancel(self.tid.get(_cb) or 0)
            # remove thread id (and callback reference)
            self.tid.pop(_cb, None)
        # end for
    # end def


    def stop_all (self, *args, **kw):
        """
            event handler;
            stops all scheduled threads;
            clears up all thread ids dictionary;
        """
        # loop on all thread ids
        for _tid in self.tid.values():
            # stop scheduled thread
            self.root.after_cancel(_tid)
        # end for
        # clear dict
        self.tid.clear()
    # end def

# end class AsyncTask
