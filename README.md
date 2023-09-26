# VideoGenerator

VideoGenerator er et projekt, der kombinerer forskellige tjenester og scripts for at generere videoer med tilføjet lyd og undertekster. Det bruger teknologier som Docker til at isolere og køre forskellige dele af applikationen.

## Teknologier
- Python: Bruges til scripting og at koordinere de forskellige dele af applikationen.
- Docker: Bruges til at containerisere og køre de forskellige tjenester.
- ElevenLabs: En tjeneste brugt til at generere lyd fra tekst.

## Formål og Eksempel

Dette projekt er inspireret af ønsket om at automatisere skabelsen af indhold, der ligner indholdet i følgende 

[eksempelvideo](https://www.youtube.com/embed/P2kRrulJsPc).

Målet er at automatisere hele processen fra at generere scripts, oprette lyd, tilføje undertekster og klippe videoer i mindre segmenter. Med en fremtidig udvidelse planlægger vi også at tilføje muligheden for automatisk at uploade bearbejdede videoer til YouTube.

### Arbejdsgang

1. **script-generator**: Starter automatisk og genererer scripts ved at interagere med ChatGPT.
2. **elevenlabs-service**: Starter, når script-generation er fuldført, og genererer lyd for det givne script.
3. **auto-subtitle**: Starter, når lydgenerationen er fuldført, og tilføjer undertekster til videoen.
4. **downloaded-videos**: Skal startes manuelt og tager et link til en video som input. Den klipper en længere video i kortere segmenter. Denne service kan også tage en liste af videoer som input.

### Planlagte Forbedringer

- Automatisk upload af bearbejdede videoer til YouTube.

## Sådan Kommer Du i Gang

### Krav
- Docker
- Docker Compose

### Opsætning
1. Klon dette repository til din lokale maskine.
   ```sh
   git clone https://github.com/taxidriver2192/VideoGenerator
   cd videoGenerator
   ```
2. Opret en .env fil i rodmappen af projektet og tilføj ElevenLabs API-nøglen:
   ```txt
   ELEVENLABS_API_KEY=din_api_nøgle
   ```
3. Kør Docker Compose for at bygge og starte tjenesterne:
   ```bash
   docker-compose up --build
   ```

4. Se i makefile

# Sikkerhed
Husk aldrig at dele dine hemmelige API-nøgler. Brug altid miljøvariabler eller andre sikre metoder til at lagre og håndtere følsomme oplysninger i dit projekt.

# License
Dette projekt er MIT licenseret.
