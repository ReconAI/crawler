// filters
$('.input-group.date').datepicker({
    format: "yyyy-mm-dd",
    clearBtn: true
});

$('.input-group .date').datepicker({
    format: "yyyy-mm-dd",
    clearBtn: true
});

// on search
$('#search-button').click(function () {
    let project_id = dropdown_menu.find("option:selected").val();
    let search_text = $('#search-input').val();
    let yt_filters = {};
    let vimeo_filters = {};

    if ($('#license-checkbox').is(':checked')){
        vimeo_filters['license'] = $('#license-select').find("option:selected").val();
    }

    if ($('#yt-location-checkbox').is(':checked')) {
        yt_filters['latitude'] = $('#yt-latitude').val();
        yt_filters['longitude'] = $('#yt-longitude').val();
        yt_filters['location_radius'] = $('#yt-location-radius').val();
    }
    if ($('#yt-published-before-checkbox').is(':checked')) {
        yt_filters['published_before'] = $('#yt-published-before').val();
    }

    if ($('#yt-published-after-checkbox').is(':checked')) {
        yt_filters['published_after'] = $('#yt-published-after').val();
    }
    if ($('#yt-safe-search-checkbox').is(':checked')) {
        yt_filters['safe_search'] = $('#yt-safe-search-select').val();
    }
    if ($('#yt-video-category-checkbox').is(':checked')) {
        yt_filters['video_category_id'] = $('#yt-video-category-select').find("option:selected").val();
    }
    if ($('#yt-video-definition-checkbox').is(':checked')) {
        yt_filters['video_definition'] = $('#yt-video-definition-select').find("option:selected").val();
    }

    // console.log(yt_filters);
    // console.log(vimeo_filters);
    api_search(project_id, search_text, yt_filters, vimeo_filters);
    alert('Search process is started');
})