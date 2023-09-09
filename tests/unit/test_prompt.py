from unittest.mock import MagicMock
from unittest.mock import Mock

import pytest

import inquirer3


@pytest.fixture()
def render_mock_raise_keyboard():
    render = Mock()
    render.render = Mock(side_effect=KeyboardInterrupt)
    yield render


def test_prompt_returns_a_hash():
    answers = inquirer3.prompt([])
    assert answers == {}


def test_prompt_renders_a_questions():
    question1 = MagicMock()
    question1.name = "foo"
    result1 = object()
    render = Mock()
    render.render.return_value = result1


def test_raise_keyboard(render_mock_raise_keyboard):
    with pytest.raises(KeyboardInterrupt):
        inquirer3.prompt([MagicMock()], render=render_mock_raise_keyboard, raise_keyboard_interrupt=True)
