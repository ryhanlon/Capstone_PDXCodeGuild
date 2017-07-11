/**
 * Created by Rebecca Hanlon on 6/30/17.
 */

"use strict";


// icons come on page after the video

// play and pause the video with the play/pause button
const myVideo = $("#myvideo");

$(document).on('ready', function(){

    myVideo.bind('ended', function() {
        $('.icon-group').css('visibility', 'visible');
       $('.icon-group').show();
       console.log('let me see you');
    });

    myVideo.bind('play', function() {
       $('.icon-group').hide();
       console.log('goodbye and thanks for the fish');
    });


});

$('#video-play').click(function(){
    console.log('it is playing');
    $('#myvideo')[0].play();

});


$('#video-pause').click(function(){
    console.log('it is paused');
    $('#myvideo')[0].pause();

});


// function playPause() {
//     if (myVideo.paused)
//         myVideo.play();
//
//     else
//         myVideo.pause();
// }



// function playVid() {
//     myVideo.play();
// }
//
// function pauseVid() {
//     myVideo.pause();
// }


// play sound on click, for words
$('.play_sound').on('click', function () {
    let sound = $(this).siblings('audio')[0];
    console.log(`playing sound... ${sound}`);
    sound.play();
}
);


// After 10 clicks, send to db for star


$(".asset").click(function(event){

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
        data: {'asset_id': '5',
               'asset_type': "ADC"},
        method: "POST",
        success: function(response){
            console.log('Yipee!, The click is clicking!');
            console.log(response.status);
         },
        error: function(error){
            console.log('Bummer! Click not captured!');

        }
    });
});





