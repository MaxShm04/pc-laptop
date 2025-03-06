class CourseCatalogNode:
    def __init__(self, department, courseId, courseName, lecture, sections):
        self.department = department.upper()
        self.courseId = courseId
        self.courseName = courseName.upper()
        self.lecture = lecture
        self.sections = sections

        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        s = f"{self.department} {self.courseId}: {self.courseName}\n"
        s += f" * Lecture: {self.lecture}\n"
        for section in self.sections:
            s += f" + Section: {section}\n"
        return s
