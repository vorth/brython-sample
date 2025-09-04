from browser import document, html, timer
import math
import random

# Canvas setup
canvas = document["canvas"]
ctx = canvas.getContext("2d")

# Circle storage
circles = []

class Circle:
    def __init__(self, x, y, radius=None, color=None):
        self.x = x
        self.y = y
        self.radius = radius or random.randint(10, 50)
        self.color = color or self.random_color()
        self.original_radius = self.radius
        
    def random_color(self):
        colors = [
            "#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", 
            "#FFEAA7", "#E48CBB", "#FDAE60", "#F7DC6F",
            "#BB8FCE", "#85C1E9", "#F8C471", "#82E0AA"
        ]
        return random.choice(colors)
    
    def draw(self, pulse_factor=1):
        ctx.beginPath()
        current_radius = self.radius * pulse_factor
        ctx.arc(self.x, self.y, current_radius, 0, math.pi * 2)
        ctx.fillStyle = self.color
        ctx.fill()
        ctx.strokeStyle = "#333"
        ctx.lineWidth = 2
        ctx.stroke()
    
def clear_canvas():
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    circles.clear()

def add_circle(x, y):
    circle = Circle(x, y)
    circles.append(circle)
    circle.draw()

def add_random_circles():
    for _ in range(8):
        x = random.randint(50, canvas.width - 50)
        y = random.randint(50, canvas.height - 50)
        add_circle(x, y)

# Event handlers
def canvas_click(event):
    rect = canvas.getBoundingClientRect()
    x = event.clientX - rect.left
    y = event.clientY - rect.top
    add_circle(x, y)

def clear_click(event):
    clear_canvas()

def random_click(event):
    add_random_circles()

# Bind events
canvas.bind("click", canvas_click)
document["clear-btn"].bind("click", clear_click)
document["random-btn"].bind("click", random_click)

# Add some initial circles
add_random_circles()
