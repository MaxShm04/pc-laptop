from CourseCatalogNode import CourseCatalogNode

class CourseCatalog:
    def __init__(self):
        self.root = None

    def addCourse(self, department, courseId, courseName, lecture, sections):
        new_node = CourseCatalogNode(department, courseId, courseName, lecture, sections)
        if self.root is None:
            self.root = new_node
            return True
        return self._insert(self.root, new_node)

    def _insert(self, current, new_node):
        if new_node == current:
            return False
        if new_node < current:
            if current.left is not None:
                return self._insert(current.left, new_node)
            else:
                current.left = new_node
                new_node.parent = current
                return True
        else:
            if current.right is not None:
                return self._insert(current.right, new_node)
            else:
                current.right = new_node
                new_node.parent = current
                return True

    def addSection(self, department, courseId, section):
        node = self.search(department, courseId)
        if node is None:
            return False
        node.sections.append(section)
        return True

    def search(self, department, courseId):
        return self._search(self.root, department.upper(), courseId)

    def _search(self, current, department, courseId):
        if current is None:
            return None
        if current.department == department and current.courseId == courseId:
            return current
        if (department, courseId) < (current.department, current.courseId):
            return self._search(current.left, department, courseId)
        return self._search(current.right, department, courseId)

    def inOrder(self):
        result = ""
        return self._inorder(self.root, result)

    def _inorder(self, current, result):
        if current is not None:
            result = self._inorder(current.left, result)
            result += str(current)
            result = self._inorder(current.right, result)
        return result

    def preOrder(self):
        result = ""
        return self._preorder(self.root, result)

    def _preorder(self, current, result):
        if current is not None:
            result += str(current)
            result = self._preorder(current.left, result)
            result = self._preorder(current.right, result)
        return result

    def postOrder(self):
        result = ""
        return self._postorder(self.root, result)

    def _postorder(self, current, result):
        if current is not None:
            result = self._postorder(current.left, result)
            result = self._postorder(current.right, result)
            result += str(current)
        return result

    def getAttendableSections(self, department, courseId, available_day, available_time):
        node = self.search(department, courseId)
        if node is None:
            return ""
        result = ""
        for section in node.sections:
            if (section.day == available_day and
                section.time[0] >= available_time[0] and
                section.time[1] <= available_time[1]):
                result += str(section).strip() + "\n"
        return result

    def countCoursesByDepartment(self):
        counts = {}
        self._countCourses(self.root, counts)
        return counts

    def _countCourses(self, current, counts):
        if current is not None:
            counts[current.department] = counts.get(current.department, 0) + 1
            self._countCourses(current.left, counts)
            self._countCourses(current.right, counts)

    def removeSection(self, department, courseId, section):
        node = self.search(department, courseId)
        if node is None:
            return False
        try:
            node.sections.remove(section)
            return True
        except ValueError:
            return False

    def removeCourse(self, department, courseId):
        node = self.search(department, courseId)
        if node is None:
            return False

        #Case0
        if node.left is None and node.right is None:
            self._replaceNodeInParent(node, None)
            return True
        #Case1
        elif node.left is None:
            self._replaceNodeInParent(node, node.right)
            return True
        #Case1
        elif node.right is None:
            self._replaceNodeInParent(node, node.left)
            return True

        # Case 2
        succ = self._succ(node.right)
        node.department = succ.department
        node.courseId = succ.courseId
        node.courseName = succ.courseName
        node.lecture = succ.lecture
        node.sections = succ.sections
        self._replaceNodeInParent(succ, succ.right)
        return True

    def _replaceNodeInParent(self, node, new_node):
        if node.parent is not None:
            if node is node.parent.left:
                node.parent.left = new_node
            else:
                node.parent.right = new_node
            if new_node is not None:
                new_node.parent = node.parent
        else:
            self.root = new_node
            if new_node is not None:
                new_node.parent = None

    def _succ(self, node):
        while node.left is not None:
            node = node.left
        return node
