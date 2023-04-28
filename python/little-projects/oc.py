import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox
import webbrowser
import os
import re
from md import extract_mediafile_links

BACKGROUND_COLOR = "#212529"
PRIMARY_COLOR = "#14746f"
SECONDARY_COLOR = "#248277"
TEXT_COLOR = "#E9ECEF"
BUTTON_COLOR = "#036666"
DISABLED_BUTTON_COLOR = "#604d53"
ERROR_COLOR = "#E74C3C"
SEARCH_BOX_COLOR = "#3D3D3D"
LISTBOX_COLOR = "#3D3D3D"
ERROR_COLOR = "#E74C3C"
FONT_FAMILY = "Arial"
FONT_SIZE = 12

class CourseDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("online-courses.club Downloader")
        self.root.configure(bg=BACKGROUND_COLOR)

        # Create search frame
        sf = tk.Frame(root, bg=BACKGROUND_COLOR)
        sf.pack(side=tk.TOP, padx=10, pady=10)

        # Create search label and entry
        sl = tk.Label(sf, text="Search for Courses:", font=(FONT_FAMILY, FONT_SIZE), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        sl.pack(side=tk.LEFT)
        self.se = tk.Entry(sf, bg=(SEARCH_BOX_COLOR), font=(FONT_FAMILY, FONT_SIZE))
        self.se.config(fg=TEXT_COLOR)
        self.se.pack(side=tk.LEFT, padx=5)

        # Create search button
        sb = tk.Button(sf, text="Search", command=self.search_courses, font=(FONT_FAMILY, FONT_SIZE), bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=SECONDARY_COLOR)
        sb.pack(side=tk.LEFT, padx=5)

        rf = tk.Frame(root, bg=BACKGROUND_COLOR)
        rf.pack(side=tk.TOP, padx=10, pady=10)

        # Create course list label and listbox
        self.cl = tk.Listbox(rf, height=15, width=50, bg=LISTBOX_COLOR, font=(FONT_FAMILY, FONT_SIZE), fg=TEXT_COLOR)
        self.cl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.ci = tk.Label(rf, font=(FONT_FAMILY, FONT_SIZE), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        self.ci.pack(side=tk.LEFT, padx=10)

        # Add scrollbar to course list
        scrollbar = tk.Scrollbar(rf, command=self.cl.yview)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.cl.config(yscrollcommand=scrollbar.set)

        # Create view and bulk download buttons
        bf = tk.Frame(root, bg=BACKGROUND_COLOR)
        bf.pack(side=tk.TOP, padx=10, pady=10)
        self.vb = tk.Button(bf, text="View", command=self.view_course, state=tk.DISABLED, font=(FONT_FAMILY, FONT_SIZE), bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=SECONDARY_COLOR)
        self.vb.pack(side=tk.LEFT, padx=5)
        self.bb = tk.Button(bf, text="Bulk Download", command=self.bulk_download, state=tk.DISABLED, font=(FONT_FAMILY, FONT_SIZE), bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=SECONDARY_COLOR)
        self.bb.pack(side=tk.LEFT, padx=5)

        self.l = {}

    def search_courses(self):
        st = self.se.get()
        url = f"https://online-courses.club/?s={st}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        courses = soup.find_all("article", {"class": "admania_gridpstlayt3"})
        self.cl.delete(0, tk.END)
        for i, course in enumerate(courses, start=1):
            title = course.find("h2", {"class": "admania_entrytitle"}).text
            link = course.find("a", {"class": "admania_pstrdmr"})["href"]
            self.cl.insert(tk.END, f"{i}. {title}")
            self.l[i] = link
        self.vb.configure(state=tk.NORMAL)
        self.bb.configure(state=tk.NORMAL)

    def view_course(self):
        if not self.l:
            messagebox.showerror("Error", "Please search for a course first.")
            return

        selected_course = self.cl.curselection()
        if not selected_course:
            messagebox.showerror("Error", "Please select a course.")
            return

        course_number = int(self.cl.get(selected_course)[0])
        link = self.l.get(course_number)
        webbrowser.open_new(link)

    def bulk_download(self):
        selected_courses = self.cl.curselection()

        for course_index in selected_courses:
            course_name = self.cl.get(course_index)
            course_url = self.l.get(course_index + 1)

            extract_mediafile_links(course_url)

        messagebox.showinfo("Download Complete", "All selected courses have been downloaded successfully!")


root = tk.Tk()
app = CourseDownloader(root)
root.mainloop()
