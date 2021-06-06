import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omui

import maya.cmds as cmds

# Exploring Contexts in Maya API
def maya_useNewAPI():
    pass


class SimpleContext(omui.MPxContext):

    TITLE = "SimpleContext"
    HELP_TEXT = "<insert help text here>"

    def __init__(self):
        super(SimpleContext, self).__init__()
        self.setTitleString(SimpleContext.TITLE)
        self.setImage("C:/Users/andre/Desktop/context_image.png", omui.MPxContext.kImage1)

    def helpStateHasChanged(self, event):
        self.setHelpString(SimpleContext.HELP_TEXT)

    def toolOnSetup(self, event):
        print("tool on setup")

    def toolOffCleanup(self):
        print("tool off cleanup")

    def doPress(self, event, draw_manager, frame_context):
        mouse_button = event.mouseButton()

        if mouse_button == omui.MEvent.kLeftMouse:
            print("left mouse button pressed")
        elif mouse_button == omui.MEvent.kMiddleMouse:
            print("right mouse button pressed")

    def doRelease(self, event, draw_manager, frame_context):
        print ("Mouse button released")

    def doDrag(self, event, draw_manager, frame_context):
        print("Mouse Drag")

    def completeAction(self):
        print("Complete action (enter/return key pressed")

    def deleteAction(self):
        print ("Delete action (backspace/delete key pressed)")

    def abortAction(self):
        print("abort action pressed (esc key pressed)")

class SimpleContextCmd(omui.MPxContextCommand):

    COMMAND_NAME = "abSimpleCtx"

    def __init__(self):
        super(SimpleContextCmd, self).__init__()

    def makeObj(self):
        return SimpleContext()

    @classmethod
    def creator(cls):
        return SimpleContextCmd()
    
def initializePlugin(plugin):

    vendor = "Andrew Hideo Boyles"
    version = "1.0.0"

    plugin_fn = om.MFnPlugin(plugin, vendor, version)

    try:
        plugin_fn.registerContextCommand(SimpleContextCmd.COMMAND_NAME, SimpleContextCmd.creator)
    except:
        om.MGlobal.displayError("Failed to register context command: {0}".format(SimpleContextCmd.COMMAND_NAME))

    

def uninitializePlugin(plugin):
    """
    """
    plugin_fn = om.MFnPlugin(plugin)

    try:
        plugin_fn.deregisterContextCommand(SimpleContextCmd.COMMAND_NAME)
    except:
        om.MGlobal.displayError("Failed to deregister context command: {0}".format(SimpleContextCmd.COMMAND_NAME))


if __name__ == "__main__":
    cmds.file(new=True, force=True)

    # Reload the plugin
    plugin_name = "simple_context.py"
    cmds.evalDeferred('if cmds.pluginInfo("{0}", q=True, loaded=True): cmds.unloadPlugin("{0}")'.format(plugin_name))
    cmds.evalDeferred('if not cmds.pluginInfo("{0}", q=True, loaded=True): cmds.loadPlugin("{0}")'.format(plugin_name))

    cmds.evalDeferred('context = cmds.czSimpleCtx(); cmds.setToolTo(context)')
