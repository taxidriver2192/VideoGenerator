<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Download Video</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <ul class="nav nav-tabs" id="myTab" role="tablist">
            <?php
            $video_count = 0;
            $script_count = 0;
            $audio_count = 0;
            $video_sound_count = 0;

            $dir = './files/videos';
            $files = scandir($dir);

            foreach ($files as $file) {
                if (preg_match('/^video_\d+\.mp4$/', $file)) {
                    $video_count++;
                } elseif (preg_match('/^video_\d+_speech\.mp4$/', $file)) {
                    $video_sound_count++;
                }
            }

            $dir = './files/scripts';
            $files = scandir($dir);

            foreach ($files as $file) {
                if (preg_match('/^.*\.txt$/', $file)) {
                    $script_count++;
                }
            }

            $dir = './files/audios';
            $files = scandir($dir);

            foreach ($files as $file) {
                if (preg_match('/^.*\.mp3$/', $file)) {
                    $audio_count++;
                }
            }
            ?>
            <li class="nav-item">
                <a class="nav-link active" id="videos-tab" data-toggle="tab" href="#videos" role="tab" aria-controls="videos" aria-selected="true">
                    <i class="fas fa-circle mr-2"></i>1. Videos from youtube <span class="badge badge-pill badge-secondary"><?php echo $video_count; ?></span>
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link" id="scripts-tab" data-toggle="tab" href="#scripts" role="tab" aria-controls="scripts" aria-selected="false">
                    <i class="fas fa-circle mr-2"></i>2. Scripts <span class="badge badge-pill badge-secondary"><?php echo $script_count; ?></span>
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link" id="audios-tab" data-toggle="tab" href="#audios" role="tab" aria-controls="audios" aria-selected="false">
                    <i class="fas fa-circle mr-2"></i>3. Audios <span class="badge badge-pill badge-secondary"><?php echo $audio_count; ?></span>
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link" id="videos-sound-tab" data-toggle="tab" href="#videos-sound" role="tab" aria-controls="videos-sound" aria-selected="false">
                    <i class="fas fa-circle mr-2"></i>4. Videos and sound <span class="badge badge-pill badge-secondary"><?php echo $video_sound_count; ?></span>
                </a>
            </li>
        </ul>
        <div class="tab-content" id="myTabContent">
            <div class="tab-pane fade show active" id="videos" role="tabpanel" aria-labelledby="videos-tab">
                <div class="row">
                    <?php
                    $dir = './files/videos';
                    $files = scandir($dir);

                    foreach ($files as $file) {
                        if (preg_match('/^video_\d+\.mp4$/', $file)) {
                            $headline = str_replace('.mp4', '', $file);
                            echo '<div class="col-md-4 mb-3">';
                            echo '<h3 class="video-headline">' . $headline . '</h3>';
                            echo '<video width="100%" controls>';
                            echo '<source src="' . $dir . '/' . $file . '" type="video/mp4">';
                            echo '</video>';
                            echo '</div>';
                        }
                    }
                    ?>
                </div>
            </div>
            <div class="tab-pane fade" id="scripts" role="tabpanel" aria-labelledby="scripts-tab">
                <div class="row">
                    <?php
                    $dir = './files/scripts';
                    $files = scandir($dir);

                    foreach ($files as $file) {
                        if (preg_match('/^.*\.txt$/', $file)) {
                            $headline = str_replace('.txt', '', $file);
                            echo '<div class="col-md-4 mb-3">';
                            echo '<h3 class="script-headline">' . $headline . '</h3>';
                            echo '<p>' . file_get_contents($dir . '/' . $file) . '</p>';
                            echo '</div>';
                        }
                    }
                    ?>
                </div>
            </div>
            <div class="tab-pane fade" id="audios" role="tabpanel" aria-labelledby="audios-tab">
                <div class="row">
                    <?php
                    $dir = './files/audios';
                    $files = scandir($dir);

                    foreach ($files as $file) {
                        if (preg_match('/^.*\.mp3$/', $file)) {
                            $headline = str_replace('.mp3', '', $file);
                            echo '<div class="col-md-4 mb-3">';
                            echo '<h3 class="audio-headline">' . $headline . '</h3>';
                            echo '<audio controls>';
                            echo '<source src="' . $dir . '/' . $file . '" type="audio/mpeg">';
                            echo '</audio>';
                            echo '</div>';
                        }
                    }
                    ?>
                </div>
            </div>
            <div class="tab-pane fade" id="videos-sound" role="tabpanel" aria-labelledby="videos-sound-tab">
                <div class="row">
                    <?php
                    $dir = './files/videos';
                    $files = scandir($dir);

                    foreach ($files as $file) {
                        if (preg_match('/^video_\d+_speech\.mp4$/', $file)) {
                            $headline = str_replace('_speech.mp4', '', $file);
                            echo '<div class="col-md-4 mb-3">';
                            echo '<h3 class="video-headline">' . $headline . '</h3>';
                            echo '<video width="100%" controls>';
                            echo '<source src="' . $dir . '/' . $file . '" type="video/mp4">';
                            echo '</video>';
                            echo '</div>';
                        }
                    }
                    ?>
                </div>
            </div>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"
            integrity="sha384-+1z6J2d5Y4ZK4wK5zjQzv5zgXzvJvJ5zgjJ4ZvJ8v6z7zvJzJfLJ5zgJzJ4ZvJ8v"
            crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>