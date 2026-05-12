# System elektronicznego awizowania korespondencji przychodzącej



Inteligentny system monitorowania skrzynek pocztowych oparty na ekosystemie IoT, który automatyzuje proces wykrywania i powiadamiania o nadejściu nowej korespondencji.



\-----------------------------------------------------------------------------------------------------------------------

Kluczowe Funkcjonalności:

Inteligentna Detekcja: Moduł ESP32 z czujnikiem i kamerą wykrywa przesyłkę i wykonuje jej zdjęcie w momencie dostarczenia.

Powiadomienia Real-time: Automatyczna wysyłka powiadomień e-mail do adresata wraz ze zdjęciem przesyłki w załączniku.

Zarządzanie Użytkownikami: Webowy panel administracyjny umożliwiający pełne zarządzanie bazą użytkowników (CRUD).

Skalowalność: Architektura przygotowana do obsługi wielu urządzeń ESP32 w jednej sieci oraz integracji z automatyką budynkową.

\-----------------------------------------------------------------------------------------------------------------------

Stos Technologiczny:

Hardware: ESP32 (z modułem kamery i czujnikiem obecności).

Backend: Flask (Python) – przetwarzanie danych i obsługa API.

Komunikacja: Protokół HTTP / SMTP (powiadomienia).

Frontend: Interfejs webowy do administracji systemem.

\-----------------------------------------------------------------------------------------------------------------------

Układ katalogów:

/core - Kod źródłowy dla mikrokontrolera ESP32.

/assets - Dodatkowe artefakty, takie jak grafiki UI panelu administracyjnego.

/docs - Specyfikacje techniczne, schematy podłączenia pinów oraz dokumentacja API.

/.vscode - Pliki konfiguracyjne środowiska IDE

