<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Download Video</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h2>Videos from youtube</h2>
        <div class="row">
            <?php
            $dir = './files/videos';
            $files = scandir($dir);

            foreach ($files as $file) {
                if (preg_match('/^video_\d+\.mp4$/', $file)) {
                    $headline = str_replace('.mp4', '', $file);
                    echo '<div class="col-md-4 mb-3">';
                    echo '<h3>' . $headline . '</h3>';
                    echo '<video width="100%" controls>';
                    echo '<source src="' . $dir . '/' . $file . '" type="video/mp4">';
                    echo '</video>';
                    echo '</div>';
                }
            }
            ?>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/3.0.3/socket.io.js"></script>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@glidejs/glide"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>