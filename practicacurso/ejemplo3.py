from kivy.app import App

from kivy.uix.camera import Camera

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button
import time

class CameraExample(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Create a camera object

        self.cameraObject = Camera(play=False)

        self.cameraObject.play = True

        self.cameraObject.resolution = (800, 500)  # Specify the resolution

        # Create a button for taking photograph

        self.camaraClick = Button(text="Take Photo", background_color=(0,0,255,255))

        self.camaraClick.size_hint = (.5, .2)

        self.camaraClick.pos_hint = {'x': .25, 'y': .75}

        # bind the button's on_press to onCameraClick

        self.camaraClick.bind(on_press=self.onCameraClick)

        # add camera and button to the layout

        layout.add_widget(self.cameraObject)

        layout.add_widget(self.camaraClick)

        # return the root widget

        return layout

    # Take the current frame of the video as the photo graph

    def onCameraClick(self, *args):
        timestr = time.strftime("%Y%m%d_%H%M%S")
        self.cameraObject.export_to_png("inumero.jpg".format(timestr))
# Start the Camera App

if __name__ == '__main__':
    CameraExample().run()