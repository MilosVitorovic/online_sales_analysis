# Online Sales Analysis

## Opis projekta
Projekat simulira sistem za upravljanje proizvodima i korpom kupca u online prodavnici.

## Klase i funkcionalnosti

### Product
- name: ime proizvoda
- price: cena proizvoda
- quantity: količina proizvoda
- Metod `display_info()`
- Metod `update_quantity(new_quantity)`

### ProductManager
- Lista svih proizvoda
- Dodavanje proizvoda (`add_product`)
- Prikaz proizvoda (`show_products`)
- Ukupna vrednost inventara (`total_inventory_value`)
- Uklanjanje proizvoda (`remove_product`)

### Cart
- Lista proizvoda u korpi (`cart_items`)
- Dodavanje proizvoda (`add_to_cart`)
- Prikaz sadržaja korpe (`show_cart`)
- Izračunavanje ukupne vrednosti (`total_cart_value`)

## Kako pokrenuti
1. Kreirati instancu `ProductManager` i dodati proizvode
2. Kreirati instancu `Cart` i dodati proizvode iz `ProductManager`
3. Pokrenuti `main.py`
