from dataclasses import dataclass, field
from typing import List

@dataclass
class Pet:
    name: str
    species: str
    age: int

@dataclass
class PetCatalog:
    pets: List[Pet] = field(default_factory=list)
    
    def add(self, name: str, species: str, age: int) -> None:
        """Добавить питомца."""
        self.pets.append(Pet(name=name, species=species, age=age))
    
    def get_younger_than(self, max_age: int) -> List[Pet]:
        """Получить питомцев младше указанного возраста."""
        return [pet for pet in self.pets if pet.age < max_age]
    
    def display(self, pets_list: List[Pet] = None) -> None:
        """Вывести список питомцев."""
        if pets_list is None:
            pets_list = self.pets
            
        if not pets_list:
            print("Список питомцев пуст.")
            return
            
        print("\n" + "=" * 50)
        print(f"{'Кличка':<15} {'Вид':<15} {'Возраст':<10}")
        print("=" * 50)
        
        for pet in pets_list:
            print(f"{pet.name:<15} {pet.species:<15} {pet.age:<10}")
        print("=" * 50)
