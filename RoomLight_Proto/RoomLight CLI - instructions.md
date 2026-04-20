## RoomLight CLI - instructions

### Käynnistys

Avaa terminaali ja aja komento tiedoston sijainnissa:

`python roomlight_cli.py`

Kun näet kehotteen `(RoomLight)` , ohjelma on valmis vastaanottamaan komentoja.

## Järjestelmäkomennot

| komento | kuvaus                                                                        |
| ------- | ----------------------------------------------------------------------------- |
| `help`  | Näyttää listan kaikista komennoista. `help [komento]` antaa tarkemmat ohjeet. |
| `leave` | Sulkee simulaation.                                                           |

### Käyttäjien simulointi

| komento | esimerkki     | kuvaus                                                                                               |
| ------- | ------------- | ---------------------------------------------------------------------------------------------------- |
| `enter` | `enter guest` | Henkilö astuu huoneeseen. Roolit: `guest` (vain eteinen syttyy) tai `staff` (kaikki valot syttyvät). |
| `leave` | `leave`       | Yksi henkilö poistuu. Kun huone on tyhjä, kaikki valot sammuvat automaattisesti.                     |

### Alueellinen liikkuminen

Saatavilla olevat alueet: `bathroom`, `bed`, `desk`, `` `entrance`, `living_room`

| komento      | esimerkki        | kuvaus                                        |
| ------------ | ---------------- | --------------------------------------------- |
| `area_enter` | `area_enter bed` | Sytyttää tietyn alueen valon (100% kirkkaus). |
| `area_leave` | `area_leave bed` | Sammuttaa tietyn alueen valon.                |

### Valaistusteemat

Saatavilla olevat teemat: `relax`, `working`, `wakeup`, `night`

| komento | esimerkki    | kuvaus                                                                                      |
| ------- | ------------ | ------------------------------------------------------------------------------------------- |
| `mood`  | `mood relax` | Muuttaa koko huoneen valaistuksen valitun teeman mukaiseksi (asettaa tietyt kirkkaustasot). |

### Huolto ja visualisointi

| komento          | esimerkki                 | kuvaus                                                                            |
| ---------------- | ------------------------- | --------------------------------------------------------------------------------- |
| `map`            | `map`                     | Tulostaa visuaalisen ASCII-pohjapiirroksen huoneesta ja valojen tiloista.         |
| `dashboard`      | `dashboard`               | Näyttää huollon ohjauspaneelin (huoneen varausaste, valojen tilat ja kirkkaudet). |
| `simulate_fault` | `simulate_fault bathroom` | Simuloi vikatilanteen tiettyyn valoon.                                            |
| `reset_fault`    | `reset_fault bathroom`    | Korjaa vikakoodin ja palauttaa valon normaaliin tilaan (pois päältä).             |
