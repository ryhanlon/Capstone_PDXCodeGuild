/**
 * Created by Rebecca Hanlon on 6/30/17.
 * Note:  Have tried multilple ways to deal with the red.  Still looking to solve this problem.
 */

"use strict";


// icons come on page after the video

// play and pause the video with the play/pause button

const myVideo = $("#myvideo");

$(document).on('ready', function () {

    myVideo.bind('ended', function () {
        $('.icon-group').css('visibility', 'visible');
        $('.icon-group').show();
        console.log('let me see you');
    });

    myVideo.bind('play', function () {
        $('.icon-group').hide();
        console.log('goodbye and thanks for the fish');
    });
});


// play button
$('#video-play').click(function () {
    console.log('it is playing');
    $('#myvideo')[0].play();
});


// pause button
$('#video-pause').click(function () {
    console.log('it is paused');
    $('#myvideo')[0].pause();
});


// play sound on click, for words
$('.play_sound').on('click', function () {
        let sound = $(this).siblings('audio')[0];
        console.log(`playing sound... ${sound}`);
        sound.play();
    }
);


// Modal window

// Get the modal
var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function () {
    modal.style.display = "block";
};

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
};


// After 10 clicks, send to db for star (this mostly likely won't be used, plan to use python in the backend)

$(".asset").click(function (event) {

    // Counter to collect clicks
    let meritCounter = $('#merit-counter');
    let current = Number(meritCounter.val());
    let nextNum = current + 1;
    meritCounter.val(String(nextNum));

    if (nextNum === 10) {
        console.log('ten clicks');
    }

    // AJAX call to collect the clicks on words clicked and send to db, insights.AssetInteracton
    $.ajax({
        url: "/insights/clicks",
        data: {
            'asset_id': '5',
            'asset_type': "ADC"
        },
        method: "POST",
        success: function (response) {
            console.log('Yipee!, The click is clicking!');
            console.log(response.status);
        },
        error: function (error) {
            console.log('Bummer! Click not captured!');

        }
    });
});





