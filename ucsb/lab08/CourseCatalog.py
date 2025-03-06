from CourseCatalogNode import CourseCatalogNode


class CourseCatalog:
    def __init__(self):
        self.root = None

    def addCourse(self, department, courseId, courseName, lecture, sections):
        new_node = CourseCatalogNode(department, courseId, courseName, lecture, sections)

        if self.root is None:
            self.root = new_node
            return True

        parent = None
        current = self.root
        dept_upper = department.upper()
        while current is not None:
            if dept_upper == current.department and courseId == current.courseId:
                return False
            parent = current
            if dept_upper < current.department or (dept_upper == current.department and courseId < current.courseId):
                current = current.left
            else:
                current = current.right

        if dept_upper < parent.department or (dept_upper == parent.department and courseId < parent.courseId):
            parent.left = new_node
        else:
            parent.right = new_node
        new_node.parent = parent
        return True

    def addSection(self, department, courseId, section):
        node = self._search(self.root, department.upper(), courseId)
        if node is None:
            return False
        node.sections.append(section)
        return True

    def _search(self, node, department, courseId):
        if node is None:
            return None
        if department == node.department and courseId == node.courseId:
            return node
        elif department < node.department or (department == node.department and courseId < node.courseId):
            return self._search(node.left, department, courseId)
        else:
            return self._search(node.right, department, courseId)

    def inOrder(self):
        result = []
        self._in_order(self.root, result)
        return "\n".join(result)

    def _in_order(self, node, result):
        if node is not None:
            self._in_order(node.left, result)
            result.append(str(node))
            self._in_order(node.right, result)

    def preOrder(self):
        result = []
        self._pre_order(self.root, result)
        return "\n".join(result)

    def _pre_order(self, node, result):
        if node is not None:
            result.append(str(node))
            self._pre_order(node.left, result)
            self._pre_order(node.right, result)

    def postOrder(self):
        result = []
        self._post_order(self.root, result)
        return "\n".join(result)

    def _post_order(self, node, result):
        if node is not None:
            self._post_order(node.left, result)
            self._post_order(node.right, result)
            result.append(str(node))

    def getAttendableSections(self, department, courseId, availableDay, availableTime):
        node = self._search(self.root, department.upper(), courseId)
        if node is None:
            return ""
        attendable = []
        for section in node.sections:
            if availableDay == section.day:
                if section.time[0] >= availableTime[0] and section.time[1] <= availableTime[1]:
                    attendable.append(str(section))
        return "\n".join(attendable)

    def countCoursesByDepartment(self):
        counts = {}
        self._count_courses(self.root, counts)
        return counts

    def _count_courses(self, node, counts):
        if node is not None:
            dept = node.department
            counts[dept] = counts.get(dept, 0) + 1
            self._count_courses(node.left, counts)
            self._count_courses(node.right, counts)


