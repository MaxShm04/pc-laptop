from CourseCatalogOld import CourseCatalog
from Event import Event

def test_add_course():
    catalog = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "TD-W 1701")
    sections = [Event("W", (1400, 1450), "NORTH HALL 1109")]
    assert catalog.addCourse("cmpsc", 9, "intermediate python", lecture, sections) is True
    assert catalog.addCourse("cmpsc", 9, "intermediate python", lecture, sections) is False

def test_add_section():
    catalog = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "TD-W 1701")
    sections = [Event("W", (1400, 1450), "NORTH HALL 1109")]
    catalog.addCourse("cmpsc", 9, "intermediate python", lecture, sections)
    new_section = Event("F", (1200, 1250), "NORTH HALL 1200")
    assert catalog.addSection("cmpsc", 9, new_section) is True
    assert catalog.addSection("cmpsc", 10, new_section) is False

def test_getNode():
    catalog = CourseCatalog()
    lecture = Event("MW", (1000, 1050), "PHELPS 1205")
    sections = []
    catalog.addCourse("math", 34, "calculus", lecture, sections)
    assert catalog.getNode("math", 34) is not None
    assert catalog.getNode("math", 35) is None

def test_traversals():
    catalog = CourseCatalog()
    catalog.addCourse("cmpsc", 9, "intermediate python", Event("TR", (1530, 1645), "TD-W 1701"), [])
    catalog.addCourse("cmpsc", 8, "intro python", Event("MW", (1000, 1050), "TD-W 1501"), [])
    catalog.addCourse("pstat", 131, "probability", Event("MW", (1400, 1450), "SBSG 3201"), [])
    in_order = catalog.inOrder()
    pre_order = catalog.preOrder()
    post_order = catalog.postOrder()
    assert "CMPSC 8" in in_order
    assert "CMPSC 9" in pre_order
    assert "PSTAT 131" in post_order

def test_get_attendable_sections():
    catalog = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "TD-W 1701")
    sections = [
        Event("W", (1400, 1450), "NORTH HALL 1109"),
        Event("W", (1500, 1550), "NORTH HALL 1109"),
    ]
    catalog.addCourse("cmpsc", 9, "intermediate python", lecture, sections)
    result = catalog.getAttendableSections("cmpsc", 9, "W", (1400, 1600))
    assert "W 14:00 - 14:50, NORTH HALL 1109" in result
    assert "W 15:00 - 15:50, NORTH HALL 1109" in result
    assert catalog.getAttendableSections("cmpsc", 9, "M", (1400, 1600)) == ""

def test_count_courses_by_department():
    catalog = CourseCatalog()
    catalog.addCourse("cmpsc", 9, "intermediate python", Event("TR", (1530, 1645), "TD-W 1701"), [])
    catalog.addCourse("cmpsc", 8, "intro python", Event("MW", (1000, 1050), "TD-W 1501"), [])
    catalog.addCourse("math", 34, "calculus", Event("MW", (1100, 1150), "PHELPS 1205"), [])
    counts = catalog.countCoursesByDepartment()
    assert counts == {"CMPSC": 2, "MATH": 1}

def test_removeSection_valid():
    catalog = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "TD-W 1701")
    section1 = Event("W", (1400, 1450), "NORTH HALL 1109")
    section2 = Event("W", (1500, 1550), "NORTH HALL 1109")
    catalog.addCourse("cmpsc", 9, "intermediate python", lecture, [section1, section2])
    result = catalog.removeSection("cmpsc", 9, section2)
    assert result is True
    node = catalog.getNode("cmpsc", 9)
    assert section2 not in node.sections

def test_removeSection_course_not_exist():
    catalog = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "TD-W 1701")
    section = Event("W", (1400, 1450), "NORTH HALL 1109")
    catalog.addCourse("cmpsc", 9, "intermediate python", lecture, [section])
    result = catalog.removeSection("math", 10, section)
    assert result is False

def test_removeSection_section_not_exist():
    catalog = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "TD-W 1701")
    section = Event("W", (1400, 1450), "NORTH HALL 1109")
    catalog.addCourse("cmpsc", 9, "intermediate python", lecture, [section])
    fake_section = Event("F", (1200, 1250), "TD-W 9999")
    result = catalog.removeSection("cmpsc", 9, fake_section)
    assert result is False

def test_removeCourse_empty_tree():
    catalog = CourseCatalog()
    result = catalog.removeCourse("cmpsc", 9)
    assert result is False
    assert catalog.root is None

def test_removeCourse_not_found():
    catalog = CourseCatalog()
    lecture = Event("MW", (1000, 1050), "PHELPS 1205")
    catalog.addCourse("math", 34, "calculus", lecture, [])
    result = catalog.removeCourse("eng", 101)
    assert result is False

def test_removeCourse_case1_leaf():
    catalog = CourseCatalog()
    lecture = Event("MW", (1000, 1050), "PHELPS 1205")
    catalog.addCourse("math", 34, "calculus", lecture, [])
    catalog.addCourse("math", 2, "algebra", lecture, [])
    node = catalog.getNode("math", 2)
    assert node.left is None and node.right is None
    result = catalog.removeCourse("math", 2)
    assert result is True
    assert catalog.getNode("math", 2) is None

def test_removeCourse_case2_one_child():
    catalog = CourseCatalog()
    lecture = Event("MW", (1000, 1050), "PHELPS 1205")
    catalog.addCourse("math", 34, "calculus", lecture, [])
    catalog.addCourse("math", 40, "linear algebra", lecture, [])
    node = catalog.getNode("math", 34)
    assert node.right is not None
    result = catalog.removeCourse("math", 34)
    assert result is True
    assert catalog.getNode("math", 34) is None
    assert catalog.getNode("math", 40) is not None

def test_removeCourse_case3_two_children():
    catalog = CourseCatalog()
    lecture = Event("MWF", (900, 950), "ROOM A")
    catalog.addCourse("cmpsc", 10, "RootCourse", lecture, [])
    catalog.addCourse("cmpsc", 5, "LeftCourse", lecture, [])
    catalog.addCourse("cmpsc", 20, "RightCourse", lecture, [])
    removed = catalog.removeCourse("cmpsc", 10)
    assert removed is True
    new_root = catalog.root
    assert new_root is not None
    assert new_root.department == "CMPSC"
    assert new_root.courseId == 20
    assert new_root.left is not None
    assert new_root.left.courseId == 5

def test_inorder_traversal_after_removals():
    catalog = CourseCatalog()
    catalog.addCourse("art", 10, "painting", Event("TR", (1300, 1550), "ARTS 2628"), [])
    catalog.addCourse("cmpsc", 20, "advanced topics", Event("MWF", (1100, 1150), "HAROLD FRANK 1104"), [])
    catalog.addCourse("math", 24, "differential equations", Event("TR", (800, 915), "BUCHANAN 1910"), [Event("F", (1000, 1050), "GIRVETZ 1112")])
    catalog.addCourse("math", 2, "college algebra", Event("TR", (1400, 1515), "CHEM 1171"), [])
    catalog.addCourse("math", 40, "linear algebra", Event("TR", (1600, 1715), "PHELPS 3515"), [])
    catalog.removeCourse("math", 2)
    catalog.removeCourse("math", 24)
    result = catalog.inOrder().strip().split("\n")
    traversal_str = "\n".join(result)
    assert "ART 10:" in traversal_str
    assert "CMPSC 20:" in traversal_str
    assert "MATH 40:" in traversal_str

def test_add_course():
    catalog = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "TD-W 1701")
    sections = [Event("W", (1400, 1450), "NORTH HALL 1109")]
    assert catalog.addCourse("cmpsc", 9, "intermediate python", lecture, sections) is True
    assert catalog.addCourse("cmpsc", 9, "intermediate python", lecture, sections) is False

def test_add_section():
    catalog = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "TD-W 1701")
    sections = [Event("W", (1400, 1450), "NORTH HALL 1109")]
    catalog.addCourse("cmpsc", 9, "intermediate python", lecture, sections)
    new_section = Event("F", (1200, 1250), "NORTH HALL 1200")
    assert catalog.addSection("cmpsc", 9, new_section) is True
    assert catalog.addSection("cmpsc", 10, new_section) is False

def test_getNode():
    catalog = CourseCatalog()
    lecture = Event("MW", (1000, 1050), "PHELPS 1205")
    sections = []
    catalog.addCourse("math", 34, "calculus", lecture, sections)
    assert catalog.getNode("math", 34) is not None
    assert catalog.getNode("math", 35) is None

def test_traversals():
    catalog = CourseCatalog()
    catalog.addCourse("cmpsc", 9, "intermediate python", Event("TR", (1530, 1645), "TD-W 1701"), [])
    catalog.addCourse("cmpsc", 8, "intro python", Event("MW", (1000, 1050), "TD-W 1501"), [])
    catalog.addCourse("pstat", 131, "probability", Event("MW", (1400, 1450), "SBSG 3201"), [])
    in_order = catalog.inOrder()
    pre_order = catalog.preOrder()
    post_order = catalog.postOrder()
    assert "CMPSC 8" in in_order
    assert "CMPSC 9" in pre_order
    assert "PSTAT 131" in post_order

def test_get_attendable_sections():
    catalog = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "TD-W 1701")
    sections = [
        Event("W", (1400, 1450), "NORTH HALL 1109"),
        Event("W", (1500, 1550), "NORTH HALL 1109"),
    ]
    catalog.addCourse("cmpsc", 9, "intermediate python", lecture, sections)
    result = catalog.getAttendableSections("cmpsc", 9, "W", (1400, 1600))
    assert "W 14:00 - 14:50, NORTH HALL 1109" in result
    assert "W 15:00 - 15:50, NORTH HALL 1109" in result
    assert catalog.getAttendableSections("cmpsc", 9, "M", (1400, 1600)) == ""

def test_count_courses_by_department():
    catalog = CourseCatalog()
    catalog.addCourse("cmpsc", 9, "intermediate python", Event("TR", (1530, 1645), "TD-W 1701"), [])
    catalog.addCourse("cmpsc", 8, "intro python", Event("MW", (1000, 1050), "TD-W 1501"), [])
    catalog.addCourse("math", 34, "calculus", Event("MW", (1100, 1150), "PHELPS 1205"), [])
    counts = catalog.countCoursesByDepartment()
    assert counts == {"CMPSC": 2, "MATH": 1}

def test_removeSection_valid():
    catalog = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "TD-W 1701")
    section1 = Event("W", (1400, 1450), "NORTH HALL 1109")
    section2 = Event("W", (1500, 1550), "NORTH HALL 1109")
    catalog.addCourse("cmpsc", 9, "intermediate python", lecture, [section1, section2])
    result = catalog.removeSection("cmpsc", 9, section2)
    assert result is True
    node = catalog.getNode("cmpsc", 9)
    assert section2 not in node.sections

def test_removeSection_course_not_exist():
    catalog = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "TD-W 1701")
    section = Event("W", (1400, 1450), "NORTH HALL 1109")
    catalog.addCourse("cmpsc", 9, "intermediate python", lecture, [section])
    result = catalog.removeSection("math", 10, section)
    assert result is False

def test_removeSection_section_not_exist():
    catalog = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "TD-W 1701")
    section = Event("W", (1400, 1450), "NORTH HALL 1109")
    catalog.addCourse("cmpsc", 9, "intermediate python", lecture, [section])
    fake_section = Event("F", (1200, 1250), "TD-W 9999")
    result = catalog.removeSection("cmpsc", 9, fake_section)
    assert result is False

def test_removeCourse_empty_tree():
    catalog = CourseCatalog()
    result = catalog.removeCourse("cmpsc", 9)
    assert result is False
    assert catalog.root is None

def test_removeCourse_not_found():
    catalog = CourseCatalog()
    lecture = Event("MW", (1000, 1050), "PHELPS 1205")
    catalog.addCourse("math", 34, "calculus", lecture, [])
    result = catalog.removeCourse("eng", 101)
    assert result is False

def test_removeCourse_case1_leaf():
    catalog = CourseCatalog()
    lecture = Event("MW", (1000, 1050), "PHELPS 1205")
    catalog.addCourse("math", 34, "calculus", lecture, [])
    catalog.addCourse("math", 2, "algebra", lecture, [])
    node = catalog.getNode("math", 2)
    assert node.left is None and node.right is None
    result = catalog.removeCourse("math", 2)
    assert result is True
    assert catalog.getNode("math", 2) is None

def test_removeCourse_case2_one_child():
    catalog = CourseCatalog()
    lecture = Event("MW", (1000, 1050), "PHELPS 1205")
    catalog.addCourse("math", 34, "calculus", lecture, [])
    catalog.addCourse("math", 40, "linear algebra", lecture, [])
    node = catalog.getNode("math", 34)
    assert node.right is not None
    result = catalog.removeCourse("math", 34)
    assert result is True
    assert catalog.getNode("math", 34) is None
    assert catalog.getNode("math", 40) is not None

def test_removeCourse_case3_two_children():
    catalog = CourseCatalog()
    lecture = Event("MWF", (900, 950), "ROOM A")
    catalog.addCourse("cmpsc", 10, "RootCourse", lecture, [])
    catalog.addCourse("cmpsc", 5, "LeftCourse", lecture, [])
    catalog.addCourse("cmpsc", 20, "RightCourse", lecture, [])
    removed = catalog.removeCourse("cmpsc", 10)
    assert removed is True
    new_root = catalog.root
    assert new_root is not None
    assert new_root.department == "CMPSC"
    assert new_root.courseId == 20
    assert new_root.left is not None
    assert new_root.left.courseId == 5

def test_inorder_traversal_after_removals():
    catalog = CourseCatalog()
    catalog.addCourse("art", 10, "painting", Event("TR", (1300, 1550), "ARTS 2628"), [])
    catalog.addCourse("cmpsc", 20, "advanced topics", Event("MWF", (1100, 1150), "HAROLD FRANK 1104"), [])
    catalog.addCourse("math", 24, "differential equations", Event("TR", (800, 915), "BUCHANAN 1910"), [Event("F", (1000, 1050), "GIRVETZ 1112")])
    catalog.addCourse("math", 2, "college algebra", Event("TR", (1400, 1515), "CHEM 1171"), [])
    catalog.addCourse("math", 40, "linear algebra", Event("TR", (1600, 1715), "PHELPS 3515"), [])
    catalog.removeCourse("math", 2)
    catalog.removeCourse("math", 24)
    result = catalog.inOrder().strip().split("\n")
    traversal_str = "\n".join(result)
    assert "ART 10:" in traversal_str
    assert "CMPSC 20:" in traversal_str
    assert "MATH 40:" in traversal_str

def test_bst_inorder_order():
    catalog = CourseCatalog()
    catalog.addCourse("math", 24, "differential equations", Event("TR", (800, 915), "BUCHANAN 1910"), [])
    catalog.addCourse("art", 10, "painting", Event("TR", (1300, 1550), "ARTS 2628"), [])
    catalog.addCourse("cmpsc", 20, "advanced topics", Event("MWF", (1100, 1150), "HAROLD FRANK 1104"), [])
    catalog.addCourse("math", 2, "algebra", Event("TR", (1400, 1515), "CHEM 1171"), [])
    catalog.addCourse("math", 40, "linear algebra", Event("TR", (1600, 1715), "PHELPS 3515"), [])
    in_order_str = catalog.inOrder()
    lines = in_order_str.splitlines()
    header_lines = [line for line in lines if line and not line.startswith(" ") and ":" in line]
    keys = []
    for hl in header_lines:
        parts = hl.split()
        dept = parts[0]
        cid = int(parts[1].replace(":", ""))
        keys.append((dept, cid))
    sorted_keys = sorted(keys)
    assert keys == sorted_keys

def test_multiple_removals():
    catalog = CourseCatalog()
    courses = [("art", 10, "painting"), ("cmpsc", 9, "intermediate python"), ("cmpsc", 20, "advanced topics"), ("math", 34, "calculus"), ("math", 2, "algebra"), ("math", 24, "differential equations"), ("math", 40, "linear algebra")]
    lecture = Event("MW", (1000, 1050), "ROOM X")
    for dept, cid, cname in courses:
        catalog.addCourse(dept, cid, cname, lecture, [])
    removals = [("math", 2), ("cmpsc", 9), ("math", 24)]
    for dept, cid in removals:
        catalog.removeCourse(dept, cid)
    in_order_str = catalog.inOrder()
    lines = in_order_str.splitlines()
    header_lines = [line for line in lines if line and not line.startswith(" ") and ":" in line]
    remaining = []
    for hl in header_lines:
        parts = hl.split()
        dept = parts[0]
        cid = int(parts[1].replace(":", ""))
        remaining.append((dept, cid))
    expected = [("art", 10), ("cmpsc", 20), ("math", 34), ("math", 40)]
    expected = [(d.upper(), cid) for d, cid in expected]
    assert sorted(remaining) == sorted(expected)

def test_remove_root_single_node():
    catalog = CourseCatalog()
    lecture = Event("MW", (1000, 1050), "ROOM Y")
    catalog.addCourse("cmpsc", 11, "singleton", lecture, [])
    removed = catalog.removeCourse("cmpsc", 11)
    assert removed is True
    assert catalog.root is None

def test_parent_pointers():
    catalog = CourseCatalog()
    courses = [("cmpsc", 10, "course10"), ("cmpsc", 5, "course5"), ("cmpsc", 20, "course20"), ("math", 15, "course15"), ("art", 30, "course30")]
    lecture = Event("MWF", (900, 950), "ROOM Z")
    for dept, cid, cname in courses:
        catalog.addCourse(dept, cid, cname, lecture, [])
    def check_parent(node):
        if node is None:
            return True
        if node.parent is not None:
            assert node.parent.left is node or node.parent.right is node
        return check_parent(node.left) and check_parent(node.right)
    assert check_parent(catalog.root)
