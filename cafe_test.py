
from kivy.config import Config
Config.set("graphics", "fullscreen", "0") #1 フル画面　0　フォームサイズ
Config.set("graphics", "resizable", "1")
Config.set("graphics", "width", "1000")
Config.set("graphics", "height", "460")

from kivy.core.window import Window
#Window.clearcolor = (0.8, 0.8, 0) 背景を黄色にできる

from kivy.lang import Builder
Builder.load_file("hiiro_kivy3.kv")


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.carousel import Carousel
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty, ListProperty
#from kivy.uix.listview import ListItemButton
#from kivy.uix.screenmanager import ScreenManager,Screen
import japanize_kivy
import sqlite3
from contextlib import closing




class DBlite():
    def __init__(self):
        sex = None
        year = None
        drink = None
        food = None
        take = '''NULL'''
        dbname = '店名.db'
        try:
            with closing(sqlite3.connect(dbname)) as con:
                cur = con.cursor()

        # テーブル作成のクエリ
                create_table_query = '''
CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY AUTOINCREMENT,日時 created TIMESTAMP DEFAULT (datetime(CURRENT_TIMESTAMP,"weekday N", "localtime"), 性別 char(1),年代 INTEGER,ドリンク char(10),食べ物 TEXT, TAKE char(10));
'''

                cur.execute(create_table_query) # テーブル作成
                con.commit() # 変更を保存
    
        except sqlite3.Error as e:
            None

    def clear(self):
        self.sex = None
        self.year = None
        self.drink = None
        self.food = None
        self.take = '''NULL'''

    def sqsend(self):
        dbname = '店名.db'
        sqlist = (self.sex, self.year, self.drink, self.food)
        with closing(sqlite3.connect(dbname)) as con:            
            cur = con.cursor()
            cur.execute("INSERT INTO my_table(id,日時, 性別, 年代, ドリンク, 食べ物, TAKE) values(NULL,NULL,?,?,?,?,?)",sqlist)
            con.commit()
        self.clear()
        sqlist = ()
#f"INSERT INTO my_table(性別, 年代, ドリンク, 食べ物) values('{self.sex}', {self.year}, {self.drink}, {self.food})"



db = DBlite()
class ChageMenuForm(BoxLayout):    #メニュー変更画面の情報

    menulist = ListProperty(["","",""])
class ShukeiCsv(BoxLayout):
    pass


class ChageMenu():
    def food_change(self, name, money):
        pass
    

class MyForm(Widget):
    sextext = StringProperty("")
    yeartext = StringProperty("")
    drinktext = StringProperty("")
    foodtext = StringProperty("")
    taketext = StringProperty("")
    
    def on_men(self, **kwargs):
        self.sextext = "男"
        db.sex = "男"
    def on_women(self, **kwargs):
        self.sextext = "女"
        db.sex = "女"
    
    def on_10s(self, **kwargs):
        self.yeartext = "10代"
        db.year = 10
    def on_20s(self, **kwargs):
        self.yeartext = "20代"
        db.year = 20
    def on_30s(self, **kwargs):
        self.yeartext = "30代"
        db.year = 30
    def on_40s(self, **kwargs):
        self.yeartext = "40代"
        db.year = 40
    def on_50s(self, **kwargs):
        self.yeartext = "50代"
        db.year = 50
    def on_60s(self, **kwargs):
        self.yeartext = "60代"
        db.year = 60

    def on_menu_1(self, **kwargs):
        db.drink = self.menu_1_t
        self.drinktext = self.menu_1_t
    def on_menu_2(self, **kwargs):
        db.drink = self.menu_2_t
        self.drinktext = self.menu_2_t

    def on_chage_menu(self,**kwargs):
        pass
        
    def on_take(self, **kwargs):
        db.take = "take"
        self.taketext = "take"
    def on_send(self, **kwargs):
        db.sqsend()
        self.sextext = ""
        self.yeartext = ""
        self.drinktext = ""
        self.foodtext = ""
    def on_clear(self, **kwargs):
        db.clear()
        self.sextext = ""
        self.yeartext = ""
        self.drinktext = ""
        self.foodtext = ""
        self.taketext = '''NULL'''
        


        
class MainApp(App):

    def build(self):
        self.title = "販売集計"
        DBlite()
        return MyForm()
    



if __name__ == "__main__":
    MainApp().run()

