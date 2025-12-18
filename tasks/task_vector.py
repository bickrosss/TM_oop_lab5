from vector_package.vector import Vector
import math

def main() -> None:
    
    print("\n1. Векторы с целыми координатами:")
    lazy_vector1 = Vector[int](3, 4)
    lazy_vector2 = Vector[int](6, 8)
    print(f"   v1: {lazy_vector1}")
    print(f"   v2: {lazy_vector2}")
    print(f"   v1 == v2? {lazy_vector1 == lazy_vector2} (одинаковые длины 5.0 и 10.0)")
    
    print("\n2. Векторы с float координатами:")
    lazy_vector3 = Vector[float](1.0, 1.0)
    lazy_vector4 = Vector[float](math.sqrt(2), 0.0)
    print(f"   v3: {lazy_vector3}")
    print(f"   v4: {lazy_vector4}")
    print(f"   v3 == v4? {lazy_vector3 == lazy_vector4} (длины ≈1.41)")
    
    print("\n3. Векторы с разными длинами:")
    lazy_vector5 = Vector[int](1, 2)
    lazy_vector6 = Vector[int](3, 4)
    print(f"   v5: {lazy_vector5}")
    print(f"   v6: {lazy_vector6}")
    print(f"   v5 == v6? {lazy_vector5 == lazy_vector6} (разные длины)")
    
    print("\n4. Сравнение с тем же вектором:")
    lazy_vector7 = Vector[float](5.0, 12.0)
    print(f"   v7: {lazy_vector7}")
    print(f"   v7 == v7? {lazy_vector7 == lazy_vector7}")
    
    print("\n5. Сравнение с не вектором:")
    print(f"   v1 == 'не вектор'? {lazy_vector1 == 'не вектор'}")


if __name__ == "__main__":
    main()