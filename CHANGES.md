<!-- encoding: UTF-8 -->


## CONTRIBUTORS

| Initials | Contributor | GitHub membership | Cool project | Current role | Previous role |
|:--------:|:------------|:-----------------:|:------------:|:------------:|:-------------:|
| CW | Cyril Walle | **[GrosSacASac] (https://github.com/GrosSacASac)** | **[WebSpree] (https://github.com/GrosSacASac/WebSpree)** | **education counselor** | - |
| DA | Dale Athanasias | **[daleathan] (https://github.com/daleathan)** | **[widget-tour-py3] (https://github.com/daleathan/widget-tour-py3)** | **wiki contributor** | - |
| RS | Raphaël Seban | **[tarball69] (https://github.com/tarball69)** | **[tkRAD] (https://github.com/tarball69/tkRAD/wiki)** | **developer** | author |
|  | who's next? |  |  |  |  |


## CHANGELOG


### $ 2014-03-31 RS $

* tagged and released **tkRAD v1.5 - Sugar Extra**;

* in `builder.py`:

    * now it is possible to use `build(xml,
    layout_options=dict(side="left", padx=10, pady=5,...))`;


### $ 2014-03-18 RS $

* in `tkRAD.core.path`:

    * added new `shorten_path()`:

        * now fully implemented;

* thought of **tkRAD v1.5** new release name: maybe **Sugar Extra**?

* in `tkRAD/widgets/rad_dialog.py`:

    * added new class `RADButtonsDialog`:

        * now fully implemented;

    * in `RADDialog._slot_quit_dialog()`:

        * fixed bug: _response is `MB.YES` *NOT* `TK.YES`;

example:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkRAD

import tkRAD.widgets.rad_dialog as DLG

def show_dialog (tk_event=None, *args, **kw):

    parent = kw["tk_parent"].tk_parent

    _contents = """
        <tkwidget>
            <ttklabel
                text="Please, enter some cool text:"
                anchor="center"
                layout="pack"
                resizable="yes"
            />
            <ttkentry
                id="entry1"
                layout="pack"
                resizable="width"
            />
            <ttkscrollbar
                connect="entry1"
                orient="horizontal"
                layout="pack"
                resizable="width"
            />
        </tkwidget>
    """

    _dlg = DLG.RADButtonsDialog(parent, xml=_contents)

    _dlg.show()

# end def

mainwindow = tkRAD.RADXMLMainWindow()

mainwindow.show_dialog = show_dialog

xml = """
    <tkwidget>
        <label
            text="hello good people!"
            bg="yellow"
            fg="blue"
            font="sans 16 bold italic"
            layout="pack"
            resizable="yes"
        />
        <button
            text="Show dialog"
            command=".show_dialog"
            layout="pack"
        />
        <button
            text="Quit"
            command="@quit"
            layout="pack"
        />
    </tkwidget>
"""

mainwindow.xml_build(xml)

mainwindow.run()
```


### $ 2014-03-17 RS $

* in `tkRAD.core.tools`:

    * added new `choose_type()`, new `choose_if()`:

        * now fully implemented;

* added new `tkRAD.widgets.RADDialog` class:

    * now fully implemented;

    * TESTED OK in dialogbox mode (transient, modal);

    * TESTED OK in toolbox mode (transient, non-modal);


### $ 2014-03-14 RS $

* in `RADXMLWidget`:

    * in `_init_deferred_attributes()`:

        * now 'common' XML attrs start inits at first;

        * it's really better this way;

* in `RADXMLBase`:

    * added new `is_xml()`:

        * now fully implemented;

* in `RADStatusBar`:

    * in `toggle_var` (setter): resync'ed along `self._previous_value`;

    * added new `self._previous_value` for real diff checkups in
    `toggle()`;

    * added new `_get_bit()`, new `show()`, new `hide()`:

        * now fully implemented;

    * in `notify()`, `info()`:

        * added `update_idletasks()` for better sync'ed text display;


### $ 2014-03-13 RS $

* in `RADXMLWidgetBase`:

    * in `_tkRAD_deferred_command_support()`:

        * enabled **more powerful** external keywords support;

        * now you may pass *ANY* additional keywords `**kw` you like
        in `self._queue.flush("widget", **kw)`, *NOT ONLY*
        `widget=created_widget`;


### $ 2014-03-12 RS $

* tagged and released **tkRAD v1.4.1 - Refer And Defer**;

* in `RADXMLWidget`:

    * fixed v1.4 deferred `_init_attributes()` inconsistency:

        * now works **as in tkRAD < v1.4**:

            * `self._init_attributes()` is again for **immediate
            attrs** parsing;

            * `self._init_deferred_attributes()` is now for
            **deferred attrs** parsing;

            * `self._init_attributes_flat()` is kept for
            compatibility reasons with tkRAD v1.4;


### $ 2014-03-11 RS $

* in `core/i18n.py`:

    * added new `switch_on()`, new `switch_off()`:

        * now fully implemented;

        * ease up debugging sessions by switching i18n support
        ON/OFF on-the-fly;

Example:

```python
import tkRAD

tkRAD.i18n.switch_off()
```


### $ 2014-03-10 RS $

* tagged and released **tkRAD v1.4 - Tasmania Sunset**.

* in `RADXMLWidget`:

    * added new `_init_attributes_flat()`:

        * now fully implemented;

    * updated code elsewhere;

* updated `RADXMLWidgetBase`, `RADXMLWidget`, `RADXMLFrame`:

    * now support `self.slot_owner` natively;

* in `RADWidgetBase`:

    * added new class member `self.slot_owner` for
    **tkRAD.command.support**;

    * by now, it is possible to separate `self.tk_owner` from
    `self.slot_owner`: useful for e.g. `RADXMLFrame`;

    * **compatibility**: by default `self.slot_owner = self.tk_owner`;

* looking for new ideas before tagging v1.4...

* all has been tested OK at this time;

* in `RADXMLWidget`, `RADXMLMenu`: updated code anywhere needed OK;

* in `RADXMLWidgetBase`:

    * in `_tkRAD_command_support` and
    `_tkRAD_deferred_command_support`:

        * updated code OK;

* in `RADXMLBase`: updated code OK;

* in `RADXMLBase`, `RADXMLWidgetBase`, `RADXMLWidget`, `RADXMLMenu`:

    * started implementing **deferred tasks** new concept;

* **not so simple** to find the good naming convention(!);

* in `RADXMLBase`:

    * renamed `self._dt_queue` to simply `self._queue`;

* `triggers` have been replaced by `actions` in comments;

* `DeferredTriggerQueue` is **inappropriate name**: now renamed
anywhere to `DeferQueue` as for deferred actions queue buffer;


### $ 2014-03-09 RS $

* in `RADXMLBase`:

    * added new class member `self._dt_queue`: private instance of
    `DeferredTriggerQueue`;

    * in `xml_build()`: added support for `self._dt_queue`;

* added new `tkRAD/core/defer.py`:

    * class name is now `DeferredTriggerQueue`;

    * get app-wide `DeferredTriggerQueue` instance with
    `get_deferred_trigger_queue()` or with its shortcut name
    `get_dt_queue()`;

    * now fully implemented OK;

* **tkRAD v1.4** new idea: now implementing deferred triggers for
XML attrs parsing;


### $ 2014-03-08 DA $

* pull request:

    * simplified grammar and spelling in `README.md` file;


### $ 2014-03-08 RS $

* added new collaborators:

    * **Cyril Walle**: education counselor;

    * **Dale Athanasias**: wiki contributor;


### $ 2014-03-03 RS $

* tagged and released **tkRAD v1.3 - The Full Monty**.

* in `RADXMLWidget`:

    * in `DTD`:

        * added new constraints for `menubutton`, `ttkmenubutton`;

* started test/debugging session;


### $ 2014-02-28 RS $

* in `RADXMLWidget`:

    * added new `_parse_attr_value()`:

        * now specialized for `<ttkscale>` and other elements;

        * now fully implemented;


### $ 2014-02-27 RS $

* in `RADXMLWidget`:

    * optimized code
    in `_build_element_ttkstyle()`,
    in `_build_element_widget()`,
    in `_init_attributes()`;

    * added new XML element `<ttktab>` child of `<ttknotebook>`;

    * added new XML element `<ttktheme use="theme_name"/>`;

    * added
    new `_build_element_ttktab()`,
    new `_build_element_ttktheme()`,
    new `_parse_attr_use()`,
    new `_parse_attr_displaycolumns()`,
    new `_parse_attr_columns()`:

        * now fully implemented;

    * in `_parse_attr_selectmode()`, `_parse_attr_show()`:

        * added special support for `ttk.Treeview`;

    * in `_build_element_scrollbar()`:

        * fixed bug: `w.cget("option")` is of `TclObj.index` type
        and *NOT* of `str` type;

        * must transtype to get real value in comparisons;

    * in `_parse_attr_orient()`:

        * added special support for `ttk.PanedWindow`;

        * `orient` attr is *READ-ONLY* in
        `ttk.PanedWindow().configure()` and *MUST* only be declared
        in **class constructor args**;

    * in `_set_layout()`:

        * added new support for `ttk.PanedWindow` child widgets;

    * added
    new `_parse_attr_maximum()`,
    new `_parse_attr_mode()`,
    new `_parse_attr_weight()`:

        * now fully implemented;


### $ 2014-02-26 RS $

* in `RADXMLMenu`:

    * in `is_menu_handler()`:

        * added support for `ttk.Menubutton`;

* in `RADXMLWidgetBase`:

    * in `_parse_attr_compound()`:

        * enlarged values to meet ttk AND tkinter natives needs;

* in `RADXMLWidget`:

    * added
    new `_parse_attr_indicatorcolor()`,
    new `_parse_attr_invalidcommand()`,
    new `_parse_attr_padding()`:

        * now fully implemented;

    * in `_build_element_ttkstyle()`:

        * now supports CDATA script with **CSS-like syntax**;

        * added support for cascading defs of same elements;

e.g. you can do things like this:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkRAD

mainwindow = tkRAD.RADXMLMainWindow()

xml_main = """
    <tkwidget>
        <!-- you can mix as if you like -->
        <ttkstyle
            apply="myButton.TButton"
            background="darkgreen"
            foreground="white"
        >
        <![CDATA[
            /*
                now you can use CSS-like syntax for
                all of your ttk widget style
                definitions;
            */

            /*
                notice: the '*' element means 'apply to ALL elements';
            */

            * {
                background: #ffffdd;
                foreground: chocolate;
            }

            /** Doxygen comments */

            /*! Doxygen comments */

            /*
                element:pseudo-format
                matches with any ttk widget state
                e.g.
                :active         :!active
                :background     :!background
                :disabled       :!disabled
                :focus          :!focus
                :invalid        :!invalid
                :pressed        :!pressed
                :readonly       :!readonly
                :selected       :!selected
            */

            *:focus {
                background: yellow; /* only when focused */
            }

            /*
                pseudo-formats:
                you may use any combination you like
                even with '!state' (not-state logic)
            */

            TButton:active:!pressed {

                background: orange; /*  when hovered,
                                        but don't press
                                        oranges!
                                    */
            }

            newName.TCheckbutton {}

            /***********************************************************
                you can put comments
                anywhere you like
            ***********************************************************/

            Treeview
                :selected
                :focus
                :!disabled
            {
                font: "URW Palladio L" 16 italic bold;
            }

            newName.TLabel,
            TLabel:!disabled,
            /* this one is the most important one! */
            TRadiobutton
                :focus      /* applies only for TRadiobutton */
                :!pressed   /* not for the previous ones */
            {
                font: sans 12;
                indicatorcolor: blue;
            }
        ]]>
        </ttkstyle>
        <!-- the following style is for Tkinter NATIVE widgets -->
        <style
            id="style1"
            font="'URW Palladio L' 16 italic bold"
            bg="red"
            fg="white"
        />
        <label
            text="Hello good people!"
            bg="maroon"
            style="style1"
            layout="pack"
            resizable="width"
        />
        <ttklabel
            text="Please, choose your favourite meal:"
            layout="pack"
            resizable="width"
        />
        <ttklabelframe
            text="Choose"
            layout="pack"
            resizable="yes"
        >
            <ttkradiobutton
                text="Pizza!"
                variable="optgroup1"
                value="pizza"
                layout="pack"
                resizable="width"
            />
            <ttkradiobutton
                text="Hot-dog!"
                variable="optgroup1"
                value="hotdog"
                selected="selected"
                layout="pack"
                resizable="width"
            />
            <ttkradiobutton
                text="Hamburger!"
                variable="optgroup1"
                value="hamburger"
                layout="pack"
                resizable="width"
            />
        </ttklabelframe>
        <ttkbutton
            text="Quit"
            style="myButton.TButton"
            command="@quit"
            layout="pack"
        />
    </tkwidget>
"""

mainwindow.xml_build(xml_main)

mainwindow.run()
```


### $ 2014-02-25 RS $

* in `RADStatusBar`:

    * replaced `TK.Label` by `ttk.Label` for fancier look'n'feel;

* in `RADXMLWidget`:

    * in `_set_widget_config()`:

        * now supports `style` profile for tkinter widgets default
        configuration;

    * added new `_parse_attr_apply()`:

        * now fully implemented;

        * XML attr of `<ttkstyle apply="newName.oldName" .../>`;

    * added new `_build_element_ttkstyle()`:

        * now implements `ttk.Style().configure(_apply, **attrs)`;

    * added new `_parse_attr_style()`:

        * now fully implemented;

        * XML attr `style` now can either be `style="style_id"` for
        tkinter native widgets or be `style="newName.oldName"` for
        ttk widgets referring to a `ttk.Style()` definition or to a
        `<ttkstyle>` XML element def (which is the same, in fact);

    * added new `_build_element_style()`:

        * building def for `<style.../>` XML element;

        * now implements a TK_CONFIG default profile to be
        overridden by other XML attrs;

        * you can put here any Tkinter attrs as
        `_set_widget_config()` will filter attrs along widget's own
        `configure()` attrs;

        * common attrs can be applied to any native widget, when
        matching attrs are met;


### $ 2014-02-24 RS $

* ***IDEA:*** what about creating `<tkstyle>` profile with
`configure()` options that any `tkinter` **NATIVE** widget could
apply with XML attr `style="tkstyle_id"`?

* studying future `<ttkmap>` XML element;

* studying future `<ttkstyle>` XML element;

* in `RADCanvas`:

    * stripped out `TK_ATTRS` class main member: now *USELESS*;

    * updated code in `__init__()` along with new constraints;

* in `RADFrame` and `RADXMLFrame`:

    * stripped out `TK_ATTRS` class main member: now *USELESS*;

    * upgraded class ancestor from `tkinter.Frame` to `ttk.Frame`;

    * now supports `ttk.Style()`, `ttk.Style().map()` and so on;

* in `RADWidgetBase`:

    * rewritten `_only_tk()`:

        * now widget *MUST* be init'ed before calling this method e.g.:
        ```python
        ttk.Frame.__init__(self, master)
        self.configure(**self._only_tk(self.CONFIG))
        ```

        * no need more to use `TK_ATTRS` main member: getting
        tkinter attrs **directly** from `self.configure().keys()`;

        * Caution: `self.configure()` needs `self.tk`: Tkinter
        widget must be init'ed before calling this;

* in `RADStatusBar`:

    * added `ttk.Sizegrip` for fancier look'n'feel;

* in `RADXMLWidgetBase`:

    * in `_parse_attr_name()`:

        * XML attr `name` no longer have to be lower-cased;

        * now accepting case-sensitive class member names;

* in `RADXMLWidget`:

    * added first level support for ttk widgets;

    * in `CLASSES`, `_build_tk_native()`, `_parse_attr_module()`:

        * enlarged to new tkinter + ttk supports;

        * this needs to be implemented further more;


### $ 2014-02-23 RS $

* in `RADXMLWidget`:

    * in
    `_build_element_configure()`,
    `_build_element_listbox()`,
    `_build_element_widget()`:

        * updated code along with `_set_widget_config()`;

    * added new `_set_widget_config()`:

        * now config `dict()` object is filtered along with widget's
        attrs to avoid useless traps;

        * now fully implemented;

        * returns True on success, False otherwise;


### $ 2014-02-21 RS $

* in `RADMainWindow`:

    * in `run()`:

        * fixed bug: added `self.destroy()`;

        * caution: even while destroying app, getting the following
        `Tcl/Tk` error while testing in console:
        ```Tcl
        invalid command name "139710702393608callit"
            while executing
        "139710702393608callit"
            ("after" script)
        ```

* in `tkRAD.easy.builder[2]`:

    * in `build()`:

        * fixed bug: in autorun mode `Tk()` persistent instance may
        cause errors elsewhere;

        * now destroying instance + returning `None` to get sure;


### $ 2014-02-20 RS $

* in `RADXMLBase`:

    * fixed `path` parameter / module name conflict bug with module
    alias `P`;

* in `tkRAD.core.options`:

    * in `save()`:

        * fixed bug on RC config saving op;


### $ 2014-02-19 RS $

* generating tag for `tkRAD v1.2`:

    * release name: `Optimized Kangaroo`;

    * this release is *STABLE*: no more future features planned;

    * all is optimized OK;

* updated wiki doc: OK;

* preparing for `tkRAD v1.2` stable release;

* optimizing code in all modules of `tkRAD`;


### $ 2014-02-18 RS $

* `TODO.md`: TODO list is up-to-date;

* updated wiki wiki documentation: OK;

* optimizing code for `tkRAD v1.2: 'Optimized Kangaroo'` release;

* in `RADXMLMenu`:

    * in `ATTRS`:

        * now only *INDISPENSABLE* item attrs *MUST* figure out in
        there, for optimization reasons;

    * added new `KEYS`:

        * now *ALL* item attrs *MUST* figure out in there, for
        optimization reasons;

    * fully optimized `_init_coptions()`, `_init_moptions()` and all
    `_build_element_*()` methods;

    * removed `_build_menu_item()`: *NOT* optimal;

    * added
    new `_init_generics()`,
    new `_init_checkables()`:

        * now fully implemented;

* in `tkRAD.core.tools`:

    * added
    new `dict_delete_items()`,
    new `dict_only_keys()`:

        * now fully implemented;

* in `RADXMLBase`:

    * `delete_dict_items()` is now *DEPRECATED*;

    * **kept** `delete_dict_items()` method **for compatibility**
    reasons;

    * use `tools.dict_delete_items()` instead, by now;


### $ 2014-02-17 RS $

* in `RADXMLWidget`:

    * in `_parse_attr_anchor()` + `ANCHORS`:

        * optimized all regexp replacements with `re.compile()`;

* in `RADXMLMenu`:

    * in `_parse_attr_accelerator()` + `SYMBOLS`:

        * optimized all regexp replacements with `re.compile()`;

* in `RADXMLBase`:

    * in `delete_dict_items()`:

        * optimized stripping of common keys between `dict.keys()`
        and `*args`;

    * in `xml_build()`:

        * now casting XML root element to match with subclass
        DOCTYPE constraints;

    * added new `_cast_root_element()`:

        * now fully implemented;

    * added new `DOCTYPE`:

        * main member defines XML root element e.g. `tkwidget`,
        `tkmenu`, etc;

* in `RADWidgetBase`:

    * added new `classname()`:

        * now fully implemented;


### $ 2014-02-16 RS $

* tagged and released `tkRAD v1.1 - Blinking Radiobutton`;

* in `TODO.md`:

    * now TODO list is up-to-date;

* in `RADXMLMainWindow`:

    * in `_init_mainframe()`:

        * now `self.xml_build` shortcut made safer;

* in `tkRAD.core.options.OptionManager`:

    * removed `_ensure_config_dir()`: *NOT* useful;

    * now exceptions will raise on incorrect paths with `load()` and
    `save()`;

    * it's better this way, OK;

* in `tkRAD.core.i18n`:

    * checked multiple loading of translations table:

        * Python does *NOT* call `install()` more than once;

        * TESTED OK;

* in `RADXMLMenu`:

    * in `_build_menu_item()`:

        * fixed minor bug: XML declared selected/checked items were
        not really activated by default;


### $ 2014-02-10 RS $

* generating tag for `tkRAD v1.0`;

* now `tkRAD` is **ready** for *STABLE RELEASE*;

* `tkRAD` has been TESTED OK on Windows 8 platform;

* in `RADApplication.APP`:

    * added `description` member;

* updated `tkRAD/__init__.py`:

    * now `import tkRAD` sets up `i18n.install()` by default;


### $ 2014-02-10 RS $

* updated wiki wiki documentation anywhere along new constraints;

* anywhere in `tkRAD` lib:

    * renamed all `*canonize*()` to `*normalize*()`;

* added new `tkRAD.core.path`:

    * duplicated incorrectly named `tkRAD.core.uri`;

    * renamed `canonize()` to `normalize()`;

    * updated all `import uri` to `import path` anywhere in `tkRAD`;

    * updated all `uri.canonize()` to `path.normalize()` anywhere in
    `tkRAD`;

* updated `tkRAD.core.uri`:

    * fixed MS-Windows normpath() bug;

    * renamed all `uri` params to `path`;

    * duplicated module to `tkRAD.core.path`;

    * abandoned maintenance: incorrect vocabulary;

    * kept module for backward compatibility;

* updated `RADMainWindow`:

    * in `run()`:

        * added `self.hide()` after event main loop to avoid
        unexpected postponed stimuli;

* updated `tkRAD.core.checkups`:

    * in `python_require()`:

        * updated code along new `parse_version()` function;

    * added new `parse_version()`:

        * now fully implemented;


### $ 2014-02-09 RS $

* updated `RADMainWindow`:

    * in `maximize()`, `_slot_root_changed()`:

        * fixed bug about WM_ATTRIBUTES:

            * not all OSes handle "-zoomed" attribute;

            * WM_STATE_MAXIMIZED state will only work if attribute
            "-zoomed" exists on running platform;

* updated `RADXMLWidget`:

    * in `_build_element_listbox()`:

        * fixed bug on `state="disabled"`:

            * list items were *NOT* showing up;

            * now config is OK;

    * in `_parse_attr_activestyle()`:

        * default value is `dotbox` *NOT* `underline` as documented
        on Tkinter's website;

    * in `_build_element_include()`:

        * removed self-inclusion security: *NOT* perfect enough;

        * let Python interpreter handle this trap;

    * in
    `_build_element_checkbutton()`,
    `_build_element_radiobutton()`:

        * made checked/unchecked status clearer;

* updated `RADXMLWidgetBase`:

    * in `_tkRAD_command_support()`:

        * now `lambda(*args, s=..., e=..., **kw)` does
        `s.raise_event(e, *args, **kw)`;

        * now added `**kw` to `lambda()` from event support;


### $ 2014-02-08 RS $

* updated `RADXMLWidget`:

    * in `_build_element_scrollbar()`:

        * now target widget is automagically connected to scrollbar,
        if it is technically possible;

        * raises `TypeError` with explanations on trouble and
        connection explicit request;

    * added new `_parse_attr_connect()`:

        * now fully implemented;


### $ 2014-02-07 RS $

* updated `RADXMLBase`:

    * added
    new `get_bitmap_uri(self, path)`,
    new `set_image(self, path)`,
    new `get_image(self, path)`:

        * now fully implemented;

* updated `RADXMLWidgetBase`:

    * in
    `_tkRAD_image_support()`,
    `_tkRAD_bitmap_support()`:

        * now fully implemented;

* updated `RADXMLWidget`:

    * moved `_set_class_member()` from `RADXMLWidget` to `RADXMLBase`:

        * method `_set_class_member()` is in fact a real generic XML
        service;

    * disabled XML attr `name`:

        * now developpers must *EXPLICITLY* declare `<widget
        name="..."/>` to get a class member in `tk_owner`;

        * this avoids unexpected `AttributeError` exceptions and
        useless memory overloads with unwanted class members;


* updated `RADXMLMenu`:

    * added `get_menu (self, attr_id)`:

        * coding comfort and shortcut for `get_object_by_id()`;

        * now fully implemented;

    * disabled XML attr `name`:

        * useless for menus (use `get_object_by_id()` instead);


### $ 2014-02-03 RS $

* updated `RADXMLBase`, `RADXMLWidget`, `RADXMLMenu`:

    * renamed `loop_on_children()` to `_loop_on_children()`,
    `parse_xml_attributes()` to `_parse_xml_attributes()`,
    `register_object_by_id()` to `_register_object_by_id()`:

        * made them `protected` (heading underscore);

* updated `RADXMLBase`:

    * in `get_xml_uri()`:

        * now enriched with new possibilities;

    * suppressed member `KEYWORD`: bad idea;

    * in `__init__()`:

        * now `XML_RC["filename"]` accepts previous inits (no more
        forced overridings);


### $ 2014-02-02 RS $

* updated `RADXMLBase`, `RADXMLWidgetBase`:

    * member `ATTRIBUTE_PARSER` now handles `{xml_attribute}`
    instead of `{xml_attr}`;


### $ 2014-02-01 RS $

* updated `RADXMLAttribute`:

    * optimized code anywhere;

* updated `RADXMLWidgetBase`, `RADXMLWidget`, `RADXMLMenu`:

    * renamed all `build_element_*()` to `_build_element_*()`;

    * renamed all `parse_attr_*()` to `_parse_attr_*()`;

    * made all of them `protected`;

* updated `RADXMLWidgetBase`:

    * in member `ATTRIBUTE_PARSER`:

        * renamed methods in template to be `protected` (heading
        underscore);

* updated `RADXMLBase`:

    * in members `ATTRIBUTE_PARSER`, `ELEMENT_BUILDER`:

        * renamed methods in template to be `protected` (heading
        underscore);


### $ 2014-01-31 RS $

* updated `RADXMLWidget`:

    * in
    `build_element_widget()`,
    `build_element_tkmenu()`,
    `build_element_optionmenu()`,
    `build_element_listbox()`:

        * now calling `_set_class_member()` for class member inits;

    * added new `_set_class_member(name, widget)`:

        * now fully implemented;

        * now widget attr `name` becomes `self.tk_owner.{name}`
        class member instead of `tk_parent.{name}` class member;

* updated `RADXMLFrame`:

    * adapted along `RADFrame` config philosophy;

* updated `RADXMLMainWindow`:

    * in `_init_mainframe()`:

        * renamed `self.slot_quit_app` to `self._slot_quit_app`;


### $ 2014-01-30 RS $

* updated `RADStatusBar`:

    * optimized code anywhere;


### $ 2014-01-29 RS $

* updated `RADMainWindow`:

    * in `connect_statusbar()`:

        * now raises `TypeError` if statusbar object type is *NOT*
        supported;

    * optimized code anywhere;

    * moved all `slot_*()` methods to `_slot_*()`:

        * made them `protected`;


### $ 2014-01-28 RS $

* updated `RADFrame`, `RADCanvas`:

    * in `__init__()`:

        * fixed bug on multiple instance `dict()` XRef `self.CONFIG`
        widget class pre-configuration;


### $ 2014-01-27 RS $

* updated `RADApplication`:

    * in `_start_gui()`:

        * added support for implicit `menu.checkbutton.cvar` named
        `show_statusbar` for testing sessions;

        * now using:
        ```
            <menu label="_Show">
                <checkbutton
                    label="Show statusbar"
                    command="@ToggleStatusbar"
                    variable="show_statusbar"
                    onvalue="1"
                />
            </menu>
        ```
        will provide automagic implementation in
        `RADApplication.mainwindow`;


### $ 2014-01-26 RS $

* updated `tkRAD.easy.builder2`:

    * TESTED OK;

    * reset all module code along `tkRAD.easy.builder` new code
    optimizations;

* updated `tkRAD.easy.builder`:

    * TESTED OK;

    * moved `Builder.canonize_id()` to `module.canonize_id()`:

        * readapted code along this new constraint;

    * moved `Builder.is_pstr()` to `module.is_pstr()`:

        * readapted code along this new constraint;


### $ 2014-01-25 RS $

* updated `tkRAD.easy.builder2`:

    * TESTED OK;

    * reset all module code along `tkRAD.easy.builder` new code
    optimizations;

* updated `tkRAD.easy.builder`:

    * in `Builder`:

        * TESTED OK;

        * optimized code anywhere in module;

        * updated `_get_correct_id()`:

            * optimized along `_get_unique_id()`;

        * added new `_get_unique_id()`:

            * copied from `RADXMLBase._get_unique_id()`;

            * adapted locally;


### $ 2014-01-24 RS $

* updated `tkRAD.core.options`:

    * in `OptionManager`:

        * updated `set_config_dir()`, `set_config_file()`:

            * now take in account loading op flag;

        * added new `_reset_load()`:

            * now fully implemented;

            * resets loading op flag;


### $ 2014-01-23 RS $

* updated `RADApplication`:

    * optimized code anywhere in whole class def;

    * in `_init_options()`:

        * fixed bug about `OptionManager.set_owner()`;


* updated `tkRAD.core.options`:

    * in `module.get_option_manager()`:

        * removed `owner` param;

    * in `OptionManager`:

        * renamed
        `ensure_config_dir()` to `_ensure_config_dir()`,
        `get_uri()` to `_get_uri()`:

            * set `public` to `protected` methods;

        * in `__init__()`:

            * removed `owner` param;

        * removed `get_owner()`, `set_owner()` :

            * have become useless;

* updated `tkRAD.core.services`:

    * added new `ServiceManager.clear_all()`:

        * now fully implemented;

        * resets service manager to a new `dict()` object;

    * added new `ServiceManager.delete_service()`:

        * now fully implemented;

        * silent deletion of named service;

    * added new `ServiceManager.replace_service()`:

        * now fully implemented;

        * allow overridings of existing named service;

    * in
    `ServiceManager.get_service()`,
    `ServiceManager.register_service()`,
    `module.register_service()`:

        * optimized code;

        * no border effect;


### $ 2014-01-22 RS $

* updated `RADApplication`:

    * added new `_init_i18n()`:

        * now fully implemented;

* updated `tkRAD.core.i18n`:

    * renamed `update_translations_table()` to
    `load_translations_table()`;

    * in `install()`:

        * optimized code;

        * now supports silent and automatic user locale language
        installation by default;

    * added
    `get_translations_dir()`,
    `get_translations_lang()`,
    `get_translations_table()`,
    `set_translations_table()`:

        * now fully implemented;


* updated `tkRAD.core.uri`:

    * in
    `canonize()`:

        * optimized code;

        * no border effect;


### $ 2014-01-21 RS $

* updated `tkRAD.core.events`:

    * in
    `connect()`,
    `connect_dict()`,
    `disconnect()`,
    `raise_event()`:

        * optimized code;

        * no border effect;


### $ 2014-01-20 RS $

* updated `tkRAD.core.tools`:

    * in
    `canonize_id()`,
    `canonize_relative_module()`:

        * optimized code;

        * no border effect;


### $ 2014-01-19 RS $

* updated `tkRAD/__init__.py`:

    * now admits direct imports for daily use classes:

        * direct import for `RADApplication`;
        * direct import for `RADMainWindow`;
        * direct import for `RADXMLMainWindow`;
        * direct import for `RADXMLFrame`;

    * usage:

```python
    # simple import
    import tkRAD
    # direct import
    app = tkRAD.RADApplication()
    # direct import
    mw = tkRAD.RADMainWindow()
    # direct import
    xmw = tkRAD.RADXMLMainWindow()
    # direct import
    xf = tkRAD.RADXMLFrame()
```

* updated `RADXMLFrame`:

    * in `__init__()`:

        * now supports `self.tk_parent = master` aside
        `self.tk_owner` as `RADXMLFrame`'s `tk_owner` is
        exceptionnally `RADXMLFrame` itself for technical reasons;


### $ 2014-01-18 RS $

* updated `RADXMLWidget`:

    * in `build_element_widget()`:

        * now supports `init()` procedure for created widgets;

        * `init()` is launched at the latest end, AFTER widget's
        CHILDREN creation;

    * added new `parse_attr_init()`:

        * now fully implemented;

        * allows any widget to launch a specific `init()` procedure
        e.g. `<label init=".mylabel_init"/>`;

        * syntax is `init="tkRAD.command.support"`;


### $ 2014-01-17 RS $

* updated `RADXMLWidgetBase`:

    * in `_tkRAD_widget_support()`:

        * added new aliases in attr value:

            * `@top` for `tk_owner.winfo_toplevel()` widget;

            * `@parent` for `tk_parent` widget;

* updated `RADXMLWidget`:

    * added
    new `parse_attr_maxheight()`,
    new `parse_attr_maxwidth()`,
    new `parse_attr_minheight()`,
    new `parse_attr_minwidth()`,
    new `parse_attr_transient()`:

        * now fully implemented;

        * specific attributes for `<toplevel>` XML element;

    * added new `_layout_toplevel()`:

        * now fully implemented;

        * Toplevel window special layouts and inits;

    * updated
    `_set_layout()`,
    `parse_attr_height()`,
    `parse_attr_width()`:

        * now handles special support for `tkinter.Toplevel` widget
        case;

    * added new `parse_attr_title()`:

        * now fully implemented;

        * specific attr for `<toplevel>` XML element;

    * added new `parse_attr_visibility()`:

        * now fully implemented;

        * must be one of 'normal', 'maximized', 'minimized',
        'hidden' fixed values;

        * specific attr for `<toplevel>` XML element;

    * in `parse_attr_seq()`:

        * new implementation;

        * now admits simplified notation e.g. `seq="Control-s"`
        instead of `seq="&lt;Control-s&gt;"` for more comfort;

    * in `build_element_tkevent()`:

        * fixed many bugs;


### $ 2014-01-16 RS $

* updated `RADXMLMenu`:

    * revised/optimized code almost anywhere;

    * updated all `parse_attr_*()` signatures along real needs;

* updated `RADXMLBase`:

    * added new `element_get_id(self, xml_element)`:

        * now fully implemented;

    * in `parse_xml_attributes()`:

        * now assumes larger anonymous parser signatures `parser(**kw)`;

* updated `RADXMLAttribute`:

    * added new `update_xml_element(self, value=None)`:

        * updates inner XML element's attribute of `attribute.name`
        name along a given `@value` param or inner `attribute.value`
        if `@value` param is `None` or omitted;

        * now fully implemented;

* updated `RADXMLWidgetBase`:

    * revised/optimized code almost anywhere;

    * added
    new `_tkRAD_bitmap_support()`,
    new `_tkRAD_image_support()`:

        * CAUTION: to be implemented;

    * added
    new `_tkRAD_state_support()`,
    new `_tkRAD_cursor_support()`,
    new `_tkRAD_widget_support()`,
    new `_is_unparsed()`,
    new `_tkRAD_command_support()`,
    new `_tkRAD_font_support()`,
    new `_tkRAD_relief_support()`,
    new `_tkRAD_cvar_support()`:

        * now fully implemented;

    * updated all `parse_attr_*()` signatures along real needs;

    * in `_fix_values()`, `parse_attr_id()`:

        * now supports `attribute.update_xml_element()`;

    * in `parse_attr_checked()`, `parse_attr_selected()`:

        * now implemented along `_tkRAD_boolean_support()`;

    * in `_tkRAD_boolean_support()`:

        * now supports `attribute.update_xml_element()`;

        * now admits logical values such as '1', '0', 'yes', 'no',
        'true', 'false' or `attribute name` itself (W3C compliant)
        e.g. `selected="selected"`;

* updated `RADXMLWidget`:

    * revised/optimized code almost anywhere;

    * updated all `parse_attr_*()` signatures along real needs;

    * in `parse_attr_wrap()`:

        * now supports fixed values 'char', 'word', 'none' for XML
        element `<text>`;

        * still supports default boolean values '0', '1' for other
        XML elements;


### $ 2014-01-15 RS $

* updated `RADXMLWidgetBase`:

    * removed `_tk_child_config()`:

        * now merged into `_tk_config(**kw)` with
        `kw.get("tk_child_config")` keyword flag instead;

    * added new `_tkRAD_dimension_support()`:

        * now fully implemented;

    * in `_tk_child_config()`:

        * added support for `_` discriminator in attr `_name` in
        order to avoid `tkinter` TK_CONFIG attrs conflict;

* updated `RADXMLWidget`:

    * added new `parse_attr__after()`, `parse_attr__before()`,
    `parse_attr__height()`, `parse_attr__minsize()`,
    `parse_attr__padx()`, `parse_attr__pady()`,
    `parse_attr__sticky()`, `parse_attr__width()`:

        * now fully implemented;

        * kept for easiness and comfort: `parse_attr_after()`,
        `parse_attr_before()`, `parse_attr_minsize()`,
        `parse_attr_sticky()`;

    * in `_set_layout()`:

        * now `tkinter.PanedWindow` child layout management fully
        implemented;

        * now attr `resizable` may override attr `sticky` if omitted;


### $ 2014-01-14 RS $

* updated `RADXMLWidgetBase`:

    * updated all `parse_attr_*()` along new `_tkRAD_*_support()`;

    * added new `_tk_child_config()`:

        * now fully implemented;

    * in `_before_building_element()`:

        * added new dict() `TK_CHILD_CONFIG`;

    * moved `ANCHORS` to `RADXMLWidget`;

    * in `parse_attr_compound()`:

        * now fully implemented;

    * in `parse_attr_command()`:

        * in event support: extended number of inner `tkinter` args
        to undefined (*args);

    * added new `_tkRAD_color_support()`,
    new `_tkRAD_float_support()`,
    new `_tkRAD_integer_support()`,
    new `_tkRAD_any_value_support()`:

        * now fully implemented;

* updated `RADXMLWidget`:

    * updated all known and possible `parse_attr_*()` along new
    `_tkRAD_*_support()`;

    * in `parse_attr_layout()`:

        * default value is now `layout="none"` (**no layout**)
        instead of previous **risky** default value `layout="pack"`;

    * in `parse_attr_format()`:

        * now fully implemented;

        * supports `%03.2f` format as in `sprintf()`;

        * accepts simplified `03.2` notation;

    * in `parse_attr_buttonup()`:

        * now implemented along `parse_attr_relief()`;

    * in `parse_attr_class()`:

        * optimized code;

    * in `parse_attr_repeatdelay()`, `parse_attr_repeatinterval()`:

        * now fully implemented;

    * in `parse_attr_confine()`, `parse_attr_jump()`:

        * now implemented along `_tkRAD_boolean_support()`;


### $ 2014-01-13 RS $

* updated `RADXMLWidget`:

    * in `parse_attr_xscrollincrement()`,
    `parse_attr_yscrollincrement()`,
    `parse_attr_wraplength()`,
    `parse_attr_takefocus()`,
    `parse_attr_sliderlength()`,
    `parse_attr_troughcolor()`,
    `parse_attr_tickinterval()`,
    `parse_attr_resolution()`,
    `parse_attr_to()`,
    `parse_attr_from_()`,
    `parse_attr_showvalue()`,
    `parse_attr_readonlybackground()`,
    `parse_attr_pady()`,
    `parse_attr_padx()`,
    `parse_attr_orient()`,
    `parse_attr_offrelief()`,
    `parse_attr_length()`,
    `parse_attr_insertwidth()`,
    `parse_attr_insertborderwidth()`,
    `parse_attr_insertbackground()`,
    `parse_attr_indicatoron()`,
    `parse_attr_highlightthickness()`,
    `parse_attr_highlightcolor()`,
    `parse_attr_highlightbackground()`,
    `parse_attr_height()`,
    `parse_attr_exportselection()`,
    `parse_attr_elementborderwidth()`,
    `parse_attr_disabledbackground()`,
    `parse_attr_digits()`,
    `parse_attr_buttondownrelief()`,
    `parse_attr_buttonbackground()`:

        * now fully implemented;

    * in `parse_attr_module()`:

        * now module `id` *NOT* found raises `KeyError`;

    * in `parse_attr_sliderrelief()`,
    `parse_attr_sashrelief()`,
    `parse_attr_overrelief()`,
    `parse_attr_activerelief()`:

        * now fully implemented along `parse_attr_relief()`;

* updated `RADXMLWidgetBase`:

    * added new `_tkRAD_boolean_support()`:

        * now fully implemented;

    * in `parse_attr_relief()`:

        * now fully implemented;


### $ 2014-01-12 RS $

* updated `RADXMLBase`:

    * in `get_correct_id()`:

        * fixed bug on already existing names while creating default
        'objectXXX' id names;

    * in `_get_object_id()`:

        * fixed bug on already existing names while creating default
        '{classname}XXX' id names;

    * added new `_get_unique_id (self, radix)`:

        * tries to retrieve a new and unique indexed 'id' name along
        `@radix` param;

* updated `RADXMLMenu`:

    * added new `DTD`:

        * added `DTD.menu` constraints;

        * added `DTD.tkmenu` constraints;

    * in `build_element_tkmenu()`:

        * now supports direct inclusion into a `tkwidget` doctype
        XML tree document;

        * now supports all menu item childs `<command>`,
        `<checkbutton>`, `<radiobutton>` and `<separator>` when
        `menu handler` is *NOT* of type `tkinter.Tk` (topmenu
        handler);

* updated `RADXMLWidget`:

    * in `parse_attr_direction()`:

        * now fully implemented;

    * in `DTD`:

        * added support for `tkmenu` in `DTD.widget`;

    * added new `build_element_tkmenu()`:

        * now fully implemented;

    * kept old `build_element_menu()` for compatibility;


### $ 2014-01-11 RS $

* updated `RADXMLWidget`:

    * in `build_element_optionmenu()`:

        * now renamed XML attr `variable` to `listvariable` in order
        to match with `<listbox>` XML tk_config attr `listvariable`;

        * XML attr `variable` is *STILL KEPT AVAILABLE* for
        retro-compatibility reasons;

        * this will ease XML scripting/switching between `<listbox>`
        and `<optionmenu>` in testing session;

        * rebounded `start` XML attr so as it might never trap out
        of list bounds;

    * in `parse_attr_choices()`:

        * fixed bug on selecting numeric values;

    * in `parse_attr_listvariable()`:

        * now fully implemented along `parse_attr_variable()`;

    * in `build_element_listbox()`:

        * now fully implemented and debugged specific code;

    * in `ATTRS`:

        * renamed `optionmenu.variable` to `optionmenu.listvariable`
        for XML scripting comfort and easiness;

        * XML attr `<optiomenu variable=""/>` is *STILL KEPT
        AVAILABLE* for retro-compatibility reasons;

        * added `listbox` default XML attrs;


### $ 2014-01-10 RS $

* updated `RADXMLWidget`:

    * in `ATTRS`:

        * added `optionmenu` default XML attrs;

    * in `build_element_optionmenu()`:

        * now fully implemented and debugged specific code;

    * added new `parse_attr_choices()`:

        * now fully implemented and debugged;

    * added new `parse_attr_start()`:

        * now fully implemented and debugged;


### $ 2014-01-09 RS $

* updated `RADXMLWidgetBase`:

    * in `parse_attr_widget()`:

        * now raises `KeyError` if widget `id` is *NOT* found;

    * in `_is_new()`:

        * fixed bug: `@attribute` param may be `None` sometimes;

* added new file `TODO.md`;

* updated `RADXMLWidget`:

    * in `parse_attr_module()`:

        * fixed bug: `@attribute` param may be `None` sometimes;

    * in `build_element_optionmenu()`:

        * disabled faulty generic code;

        * must implement *SPECIFIC CODE* for this object /!\;


### $ 2014-01-08 RS $

* updated `RADXMLWidget`:

    * in `parse_attr_labelanchor()`:

        * now fully implemented along `parse_attr_anchor()`;

        * CAUTION: will *NOT* accept values such as 'wn', 'ws', 'en'
        and 'es' (dummy values?);

    * in `parse_attr_labelwidget()`:

        * now fully implemented along `parse_attr_widget()`;

    * in `parse_attr_slot()`:

        * tkRAD.command.support is now fully implemented;

        * allows EventName aliasing;

* now working on an `ASUS R500VD-SX173H` laptop, Intel QuadCore
i5-3210M @ 2.5 GHz, HDD 500GB, RAM 4GB, widescreen 17.3" 16:9,
turbo'ed by an awesome Ubuntu 13.10 Saucy Salamander distro;


### $ 2014-01-06 RS $

* updated `RADXMLWidget`:

    * in `build_element_include()`:

        * new XML tree is now fully included into current XML tree;

        * all internal cvars, objects, `id` references, etc, are now
        entirely respected;

        * no more extra widget building with extra hassle;

* updated `RADXMLBase`:

    * in `xml_load()`:

        * minor change - no border effect;


### $ 2014-01-04 RS $

* updated `RADXMLWidget`:

    * in `ATTRS`:

        * added `button`, `checkbutton`, `label`, `menubutton`,
        `radiobutton` dict() attrs;

    * in `build_element_widget()`:

        * now supports external keywords (**kw) for XML attr inits;

    * in `_build_tk_native()`:

        * now supports specific XML attrs for tk natives;

    * in `parse_attr_textvariable()`:

        * now fully implemented;

    * in `parse_attr_text()`:

        * now linked to `_tkRAD_label_support()`;

* updated `RADXMLMenu`:

    * in `parse_attr_label()`:

        * now linked to `_tkRAD_label_support()`;

* updated `RADXMLWidgetBase`:

    * added `_tkRAD_label_support (self, attribute, attrs, **kw)`;

* moved file `widget_template.xml` from `tkRAD/xml` to `tkRAD/xml/doc`;


### $ 2014-01-02 RS $

* updated `CHANGES`:

    * moved file from `CHANGES` to `CHANGES.md`;

    * rewritten text to best suit MarkDown (.md) syntax;


### $ 2013-12-31 RS $

* updated `RADMainWindow`:

    * in `connect_statusbar()`:

        * now only connects `self.statusbar` if it is of type
        `RADStatusBar` as devs may redefine `self.statusbar` to meet
        their own needs;

        * devs should override this method if they implement their
        own `MyStatusBar` type in `self.statusbar`;

* updated `RADXMLBase`:

    * in `get_xml_uri()`:

        * fixed ugly URI construction on faulty paths;

        * now `FileNotFoundError` exception traceback is clearer;


### $ 2013-12-30 RS $

* updated `RADStatusBar`:

    * in `toggle()`:

        * fixed bug when `self.toggle_var` is *NOT* set up;

        * added `[WARNING]` message to help developers know about it;


### $ 2013-12-29 RS $

* updated `RADXMLBase`:

    * in `register_object_by_id()`:

        * made it safer: objects of same `id` now raise `KeyError`;

        * no more faulty overridings;

* updated `RADXMLWidgetBase`:

    * `parse_attr_checked()` and `parse_attr_selected()` are now
    fully implemented;

    * in `_before_building_element()`:

        * added `self.WIDGET` for post-implementations of last built
        widget e.g. see `RADXMLWidget.build_element_checkbutton()`
        and `RADXMLWidget.build_element_radiobutton()` for more;

* updated `RADXMLWidget`:

    * in `build_element_checkbutton()`:

        * fixed attr `checked="checked"` bug due to `tkinter`
        inconsistencies --> must set `object.select()` rather than
        `cvar value` which is the exact opposite behaviour of
        `Menu.Checkbutton` menu item /!\;

    * in `build_element_radiobutton()`:

        * fixed attr `selected="selected"` bug due to `tkinter`
        inconsistencies --> must set `object.select()` rather than
        `cvar value` which is the exact opposite behaviour of
        `Menu.Radiobutton` menu item /!\;


### $ 2013-12-28 RS $

* updated `RADMainWindow`:

    * in `connect_statusbar()`:

        * fixed bug: `self.topmenu` and `self.mainframe` may *NOT*
        have attr `get_stringvar()` if user-defined otherwise;


### $ 2013-12-27 RS $

* updated `RADXMLWidgetBase`:

    * in `parse_attr_command()`:

        * event support now works along `Menu.tearoffcommand` 2 args;

* updated `RADXMLMenu`:

    * in `build_element_menu()`:

        * added restriction to `loop_on_child()`: menu now accepts
        only `<menu>`, `<command>`, `<checkbutton>`, `<radiobutton>`
        and `<separator>` XML subelements;


### $ 2013-12-25 RS $

* updated `RADStatusBar`:

    * added `toggle_var_set (self, value)`;

* updated `RADMainWindow`:

    * added `connect_statusbar (self, stringvarname)`;

* updated `RADXMLBase`:

    * added `get_cvars (self)`;

    * added `get_doublevars (self)`;

    * added `get_intvars (self)`;

    * added `get_stringvars (self)`;

* updated `RADXMLWidget`:

    * in `build_element_menu()`:

        * created menu widget is now registered with
        `register_object_by_id()`;

        * menu `stringvars` are now transferred to widget's
        `stringvars` collection;

* updated `RADXMLMenu`:

    * in `RADXMLMenu.ATTRS`:

        * commented all non-essential XML attrs to be init'ed;


### $ 2013-12-23 RS $

* fixed `WM_DELETE_WINDOW` bug @ easy.builder[2];


### $ 2013-12-22 RS $

* upgraded `tkRAD.easy.builder[2]` modules;

* now support `<tkwidget>` XML root node for testing;

* still support `<root>` XML root node for testing;

* rewritten some portions of code with no border effects;


### $ 2013-12-21 RS $

* updated `README.md` file to best suit to Markdown (.md) syntax;


### $ 2013-12-20 RS $

* set up first public release of `tkRAD` library;

* this is the first official version number: **2013.12.20b**;

* release name: **"Christmas Gift"**;

* prepared git repository on `GitHub`:

    git://github.com/tarball69/tkRAD.git

* cloned repository in:

    file://home/rs/apps/official/git/

* expanded GNU GPL v3 license ---> LGPL v3;

* filled with previous project files;

* written entire new `README` file;

* written entire new `CHANGES` file;

* updated license terms in all `*.py` file headers in the project;

* Merry Christmas you all!

===   END OF FILE   ===
