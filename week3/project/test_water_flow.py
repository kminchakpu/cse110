from pytest import approx
import pytest
from water_flow import (
    water_column_height,
    pressure_gain_from_water_height,
    pressure_loss_from_pipe,
    pressure_loss_from_fittings,
    reynolds_number,
    pressure_loss_from_pipe_reduction
)


def test_water_column_height() -> None:
    assert water_column_height(0.0, 0.0) == approx(0.0)
    assert water_column_height(0.0, 10.0) == approx(7.5)
    assert water_column_height(25.0, 0.0) == approx(25.0)
    assert water_column_height(25.0, 10.0) == approx(32.5)


def test_pressure_gain_from_water_height() -> None:
    assert pressure_gain_from_water_height(0.0) == approx(0.0, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)


def test_pressure_loss_from_pipe() -> None:
    assert pressure_loss_from_pipe(0.28687, 0.0, 0.013, 1.65 ) == approx(0.0, abs=0.001)
    assert pressure_loss_from_pipe(0.28687, 1518.2, 0.013, 1.65 ) == approx(-93.485, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 15.0, 0.018, 1.75) == approx(-8.476, abs=0.001)


def test_pressure_loss_from_fittings() -> None:
    assert pressure_loss_from_fittings(1.65, 0) == approx(0.0, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 4) == approx(-0.217, abs=0.01)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=0.01)


def test_reynolds_number() -> None:
    assert reynolds_number(0.28687, 1.65) == approx(471729, rel=0.01)
    assert reynolds_number(0.048692, 1.75) == approx(84922, rel=0.01)


def test_pressure_loss_from_pipe_reduction() -> None:
    reynolds = reynolds_number(0.28687, 1.65)
    loss = pressure_loss_from_pipe_reduction(0.28687, 1.65, reynolds, 0.048692)
    assert loss == approx(-163.744, rel=0.01)

pytest.main(["-v", "--tb=line", "-rN", __file__])