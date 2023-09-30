
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Download Video</title>
</head>
<body>
    <button id="downloadButton">Download Video</button>
    <div id="status-messages"></div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/3.0.3/socket.io.js"></script>
    <script type="text/javascript">
        var socket = io('http://0.0.0.0:5001', { transports: ['websocket'] });

        // Event listeners for socket
        socket.on('status', function (data) {
            console.log(data.msg);
            var p = document.createElement('p');
            p.textContent = data.msg;
            document.getElementById('status-messages').appendChild(p);
        });
        
        socket.on('connect_error', function (error) {
            console.error('Connection Error: ', error);
            var p = document.createElement('p');
            p.textContent = 'Connection Error: ' + error;
            document.getElementById('status-messages').appendChild(p);
        });

        socket.on('connect_timeout', function (timeout) {
            console.error('Connection Timeout: ', timeout);
            var p = document.createElement('p');
            p.textContent = 'Connection Timeout: ' + timeout;
            document.getElementById('status-messages').appendChild(p);
        });

        socket.on('reconnect_attempt', function () {
            console.log('Attempting to reconnect...');
            var p = document.createElement('p');
            p.textContent = 'Attempting to reconnect...';
            document.getElementById('status-messages').appendChild(p);
        });

        socket.on('reconnect_error', function (error) {
            console.error('Reconnection Error: ', error);
            var p = document.createElement('p');
            p.textContent = 'Reconnection Error: ' + error;
            document.getElementById('status-messages').appendChild(p);
        });

        socket.on('reconnect_failed', function () {
            console.error('Reconnection Failed');
            var p = document.createElement('p');
            p.textContent = 'Reconnection Failed';
            document.getElementById('status-messages').appendChild(p);
        });


        // Fetch API to download video
        document.getElementById('downloadButton').addEventListener('click', function() {
            const url = 'http://downloaded-videos:5001/download_video';
            const data = {
                url: 'https://www.youtube.com/watch?v=UuWwIhHY9oE'
            };
            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                const p = document.createElement('p');
                p.textContent = 'Response: ' + JSON.stringify(data);
                document.getElementById('status-messages').appendChild(p);
            })
            .catch((error) => {
                console.error('Error:', error);
                const p = document.createElement('p');
                p.textContent = 'Error: ' + error;
                document.getElementById('status-messages').appendChild(p);
            });
        });
    </script>
</body>
</html>