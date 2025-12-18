#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from pet_catalog import Pet, PetCatalog


class TestPet:
    def test_pet_creation(self):
        pet = Pet(name="Барсик", species="Кот", age=3)
        assert pet.name == "Барсик"
        assert pet.species == "Кот"
        assert pet.age == 3

    def test_pet_defaults(self):
        pet = Pet(name="Шарик", species="Собака", age=5)
        assert pet.name == "Шарик"
        assert pet.species == "Собака"
        assert pet.age == 5

    def test_pet_repr(self):
        pet = Pet(name="Кеша", species="Попугай", age=2)
        repr_str = repr(pet)
        assert "Кеша" in repr_str
        assert "Попугай" in repr_str
        assert "2" in repr_str


class TestPetCatalog:
    @pytest.fixture
    def empty_catalog(self):
        return PetCatalog()

    @pytest.fixture
    def filled_catalog(self):
        catalog = PetCatalog()
        catalog.add("Барсик", "Кот", 3)
        catalog.add("Шарик", "Собака", 5)
        catalog.add("Кеша", "Попугай", 2)
        return catalog

    def test_empty_catalog(self, empty_catalog):
        assert len(empty_catalog.pets) == 0
        assert empty_catalog.pets == []

    def test_add_pet(self, empty_catalog):
        empty_catalog.add("Мурзик", "Кот", 1)
        assert len(empty_catalog.pets) == 1
        assert empty_catalog.pets[0].name == "Мурзик"
        assert empty_catalog.pets[0].species == "Кот"
        assert empty_catalog.pets[0].age == 1

    def test_add_multiple_pets(self, empty_catalog):
        empty_catalog.add("Барсик", "Кот", 3)
        empty_catalog.add("Шарик", "Собака", 5)
        empty_catalog.add("Кеша", "Попугай", 2)
        
        assert len(empty_catalog.pets) == 3
        assert empty_catalog.pets[0].name == "Барсик"
        assert empty_catalog.pets[1].name == "Шарик"
        assert empty_catalog.pets[2].name == "Кеша"

    def test_get_younger_than_empty(self, empty_catalog):
        result = empty_catalog.get_younger_than(4)
        assert result == []
        assert len(result) == 0

    def test_get_younger_than(self, filled_catalog):
        young_pets = filled_catalog.get_younger_than(4)
        assert len(young_pets) == 2
        
        names = [pet.name for pet in young_pets]
        assert "Барсик" in names
        assert "Кеша" in names
        assert "Шарик" not in names

    def test_get_younger_than_all(self, filled_catalog):
        all_pets = filled_catalog.get_younger_than(10)
        assert len(all_pets) == 3
        assert all_pets == filled_catalog.pets

    def test_get_younger_than_none(self, filled_catalog):
        no_pets = filled_catalog.get_younger_than(1)
        assert len(no_pets) == 0
        assert no_pets == []

    def test_display_empty(self, empty_catalog, capsys):
        empty_catalog.display()
        captured = capsys.readouterr()
        assert "Список питомцев пуст." in captured.out

    def test_display_with_pets(self, filled_catalog, capsys):
        filled_catalog.display()
        captured = capsys.readouterr()
        
        assert "Барсик" in captured.out
        assert "Шарик" in captured.out
        assert "Кеша" in captured.out
        assert "Кот" in captured.out
        assert "Собака" in captured.out
        assert "Попугай" in captured.out

    def test_display_custom_list(self, filled_catalog, capsys):
        custom_list = [Pet(name="Тест", species="Животное", age=1)]
        filled_catalog.display(custom_list)
        
        captured = capsys.readouterr()
        assert "Тест" in captured.out
        assert "Животное" in captured.out
        assert "1" in captured.out
        assert "Барсик" not in captured.out

    def test_pet_equality(self):
        pet1 = Pet(name="Барсик", species="Кот", age=3)
        pet2 = Pet(name="Барсик", species="Кот", age=3)
        pet3 = Pet(name="Мурзик", species="Кот", age=3)
        
        assert pet1 == pet2
        assert pet1 != pet3

    def test_catalog_equality(self):
        catalog1 = PetCatalog()
        catalog1.add("Барсик", "Кот", 3)
        
        catalog2 = PetCatalog()
        catalog2.add("Барсик", "Кот", 3)
        
        catalog3 = PetCatalog()
        catalog3.add("Шарик", "Собака", 5)
        
        assert catalog1 == catalog2
        assert catalog1 != catalog3


def test_pet_catalog_integration():
    catalog = PetCatalog()
    
    assert len(catalog.pets) == 0
    
    catalog.add("Барсик", "Кот", 3)
    catalog.add("Шарик", "Собака", 5)
    catalog.add("Кеша", "Попугай", 2)
    
    assert len(catalog.pets) == 3
    
    young_pets = catalog.get_younger_than(4)
    assert len(young_pets) == 2
    
    old_pets = catalog.get_younger_than(10)
    assert len(old_pets) == 3
    
    no_pets = catalog.get_younger_than(1)
    assert len(no_pets) == 0
    
    pet_names = [pet.name for pet in catalog.pets]
    assert "Барсик" in pet_names
    assert "Шарик" in pet_names
    assert "Кеша" in pet_names


if __name__ == "__main__":
    pytest.main([__file__, "-v"])