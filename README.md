# File manager
---

1. **`file_operations.py`**:
   Ten moduł zawiera zestaw funkcji służących do zarządzania plikami i katalogami. Oferuje takie operacje jak:
   - Usuwanie plików lub katalogów (`remove_file_or_dir`).
   - Zmiana nazwy lub przenoszenie plików/katalogów (`rename_file_or_dir`).
   - Kopiowanie plików (`copy_file`).
   Każda operacja uwzględnia kontrolę istnienia plików oraz obsługę błędów. Funkcje te są odpowiednie do automatyzacji zadań związanych z zarządzaniem plikami.

---

2. **`manager.py`**:
   Menedżer operacji masowych na plikach, który pozwala na wykonywanie akcji takich jak masowe kopiowanie i przenoszenie plików na podstawie ich rozszerzeń. Dzięki temu narzędziu użytkownik może automatyzować procesy zarządzania dużą ilością plików. Implementacja uwzględnia obsługę potencjalnych konfliktów, takich jak nadpisywanie istniejących plików.

---

3. **`mass_operations.py`**:
   Moduł ten dostarcza funkcje do masowej manipulacji plikami, takie jak kopiowanie, przenoszenie czy usuwanie wielu plików na podstawie ich rozszerzeń. Funkcje mogą działać interaktywnie, pytając użytkownika o zgodę na nadpisanie plików, co czyni je bardziej elastycznymi w użytkowaniu. Narzędzie to jest przydatne w zarządzaniu dużymi zbiorami plików, zwłaszcza w kontekście systemów plików zawierających wiele plików o podobnych rozszerzeniach.

---

4. **`utilities.py`**:
   Moduł pomocniczy zawierający różne narzędzia do obsługi systemu plików:
   - Funkcja `converting_bytes` umożliwia konwersję rozmiarów plików na czytelne jednostki (B, KB, MB, itd.).
   - Funkcja `printing_directory` wyświetla w uporządkowany sposób zawartość katalogu, dzieląc wyniki na pliki i podkatalogi. Ten moduł dostarcza prostych, ale przydatnych funkcji do codziennej pracy z plikami.
