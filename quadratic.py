from manim import *

class quadratic1(Scene):
    def construct(self):
        
        tab0 = MathTable(
            [   ["x", "y"],
                [-2, 2 ],             
                [-1, 2 ],
                [0, 2 ],             
                [1, 2],
                [2, 2]], include_outer_lines=True)
        
        tab0.get_horizontal_lines()[:3].set_color(BLUE_E)
        tab0.get_vertical_lines()[:3].set_color(BLUE_E)
        tab0.get_horizontal_lines()[:3].set_z_index(1)
        tab0.add_highlighted_cell((4,1), color=PURE_RED)
        tab0.add_highlighted_cell((4,2), color=PURE_GREEN)
        self.play(tab0.animate.scale(0.36).move_to(LEFT*6+UP*2.5))


        ax0 = Axes(x_range=[-5, 5, 1],
            y_range=[0, 4, 1],
            tips=True,axis_config={"include_numbers": True})
        
        self.play(Create(ax0),run_time=2)
        t0=MathTex(r"y=constant",color=BLUE_D).move_to(RIGHT*2+UP*1.5)
        self.play(Write(t0))
        xc = ax0.plot(lambda x: 2, color=BLUE_C)
        self.play(Create(xc),run_time=4)     
        lines0 = ax0.get_vertical_lines_to_graph(
        xc, x_range=[-2, 2], num_lines=30, color=BLUE
        )
        self.play(Create(lines0),run_time=3)
        area0 = ax0.get_area(
            xc,
            x_range=(-2,2),
            color=(YELLOW, LOGO_WHITE),
            opacity=1,
        )
        
        self.play(FadeIn(area0),run_time=3)
        self.play(FadeOut(xc),FadeOut(lines0),FadeOut(area0),FadeOut(ax0),FadeOut(t0),FadeOut(tab0))        

        
        tab1 = MathTable(
            [   ["x", "y"],
                [-2, -2 ],             
                [-1, -1 ],
                [0, 0 ],             
                [1, 1],
                [2, 2]], include_outer_lines=True)
        
        tab1.get_horizontal_lines()[:3].set_color(DARKER_GRAY)
        tab1.get_vertical_lines()[:3].set_color(DARKER_GREY)
        tab1.get_horizontal_lines()[:3].set_z_index(1)
        tab1.add_highlighted_cell((4,1), color=YELLOW)
        tab1.add_highlighted_cell((4,2), color=GREEN)
        self.play(tab1.animate.scale(0.36).move_to(LEFT*6+UP*2.5))
        ax1 = Axes(x_range=[-5, 5, 1],
            y_range=[-4, 4, 1],
            tips=True,axis_config={"include_numbers": True})    
        self.play(Create(ax1),run_time=2)      
        t1=MathTex(r"y=x",color=DARK_GREY).move_to(RIGHT*2+DOWN*1.5)
        self.play(Write(t1))              
        yx = ax1.plot(lambda x: x, color=DARK_BROWN)
        self.play(Create(yx),run_time=4)    
        lines1 = ax1.get_vertical_lines_to_graph(
        yx, x_range=[-2, 2], num_lines=30, color=PURE_RED
        )
        self.play(Create(lines1),run_time=3)
        area1 = ax1.get_area(
            yx,
            x_range=(-2,2),
            color=(GREEN, GOLD_A),
            opacity=1,
        )
        
        self.play(FadeIn(area1),run_time=3) 
        self.play(  FadeOut(yx),FadeOut(ax1),FadeOut(t1),
                    FadeOut(tab1),FadeOut(lines1),FadeOut(area1))        


        tab2 = MathTable(
            [   ["x", "y"],
                [-2.333, -2 ],             
                [-1.122, -1 ],
                [0, 0 ],             
                [1.321, 1],
                [2.112, 2]], include_outer_lines=True)
        
        tab2.get_horizontal_lines()[:3].set_color(GOLD_A)
        tab2.get_vertical_lines()[:3].set_color(GOLD_B)
        tab2.get_horizontal_lines()[:3].set_z_index(1)
        tab2.add_highlighted_cell((4,1), color=YELLOW)
        tab2.add_highlighted_cell((4,2), color=GREEN)
        self.play(tab2.animate.scale(0.36).move_to(LEFT*6+UP*2.5)) 
        ax11 = Axes(x_range=[-6, 6, 1],
            y_range=[-6, 6 ,1],
            tips=True,axis_config={"include_numbers": True})    
        self.play(Create(ax11),run_time=2)      
        t11=MathTex(r"y=np.floor(x)",color=GOLD_E).move_to(RIGHT*2+DOWN*1.5)
        self.play(Write(t11))    
        xinput=  (np.linspace(-5,5,600))         
        yx2 = ax11.plot(lambda xinput: np.floor(xinput), color=GOLD_D)
        self.play(Create(yx2),run_time=4)    
        lines2 = ax11.get_vertical_lines_to_graph(
        yx2, x_range=[-2, 2], num_lines=30, color=YELLOW
        )
        self.play(Create(lines2),run_time=3)
        area2 = ax11.get_area(
            yx2,
            x_range=(-2,2),
            color=(TEAL_C, PURPLE),
            opacity=1,
        )
        
        self.play(FadeIn(area2),run_time=3)  
        self.play(FadeOut(yx2),FadeOut(ax11),
                  FadeOut(t11),FadeOut(tab2),
                  FadeOut(lines2),FadeOut(area2))      
        
        tab21 = MathTable(
            [   ["x", "y"],
                [-2, 4 ],             
                [-1, 1 ],
                [0, 0 ],             
                [1, 1],
                [2, 4]], include_outer_lines=True)
        
        tab21.get_horizontal_lines()[:3].set_color(GREEN_A)
        tab21.get_vertical_lines()[:3].set_color(GREEN_B)
        tab21.get_horizontal_lines()[:3].set_z_index(1)
        tab21.add_highlighted_cell((4,1), color=YELLOW)
        tab21.add_highlighted_cell((4,2), color=GREEN)
        self.play(tab21.animate.scale(0.36).move_to(LEFT*6+UP*2.5))               
        ax2 = Axes(x_range=[-5, 5, 1],
            y_range=[-2, 4, 1],
            tips=True,axis_config={"include_numbers": True})      
        self.play(Create(ax2),run_time=2)        
        t2=MathTex(r"x^2",color=GREEN_C).move_to(RIGHT*4)
        self.play(Write(t2))
        xsq2 = ax2.plot(lambda x: x**2, color=GREEN_E)
        self.play(Create(xsq2),run_time=4)

        label1 = ax1.get_graph_label(
                        graph=xsq2,
                        label= MathTex(r"x=0"),
                        x_val=0,
                        dot=True,
                        direction=DOWN,color=LOGO_WHITE
        )        
        self.play(Create(label1),run_time=2)        
        lines3 = ax2.get_vertical_lines_to_graph(
        xsq2, x_range=[-2, 2], num_lines=30, color=TEAL_E
        )
        self.play(Create(lines3),run_time=3)
        area3 = ax2.get_area(
            xsq2,
            x_range=(-2,2),
            color=(RED_A, WHITE),
            opacity=1,
        )
        
        self.play(FadeIn(area3),run_time=3)          
        self.play(FadeOut(xsq2),FadeOut(ax2),
                  FadeOut(label1),FadeOut(t2),
                  FadeOut(tab21),FadeOut(lines3),
                  FadeOut(area3))


        tab22 = MathTable(
            [   ["x", "y"],
                [-2, -4 ],             
                [-1, -1 ],
                [0, 0 ],             
                [1, -1],
                [2, -4]], include_outer_lines=True)
        
        tab22.get_horizontal_lines()[:3].set_color(LIGHT_GRAY)
        tab22.get_vertical_lines()[:3].set_color(LIGHT_PINK)
        tab22.get_horizontal_lines()[:3].set_z_index(1)
        tab22.add_highlighted_cell((4,1), color=YELLOW)
        tab22.add_highlighted_cell((4,2), color=GREEN)
        self.play(tab22.animate.scale(0.36).move_to(LEFT*6))            
        ax2x = Axes(x_range=[-5, 5, 1],
            y_range=[-5, 0, 1],
            tips=True,axis_config={"include_numbers": True})      
        self.play(Create(ax2x),run_time=2) 
        t21=MathTex(r"-x^2",color=MAROON).move_to(LEFT*4)
        self.play(Write(t21))    
        xsq2nx = ax2x.plot(lambda x: -(x**2), color=MAROON_C)
        self.play(Create(xsq2nx),run_time=4)
        position = ax2x.input_to_graph_point(x=0, graph=xsq2nx)
        cir = Circle(radius=0.1, color=PURPLE_E,fill_opacity=1).move_to(position)   
        self.play(Create(cir),run_time=2)        
        lines4 = ax2x.get_vertical_lines_to_graph(
        xsq2nx, x_range=[-2, 2], num_lines=30, color=PURE_MAGENTA)
        self.play(Create(lines4),run_time=3)
        area4 = ax2x.get_area(
            xsq2nx,
            x_range=(-2,2),
            color=(PURE_CYAN, PURPLE_E),
            opacity=1,
        )
        
        self.play(FadeIn(area4),run_time=3)           
        self.play(  FadeOut(xsq2nx),
                    FadeOut(cir),FadeOut(ax2x),
                    FadeOut(t21),FadeOut(tab22),
                    FadeOut(lines4),FadeOut(area4))     

        tab23 = MathTable(
            [   ["x", "y"],
                [-2, 27 ],             
                [-1, 18],
                [0, 11 ],             
                [1, 6],
                [2, 3]], include_outer_lines=True)
        
        tab23.get_horizontal_lines()[:3].set_color(RED_A)
        tab23.get_vertical_lines()[:3].set_color(RED_B)
        tab23.get_horizontal_lines()[:3].set_z_index(1)
        tab23.add_highlighted_cell((4,1), color=YELLOW)
        tab23.add_highlighted_cell((4,2), color=GREEN)
        self.play(tab23.animate.scale(0.36).move_to(LEFT*6+UP*2.5))           
        ax3 = Axes(x_range=[-5, 5, 1],
            y_range=[-1, 6, 1],
            tips=True,axis_config={"include_numbers": True})
        self.play(Create(ax3),run_time=2)     
        t3=MathTex(r"(x-3)^2+2",color=RED_C).move_to(LEFT*5)
        self.play(Write(t3))   
        xsq2xy = ax3.plot(lambda x: (x-3)**2+2, color=RED_E)   
        self.play(Create(xsq2xy),run_time=4)   
        label2 = ax3.get_graph_label(
                        graph=xsq2xy,
                        label= MathTex(r"x=3"),
                        x_val=3,
                        dot=True,
                        direction=DOWN,color=GOLD_D
        )        
        self.play(Create(label2),run_time=2)  
        lines5 = ax3.get_vertical_lines_to_graph(
        xsq2xy, x_range=[-2, 2], num_lines=30, color=LOGO_RED
        )
        self.play(Create(lines5),run_time=3)
        area5 = ax3.get_area(
            xsq2xy,
            x_range=(-2,2),
            color=(MAROON_E, PINK),
            opacity=1,
        )
        
        self.play(FadeIn(area5),run_time=3)    
        self.play(FadeOut(xsq2xy),FadeOut(label2),
                  FadeOut(ax3),FadeOut(t3),
                  FadeOut(tab23),FadeOut(lines5),
                  FadeOut(area5))        
        

        tab24 = MathTable(
            [   ["x", "y"],
                [-2, 3 ],             
                [-1, 0 ],
                [0, -1 ],             
                [1, 0],
                [2, 3]], include_outer_lines=True)
        
        tab24.get_horizontal_lines()[:3].set_color(YELLOW_A)
        tab24.get_vertical_lines()[:3].set_color(YELLOW_A)
        tab24.get_horizontal_lines()[:3].set_z_index(1)
        tab24.add_highlighted_cell((4,1), color=RED)
        tab24.add_highlighted_cell((4,2), color=GREEN)
        self.play(tab24.animate.scale(0.36).move_to(LEFT*6+UP*2.5))         
        ax4 = Axes(x_range=[-5, 5, 1],
            y_range=[-1, 5, 1],
            tips=True,axis_config={"include_numbers": True})
        self.play(Create(ax4),run_time=2)        
        t5=MathTex(r"y=x^2-1",color=YELLOW_E).move_to(RIGHT*4+UP*2.5)
        self.play(Write(t5))       

        xsq2x1x2 = ax4.plot(lambda x: x**2-1, color=YELLOW_D)
        self.play(Create(xsq2x1x2),run_time=4) 
        label42 = ax4.get_graph_label(
                        graph=xsq2x1x2,
                        label= MathTex(r"x=-1"),
                        x_val=-1,
                        dot=True,
                        direction=UP*1.5,color=GOLD_D
        )               
        self.play(Create(label42),run_time=2)  
        label41 = ax4.get_graph_label(
                        graph=xsq2x1x2,
                        label= MathTex(r"x=1"),
                        x_val=1,
                        dot=True,
                        direction=UP*1.5,color=GOLD_A
        )
        lines6 = ax4.get_vertical_lines_to_graph(
        xsq2x1x2, x_range=[-2, 2], num_lines=30, color=DARK_BROWN
        )
        self.play(Create(lines6),run_time=3)
        area6 = ax4.get_area(
            xsq2x1x2,
            x_range=(-2,2),
            color=(GREEN, GREY_BROWN),
            opacity=1,
        )
        
        self.play(FadeIn(area6),run_time=3)  
        self.play(FadeOut(xsq2x1x2),
                    FadeOut(label41),
                    FadeOut(label42),
                    FadeOut(ax4),
                    FadeOut(t5),FadeOut(tab24),
                    FadeOut(lines6),FadeOut(area6))        

        tab261 = MathTable(
            [   ["x", "y"],
                [-2,-8 ],             
                [-1, -1],
                [0, 0],             
                [1, 1],
                [2,8]], include_outer_lines=True)
        
        tab261.get_horizontal_lines()[:3].set_color(GOLD_E)
        tab261.get_vertical_lines()[:3].set_color(RED_A)
        tab261.get_horizontal_lines()[:3].set_z_index(1)
        tab261.add_highlighted_cell((4,1), color=YELLOW)
        tab261.add_highlighted_cell((4,2), color=GREEN)
        self.play(tab261.animate.scale(0.36).move_to(LEFT*6+UP*2.5))      
        t71=MathTex(r"x^3",color=LOGO_WHITE).move_to(RIGHT+UP*2)
        self.play(Write(t71))      
        ax45 = Axes(x_range=[-3, 3, 1],
            y_range=[-9, 9, 1],
            tips=True,axis_config={"include_numbers": True})
        self.play(Create(ax45),run_time=2)        
        xsq2x1x71 = ax45.plot(lambda x: x**7, color=PURE_RED)
        self.play(Create(xsq2x1x71),run_time=4)
        lines7 = ax45.get_vertical_lines_to_graph(
        xsq2x1x71, x_range=[-2, 2], num_lines=30, color=BLUE_A
        )
        self.play(Create(lines7),run_time=3)
        area7 = ax45.get_area(
            xsq2x1x71,
            x_range=(-2,2),
            color=(GOLD, GRAY_E),
            opacity=1,
        )
        
        self.play(FadeIn(area7),run_time=3)  
        self.play(FadeOut(xsq2x1x71),FadeOut(tab261),
                        FadeOut(t71),FadeOut(ax45),
                        FadeOut(lines7),FadeOut(area7))           
        
        tab262 = MathTable(
            [   ["x", "y"],
                [-2,16 ],             
                [-1, 1 ],
                [0, 0 ],             
                [1, 1],
                [2,16]], include_outer_lines=True)
        
        tab262.get_horizontal_lines()[:3].set_color(GOLD_E)
        tab262.get_vertical_lines()[:3].set_color(RED_A)
        tab262.get_horizontal_lines()[:3].set_z_index(1)
        tab262.add_highlighted_cell((4,1), color=YELLOW)
        tab262.add_highlighted_cell((4,2), color=GREEN)
        self.play(tab262.animate.scale(0.36).move_to(LEFT*6+UP*2.5))      
        t72=MathTex(r"x^4",color=RED_D).move_to(RIGHT*2)
        ax454 = Axes(x_range=[-3, 3, 1],
            y_range=[0, 12, 1],
            tips=True,axis_config={"include_numbers": True})
        self.play(Create(ax454),run_time=2)     
        self.play(Write(t72))      
        xsq2x1x72 = ax454.plot(lambda x: x**4, color=PURE_RED)
        self.play(Create(xsq2x1x72),run_time=4)
        lines8 = ax454.get_vertical_lines_to_graph(
        xsq2x1x72, x_range=[-2, 2], num_lines=30, color=DARKER_GRAY
        )
        self.play(Create(lines8),run_time=3)
        area8 = ax454.get_area(
            xsq2x1x72,
            x_range=(-2,2),
            color=(BLACK, BLUE),
            opacity=1,
        )
        
        self.play(FadeIn(area8),run_time=3) 
        self.play(FadeOut(xsq2x1x72),FadeOut(tab262),FadeOut(ax454))                   
        # area = ax.get_area(
        #     xsq2,
        #     x_range=(PI / 2, 3 * PI / 2),
        #     color=(BLUE, LOGO_WHITE),
        #     opacity=1,
        # )
        # self.play(FadeIn(area),run_time=3)
        
        # area1 = ax.get_area(
        #     curve,
        #     x_range=(-2*PI, -PI),
        #     color=(YELLOW, LOGO_WHITE),
        #     opacity=1,
        # )
        
        # self.play(FadeIn(area1),run_time=3)
    
        # label1 = ax.get_graph_label(
        #     graph=curve,
        #     label= MathTex(r"\frac{\pi}{2}"),
        #     x_val=PI / 2,
        #     dot=True,
        #     direction=UP,color=MAROON
        # )
        
        # lines = ax.get_vertical_lines_to_graph(
        #     curve, x_range=[-1.5, 1.5], num_lines=30, color=BLUE
        # )
        # self.play(Create(lines),run_time=3)
        
        # label2 = ax.get_graph_label(
        #     graph=curve,
        #     label= MathTex(r"-\frac{\pi}{2}"),
        #     x_val=-PI / 2,
        #     dot=True,
        #     direction=DOWN,color=LOGO_WHITE
        # )
        # label3 = ax.get_graph_label(
        #     graph=curve,
        #     label= MathTex(r"-\frac{3\pi}{2}"),
        #     x_val=-3*PI / 2,
        #     dot=True,
        #     direction=UP,color=YELLOW
        # )
        # label4 = ax.get_graph_label(
        #     graph=curve,
        #     label= MathTex(r"\frac{3\pi}{2}"),
        #     x_val=3*PI / 2,
        #     dot=True,
        #     direction=DOWN,color=LOGO_WHITE
        # )


        # self.play(Create(label1),run_time=2)
        # self.play(Create(label2),run_time=2)
        # self.play(Create(label3),run_time=2)
        # self.play(Create(label4),run_time=2)
        # self.wait(2)
 
        # self.play(Flash(
        #     label1, line_length=1,
        #     num_lines=30, color=PURE_GREEN,
        #     flash_radius=0.7+SMALL_BUFF,
        #     time_width=0.5, run_time=3,
        #     rate_func = rush_from  ))     
        
        # self.play(FadeOut(label1),run_time=2)
        # self.play(FadeOut(label2),run_time=2)
        # self.play(FadeOut(label3),run_time=2)
        # self.play(FadeOut(label4),run_time=2)
        
        # self.play(FadeOut(area),run_time=2)
        # self.play(FadeOut(area1),run_time=2)
        # self.play(FadeOut(lines),run_time=2)
        # self.play(FadeOut(curve),run_time=2)
        # self.play(FadeOut(ax),run_time=2)       