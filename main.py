from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from datetime import datetime
from kivy.uix.camera import Camera 

KV = '''
CustomScreenManager:
    HomeScreen:
    NameScreen:
    CheckScreen:
    

<HomeScreen>:
    name: 'home'
    
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1  # White color
        Rectangle:
            size: self.size
            pos: self.pos
    
    MDTopAppBar:
        type: "small"
        size_hint_x: 1
        pos_hint: {"top": 1}
        MDTopAppBarTitle:
            text: "QuickMark"
            theme_text_color: "Custom"
            text_color: .5, 0, .5, 1
        MDTopAppBarTrailingButtonContainer:
            MDIconButton:
                icon: "plus-circle"
                pos_hint: {"center_y": 0.5}
                theme_font_size: "Custom"
                font_size: "40sp"
                radius: [self.height / 2,]
                size_hint: None, None
                size: "84dp", "84dp"
                on_press: root.manager.current = 'name' 


<NameScreen>:
    name: 'name'

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1  # White color
        Rectangle:
            size: self.size
            pos: self.pos

    MDLabel:
        id: display_label
        text: ""
        halign: "center"
        pos_hint: {"top": 1.33}
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1

    MDTopAppBar:
        type: "small"
        size_hint_x: 1
        pos_hint: {"top": 1}
        
        MDTopAppBarTitle:
            text: "QuickMark"
            theme_text_color: "Custom"
            text_color: .5, 0, .5, 1
    
    MDTextField:
        id: text_field
        mode: "outlined"
        size_hint_x: None
        width: "240dp"
        pos_hint: {"top":.879, "center_x": .5}
        on_text_validate: app.update_label(self)

        MDTextFieldHintText:
            text: "Name of test"

        MDTextFieldTrailingIcon:
            icon: "content-save"

    MDButton:
        style: "text"
        pos_hint: {'x': .7, 'y': .8}
        on_press: app.save_and_display_text()

        MDButtonText:
            text: "SAVE"
    
    MDDivider:
        size_hint_x: .5
        pos_hint: {"top":.76, "center_x": .5}

    MDLabel:
        id: buttons
        text:"Appraisal"
        halign: "center"
        pos_hint: {"center_y":.7}

    MDButton:
        style: "outlined"
        pos_hint: {"top":.65, "center_x": .5}
        on_press: root.manager.current = 'check'
        MDButtonText:
            text: "CHECK SHEETS"   

    MDButton:
        style: "outlined"
        pos_hint: {"top":.55, "center_x": .5}
        MDButtonText:
            text: "ANALYSIS"        

    MDDivider:
        size_hint_x: .5
        pos_hint: {"top":.45, "center_x": .5}

    MDLabel:
        id: buttons
        text:"Edit Answer Key"
        halign: "center"
        pos_hint: {"center_y":.4}

    MDButton:
        style: "outlined"
        pos_hint: {"top":.35, "center_x": .5}
        MDButtonText:
            text: "MULTIPLE CHOICE"

    MDButton:
        style: "outlined"
        pos_hint: {"top":.25, "center_x": .5}
        MDButtonText:
            text: "TRUE OR FALSE"

    MDButton:
        style: "outlined"
        pos_hint: {"top":.15, "center_x": .5}
        MDButtonText:
            text: "IDENTIFICATION"

<CheckScreen>:
    name: 'check'

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1  # White color
        Rectangle:
            size: self.size
            pos: self.pos

    MDTopAppBar:
        type: "small"
        size_hint_x: 1
        pos_hint: {"top": 1}
        
        MDTopAppBarTitle:
            text: "QuickMark"
            theme_text_color: "Custom"
            text_color: .5, 0, .5, 1

    MDIconButton:
        id: camera_icon
        icon: "camera-outline"
        style: "standard"
        theme_font_size: "Custom"
        font_size: "48sp"
        radius: [self.height / 2, ]
        size_hint: None, None
        size: "84dp", "84dp"
        pos_hint: {"top":.2, "center_x": .5}

    MDIconButton:
        id: camera_icon
        icon: "arrow-left"
        style: "standard"
        pos_hint: {"top":.07, "center_x": .5}
        on_press: root.manager.current = 'name'
'''

class CustomScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = NoTransition()

class HomeScreen(Screen):
    pass

class NameScreen(Screen):
    pass

class CheckScreen(Screen):
    pass

class App(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Purple"
        screen = Builder.load_string(KV)
        return screen
    
    # Pressing enter will get the text input then display. Make the text field vanish
    def update_label(self, instance):
        text_input = instance.text
        display_label = self.root.get_screen('name').ids.display_label
        current_date = datetime.now().strftime('%Y-%m-%d')
        display_label.text = f"{text_input}\n{current_date}"
        text_field = self.root.get_screen('name').ids.text_field
        self.root.get_screen('name').remove_widget(text_field)

    # Pressing save same function sa babaw
    def save_and_display_text(self):
        text_input = self.root.get_screen('name').ids.text_field.text
        self.update_label(self.root.get_screen('name').ids.text_field)

App().run()

