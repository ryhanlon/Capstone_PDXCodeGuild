// js for story_page.html

$('.play_sound').on('click', function () {
    let sound = $(this).siblings('audio')[0];
    console.log(`playing sound... ${sound}`);
    sound.play();
}
);


