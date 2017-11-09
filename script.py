""" So this script should contain some text, and import test.py, call some functions inside it and print out some results. Let's see if it works. """
import test
import circumference_circle
print("Would you mind giving me the radius of the circle?")
radius=float(input())
print("How many significant figures?")
sig_figures=int((input()))
print("The circumference with radius ",radius,"is ",circumference_circle.round_sig(circumference_circle.circumference(radius),sig_figures), "and its area is", test.calc_circ_area(radius))
#      
#    
#Area=", test.calc_circ_area(radius), "Circumference=", circumference_circle.circumference(radius))
#print("The circumference with radius ",radius,"is ",round_sig(circumference(radius),sig_figures))