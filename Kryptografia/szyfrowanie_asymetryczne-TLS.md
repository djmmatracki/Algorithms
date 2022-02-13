# Szyfrowanie asymetryczne

Pierwszym krokiem jest wygenerowanie dwóch różnych kluczy, które wyglądają zupełnie inaczej, ale są związane algorytmem. Jeden z nich to klucz prywatny, a drugi to klucz publiczny. Klucze publiczne można dowolnie dytrybułować zgodnie z potrzebami, natomiast klucz prywatny ma być sekretem właściciela pary kluczy.

Główna zasada procesu polega na tym, że jeśli coś zostanie zaszyfrowane za pomocą jednego z kluczy, można to odszyfrować tylko za pomocą drugiego z nich.

## Algorytm SSL/TLS

Protokół SSL powstał, by zapewnić więkrze bezpieczeństwo protokołowi HTTP. Po latach SSL ustąpił miejsca bardziej wydajnemu i bezpieczniejszemu standardowi TLS.

Podczas procesu TLS wykonywane są następujące kroki:


1. Klient wysyłą do serwera wiadomość "hello world". Wiadomość ta zawiera również:
 - wersję używanego protokołu TLS.
 - zestaw szyfrów wspieranych po stronie klienta
 - algorytm kompresji
 - losowy łańcuch bajtów określany jako byte_client.

2. Serwer w odpowiedzi wysyła wiadomość "hello". Wiadomość ta zawiera również:
 - zestaw szyfrów wybranych przez serwer z listy otrzymanej od klienta
 - identyfikator sesji
 - losowy łańcuch bajtów określany jako byte_server
 - cyfrowy certyfikat serwera, identyfikowany jak cert_server, zawierający klucz publiczny serwera

3. Klient weryfikuje cert_server
4. Klient generuje losowy łańcuch bajtów, identyfikowany jako byte_client2 i szyfruje go kluczem publicznym serwera uzyskanym za pomocą cert_server.
5. Klient generuje losowy łańcuch bajtów i rozpoznaje wiadomości zaszyfrowane za pomocą klucza publicznego.
6. Serwer weryfikuje certyfikat klienta.
7. Klient wysyła wiadomość do serwera finished, która została wcześniej zaszyfrowana tajnym kluczem.
8. Aby potwierdzić komunikację ze strony serwera, serwer wysyła klientowi wiadomość finished, która równiez została wcześniej zaszyfrowana tajnym kluczem.
9. Serwer i klient teraz stworzyły bezpieczny kanał. Mogą wymieniać wiadomości szyfrowane symetrycznie za pomocą współdzielonego sekretnego klucza.