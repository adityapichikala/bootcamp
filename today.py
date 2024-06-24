import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class RoundedButton(tk.Canvas):
    def __init__(self, parent, width, height, corner_radius, padding, color, text, command=None):
        tk.Canvas.__init__(self, parent, width=width, height=height, highlightthickness=0)
        self.command = command
        self.padding = padding

        self.width = width - padding * 2
        self.height = height - padding * 2
        self.corner_radius = corner_radius
        self.color = color
        self.text = text

        if self.corner_radius > self.width / 2:
            self.corner_radius = self.width / 2
        if self.corner_radius > self.height / 2:
            self.corner_radius = self.height / 2

        self.create_rounded_rectangle(padding, padding, self.width + padding, self.height + padding, self.corner_radius, fill=self.color, outline="")

        self.text_id = self.create_text(self.width / 2 + padding, self.height / 2 + padding, text=self.text, fill="white", font=("Arial", 12, "bold"))
        self.bind("<ButtonPress-1>", self.on_press)
        self.bind("<ButtonRelease-1>", self.on_release)

    def create_rounded_rectangle(self, x1, y1, x2, y2, r, **kwargs):
        self.create_arc(x1, y1, x1 + 2 * r, y1 + 2 * r, start=90, extent=90, **kwargs)
        self.create_arc(x2 - 2 * r, y1, x2, y1 + 2 * r, start=0, extent=90, **kwargs)
        self.create_arc(x2 - 2 * r, y2 - 2 * r, x2, y2, start=270, extent=90, **kwargs)
        self.create_arc(x1, y2 - 2 * r, x1 + 2 * r, y2, start=180, extent=90, **kwargs)
        self.create_rectangle(x1 + r, y1, x2 - r, y2, **kwargs)
        self.create_rectangle(x1, y1 + r, x2, y2 - r, **kwargs)

    def on_press(self, event):
        self.itemconfig(self.text_id, fill="black")
        if self.command:
            self.command()

    def on_release(self, event):
        self.itemconfig(self.text_id, fill="white")

class CourseAppBase(tk.Toplevel):
    def __init__(self, title, logo_left_path, logo_right_path):
        super().__init__()
        
        self.title(title)
        self.geometry("800x600")
        
        # Create top frame for logo and menu button
        top_frame = tk.Frame(self, bg='black', height=100)
        top_frame.pack(side=tk.TOP, fill=tk.X)
        
        # Left Logo
        logo_left = Image.open(logo_left_path)
        logo_left = logo_left.resize((80, 80), Image.LANCZOS)
        logo_left_image = ImageTk.PhotoImage(logo_left)
        logo_left_label = tk.Label(top_frame, image=logo_left_image, bg='black')
        logo_left_label.image = logo_left_image
        logo_left_label.pack(side=tk.LEFT, padx=20, pady=10)
        
        # Right Logo
        logo_right = Image.open(logo_right_path)
        logo_right = logo_right.resize((80, 80), Image.LANCZOS)
        logo_right_image = ImageTk.PhotoImage(logo_right)
        logo_right_label = tk.Label(top_frame, image=logo_right_image, bg='black')
        logo_right_label.image = logo_right_image
        logo_right_label.pack(side=tk.RIGHT, padx=20, pady=10)
        
        # Sidebar button
        sidebar_btn = tk.Button(top_frame, text="Menu", bg='black', fg='white', font=('Arial', 12), command=self.toggle_sidebar)
        sidebar_btn.pack(side=tk.LEFT, padx=20, pady=10)
        
        # Sidebar frame
        self.sidebar_frame = tk.Frame(self, bg='lightgray', width=200)
        self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar_frame.pack_propagate(False)
        
        sidebar_buttons = ["Profile", "Grades", "Logout", "Support"]
        for btn_text in sidebar_buttons:
            btn = tk.Button(self.sidebar_frame, text=btn_text, bg='white', font=('Arial', 12), command=lambda t=btn_text: self.show_content(t))
            btn.pack(fill=tk.X, pady=2)
        
        self.sidebar_visible = True
        
        # Main content frame
        self.content_frame = tk.Frame(self, bg='white')
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.current_content = tk.Label(self.content_frame, text=f"Welcome to {title}", font=('Arial', 16), bg='white')
        self.current_content.pack(expand=True)
    
    def toggle_sidebar(self):
        if self.sidebar_visible:
            self.sidebar_frame.pack_forget()
            self.content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        else:
            self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)
            self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.sidebar_visible = not self.sidebar_visible
    
    def show_content(self, content):
        self.current_content.pack_forget()
        self.current_content = tk.Label(self.content_frame, text=content, font=('Arial', 16), bg='white')
        self.current_content.pack(expand=True)

class Course1App(CourseAppBase):
    def __init__(self):
        super().__init__("Course 1 Application", r"C:\Users\Kumari\OneDrive\Desktop\coding\bootcamp\background2.jpeg", r"C:\Users\Kumari\OneDrive\Desktop\coding\bootcamp\background3.jpeg")
        
class Course2App(CourseAppBase):
    def __init__(self):
        super().__init__("Course 2 Application", r"C:\Users\Kumari\OneDrive\Desktop\coding\bootcamp\background2.jpeg", r"C:\Users\Kumari\OneDrive\Desktop\coding\bootcamp\background3.jpeg")

class Course3App(CourseAppBase):
    def __init__(self):
        super().__init__("Course 3 Application", r"C:\Users\Kumari\OneDrive\Desktop\coding\bootcamp\background2.jpeg", r"C:\Users\Kumari\OneDrive\Desktop\coding\bootcamp\background3.jpeg")

class Course4App(CourseAppBase):
    def __init__(self):
        super().__init__("Course 4 Application", r"C:\Users\Kumari\OneDrive\Desktop\coding\bootcamp\background2.jpeg", r"C:\Users\Kumari\OneDrive\Desktop\coding\bootcamp\background3.jpeg")

class Course5App(CourseAppBase):
    def __init__(self):
        super().__init__("Course 5 Application", r"C:\Users\Kumari\OneDrive\Desktop\coding\bootcamp\background2.jpeg", r"C:\Users\Kumari\OneDrive\Desktop\coding\bootcamp\background3.jpeg")

class Course6App(CourseAppBase):
    def __init__(self):
        super().__init__("Course 6 Application", r"C:\Users\Kumari\OneDrive\Desktop\coding\bootcamp\background2.jpeg", r"C:\Users\Kumari\OneDrive\Desktop\coding\bootcamp\background3.jpeg")

class CoursesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Courses Application")
        self.geometry("800x600")
        
        # Create top frame for logo and dashboard options
        top_frame = tk.Frame(self, bg='black', height=100)
        top_frame.pack(side=tk.TOP, fill=tk.X)
        
        # Left Logo
        logo_left_path = r"C:\Users\Kumari\OneDrive\Desktop\coding\bootcamp\background2.jpeg"
        logo_left = Image.open(logo_left_path)
        logo_left = logo_left.resize((80, 80), Image.LANCZOS)
        logo_left_image = ImageTk.PhotoImage(logo_left)
        
        logo_left_label = tk.Label(top_frame, image=logo_left_image, bg='black')
        logo_left_label.image = logo_left_image
        logo_left_label.pack(side=tk.LEFT, padx=20, pady=10)
        
        # Right Logo
        logo_right_path = r"C:\Users\Kumari\OneDrive\Desktop\coding\bootcamp\background3.jpeg"
        logo_right = Image.open(logo_right_path)
        logo_right = logo_right.resize((80, 80), Image.LANCZOS)
        logo_right_image = ImageTk.PhotoImage(logo_right)
        
        logo_right_label = tk.Label(top_frame, image=logo_right_image, bg='black')
        logo_right_label.image = logo_right_image
        logo_right_label.pack(side=tk.RIGHT, padx=20, pady=10)
        
        # Sidebar button
        sidebar_btn = tk.Button(top_frame, text="Menu", bg='black', fg='white', font=('Arial', 12), command=self.toggle_sidebar)
        sidebar_btn.pack(side=tk.LEFT, padx=20, pady=10)
        
        # Sidebar frame
        self.sidebar_frame = tk.Frame(self, bg='lightgray', width=200)
        self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar_frame.pack_propagate(False)
        
        sidebar_buttons = ["Profile", "Grades", "Logout", "Support"]
        for btn_text in sidebar_buttons:
            btn = tk.Button(self.sidebar_frame, text=btn_text, bg='white', font=('Arial', 12), command=lambda t=btn_text: self.show_content(t))
            btn.pack(fill=tk.X, pady=2)
        
        self.sidebar_visible = True
        
        # Main courses frame
        self.courses_frame = tk.Frame(self, bg='white')
        self.courses_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        courses = [
            {"title": "Course 1", "description": "Description for course 1"},
            {"title": "Course 2", "description": "Description for course 2"},
            {"title": "Course 3", "description": "Description for course 3"},
            {"title": "Course 4", "description": "Description for course 4"},
            {"title": "Course 5", "description": "Description for course 5"},
            {"title": "Course 6", "description": "Description for course 6"}
        ]
        
        self.create_course_cards(self.courses_frame, courses)
        self.bind("<Configure>", self.on_resize)
    
    def toggle_sidebar(self):
        if self.sidebar_visible:
            self.sidebar_frame.pack_forget()
            self.courses_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        else:
            self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)
            self.courses_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.sidebar_visible = not self.sidebar_visible
    
    def create_course_cards(self, parent, courses):
        self.course_cards = []
        for index, course in enumerate(courses):
            card = tk.Frame(parent, bg='white', relief=tk.RAISED, bd=2)
            card.grid(row=index//2, column=index%2, padx=10, pady=10, sticky="nsew")
            
            title_label = tk.Label(card, text=course["title"], bg='white', font=('Arial', 14, 'bold'))
            title_label.pack(pady=5)
            
            desc_label = tk.Label(card, text=course["description"], bg='white', font=('Arial', 10))
            desc_label.pack(pady=5)
            
            open_btn = RoundedButton(card, width=100, height=40, corner_radius=20, padding=5, color='blue', text='Open', command=lambda c=course: self.open_course(c))
            open_btn.pack(pady=5)
            
            self.course_cards.append(card)
        
        for i in range(len(courses)//2 + len(courses)%2):
            self.courses_frame.grid_rowconfigure(i, weight=1)
        for i in range(2):  # Assume a max of 2 columns for simplicity
            self.courses_frame.grid_columnconfigure(i, weight=1)
    
    def on_resize(self, event):
        width = self.courses_frame.winfo_width()
        if width < 400:
            columns = 1
        elif width < 800:
            columns = 2
        else:
            columns = 3
        
        for index, card in enumerate(self.course_cards):
            card.grid_forget()
            card.grid(row=index//columns, column=index%columns, padx=10, pady=10, sticky="nsew")
        
        for i in range(len(self.course_cards)//columns + len(self.course_cards)%columns):
            self.courses_frame.grid_rowconfigure(i, weight=1)
        for i in range(columns):
            self.courses_frame.grid_columnconfigure(i, weight=1)
    
    def open_course(self, course):
        print(f"Opening {course['title']}: {course['description']}")
        
        if course["title"] == "Course 1":
            self.open_course1_window(course)
        elif course["title"] == "Course 2":
            self.open_course2_window(course)
        elif course["title"] == "Course 3":
            self.open_course3_window(course)
        elif course["title"] == "Course 4":
            self.open_course4_window(course)
        elif course["title"] == "Course 5":
            self.open_course5_window(course)
        elif course["title"] == "Course 6":
            self.open_course6_window(course)

    def open_course1_window(self, course):
        course1_app = Course1App()
        course1_app.mainloop()

    def open_course2_window(self, course):
        course2_app = Course2App()
        course2_app.mainloop()

    def open_course3_window(self, course):
        course3_app = Course3App()
        course3_app.mainloop()

    def open_course4_window(self, course):
        course4_app = Course4App()
        course4_app.mainloop()

    def open_course5_window(self, course):
        course5_app = Course5App()
        course5_app.mainloop()

    def open_course6_window(self, course):
        course6_app = Course6App()
        course6_app.mainloop()

if __name__ == "__main__":
    app = CoursesApp()
    app.mainloop()

