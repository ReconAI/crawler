var serverHost = 'http://'+location.hostname+':8000/';

let dropdown_menu = $('#dropdown-menu-id');

function api_read_projects(dropdown_menu)
    {
        $.ajax({
        method: "GET",
            url: serverHost + "api/video-project/",
        })
            .done(function (data) {
                dropdown_menu.html('');
                data.forEach(function(item, i, arr) {
                    dropdown_menu.append(`<option value=${item.id}>${item.name}</option>`);
                });
                dropdown_menu.selectpicker('refresh');
            });
    }
function api_delete_project(project_id)
    {
        $.ajax({
            method: "DELETE",
            url: serverHost + "api/video-project/" + project_id,
        })
            .done(function (data) {
            });
    }

function api_search(project_id, search_text, yt_filters, vimeo_filters) {

    let data_in = {
        "search_text": search_text,
        'vimeo_filters': {},
        'yt_filters': {},
    };

    // override here is you need it
    data_in['vimeo_filters'] = vimeo_filters;
    data_in['yt_filters'] = yt_filters;
    console.log(data_in);
    $.ajax({
        method: "POST",
        url: serverHost + "api/video-project/" + project_id + "/search/",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(data_in)
    }).done(function (data) {
        console.log(data);
        alert('Search process is started');
    }).fail(function (jqXHR, exception) {
        alert(exception);
    });
}
// on  add new project
$("#add_new_project").click(function () {
    let project_name = $("#add_new_project_input").val();
    $.ajax({
        method: "POST",
        url: serverHost + "api/video-project/",
        data: {"name": project_name}
    })
        .done(function (data) {
            alert('Project is added');
            $("#add_new_project_input").val('');
        });
});

// on select
dropdown_menu.on('show.bs.select', function (e, clickedIndex, isSelected, previousValue) {
    api_read_projects(dropdown_menu);
});

dropdown_menu.on('changed.bs.select', function (e, clickedIndex, isSelected, previousValue) {
    console.log(dropdown_menu.find("option:selected").val());
});

// on delete button
$('#delete-project').click(function () {
    let project_id = dropdown_menu.find("option:selected").val();
    api_delete_project(project_id);
    api_read_projects();
    alert('Project is deleted')
})




