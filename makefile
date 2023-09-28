
up:
	docker-compose up --build -d

down:
	docker-compose down

ssh_app:
	docker exec -it videogenerator-my-app-1 /bin/bash

ssh_elevenlabs-service:
	docker exec -it videogenerator-elevenlabs-service-1 /bin/bash

ssh_downloaded-videos:
	docker exec -it videogenerator-downloaded-videos-1 /bin/bash

ssh_auto-subtitle:
	docker exec -it videogenerator-auto-subtitle-1 /bin/bash
