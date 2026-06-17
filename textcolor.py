from manim import *

class textcolor(Scene):
    def construct(self):
        cr=Ellipse(height=6,width=12,color=PURE_GREEN,stroke_width=15)
        self.play(Create(cr),run_time=3)
        
        line=Line(start=np.array([-6., 0., 0.]), end=np.array([6., 0., 0.]),color=BLUE)
        self.play(Create(line))
        
        crr1=Circle(0.7,color=MAROON,fill_opacity=1).move_to(RIGHT*0.15)
        self.play(Create(crr1),run_time=2)
        

        
        carpe =Text("carpe", t2c={'[1:-1]':BLUE}).scale(1.5).move_to(LEFT*2+DOWN*0.75)
        díem=Text("díem",t2c={'[1:-1]':RED}).scale(1.5).move_to(RIGHT*2+DOWN*0.75)
        
        inde1=Text("01234",t2c={'[1:-1]':BLUE}).scale(1.5).next_to(carpe ,UP*1.7)
        inde2=Text("0123",t2c={'[1:-1]':RED}).scale(1.5).next_to(díem,UP*1.7)   
        
        self.play(Write(carpe ),run_time=3)
        self.play(Write(inde1),run_time=3)        
        self.play(Write(díem),run_time=3)     
        self.play(Write(inde2),run_time=3)        
        
        for i in range(len(carpe )):
            self.play(Circumscribe(carpe [i]),run_time=0.5,color=TEAL)
            self.play(Circumscribe(inde1[i]),run_time=0.5,color=TEAL)
            
        for i in range(len(díem)):    
            self.play(Circumscribe(díem[i]),run_time=0.5,color=YELLOW)
            self.play(Circumscribe(inde2[i]),run_time=0.5,color=YELLOW)
            
        for i in range(len(carpe )):
            self.play(Indicate(carpe [i]),run_time=0.5,scale_factor=0.8,color=GREEN)
            self.play(Indicate(inde1[i]),run_time=0.5,scale_factor=0.8,color=GREEN)
            
        for i in range(len(díem)):    
            self.play(Indicate(díem[i]),run_time=0.5,scale_factor=0.8,color=PINK)
            self.play(Indicate(inde2[i]),run_time=0.5,scale_factor=1.2,color=PINK)
            
        self.wait(3)
        
        self.play(Flash(crr1, line_length=1,
                        num_lines=30, color=YELLOW_C,flash_radius=0.7+SMALL_BUFF,
                        time_width=1, run_time=5,rate_func = rush_from))    
        