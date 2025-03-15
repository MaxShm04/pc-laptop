class CourseCatalogNode:
    def __init__(self, department, courseId, courseName, lecture, sections):
        self.courseId = courseId
        if courseName:
            self.courseName = courseName.upper()
        else:
            self.courseName = courseName
        if department:
            self.department = department.upper()
        else:
            self.department = department
        self.lecture = lecture
        self.sections = sections

        self.parent = None
        self.left = None
        self.right = None

    def replaceNodeData(self, department, courseId, courseName, lecture, sections, parent=None, leftChild=None, rightChild=None):
        self.department = department.upper()
        self.courseId = courseId
        self.courseName = courseName.upper()
        self.lecture = lecture
        self.sections = sections
        if parent:
            self.parent = parent
        if leftChild:
            self.left = leftChild
        if rightChild:
            self.right = rightChild

    def hasLeftChild(self):
        return self.left  # Note: Python considers None as a False value

    def hasRightChild(self):
        return self.right

    def isLeftChild(self):
        return self.parent is not None and self.parent.left is self

    def isRightChild(self):
        return self.parent is not None and self.parent.right is self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left

    def __str__(self):
        s = f"{self.department} {self.courseId}: {self.courseName}\n"
        s += f" * Lecture: {self.lecture}\n"
        for section in self.sections:
            s += f" + Section: {section}\n"
        return s

    def __eq__(self, rhs):
        return self.courseId == rhs.courseId and self.department == rhs.department

    def __gt__(self, rhs):
        return True if (self.department > rhs.department or (self.department == rhs.department and self.courseId > rhs.courseId)) else False

    def __lt__(self, rhs):
        return True if (self.department < rhs.department or (self.department == rhs.department and self.courseId < rhs.courseId)) else False

    def removeSection(self, section):
        return self.sections.pop(section)

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.left = None
            else:
                self.parent.right = None

        elif self.hasAnyChildren():
            if self.hasRightChild():
                if self.isLeftChild():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
