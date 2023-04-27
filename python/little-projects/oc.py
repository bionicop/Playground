import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox
import webbrowser

class CourseDownloader:
    def __init__(self, root):
        """
        Initializes the CourseDownloader class with the given tkinter root window.
        """
        self.root = root
        self.root.title("Online-Courses.club Downloader")

        # Search Frame
        search_frame = tk.Frame(root)
        search_frame.pack(side=tk.TOP, padx=10, pady=10)
        search_label = tk.Label(search_frame, text="Search for Courses:")
        search_label.pack(side=tk.LEFT)
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        search_button = tk.Button(search_frame, text="Search", command=self.search_courses)
        search_button.pack(side=tk.LEFT, padx=5)

        # Result Frame
        result_frame = tk.Frame(root)
        result_frame.pack(side=tk.TOP, padx=10, pady=10)
        self.course_listbox = tk.Listbox(result_frame, height=15, width=50)
        self.course_listbox.pack(side=tk.LEFT)
        self.course_info_label = tk.Label(result_frame)
        self.course_info_label.pack(side=tk.LEFT, padx=10)

        # Button Frame
        button_frame = tk.Frame(root)
        button_frame.pack(side=tk.TOP, padx=10, pady=10)
        self.view_button = tk.Button(button_frame, text="View", command=self.view_course, state=tk.DISABLED)
        self.view_button.pack(side=tk.LEFT, padx=5)
        self.bulk_download_button = tk.Button(button_frame, text="Bulk Download", command=self.bulk_download, state=tk.DISABLED)
        self.bulk_download_button.pack(side=tk.LEFT, padx=5)

        # Dictionary to store course links
        self.course_links = {}

    def search_courses(self):
        """
        Searches the online-courses.club website for courses that match the search term entered by the user.
        Populates the course_listbox with the search results.
        """
        search_term = self.search_entry.get()
        url = f"https://online-courses.club/?s={search_term}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        courses = soup.find_all("article", {"class": "admania_gridpstlayt3"})
        self.course_listbox.delete(0, tk.END)
        for i, course in enumerate(courses, start=1):
            title = course.find("h2", {"class": "admania_entrytitle"}).text
            link = course.find("a", {"class": "admania_pstrdmr"})["href"]
            self.course_listbox.insert(tk.END, f"{i}. {title}")
            self.course_links[i] = link
        self.view_button.configure(state=tk.NORMAL)
        self.bulk_download_button.configure(state=tk.NORMAL)

    def view_course(self):
        """
        Opens the link to the selected course in the user's default web browser.
        """
        if not self.course_links:
            messagebox.showerror("Error", "Please search for a course first.")
            return

        selected_course = self.course_listbox.curselection()
        if not selected_course:
            messagebox.showerror("Error", "Please select a Course.")
            return

        course_number = int(self.course_listbox.get(selected_course)[0])
        link = self.course_links.get(course_number)

        webbrowser.open_new(link)

    def bulk_download(self):
        """
        Displays a warning message indicating that the bulk download feature is not yet implemented.
        """
        messagebox.showwarning("Bulk download", "This feature is not implemented yet.")

root = tk.Tk()
app = CourseDownloader(root)
root.mainloop()
