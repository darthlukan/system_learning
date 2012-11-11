import notify2

'''
    Uses notify2 to send a DBUS notification.
    
    First we have to initialize the notifier, we do this
    with the "init" method, providing a string as an argument.
    
    Next, we setup our notification with the "Notification" method.
    This method takes the string argument for our program name/title,
    as well as the text that we want displayed in the body.
    
    Chaining the "show()" method allows us to save lines of code
    and memory as we don't have to save the "notify2.Notification"
    object to a variable and then call "show()" in it.
'''

def note_set_and_send(app, summary):
    '''
        Creates a DBUS notification.
    '''
    notify2.init('Piddle: ')
    return notify2.Notification(app, summary).show()

'''
    Uses the dbus module to send a dbus notification.
    
    This is a more complicated and "manual" example than the one
    above.  First we set the name of the bus we want to use,
    in this case, org.freedesktop.Notifications.  Then we set the path
    to this bus.  We connect to the session bus using "dbus.SessionBus()",
    grab our notification bus object, use it and the bus name to set an
    interface, and then, finally, return the notification.
    
    While this example uses notifications, the structure is the same
    for other available busses.
'''

import dbus

def complicated_note_send(name, summary, body):
    bus = 'org.freedesktop.Notifications'
    path = '/org/freedesktop/Notifications'
    
    session = dbus.SessionBus()
    obj = session.get_object(bus, path)
    iface = dbus.Interface(obj, bus)
    return iface.Notify(name, summary, body)