from manim import *

class pangofontsta(Scene):
    def construct(self):
        
        tx1=Text("AMGDT",font='AMGDT',color=LOGO_WHITE).scale(0.25).move_to([-6.5,3,0])
        tx2=Text("Vivaldi",font='Vivaldi',color=LOGO_WHITE).scale(0.25).move_to([-5.5,3,0])
        tx3=Text("Txt",font='Txt',color=LOGO_WHITE).scale(0.25).move_to([-4.5,3,0])
        tx4=Text("Times_NR",font='GREEN_A',color=LOGO_WHITE).scale(0.25).move_to([-2.5,3,0])
        tx5=Text("Cooper",font='Cooper',color=LOGO_WHITE).scale(0.25).move_to([-1.5,3,0])
        tx6=Text("Forte",font='Forte',color=LOGO_WHITE).scale(0.25).move_to([-0.5,3,0])
        self.add(tx1,tx2,tx3,tx4,tx5,tx6)   
        
# needs to update 
        tx7=Text("Goudy",font='Goudy Old Style',color=PURE_RED).scale(0.25).move_to([-6.5,2,0])
        tx8=Text("ArialMT",font='Arial Rounded MT',color=RED_A).scale(0.25).move_to([-5.5,2,0])
        tx9=Text("ArialMS'",font='Arial Unicode MS',color=RED_B).scale(0.25).move_to([-4,2,0])
        ts1=Text("ArtifaktE",font='Artifakt Element',color=RED_C).scale(0.25).move_to([-3,2,0])
        ts2=Text("ArtifaktEA",font='Artifakt Element Hair',color=RED_D).scale(0.25).move_to([-1.5,2,0])
        ts3=Text("Bahnschrift",font='Bahnschrift',color=RED_E).scale(0.25).move_to([-0.5,2,0])
        self.add(tx7,tx8,tx9,ts1,ts2,ts3)                        
#----------------------------        
        tx7=Text("BankGotLBT",font='BankGothic Lt BT',color=PURE_GREEN).scale(0.25).move_to([-6.5,1,0])
        tx8=Text("BankGotMd",font='BankGothic Md BT',color=GREEN_A).scale(0.25).move_to([-5.5,1,0])
        tx9=Text("Basker",font='Baskerville Old Face',color=GREEN_B).scale(0.25).move_to([-4,1,0])
        ts1=Text("Bauhaus",font='Bauhaus 93',color=GREEN_C).scale(0.25).move_to([-3,1,0])
        ts2=Text("Bell",font='Bell MT',color=GREEN_D).scale(0.25).move_to([-1.5,1,0])
        ts3=Text("Berlin",font='Berlin Sans FB',color=GREEN_E).scale(0.25).move_to([-0.5,1,0])
        
        self.add(tx7,tx8,tx9,ts1,ts2,ts3)

        tx11=Text("'Bernard",font='Bernard MT',color=PURE_BLUE).scale(0.25).move_to([-6.5,-1,0])
        tx12=Text("Blackadder",font='Blackadder ITC',color=BLUE_A).scale(0.25).move_to([-5,-1,0])
        tx13=Text("Bodoni",font='Bodoni MT',color=BLUE_B).scale(0.25).move_to([-4,-1,0])
        tx14=Text("BookAn",font="Book Antiqua",color=BLUE_C).scale(0.25).move_to([-2,-1,0])
        tx15=Text("GothicG",font='GothicG',color=BLUE_D).scale(0.25).move_to([-1,-1,0])
        tx16=Text("Bodoni",font='Bodoni MT Poster',color=BLUE_E).scale(0.25).move_to([0,-1,0])
        
        self.add(tx11,tx12,tx13,tx14,tx15,tx16)
# update is needed
        tx11=Text("Bookman",font='Bookman Old Style',color=PURE_CYAN).scale(0.25).move_to([-6.5,-2,0])
        tx12=Text("Bradley",font='Bradley Hand ITC',color=TEAL_A).scale(0.25).move_to([-5,-2,0])
        tx13=Text("Brush",font='Brush Script MT',color=TEAL_B).scale(0.25).move_to([-4,-2,0])
        tx14=Text("Calibri",font="Calibri",color=TEAL_C).scale(0.25).move_to([-2,-2,0])
        tx15=Text("Californ",font='Californian FB',color=TEAL_D).scale(0.25).move_to([-1,-2,0])
        tx16=Text("'Calisto",font='Calisto MT',color=TEAL_E).scale(0.25).move_to([0,-2,0])
        
        self.add(tx11,tx12,tx13,tx14,tx15,tx16)
#----------------------------               
        tx17=Text("Cambria",font='Cambria',color=PURE_MAGENTA).scale(0.25).move_to([-6.5,-3,0])
        tx18=Text("CambrMa",font='Cambria Math',color=MAROON_A).scale(0.25).move_to([-5,-3,0])
        tx19=Text("Constantia",font='Constantia',color=MAROON_B).scale(0.25).move_to([-3.5,-3,0])
        ts11=Text("Candara",font='Candara',color=MAROON_C).scale(0.25).move_to([-2.5,-3,0])
        ts12=Text("Cascadia",font='Cascadia Code',color=MAROON_D).scale(0.25).move_to([-1.5,-3,0])
        ts13=Text("CasMono",font='Cascadia Mono',color=MAROON_E).scale(0.25).move_to([0,-3,0])
        self.add(tx17,tx18,tx19,ts11,ts12,ts13)        
#----------------------------    update is needed    
        tx07=Text("Castellar",font='Castellar',color=PURE_YELLOW).scale(0.25).move_to([-6.5,0,0])
        tx08=Text("Centaur",font='Centaur',color=YELLOW_A).scale(0.25).move_to([-5,0,0])
        tx09=Text("Century",font='Century',color=YELLOW_B).scale(0.25).move_to([-3.5,0,0])
        ts01=Text("Centuryg",font='Century Gothic',color=YELLOW_C).scale(0.25).move_to([-2.5,0,0])
        ts02=Text("Centurys",font='Century Schoolbook',color=YELLOW_D).scale(0.25).move_to([-1.5,0,0])
        ts03=Text("Chiller",font='Chiller',color=YELLOW_E).scale(0.25).move_to([0,0,0])
        self.add(tx07,tx08,tx09,ts01,ts02,ts03)        

        tx10=Text("ColonMT",font='Colonna MT',color=BLUE_A).scale(0.25).move_to([6.5,0,0])
        tx20=Text("Comic",font='Comic Sans MS',color=BLUE_B).scale(0.25).move_to([5.5,0,0])
        tx30=Text("CommerBT",font='CommercialScript BT',color=BLUE_C).scale(0.25).move_to([4.5,0,0])
        tx40=Text("Consolas",font='Consolas',color=BLUE_E).scale(0.25).move_to([2.5,0,0])
        tx50=Text("Constantia",font='CooConstantiaper',color=BLUE_A).scale(0.25).move_to([1.5,0,0])
        tx60=Text("Corbel",font='Corbel',color=BLUE_C).scale(0.25).move_to([0.5,0,0])
        
        self.add(tx10,tx20,tx30,tx40,tx50,tx60)       
#----------------------------    update is needed   

# right portion #####################################----------------------------        
        tx1r=Text("AMGDT",font='AMGDT',color=GOLD_A).scale(0.25).move_to([6.5,3,0])
        tx2r=Text("Vivaldi",font='Vivaldi',color=GOLD_A).scale(0.25).move_to([5.5,3,0])
        tx3r=Text("Txt",font='Txt',color=GOLD_A).scale(0.25).move_to([4.5,3,0])
        tx4r=Text("Times_NR",font='Times_NR',color=GOLD_A).scale(0.25).move_to([2.5,3,0])
        tx5r=Text("Cooper",font='Cooper',color=GOLD_A).scale(0.25).move_to([1.5,3,0])
        tx6r=Text("Forte",font='Forte',color=GOLD_A).scale(0.25).move_to([0.5,3,0])
        
        self.add(tx1r,tx2r,tx3r,tx4r,tx5r,tx6r)
# needs to update 
        tx7r=Text("CoGothic",font='Copperplate Gothic',color=GREEN_A).scale(0.25).move_to([6.5,2,0])
        tx8r=Text("CourNew",font='Courier New',color=GREEN_A).scale(0.25).move_to([5.5,2,0])
        tx9r=Text("GreekC",font='GreekC',color=GREEN_A).scale(0.25).move_to([4,2,0])
        ts1r=Text("CurlMT",font='Curlz MT',color=GREEN_A).scale(0.25).move_to([3,2,0])
        ts2r=Text("Dutch",font='Dutch801 Rm BT',color=GREEN_A).scale(0.25).move_to([1.5,2,0])
        ts3r=Text("EngrMT",font='Engravers MT',color=GREEN_A).scale(0.25).move_to([0.5,2,0])
        self.add(tx7r,tx8r,tx9r,ts1r,ts2r,ts3r)                

        tx7r=Text("Cursive",font='Cursive',color=GREY_A).scale(0.25).move_to([6.5,1,0])
        tx8r=Text("DengXian",font='DengXian',color=GREY_A).scale(0.25).move_to([5.5,1,0])
        tx9r=Text("GreekC",font='GreekC',color=GREY_A).scale(0.25).move_to([4,1,0])
        ts1r=Text("Elephant",font='Elephant',color=GREY_A).scale(0.25).move_to([3,1,0])
        ts2r=Text("FangSong",font='FangSong',color=GREY_A).scale(0.25).move_to([1.5,1,0])
        ts3r=Text("Arial",font='Arial',color=GREY_A).scale(0.25).move_to([0.5,1,0])
        
        self.add(tx7r,tx8r,tx9r,ts1r,ts2r,ts3r)

        tx11r=Text("Jokerman",font='Jokerman',color=TEAL_A).scale(0.25).move_to([6.5,-1,0])
        tx12r=Text("Gabriola",font='Gabriola',color=TEAL_A).scale(0.25).move_to([5,-1,0])
        tx13r=Text("Harrington",font='Harrington',color=TEAL_A).scale(0.25).move_to([4,-1,0])
        tx14r=Text("GDT",font="GDT",color=TEAL_A).scale(0.25).move_to([2,-1,0])
        tx15r=Text("GothicG",font='GothicG',color=TEAL_A).scale(0.25).move_to([1,-1,0])
        
        self.add(tx11r,tx12r,tx13r,tx14r,tx15r)
# update is needed
        tx11r=Text("Jokerman",font='Jokerman',color=MAROON_A).scale(0.25).move_to([6.5,-2,0])
        tx12r=Text("Gabriola",font='Gabriola',color=MAROON_A).scale(0.25).move_to([5,-2,0])
        tx13r=Text("Harrington",font='Harrington',color=MAROON_A).scale(0.25).move_to([4,-2,0])
        tx14r=Text("GDT",font="GDT",color=MAROON_A).scale(0.25).move_to([2,-2,0])
        tx15r=Text("GothicG",font='GothicG',color=MAROON_A).scale(0.25).move_to([1,-2,0])
        self.add(tx11r,tx12r,tx13r,tx14r,tx15r)
        
        tx17r=Text("Complex",font='Complex',color=GREEN_A).scale(0.25).move_to([6.5,-3,0])
        tx18r=Text("Britannic",font='Britannic',color=GREEN_A).scale(0.25).move_to([5,-3,0])
        tx19r=Text("Constantia",font='Constantia',color=GREEN_A).scale(0.25).move_to([3.5,-3,0])
        ts11r=Text("Corbel",font='Corbel',color=GREEN_A).scale(0.25).move_to([2.5,-3,0])
        ts12r=Text("Chiller",font='Chiller',color=GREEN_A).scale(0.25).move_to([1.5,-3,0])
        self.add(tx17r,tx18r,tx19r,ts11r,ts12r)        
