from CourseCatalogNodeOld import CourseCatalogNode
from Event import Event


class CourseCatalog:
    def __init__(self):
        self.root = None
        self.size = 0

    def addCourse(self, department, courseId, courseName, lecture, sections):
        new_node = CourseCatalogNode(department.upper(), courseId, courseName, lecture, sections)

        if self.root is None:
            self.root = new_node
            self.size = self.size + 1
            return True

        if self._insert(self.root, new_node):
            self.size += 1
            return True
        return False

    def _insert(self, current_node, new_node):
        if new_node == current_node:
            return False
        elif new_node > current_node:
            if current_node.hasRightChild():
                return self._insert(current_node.right, new_node)
            else:
                current_node.right = new_node
                new_node.parent = current_node
                return True
        else:
            if current_node.hasLeftChild():
                return self._insert(current_node.left, new_node)
            else:
                current_node.left = new_node
                new_node.parent = current_node
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
        return "".join(result)

    def _in_order(self, node, result):
        if node is not None:
            self._in_order(node.left, result)
            result.append(str(node))
            self._in_order(node.right, result)

    def preOrder(self):
        result = []
        self._pre_order(self.root, result)
        return "".join(result)

    def _pre_order(self, node, result):
        if node is not None:
            result.append(str(node))
            self._pre_order(node.left, result)
            self._pre_order(node.right, result)

    def postOrder(self):
        result = []
        self._post_order(self.root, result)
        return "".join(result)

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
            if availableDay in section.day:
                if section.time[0] >= availableTime[0] and section.time[1] <= availableTime[1]:
                    attendable.append(str(section))
        return "\n".join(attendable) + "\n" if len(attendable) > 0 else ""

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

    def getNode(self, department, courseID):
        key = CourseCatalogNode(department.upper(), courseID, None, None, None)

        if self.root:
            res = self._get(self.root, key)
            if res:
                return res
            return None
        return None

    def _get(self, node, key):
        if node == key:
            return node
        if node.hasLeftChild() and node > key:
            return self._get(node.left, key)
        if node.hasRightChild() and node < key:
            return self._get(node.right, key)
        return False

    def succ(self, node):
        if node.hasRightChild():
            return self._succ(node.right)
        return False

    def _succ(self, node):
        if node.hasLeftChild():
            return self._succ(node.left)
        return node

    def removeCourse(self, department, courseId):
        node = self.getNode(department.upper(), courseId)
        if not node:
            return False
        if self.size > 1:
            if node.isRoot():
                if node.hasBothChildren():
                    succ = self.succ(node)
                    succ.spliceOut()
                    node.replaceNodeData(succ.department,
                                         succ.courseId,
                                         succ.courseName,
                                         succ.lecture,
                                         succ.sections)
                    return True
                else:
                    if node.hasLeftChild():
                        self.root = node.left
                        self.root.parent = None
                    elif node.hasRightChild():
                        self.root = node.right
                        self.root.parent = None
                    else:
                        self.root = None
                    return True
            else:
                if not self._removeCourse(node):
                    return False
            self.size -= 1
            return True
        if self.size == 1 and (self.root.department == department.upper() and self.root.courseId):
            self.root = None
            self.size = self.size -1
            return True
        else:
            return False

    def _removeCourse(self, node):
        if not node:
            return False
        if node.isLeaf():
            if node.isLeftChild():
                node.parent.left = None
            else:
                node.parent.right = None
            return True
        elif node.hasBothChildren():
            succ = self.succ(node)
            succ.spliceOut()
            node.replaceNodeData(succ.department,
                                 succ.courseId,
                                 succ.courseName,
                                 succ.lecture,
                                 succ.sections)
            return True
        else:
            if node.hasLeftChild():
                if node.isLeftChild():
                    node.parent.left = node.left
                    node.left.parent = node.parent
                elif node.isRightChild():
                    node.left.parent = node.parent
                    node.parent.right = node.left
                else:
                    node.replaceNodeData(node.left.department, node.left.courseId, node.left.courseName,node.left.lecture,node.left.sections, node.left.left,node.left.right)
                return True
            elif node.hasRightChild():
                if node.isLeftChild():
                    node.right.parent = node.parent
                    node.parent.left = node.right
                elif node.isRightChild():
                    node.right.parent = node.parent
                    node.parent.right = node.right
                else:
                    node.replaceNodeData(node.right.department,node.right.courseId,node.right.courseName,node.right.lecture,node.right.sections,node.right.left,node.right.right)
                return True
            else:
                return False

    def removeSection(self, department, courseId, section):
        node = self.getNode(department.upper(), courseId)
        if node:
            if section in node.sections:
                node.sections.remove(section)
                return True
        return False




    def visualize(self):
        """
        Returns a string with an ASCII-art representation of the BST,
        showing department and courseId for each node.
        Right subtrees appear at the top, the root in the middle,
        and left subtrees toward the bottom.
        """
        return self._visualize(self.root, prefix="", is_left=True)

    def _visualize(self, node, prefix, is_left):

        if node is None:
            return ""

        # 1) Visualize right subtree first (goes toward the top).
        result = ""
        if node.right:
            # If this node is a left child, then the next level down
            # has one style of prefix; if it’s a right child, we use another.
            new_prefix = prefix + ("     " if is_left else "│    ")
            result += self._visualize(node.right, new_prefix, False)

        # 2) Visualize the current node itself.
        #    Use "└──" if this node is a left child, otherwise "┌──"
        branch_char = "└── " if is_left else "┌── "
        result += f"{prefix}{branch_char}{node.department} {node.courseId}\n"

        # 3) Visualize left subtree (goes toward the bottom).
        if node.left:
            new_prefix = prefix + ("│    " if is_left else "     ")
            result += self._visualize(node.left, new_prefix, True)

        return result

    def visualizeTopDown(self):
        """
        Returns a string with a top-down ASCII representation of the BST.
        The root appears at the top. Each node shows (L) or (R) to
        indicate whether it's a left or right child.
        Example shape:

            CHEM 200
            ├── (L) BIO 150
            │   ├── (L) BIO 50
            │   └── (R) BIO 175
            │       └── (L) BIO 160
            └── (R) CHEM 300
                ├── (L) CHEM 250
                └── (R) CS 100
        """
        return self._visualizeTopDown(self.root, prefix="", is_left=None, is_last=True)

    def _visualizeTopDown(self, node, prefix, is_left, is_last):
        """
        Recursive helper for visualizeTopDown().
        node: current CourseCatalogNode or None
        prefix: the current indentation string
        is_left: True if this node is a left child, False if right child, None if root
        is_last: True if this node is the last child at its level
        """
        if node is None:
            return ""

        result = ""

        if is_left is None:
            # This is the root, so just print department & courseId with no branch label.
            result += f"{node.department} {node.courseId}\n"
        else:
            # Build a branch label with (L) or (R).
            # We have four possibilities:
            #   ├── (L), └── (L), ├── (R), └── (R)
            # depending on is_left and is_last.
            branch_label = (
                "├── (L) " if (is_left and not is_last) else
                "└── (L) " if (is_left and is_last) else
                "├── (R) " if (not is_left and not is_last) else
                "└── (R) "
            )
            result += prefix + branch_label + f"{node.department} {node.courseId}\n"

        # Gather children in order: left first, then right
        children = []
        if node.left is not None:
            children.append(("left", node.left))
        if node.right is not None:
            children.append(("right", node.right))

        # For each child, we need to decide if it’s the last one
        # and update the prefix accordingly.
        for i, (side, child) in enumerate(children):
            child_is_last = (i == len(children) - 1)
            # If this node is not last, we keep the vertical bar for siblings; otherwise, just spaces.
            new_prefix = prefix + ("│   " if not is_last else "    ")
            child_is_left = (side == "left")
            result += self._visualizeTopDown(child, new_prefix, child_is_left, child_is_last)

        return result

