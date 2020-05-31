function api_read_results(project_id, custom_url) {
    let url = serverHost + "api/video-project/" + project_id + '/search/results/';
    if (custom_url) {
        url = custom_url
    }

    $.ajax({
        method: "GET",
        url: url
    })
        .done(function (data) {
            // $('#container-result').html('');
            ReactDOM.render(
                <SearchResult data={data}/>,
                document.getElementById('container-result')
            );
        });
}

let dropdown_results_menu = $('#dropdown-menu-results-id')
dropdown_results_menu.on('show.bs.select', function (e, clickedIndex, isSelected, previousValue) {
    api_read_projects(dropdown_results_menu);
});

dropdown_results_menu.on('changed.bs.select', function (e, clickedIndex, isSelected, previousValue) {
    let project_id = dropdown_results_menu.find("option:selected").val();
    api_read_results(project_id);
});