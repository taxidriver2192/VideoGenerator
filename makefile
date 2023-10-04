
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

build_downloaded-videos:
	docker-compose up --build -d downloaded-videos
	docker-compose exec downloaded-videos /bin/bash -c "python3 download_video.py https://www.youtube.com/watch?v=C40Ds-0_kX4"

build_and_start_my_app:
	docker-compose up --build -d my-app
	docker-compose exec my-app /bin/bash
	
build_and_start_elevenlabs_service:
	docker-compose up --build -d elevenlabs-service
	docker-compose exec elevenlabs-service /bin/bash -c "python3 generateAudio.py"

build_and_start_elevenlabs_service_skip_api:
	docker-compose up --build -d elevenlabs-service
	docker-compose exec elevenlabs-service /bin/bash -c "python3 generateAudio.py --skip-api"

build_and_start_auto_subtitle:
	docker-compose up --build -d auto-subtitle
	docker-compose exec auto-subtitle /bin/bash -c "python3 auto_subtitle.py"