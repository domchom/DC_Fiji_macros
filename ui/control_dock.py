from ij import IJ, WindowManager
from ij.plugin.frame import RoiManager
from java.awt import Frame, Panel, GridLayout

def get_or_create(cmd, title):
    win = WindowManager.getFrame(title)
    if win is None:
        IJ.run(cmd)
        win = WindowManager.getFrame(title)
    return win

def build_dock():
    bc = get_or_create("Brightness/Contrast...", "B&C")
    ch = get_or_create("Channels Tool...", "Channels")
    rm = RoiManager.getRoiManager()

    dock = Frame("Control Dock")
    dock.setLayout(GridLayout(3, 1))

    for win in (bc, ch, rm):
        win.setVisible(False)
        panel = Panel()
        for c in list(win.getComponents()):
            win.remove(c)
            panel.add(c)
        dock.add(panel)

    dock.pack()
    dock.setLocation(0, 0)
    dock.setVisible(True)

build_dock()