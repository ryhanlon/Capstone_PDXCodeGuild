/**
 * Created by Rebecca Hanlon on 6/30/17.
 */

"use strict";


$(".asset").click(function(event){
    // let asset_id = $(this).attr("data-id");


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