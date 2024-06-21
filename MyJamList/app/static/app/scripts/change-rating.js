$(document).ready(function () {
    $('#updateSongForm').on('submit', function (event) {
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: "{% url 'update_song' %}",
            data: $(this).serialize(),
            success: function (response) {
                $('#formMessage').html('<p>Song updated successfully!</p>');
            },
            error: function (response) {
                $('#formMessage').html('<p>An error occurred. Please try again.</p>');
            }
        });
    });
});