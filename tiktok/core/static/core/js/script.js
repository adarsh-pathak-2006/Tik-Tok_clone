function likeVideo(videoId) {
    fetch(`/like/${videoId}/`, {
        method: "POST",
        headers: {
            "X-CSRFToken": getCSRFToken()
        }
    })
    .then(response => response.json())
    .then(data => {
        location.reload();
    });
}

function getCSRFToken() {
    let cookie = document.cookie.split('; ').find(row => row.startsWith('csrftoken='));
    return cookie ? cookie.split('=')[1] : '';
}