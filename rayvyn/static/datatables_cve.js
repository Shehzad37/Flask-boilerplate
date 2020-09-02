
$(document).ready(function(){
// debugger
    let table;
    let index;
    $.get('/getData', function (data) {
        let response = JSON.parse(data);
        table = $("#cve_table").on( 'error.dt', function ( e, settings, techNote, message ) {
            console.log( 'An error has been reported by DataTables: ', message );
        } ).DataTable({
            data: response,
            columnDefs: [ {
                targets: [5],
                render: function ( data, type, row ) {
                    return data.length > 255 ?
                        data.substr( 0, 255 ) +'…' :
                        data;
                }
            } ],
            paging: true,
            searching: true,
            columns: [
                { title: "", render: function(){
                    return '<a href="#" class="my_link" data-val="user1" data-toggle="modal" data-target="#my-modal">[+]</a>'}
                },
                {title: "CVE ID"},
                {title: "Feed"},
                { title: "Date Modified" },
                { title: "Impact" },
                { title: "Description" },
                { title: "Vector" },
                { title: "Severity" },
            ]
        });
        $('#my-modal').on('show.bs.modal', function (event) {
            $(this).find("#cvid").text(response[index][1]);
            $(this).find("#feed").text(response[index][2]);
            $(this).find("#dateM").text(response[index][3]);
            $(this).find("#impact").text(response[index][4]);
            $(this).find("#desc").text(response[index][5]);
            $(this).find("#vector").text(response[index][6]);
            // $(this).find("#sev").text(response[index][7]);
        });
    });
    $('#cve_table tbody').on( 'click', 'tr', function () {
        index = table.row( this ).index();
    } );

})
