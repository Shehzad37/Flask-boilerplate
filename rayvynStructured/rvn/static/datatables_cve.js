
$(document).ready(function(){
// debugger
     $.get('/getData', function (data) {
         let response = JSON.parse(data);
         $("#cve_table").on( 'error.dt', function ( e, settings, techNote, message ) {
            alert(message);
    } ).DataTable({
             data: response,
             responsive: true,
             columnDefs: [
						{ targets: [-1, -3], className: 'dt-body-right' }
					],
             paging: true,
             searching: true,
            columns: [
			{ title: "CVE ID" },
            {title: "Feed"},
			{ title: "Date Modified" },
			{ title: "Impact" },
			{ title: "Description" },
			{ title: "Vector" },
		]
        });
         // console.log(data.data)
     });
})