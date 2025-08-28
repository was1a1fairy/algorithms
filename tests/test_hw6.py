#2
import pytest
from hw6 import TaskStack, ProjectTask


@pytest.fixture
def empty_stack():
    return TaskStack()


@pytest.fixture
def task():
    return ProjectTask("meow1", "01.01.2025")


@pytest.fixture
def task1():
    return ProjectTask("meow2", "01.01.2024")


@pytest.fixture
def task2():
    return ProjectTask("meow3", "01.01.2023")


@pytest.fixture
def fill_stack():
    stack = TaskStack()
    stack.push(ProjectTask("meow", "01.01.2025"))
    return stack


def test_peek(fill_stack, empty_stack):
    assert fill_stack.peek() == "meow, 01.01.2025"
    assert empty_stack.peek() is None


def test_count(fill_stack, empty_stack):
    assert fill_stack.count() == 1
    assert empty_stack.count() == 0


def test_is_empty(fill_stack, empty_stack):
    assert empty_stack.is_empty() == True
    assert fill_stack.is_empty() == False


def test_pop(empty_stack, fill_stack):
    assert empty_stack.pop() is None
    assert fill_stack.pop() == "meow, 01.01.2025"
    assert fill_stack.pop() is None


def test_stack_push(empty_stack, task):
    empty_stack.push(task)
    assert empty_stack.is_empty() == False
    assert empty_stack.peek() == task.__str__()
    assert empty_stack.pop() == task.__str__()


def test_script(empty_stack, task, task1, task2):
    empty_stack.push(task)
    empty_stack.push(task1)
    empty_stack.push(task2)
    assert empty_stack.count() == 3
    assert empty_stack.pop() == task2.__str__()
    assert empty_stack.count() == 2
    assert empty_stack.pop() == task1.__str__()
    assert empty_stack.is_empty() == False



#3