# VideoGenerator

VideoGenerator er et projekt, der kombinerer forskellige tjenester og scripts for at generere videoer med tilføjet lyd og undertekster. Det bruger teknologier som Docker til at isolere og køre forskellige dele af applikationen.

## Teknologier
- Python: Bruges til scripting og at koordinere de forskellige dele af applikationen.
- Docker: Bruges til at containerisere og køre de forskellige tjenester.
- ElevenLabs: En tjeneste brugt til at generere lyd fra tekst.

## Struktur
Projektet er opdelt i forskellige undermapper, hver repræsenterer en del af applikationen:
- `elevenlabs-service`: Indeholder scripts og Dockerfile for at generere lyd fra tekst ved hjælp af ElevenLabs.
- `auto-subtitle`: Indeholder scripts og Dockerfile for at generere undertekster.
- `downloaded-videos`: Indeholder scripts og Dockerfile for at hente videoer.
- `script-generator`: Indeholder scripts og Dockerfile for at generere scripts gennem chatgpt.

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