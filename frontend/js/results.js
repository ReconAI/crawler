let dropdown_results_menu = $('#dropdown-menu-results-id')

function api_read_results(project_id) {
    $.ajax({
        method: "GET",
            url: serverHost + "api/video-project/" + project_id + '/search/results/'
        })
            .done(function (data) {
                // $('#container-result').html('');
                ReactDOM.render(
                  <SearchResult data={data}/>,
                   document.getElementById('container-result')
                );
            });
}

dropdown_results_menu.on('show.bs.select', function (e, clickedIndex, isSelected, previousValue) {
    api_read_projects(dropdown_results_menu);
});

dropdown_results_menu.on('changed.bs.select', function (e, clickedIndex, isSelected, previousValue) {
    let project_id = dropdown_results_menu.find("option:selected").val();
    api_read_results(project_id);
});