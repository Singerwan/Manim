from manim import *

class pangofont(Scene):
    def construct(self):
        fon=Text("ManimPango font family",color=PURE_GREEN)
        
        tx1=Text("AMGDT",font='AMGDT')
        tx2=Text("Vivaldi",font='Vivaldi')
        tx3=Text("Txt",font='Txt')
        tx4=Text("Times New Roman",font='Times New Roman')
        tx5=Text("Cooper",font='Cooper')
        tx6=Text("Forte",font='Forte')
        tx7=Text("Cursive",font='Cursive')
        tx8=Text("DengXian",font='DengXian')
        tx9=Text("GreekC",font='GreekC')
        ts1=Text("Elephant",font='Elephant')
        ts2=Text("仿宋字体",font='FangSong')
        ts3=Text("Arial",font='Arial')
        
        self.play(Write(fon),run_time=2)
        self.play(FadeOut(fon),run_time=2)       
        
        self.play(Write(tx1),run_time=2)
        self.play(FadeOut(tx1),run_time=2)
        
        self.play(Write(tx2),run_time=2)
        self.play(FadeOut(tx2),run_time=2)
        
        self.play(Write(tx3),run_time=2)
        self.play(FadeOut(tx3),run_time=2)
        
        self.play(Write(tx4),run_time=2)
        self.play(FadeOut(tx4),run_time=2)
        
        self.play(Write(tx5),run_time=2)
        self.play(FadeOut(tx5),run_time=2)
        
        self.play(Write(tx6),run_time=2)
        self.play(FadeOut(tx6),run_time=2)
        
        self.play(Write(tx7),run_time=2)
        self.play(FadeOut(tx7),run_time=2)
        
        self.play(Write(tx8),run_time=2)
        self.play(FadeOut(tx8),run_time=2)
        
        self.play(Write(tx9),run_time=2)
        self.play(FadeOut(tx9),run_time=2)
        
        self.play(Write(ts1),run_time=2)
        self.play(FadeOut(ts1),run_time=2)
        
        self.play(Write(ts2),run_time=2)
        self.play(FadeOut(ts2),run_time=2)
        
        self.play(Write(ts3),run_time=2)
        self.play(FadeOut(ts3),run_time=2)
        

        
        tx11=Text("Jokerman",font='Jokerman')
        tx12=Text("Gabriola",font='Gabriola')
        tx13=Text("Harrington",font='Harrington')
        tx14=Text("GDT",font="GDT")
        tx15=Text("GothicG",font='GothicG')
        tx16=Text("Dubai",font='Dubai')
        tx17=Text("Complex",font='Complex')
        tx18=Text("Britannic",font='Britannic')
        tx19=Text("Constantia",font='Constantia')
        ts11=Text("Corbel",font='Corbel')
        ts12=Text("Chiller",font='Chiller')
        ts13=Text("Broadway",font='Broadway')
        

        self.play(Write(tx11),run_time=2)
        self.play(FadeOut(tx11),run_time=2)
        
        self.play(Write(tx12),run_time=2)
        self.play(FadeOut(tx12),run_time=2)
        
        self.play(Write(tx13),run_time=2)
        self.play(FadeOut(tx13),run_time=2)
        
        self.play(Write(tx14),run_time=2)
        self.play(FadeOut(tx14),run_time=2)
        
        self.play(Write(tx15),run_time=2)
        self.play(FadeOut(tx5),run_time=2)
        
        self.play(Write(tx16),run_time=2)
        self.play(FadeOut(tx16),run_time=2)
        
        self.play(Write(tx17),run_time=2)
        self.play(FadeOut(tx17),run_time=2)
        
        self.play(Write(tx18),run_time=2)
        self.play(FadeOut(tx18),run_time=2)
        
        self.play(Write(tx19),run_time=2)
        self.play(FadeOut(tx19),run_time=2)
        
        self.play(Write(ts11),run_time=2)
        self.play(FadeOut(ts11),run_time=2)
        
        self.play(Write(ts12),run_time=2)
        self.play(FadeOut(ts12),run_time=2)
        
        self.play(Write(ts13),run_time=2)
        self.play(FadeOut(ts13),run_time=2)