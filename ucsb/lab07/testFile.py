import pytest
from Tea import Tea
from CustomTea import CustomTea
from SpecialtyTea import SpecialtyTea
from TeaOrder import TeaOrder
from OrderQueue import OrderQueue, QueueEmptyException

def test_custom_tea():
    tea1 = CustomTea("M", "White")
    assert tea1.getTeaDetails() == "CUSTOM TEA\nSize: M\nBase: White\nFlavors:\nPrice: $15.00\n"

    tea1.addFlavor("vanilla")
    tea1.addFlavor("mint")
    assert tea1.getTeaDetails() == \
        "CUSTOM TEA\nSize: M\nBase: White\nFlavors:\n\t+ vanilla\n\t+ mint\nPrice: $16.00\n"

    tea2 = CustomTea("S", "Black")
    assert tea2.getTeaDetails() == "CUSTOM TEA\nSize: S\nBase: Black\nFlavors:\nPrice: $10.00\n"

    tea3 = CustomTea("L", "Green")
    for i in range(10):
        tea3.addFlavor(f"flavor{i}")
    assert tea3.getPrice() == 20 + (10 * 0.75)

def test_specialty_tea():
    tea1 = SpecialtyTea("L", "Chamomile")
    assert tea1.getTeaDetails() == "SPECIALTY TEA\nSize: L\nName: Chamomile\nPrice: $20.00\n"

    tea2 = SpecialtyTea("S", "Hibiscus")
    assert tea2.getTeaDetails() == "SPECIALTY TEA\nSize: S\nName: Hibiscus\nPrice: $12.00\n"

    sp1 = SpecialtyTea("L", "MAX S")

    expected_output = (
        "SPECIALTY TEA\n"
        "Size: L\n"
        "Name: MAX S\n"
        "Price: $20.00\n"
    )
    assert sp1.getTeaDetails() == expected_output

def test_tea_order():
    order = TeaOrder(150)
    assert order.getOrderDescription() == "******\nShipping Distance: 150 miles\nTOTAL ORDER PRICE: $0.00\n******\n"

    tea1 = CustomTea("S", "Oolong")
    tea1.addFlavor("honey")
    tea2 = SpecialtyTea("M", "Matcha")

    order.addTea(tea1)
    order.addTea(tea2)

    assert "CUSTOM TEA" in order.getOrderDescription()
    assert "SPECIALTY TEA" in order.getOrderDescription()
    assert "TOTAL ORDER PRICE: $26.25" in order.getOrderDescription()

    ct1 = CustomTea("M", "Black")
    ct1.addFlavor("honey")
    ct1.addFlavor("cardamom")
    st1 = SpecialtyTea("L", "Matcha")
    order = TeaOrder(200)
    order.addTea(ct1)
    order.addTea(st1)

    expected_output = (
        "******\n"
        "Shipping Distance: 200 miles\n"
        "CUSTOM TEA\n"
        "Size: M\n"
        "Base: Black\n"
        "Flavors:\n"
        "\t+ honey\n"
        "\t+ cardamom\n"
        "Price: $16.00\n"
        "\n"
        "----\n"
        "SPECIALTY TEA\n"
        "Size: L\n"
        "Name: Matcha\n"
        "Price: $20.00\n"
        "\n"
        "----\n"
        "TOTAL ORDER PRICE: $36.00\n"
        "******\n"
    )

    assert order.getOrderDescription() == expected_output
def test_order_queue():
    queue = OrderQueue()

    with pytest.raises(QueueEmptyException):
        queue.processNextOrder()

    order1 = TeaOrder(300)
    order2 = TeaOrder(100)
    order3 = TeaOrder(500)
    order4 = TeaOrder(400)

    queue.addOrder(order1)
    queue.addOrder(order2)
    queue.addOrder(order3)
    queue.addOrder(order4)

    assert "Shipping Distance: 500 miles" in queue.processNextOrder()
    assert "Shipping Distance: 400 miles" in queue.processNextOrder()
    assert "Shipping Distance: 300 miles" in queue.processNextOrder()
    assert "Shipping Distance: 100 miles" in queue.processNextOrder()

    with pytest.raises(QueueEmptyException):
        queue.processNextOrder()

def test_edge_cases():
    queue = OrderQueue()
    order1 = TeaOrder(250)
    order2 = TeaOrder(250)

    queue.addOrder(order1)
    queue.addOrder(order2)

    desc1 = queue.processNextOrder()
    desc2 = queue.processNextOrder()
    assert "Shipping Distance: 250 miles" in desc1
    assert "Shipping Distance: 250 miles" in desc2

    empty_order = TeaOrder(50)
    queue.addOrder(empty_order)
    assert "TOTAL ORDER PRICE: $0.00" in queue.processNextOrder()

    large_order = TeaOrder(999999)
    queue.addOrder(large_order)
    assert "Shipping Distance: 999999 miles" in queue.processNextOrder()
