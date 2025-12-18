#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import math
from vector_package.vector import Vector


class TestVector:
    def test_vector_creation_int(self):
        v = Vector[int](3, 4)
        assert v.x == 3
        assert v.y == 4
        assert isinstance(v.x, int)
        assert isinstance(v.y, int)

    def test_vector_creation_float(self):
        v = Vector[float](3.5, 4.5)
        assert v.x == 3.5
        assert v.y == 4.5
        assert isinstance(v.x, float)
        assert isinstance(v.y, float)

    def test_vector_invalid_type(self):
        with pytest.raises(TypeError):
            Vector[str]("a", "b")

    def test_length_calculation(self):
        v1 = Vector[int](3, 4)
        assert math.isclose(v1.length(), 5.0, rel_tol=1e-10)

        v2 = Vector[int](0, 0)
        assert math.isclose(v2.length(), 0.0, rel_tol=1e-10)

        v3 = Vector[float](1.0, 1.0)
        expected_length = math.sqrt(2.0)
        assert math.isclose(v3.length(), expected_length, rel_tol=1e-10)

    def test_eq_same_length(self):
        v1 = Vector[int](3, 4)
        v2 = Vector[int](0, 5)
        v3 = Vector[float](5.0, 0.0)
        
        assert v1 == v2
        assert v1 == v3
        assert v2 == v3

    def test_eq_different_length(self):
        v1 = Vector[int](1, 1)
        v2 = Vector[int](3, 4)
        v3 = Vector[int](0, 0)
        
        assert v1 != v2
        assert v1 != v3
        assert v2 != v3

    def test_eq_with_same_vector(self):
        v = Vector[int](3, 4)
        assert v == v

    def test_eq_with_different_type(self):
        v = Vector[int](3, 4)
        assert v != "not a vector"
        assert v != 123
        assert v != [3, 4]

    def test_eq_float_precision(self):
        v1 = Vector[float](1.0, 1.0)
        v2 = Vector[float](math.sqrt(2.0), 0.0)
        
        assert v1 == v2
        
        v3 = Vector[float](0.0, math.sqrt(2.0))
        assert v1 == v3
        
        v4 = Vector[float](2.0, 0.0)
        assert v1 != v4

    def test_repr_includes_length(self):
        v = Vector[int](3, 4)
        repr_str = repr(v)
        assert "Vector" in repr_str
        assert "x=3" in repr_str
        assert "y=4" in repr_str
        assert "length=5.00" in repr_str

    def test_post_init_type_check(self):
        Vector[int](1, 2)
        Vector[float](1.0, 2.0)
        Vector[float](1, 2.0)
        
        with pytest.raises(TypeError):
            Vector[str]("a", "b")
        
        with pytest.raises(TypeError):
            Vector[list]([1], [2])

    def test_generic_type_parameter(self):
        v_int: Vector[int] = Vector[int](1, 2)
        assert isinstance(v_int.x, int)
        
        v_float: Vector[float] = Vector[float](1.5, 2.5)
        assert isinstance(v_float.x, float)
        
        result = v_int.length()
        assert isinstance(result, float)

    def test_compare_false_decorator(self):
        v1 = Vector[int](1, 2)
        v2 = Vector[int](1, 2)
        v3 = Vector[int](2, 1)
        
        assert v1 == v2
        assert v1 == v3


def test_vector_integration():
    vectors = [
        Vector[int](3, 4),
        Vector[int](5, 0),
        Vector[int](0, 5),
        Vector[int](1, 2),
        Vector[int](2, 1),
    ]
    
    length_groups = {}
    for v in vectors:
        length = round(v.length(), 3)
        if length not in length_groups:
            length_groups[length] = []
        length_groups[length].append(v)
    
    for length, group in length_groups.items():
        if len(group) > 1:
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    assert group[i] == group[j]
    
    lengths = list(length_groups.keys())
    for i in range(len(lengths)):
        for j in range(i + 1, len(lengths)):
            v1 = length_groups[lengths[i]][0]
            v2 = length_groups[lengths[j]][0]
            assert v1 != v2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])