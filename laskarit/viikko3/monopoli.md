```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Aloitusruutu "1" -- "1" Monopolipeli
    Aloitusruutu "1" -- "40" Ruutu
    Vankila "1" -- "1" Monopolipeli
    Vankila "1" -- "40" Ruutu
    Sattuma ja yhteismaa "2" -- "40" Ruutu
    Sattuma ja yhteismaa "2" -- "*" Toimintokortti
    Asemat ja Laitokset "4" -- "40" Ruutu
    Normaalit kadut "4" -- "40" Ruutu
    Normaalit kadut "4" -- "2..8" Pelaaja
```