from pet_catalog import PetCatalog, Pet
if __name__ == "__main__":
    catalog = PetCatalog()
    
    catalog.add("Барсик", "Кот", 3)
    catalog.add("Шарик", "Собака", 5)
    catalog.add("Кеша", "Попугай", 2)
    
    print("Все питомцы:")
    catalog.display()
    
    young_pets = catalog.get_younger_than(4)
    print(f"\nПитомцы младше 4 лет:")
    catalog.display(young_pets)