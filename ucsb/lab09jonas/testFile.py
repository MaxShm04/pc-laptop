import pytest
from Event import Event
from CourseCatalogNode import CourseCatalogNode
from CourseCatalog import CourseCatalog


# =======================
# Tests for Event class
# =======================
def test_event_equality_and_str():
    # Create events with different casing in location to test uppercase conversion.
    e1 = Event("MW", (900, 1030), "liberty hall")
    e2 = Event("MW", (900, 1030), "LIBERTY HALL")
    e3 = Event("MW", (900, 1030), "Liberty Hall")
    e4 = Event("TR", (900, 1030), "liberty hall")

    # All events with same day, time and (uppercased) location should be equal.
    assert e1 == e2
    assert e1 == e3
    # Different day → not equal.
    assert not (e1 == e4)

    # Test the string representation (time formatting should yield two-digit hours/minutes)
    expected_str = "MW 09:00 - 10:30, LIBERTY HALL"
    assert str(e1) == expected_str


# ================================
# Tests for CourseCatalogNode class
# ================================
def test_course_catalog_node_str():
    lecture = Event("TR", (1100, 1230), "new hall")
    section = Event("F", (1300, 1400), "old lab")
    node = CourseCatalogNode("econ", 101, "microeconomics", lecture, [section])

    # The node should store department and course name in uppercase.
    assert node.department == "ECON"
    assert node.courseName == "MICROECONOMICS"

    # The node's string should include the lecture and section information.
    node_str = str(node)
    assert "ECON 101: MICROECONOMICS" in node_str
    assert "TR 11:00 - 12:30, NEW HALL" in node_str
    assert "F 13:00 - 14:00, OLD LAB" in node_str


# =========================================
# Tests for CourseCatalog (Lab08 & Lab09)
# =========================================

def test_add_course_and_duplicates():
    cc = CourseCatalog()
    lecture1 = Event("MW", (1000, 1130), "alpha hall")
    section1 = Event("F", (1200, 1300), "beta lab")

    # Adding a new course should return True.
    result = cc.addCourse("cs", 101, "intro to computing", lecture1, [section1])
    assert result is True

    # Adding a duplicate course (same department and courseId) should return False.
    result_dup = cc.addCourse("CS", 101, "intro to computing", lecture1, [section1])
    assert result_dup is False


def test_add_section():
    cc = CourseCatalog()
    lecture = Event("TR", (900, 1030), "gamma hall")
    section1 = Event("W", (1100, 1200), "delta lab")
    cc.addCourse("math", 202, "calculus", lecture, [])

    # Adding a section to an existing course.
    result = cc.addSection("MATH", 202, section1)
    assert result is True
    in_order = cc.inOrder()
    assert "W 11:00 - 12:00, DELTA LAB" in in_order

    # Attempting to add a section to a non-existent course should return False.
    result_nonexist = cc.addSection("PHYS", 101, section1)
    assert result_nonexist is False


def test_get_attendable_sections():
    cc = CourseCatalog()
    lecture = Event("MW", (800, 930), "epsilon hall")
    # Create several sections – only those on "MW" and within the specified time should be returned.
    section1 = Event("T", (1000, 1100), "room 1")  # Wrong day.
    section2 = Event("MW", (900, 1000), "room 2")  # Valid.
    section3 = Event("MW", (1000, 1100), "room 3")  # Valid.
    section4 = Event("MW", (1100, 1200), "room 4")  # Ends at 1200 (assume availableTime is exclusive at the end).

    cc.addCourse("hist", 301, "world history", lecture, [section1, section2, section3, section4])

    # Request sections on "MW" within time period 900 to 1100.
    attendable = cc.getAttendableSections("hist", 301, "MW", (900, 1100))

    # Expect sections 2 and 3 only.
    assert "MW 10:00 - 11:00, ROOM 3" in attendable or "MW 09:00 - 10:00, ROOM 2" in attendable
    # Ensure section4 (1100-1200) is not included.
    assert "MW 11:00 - 12:00, ROOM 4" not in attendable


def test_count_courses_by_department():
    cc = CourseCatalog()
    lecture = Event("MW", (800, 900), "alpha")
    cc.addCourse("bio", 101, "biology", lecture, [])
    cc.addCourse("bio", 102, "zoology", lecture, [])
    cc.addCourse("chem", 201, "chemistry", lecture, [])
    cc.addCourse("cs", 301, "algorithms", lecture, [])

    counts = cc.countCoursesByDepartment()
    assert counts.get("BIO", 0) == 2
    assert counts.get("CHEM", 0) == 1
    assert counts.get("CS", 0) == 1


def test_traversals_empty_tree():
    cc = CourseCatalog()
    # All traversal methods should return an empty string when the tree is empty.
    assert cc.inOrder() == ""
    assert cc.preOrder() == ""
    assert cc.postOrder() == ""


def test_traversals_order():
    cc = CourseCatalog()
    lecture = Event("TR", (900, 1000), "hall1")
    # Inserting courses (using new values) in an order that yields a nontrivial BST.
    cc.addCourse("eng", 210, "poetry", lecture, [])
    cc.addCourse("eng", 105, "prose", lecture, [])
    cc.addCourse("art", 300, "painting", lecture, [])

    in_order = cc.inOrder()
    pre_order = cc.preOrder()
    post_order = cc.postOrder()

    # In-order traversal should list courses in sorted order: by department then courseId.
    # Expected order: "ART 300: PAINTING" before "ENG 105: PROSE" before "ENG 210: POETRY".
    assert in_order.find("ART 300: PAINTING") < in_order.find("ENG 105: PROSE")
    assert in_order.find("ENG 105: PROSE") < in_order.find("ENG 210: POETRY")

    # Pre-order and post-order outputs should include all courses.
    for course in ["ART 300: PAINTING", "ENG 105: PROSE", "ENG 210: POETRY"]:
        assert course in pre_order
        assert course in post_order


# --------------------------
# Tests for removal methods
# --------------------------

def test_remove_section():
    cc = CourseCatalog()
    lecture = Event("MW", (1000, 1130), "delta hall")
    section1 = Event("F", (1200, 1300), "lab a")
    section2 = Event("F", (1300, 1400), "lab b")
    section3 = Event("F", (1400, 1500), "lab c")

    cc.addCourse("phy", 110, "physics", lecture, [section1, section2])

    # Remove an existing section.
    result = cc.removeSection("PHY", 110, section2)
    assert result is True
    node_str = cc.inOrder()
    assert "F 13:00 - 14:00, LAB B" not in node_str

    # Removing a section that does not exist should return False.
    result_nonexist = cc.removeSection("PHY", 110, section3)
    assert result_nonexist is False

    # Removing a section from a non-existent course.
    result_no_course = cc.removeSection("phy", 999, section1)
    assert result_no_course is False


def test_remove_course_leaf():
    cc = CourseCatalog()
    lecture = Event("TR", (1100, 1230), "zeta hall")
    cc.addCourse("econ", 301, "economics", lecture, [])

    # Removing the only node (a leaf) should succeed.
    result = cc.removeCourse("ECON", 301)
    assert result is True
    assert cc.inOrder() == ""


def test_remove_course_one_child():
    cc = CourseCatalog()
    # Build a tree such that one node has exactly one child.
    lecture_root = Event("MW", (900, 1000), "root hall")
    cc.addCourse("cs", 150, "data structures", lecture_root, [])

    lecture_left = Event("TR", (1000, 1100), "child hall")
    cc.addCourse("bio", 200, "genetics", lecture_left, [])

    lecture_right = Event("MW", (1100, 1200), "right hall")
    cc.addCourse("eng", 100, "literature", lecture_right, [])

    lecture_child = Event("TR", (1200, 1300), "child2 hall")
    cc.addCourse("eng", 150, "modern literature", lecture_child, [])

    # Remove "eng", 100 which has a single child ("eng",150).
    result = cc.removeCourse("ENG", 100)
    assert result is True
    tree_str = cc.inOrder()
    assert "ENG 100: LITERATURE" not in tree_str
    assert "ENG 150: MODERN LITERATURE" in tree_str


def test_remove_course_two_children():
    cc = CourseCatalog()
    # Build a tree to force removal of a node with two children.
    lecture_cs = Event("MW", (1000, 1130), "main hall")
    cc.addCourse("cs", 200, "computer architecture", lecture_cs, [])

    lecture_bio = Event("TR", (900, 1030), "bio center")
    cc.addCourse("bio", 150, "intro biology", lecture_bio, [])

    lecture_eng = Event("MW", (1300, 1430), "eng center")
    cc.addCourse("eng", 101, "creative writing", lecture_eng, [])

    lecture_cs2 = Event("TR", (1400, 1530), "tech hall")
    cc.addCourse("cs", 300, "operating systems", lecture_cs2, [])

    lecture_math = Event("MW", (800, 910), "math center")
    cc.addCourse("math", 400, "linear algebra", lecture_math, [])

    lecture_hist = Event("F", (1000, 1130), "history hall")
    cc.addCourse("hist", 250, "modern history", lecture_hist, [])

    # The BST (by department and courseId) is now nontrivial.
    # Remove "eng", 101 which should have two children (its left child is "cs",300 and its right child is "math",400 with a left child "hist",250).
    result = cc.removeCourse("ENG", 101)
    assert result is True
    tree_str = cc.inOrder()
    # "ENG 101: CREATIVE WRITING" should no longer be present.
    assert "ENG 101: CREATIVE WRITING" not in tree_str
    # Other courses should still be in the tree.
    assert "CS 300: OPERATING SYSTEMS" in tree_str
    assert "MATH 400: LINEAR ALGEBRA" in tree_str
    assert "HIST 250: MODERN HISTORY" in tree_str


def test_remove_course_nonexistent():
    cc = CourseCatalog()
    lecture = Event("MW", (1000, 1130), "alpha")
    cc.addCourse("cs", 101, "intro programming", lecture, [])

    # Trying to remove a course that doesn't exist should return False.
    result = cc.removeCourse("cs", 999)
    assert result is False#



def test_remove_complex_bst_cases():
    """
    Builds a complex BST with these (department='A', courseId) pairs inserted in order:
      1) A 200   (root)
      2) A 150   (left of 200)
      3) A 50    (left of 150)
      4) A 175   (right of 150)
      5) A 160   (left child of 175 -> ensures '175' has one child)
      6) A 300   (right of 200)
      7) A 250   (left of 300)
      8) A 400   (right of 300)

    Then tests:
      - Removing a leaf node (A 50)
      - Removing a node with one child (A 175)
      - Removing a node with two children (A 200, the root)
      - Removing a non-existent course (A 999)

    Verifies correct removals via inOrder traversal checks.
    """

    # A simple lecture event reused for all courses
    lecture = Event("MW", (800, 900), "some building")

    cc = CourseCatalog()

    # Insert the courses in the exact order to create our known BST shape:
    cc.addCourse("A", 200, "Course 200", lecture, [])
    cc.addCourse("A", 150, "Course 150", lecture, [])
    cc.addCourse("A", 50,  "Course 50",  lecture, [])
    cc.addCourse("A", 175, "Course 175", lecture, [])
    cc.addCourse("A", 160, "Course 160", lecture, [])
    cc.addCourse("A", 300, "Course 300", lecture, [])
    cc.addCourse("A", 250, "Course 250", lecture, [])
    cc.addCourse("A", 400, "Course 400", lecture, [])

    # For debugging, print the BST structure (if you have visualizeTopDown)
    print("Here is the BST structure (top-down):")

    # --------------------------------------------------
    # 1) Remove a leaf node: "A" 50
    # --------------------------------------------------
    assert "A 50: COURSE 50" in cc.inOrder(), "Node A 50 should exist initially."
    removed_leaf = cc.removeCourse("A", 50)
    assert removed_leaf is True, "Removing the leaf node (A 50) should return True."
    assert "A 50: COURSE 50" not in cc.inOrder(), "A 50 should be gone from the tree."

    # --------------------------------------------------
    # 2) Remove a node with one child: "A" 175
    #    We gave it a single child (A 160).
    # --------------------------------------------------
    assert "A 175: COURSE 175" in cc.inOrder()
    removed_one_child = cc.removeCourse("A", 175)
    assert removed_one_child is True, "Removing the node (A 175) with one child should succeed."
    assert "A 175: COURSE 175" not in cc.inOrder(), "A 175 should be removed."
    # Its child (A 160) should remain in the tree
    assert "A 160: COURSE 160" in cc.inOrder(), "A 160 should still exist."

    # --------------------------------------------------
    # 3) Remove a node with two children: "A" 200 (the root)
    # --------------------------------------------------
    assert "A 200: COURSE 200" in cc.inOrder()
    removed_two_children = cc.removeCourse("A", 200)
    assert removed_two_children is True, "Removing the root (with two children) should succeed."
    assert "A 200: COURSE 200" not in cc.inOrder(), "A 200 should be removed from the tree."

    # Confirm "A 200" is gone, others remain
    for existing in [
        "A 150: COURSE 150",
        "A 160: COURSE 160",
        "A 250: COURSE 250",
        "A 300: COURSE 300",
        "A 400: COURSE 400"
    ]:
        assert existing in cc.inOrder(), f"{existing} should still be in the tree."

    # --------------------------------------------------
    # 4) Attempt removing a non-existent course
    # --------------------------------------------------
    removed_non_existent = cc.removeCourse("A", 999)
    assert removed_non_existent is False, "Removing a non-existent course should return False."
    final_in_order = cc.inOrder()
    assert "A 999" not in final_in_order, "A 999 was never in the tree."

def test_instruction():
    cc = CourseCatalog()

    # add a new course: cmpsc 9
    lecture = Event("TR", (1530, 1645), "td-w 1701")
    section1 = Event("W", (1400, 1450), "north hall 1109")
    section2 = Event("W", (1500, 1550), "north hall 1109")
    section3 = Event("W", (1600, 1650), "north hall 1109")
    section4 = Event("W", (1700, 1750), "girvetz hall 1112")
    sections = [section1, section2, section3, section4]
    assert True == cc.addCourse("cmpsc", 9, "intermediate python", lecture, sections)

    # add a new course: art 10
    lecture = Event("TR", (1300, 1550), "arts 2628")
    sections = []
    assert True == cc.addCourse("art", 10, "introduction to painting", lecture, sections)

    '''
                                                                       root
                                                 ------------------------------------------------
                                                | CMPSC 9: INTERMEDIATE PYTHON                   |
                                                |  * Lecture: TR 15:30 - 16:45, TD-W 1701        |
                                                |  + Section: W 14:00 - 14:50, NORTH HALL 1109   |
                                                |  + Section: W 15:00 - 15:50, NORTH HALL 1109   |
                                                |  + Section: W 16:00 - 16:50, NORTH HALL 1109   |
                                                |  + Section: W 17:00 - 17:50, GIRVETZ HALL 1112 |
                                                 ------------------------------------------------
                                                /
         -----------------------------------------
        | ART 10: INTRODUCTION TO PAINTING        |
        |  * Lecture: TR 13:00 - 15:50, ARTS 2628 |
         -----------------------------------------
    '''

    print("----- in-order traversal -----")
    print(cc.inOrder())

    print("----- pre-order traversal -----")
    print(cc.preOrder())

    # remove a section from cmpsc 9
    section = Event("W", (1500, 1550), "north hall 1109")
    assert True == cc.removeSection("cmpsc", 9, section)

    '''
                                                                       root
                                                 ------------------------------------------------
                                                | CMPSC 9: INTERMEDIATE PYTHON                   |
                                                |  * Lecture: TR 15:30 - 16:45, TD-W 1701        |
                                                |  + Section: W 14:00 - 14:50, NORTH HALL 1109   |
                                                |  + Section: W 16:00 - 16:50, NORTH HALL 1109   |
                                                |  + Section: W 17:00 - 17:50, GIRVETZ HALL 1112 |
                                                 ------------------------------------------------
                                                /
         -----------------------------------------
        | ART 10: INTRODUCTION TO PAINTING        |
        |  * Lecture: TR 13:00 - 15:50, ARTS 2628 |
         -----------------------------------------
    '''

    print("----- in-order traversal -----")
    print(cc.inOrder())

    print("----- pre-order traversal -----")
    print(cc.preOrder())

    # remove cmpsc 9
    assert True == cc.removeCourse("cmpsc", 9)

    '''
                           root
         -----------------------------------------
        | ART 10: INTRODUCTION TO PAINTING        |
        |  * Lecture: TR 13:00 - 15:50, ARTS 2628 |
         -----------------------------------------
    '''

    print("----- in-order traversal -----")
    print(cc.inOrder())

    print("----- pre-order traversal -----")
    print(cc.preOrder())


def test_remove_course_leaf():
    # Case 1: Removing a leaf node.
    cc = CourseCatalog()
    lecture = Event("TR", (1300, 1550), "td-w 1701")
    # Add a course that will be a leaf.
    assert cc.addCourse("cmpsc", 9, "Intermediate Python", lecture, []) is True
    # Remove the leaf node.
    assert cc.removeCourse("cmpsc", 9) is True
    # Removing again should return False.
    assert cc.removeCourse("cmpsc", 9) is False


def test_remove_course_one_child():
    # Case 2: Removing a node with one child.
    cc = CourseCatalog()
    lecture_root = Event("TR", (1530, 1645), "td-w 1701")
    lecture_child = Event("TR", (1300, 1550), "td-w 1701")

    # Insert root node.
    assert cc.addCourse("cmpsc", 9, "Intermediate Python", lecture_root, []) is True
    # Insert a course that will be the only child.
    # For nodes with the same department, the one with the larger courseId goes to the right.
    assert cc.addCourse("cmpsc", 10, "Advanced Python", lecture_child, []) is True

    # Remove the root node (which has one child).
    assert cc.removeCourse("cmpsc", 9) is True
    # Now, the tree should contain only the course with courseId 10.
    # Removing the remaining course should succeed.
    assert cc.removeCourse("cmpsc", 10) is True


def test_remove_course_two_children():
    # Case 3: Removing a node with two children.
    cc = CourseCatalog()
    lecture_root = Event("TR", (1530, 1645), "td-w 1701")
    lecture_left = Event("TR", (1300, 1550), "td-w 1701")
    lecture_right = Event("TR", (1100, 1230), "td-w 1701")

    # Build a tree:
    #   Insert node: (CMPSC, 9) --> becomes the root.
    #   Insert node: (CMPSC, 8) --> becomes left child.
    #   Insert node: (CMPSC, 10) --> becomes right child.
    assert cc.addCourse("cmpsc", 9, "Intermediate Python", lecture_root, []) is True
    assert cc.addCourse("cmpsc", 8, "Intro to CS", lecture_left, []) is True
    assert cc.addCourse("cmpsc", 10, "Advanced Python", lecture_right, []) is True

    # Remove the root (which now has two children).
    # In a proper implementation, the successor (here, the node with courseId 10) should replace the removed node.
    assert cc.removeCourse("cmpsc", 9) is True

    # Now, check that the remaining courses can be removed:
    # The tree should contain (CMPSC, 8) and (CMPSC, 10) only.
    assert cc.removeCourse("cmpsc", 8) is True
    assert cc.removeCourse("cmpsc", 10) is True
