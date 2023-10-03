# VideoGenerator

VideoGenerator is a project that combines different services and scripts to generate videos with added audio and subtitles. It uses technologies such as Docker to isolate and run different parts of the application.

## 🚧 Disclaimer: Work in Progress 🚧

This project is currently in its early stages of development and is not fully functional yet. It serves as a learning and experimentation ground, and as such, it may contain incomplete features, bugs, and non-operational components.

## Technologies
- Python: Used for scripting and coordinating the different parts of the application.
- Docker: Used to containerize and run the different services.
- ElevenLabs: A service used to generate audio from text.

## Purpose and Example

This project is inspired by the desire to automate the creation of content that resembles the content in the following [example video](https://www.youtube.com/embed/P2kRrulJsPc). The goal is to automate the entire process from generating scripts, creating audio, adding subtitles, and cutting videos into smaller segments. With a future expansion plan, we also plan to add the ability to automatically upload processed videos to YouTube.

### Workflow

1. **Script-generator**: Starts automatically and generates scripts by interacting with ChatGPT.
2. **Elevenlabs-service**: Starts when script-generation is complete and generates audio for the given script.
3. **Auto-subtitle**: Starts when audio generation is complete and adds subtitles to the video.
4. **Downloaded-videos**: Done. Starts manually and takes a link to a video as input. It cuts a longer video into shorter segments. This service can also take a list of videos as input.
5. **Device-cloning**: Done. Starts manually and clones a device.

### Planned Improvements

- Automatic upload of processed videos to YouTube.

## Getting Started

### Requirements
- Docker
- Docker Compose

### Setup
1. Clone this repository to your local machine.
   ```sh
   git clone https://github.com/taxidriver2192/VideoGenerator
   cd videoGenerator
   ```
2. Create a .env file in the root directory of the project and add the ElevenLabs API key:
   ```txt
   ELEVENLABS_API_KEY=your_api_key
   ```
3. Run Docker Compose to build and start the services:
   ```bash
   docker-compose up --build
   ```

4. See the makefile.

## Security
Never share your secret API keys. Always use environment variables or other secure methods to store and handle sensitive information in your project.

## License
This project is MIT licensed.