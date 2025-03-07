from Event import Event
from CourseCatalogNode import CourseCatalogNode
from CourseCatalog import CourseCatalog


def test_event_equality_und_str():
    e1 = Event("MWF", (900, 1030), "raum a")
    e2 = Event("MWF", (900, 1030), "RAUM A")
    e3 = Event("MWF", (900, 1030), "Raum B")
    assert e1 == e2
    assert e1 != e3
    expected = "MWF 09:00 - 10:30, RAUM A"
    assert str(e1) == expected


def test_course_catalog_node_str():
    lecture = Event("TR", (1100, 1230), "labor 101")
    section1 = Event("M", (1300, 1400), "labor 102")
    section2 = Event("W", (1400, 1500), "labor 103")
    lecture2 = Event("TR", (1100, 1230), "labor 101")
    section3 = Event("M", (1300, 1400), "labor 102")
    section4 = Event("W", (1400, 1500), "labor 103")
    node = CourseCatalogNode("bio", 201, "biologie grundkurs", lecture, [section1, section2])
    node2 = CourseCatalogNode("bio", 201, "biologie grundkurs", lecture2, [section3, section4])
    expected = (
            "BIO 201: BIOLOGIE GRUNDKURS\n"
            " * Lecture: TR " + Event.format((1100, 1230)) + ", LABOR 101\n"
            " + Section: M " + Event.format((1300, 1400)) + ", LABOR 102\n"
            " + Section: W " + Event.format((1400, 1500)) + ", LABOR 103\n"
            "BIO 201: BIOLOGIE GRUNDKURS\n"
            " * Lecture: TR " + Event.format((1100, 1230)) + ", LABOR 101\n"
            " + Section: M " + Event.format((1300, 1400)) + ", LABOR 102\n"
            " + Section: W " + Event.format((1400, 1500)) + ", LABOR 103\n"
    )
    assert str(node) + str(node2) == expected


def test_add_course_und_duplicates():
    cc = CourseCatalog()
    lecture = Event("TR", (1000, 1130), "halle 1")
    section = Event("M", (1200, 1300), "halle 2")
    assert cc.addCourse("chem", 101, "allgemeine chemie", lecture, [section]) is True
    assert cc.addCourse("CHEM", 101, "allgemeine chemie", lecture, [section]) is False


def test_add_section():
    cc = CourseCatalog()
    lecture = Event("MW", (900, 1030), "raum x")
    cc.addCourse("phys", 202, "physik II", lecture, [])
    new_section = Event("F", (1100, 1200), "raum y")
    assert cc.addSection("phys", 202, new_section) is True
    result = cc.getAttendableSections("phys", 202, "F", (0, 2359))
    expected = "F " + Event.format((1100, 1200)) + ", RAUM Y\n"
    assert result == expected
    fake_section = Event("T", (1300, 1400), "raum z")
    assert cc.addSection("phys", 999, fake_section) is False


def test_traversals():
    cc = CourseCatalog()
    eng_202 = Event("TR", (900, 1030), "engl hall")
    math_101 = Event("MW", (1000, 1130), "mathe hall")
    eng_101 = Event("MW", (1100, 1230), "engl hall")
    hist_300 = Event("TR", (1300, 1430), "gesch hall")
    cc.addCourse("eng", 202, "fortgeschrittenes english", eng_202, [])
    cc.addCourse("math", 101, "analysis", math_101, [])
    cc.addCourse("eng", 101, "grundlagen english", eng_101, [])
    cc.addCourse("hist", 300, "weltgeschichte", hist_300, [])

    in_order = cc.inOrder()
    lines = in_order.split("\n")
    expected_order = [
        "ENG 101: GRUNDLAGEN ENGLISH",
        "ENG 202: FORTGESCHRITTENES ENGLISH",
        "HIST 300: WELTGESCHICHTE",
        "MATH 101: ANALYSIS"
    ]
    node_headers = [line for line in lines if line and not line.startswith(" ") and ":" in line]
    assert node_headers == expected_order

    pre_order = cc.preOrder().split("\n")
    post_order = cc.postOrder().split("\n")
    for expected in expected_order:
        assert any(expected in line for line in pre_order)
        assert any(expected in line for line in post_order)


def test_get_attendable_sections_edge_cases():
    cc = CourseCatalog()
    lecture = Event("TR", (800, 930), "raum a")
    section1 = Event("M", (1000, 1100), "raum b")
    section2 = Event("W", (1200, 1300), "raum c")
    section3 = Event("F", (1400, 1500), "raum d")
    cc.addCourse("econ", 205, "mikroökonomie", lecture, [section1, section2, section3])

    result = cc.getAttendableSections("econ", 205, "T", (0, 2359))
    assert result == ""

    result = cc.getAttendableSections("econ", 205, "M", (1100, 1200))
    assert result == ""

    result = cc.getAttendableSections("econ", 205, "M", (1000, 1100))
    expected = "M " + Event.format((1000, 1100)) + ", RAUM B\n"
    assert result == expected


def test_count_courses_by_department():
    cc = CourseCatalog()
    lecture = Event("MW", (900, 1030), "raum x")
    cc.addCourse("eng", 101, "grundlagen english", lecture, [])
    cc.addCourse("eng", 102, "literatur", lecture, [])
    cc.addCourse("hist", 201, "moderne geschichte", lecture, [])
    cc.addCourse("math", 301, "lineare algebra", lecture, [])
    cc.addCourse("math", 302, "diskrete mathematik", lecture, [])
    counts = cc.countCoursesByDepartment()
    expected = {"ENG": 2, "HIST": 1, "MATH": 2}
    assert counts == expected
