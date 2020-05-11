var serverHost = "http://192.168.88.245:8000/";

let dropdown_menu = $('#dropdown-menu-id');

function api_read_projects()
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
    api_read_projects();
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
