import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class CourseAppBase(tk.Toplevel):
    def __init__(self, title, logo_image, left_logo_image):
        super().__init__()
        
        self.title(title)
        self.geometry("800x600")
        
        # Create top canvas for logo and menu button
        top_canvas = tk.Canvas(self, bg='black', height=100)
        top_canvas.pack(side=tk.TOP, fill=tk.X)
        
        # Left logo
        left_logo_label = tk.Label(self, image=left_logo_image, bg='black')
        left_logo_label.image = left_logo_image
        left_logo_label.place(x=20, y=10)
        
        # Right logo
        right_logo_label = tk.Label(self, image=logo_image, bg='black')
        right_logo_label.image = logo_image
        right_logo_label.place(x=700, y=10)
        
        # Sidebar button
        sidebar_btn = tk.Button(self, text="Menu", bg='white', font=('Arial', 12), command=self.toggle_sidebar)
        sidebar_btn.place(x=120, y=35)
        
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
    def __init__(self, logo_image, left_logo_image):
        super().__init__("Course 1 Application", logo_image, left_logo_image)
        
class Course2App(CourseAppBase):
    def __init__(self, logo_image, left_logo_image):
        super().__init__("Course 2 Application", logo_image, left_logo_image)

class Course3App(CourseAppBase):
    def __init__(self, logo_image, left_logo_image):
        super().__init__("Course 3 Application", logo_image, left_logo_image)

class Course4App(CourseAppBase):
    def __init__(self, logo_image, left_logo_image):
        super().__init__("Course 4 Application", logo_image, left_logo_image)

class Course5App(CourseAppBase):
    def __init__(self, logo_image, left_logo_image):
        super().__init__("Course 5 Application", logo_image, left_logo_image)

class Course6App(CourseAppBase):
    def __init__(self, logo_image, left_logo_image):
        super().__init__("Course 6 Application", logo_image, left_logo_image)

class CoursesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Courses Application")
        self.geometry("800x600")
        
        # Create top canvas for logo and dashboard options
        top_canvas = tk.Canvas(self, bg='black', height=100)
        top_canvas.pack(side=tk.TOP, fill=tk.X)
        
        # Right logo
        logo_path = r"C:\Users\Kumari\OneDrive\Desktop\coding\bootcamp\right.jpeg"
        logo = Image.open(logo_path)
        logo = logo.resize((80, 80), Image.LANCZOS)
        self.logo_image = ImageTk.PhotoImage(logo)

        # Left logo
        left_logo_path = r"C:\Users\Kumari\OneDrive\Desktop\coding\bootcamp\left.jpeg"
        left_logo = Image.open(left_logo_path)
        left_logo = left_logo.resize((80, 80), Image.LANCZOS)
        self.left_logo_image = ImageTk.PhotoImage(left_logo)
        
        # Left logo label
        left_logo_label = tk.Label(self, image=self.left_logo_image, bg='black')
        left_logo_label.image = self.left_logo_image
        left_logo_label.place(x=20, y=10)
        
        # Right logo label
        right_logo_label = tk.Label(self, image=self.logo_image, bg='black')
        right_logo_label.image = self.logo_image
        right_logo_label.place(x=700, y=10)
        
        # Sidebar button
        sidebar_btn = tk.Button(self, text="Menu", bg='white', font=('Arial', 12), command=self.toggle_sidebar)
        sidebar_btn.place(x=120, y=35)
        
        # Sidebar frame
        self.sidebar_frame = tk.Frame(self, bg='lightgray', width=200)
        self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar_frame.pack_propagate(False)
        
        sidebar_buttons = ["Profile", "Grades", "Logout","Support"]
        for btn_text in sidebar_buttons:
            btn = tk.Button(self.sidebar_frame, text=btn_text, bg='white', font=('Arial', 12))
            btn.pack(fill=tk.X, pady=2)
        
        self.sidebar_visible = True
        
        # Main content frame for courses
        self.courses_frame = tk.Frame(self, bg='gray')  # Change bg to gray
        self.courses_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Sample courses data
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
            card = tk.Frame(parent, bg='yellow', relief=tk.RAISED, bd=2)  # Change bg to yellow
            card.grid(row=index//2, column=index%2, padx=10, pady=10, sticky="nsew")
            
            title_label = tk.Label(card, text=course["title"], bg='yellow', font=('Arial', 14, 'bold'))  # Change bg to yellow
            title_label.pack(pady=5)
            
            desc_label = tk.Label(card, text=course["description"], bg='yellow', font=('Arial', 10))  # Change bg to yellow
            desc_label.pack(pady=5)
            
            open_btn = tk.Button(card, text="Get Started", font=('Arial', 12), bg='blue', fg='white', padx=10, pady=5, command=lambda c=course: self.open_course(c))
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
        Course1App(self.logo_image, self.left_logo_image)

    def open_course2_window(self, course):
        Course2App(self.logo_image, self.left_logo_image)

    def open_course3_window(self, course):
        Course3App(self.logo_image, self.left_logo_image)

    def open_course4_window(self, course):
        Course4App(self.logo_image, self.left_logo_image)

    def open_course5_window(self, course):
        Course5App(self.logo_image, self.left_logo_image)

    def open_course6_window(self, course):
        Course6App(self.logo_image, self.left_logo_image)

if __name__ == "__main__":
    app = CoursesApp()
    app.mainloop()
