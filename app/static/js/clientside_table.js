/*jslint browser: true*/
/*global $*/
var table1
var table2

$(document).ready(function () {
    $.get('/tables/clientside_table', function (data) {
        table1 = $('#FIRST_TABLE').DataTable({
            data: data.data,
            paging: true,
            "paging": false,
            "ordering": false,
            "info": false,
            "searching": false,
            dom: 'frtip',
            columns: data.columns,
            select: {
                style: 'multi+shift',
                items: 'cell',
                selector: 'td:not(:first-child)'
            },
            columnDefs: [
                {
                    targets: -1,
                    className: 'dt-body-center'
                }
            ],

        });
    });


    $.get('/tables/clientside_table', function (data) {
        table2 = $('#SECOND_TABLE').DataTable({
            data: data.data,
            paging: true,
            "paging": false,
            "ordering": false,
            "info": false,
            "searching": false,
            dom: 'frtip',
            columns: data.columns,
            select: {
                style: 'multi+shift',
                items: 'cell',
                selector: 'td:not(:first-child)'
            },

        });
    });

    $('button').click(function () {
        var data1 = table1.cells(['.selected']).toArray();
        var json1 = JSON.stringify(data1);
        var ncells1 = table1.cells(['.selected']).data().toArray().reduce((a, b) => a + b, 0)

        var data2 = table2.cells(['.selected']).toArray();
        var json2 = JSON.stringify(data2);
        var ncells2 = table2.cells(['.selected']).data().toArray().reduce((a, b) => a + b, 0);

        var emailform = $('form').serializeArray()
        var email = emailform[Object.keys(emailform)[0]].value

        console.log(email)


        var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
        var validemail = emailPattern.test(email)

        console.log(validemail)

        if (!validemail) {
            alert('Please enter a valid email address.');
            return false;
        }
        console.log(ncells1)
        console.log(ncells2)


        if (ncells1 == 0) {
            alert(' You did not select any cells for group 1')
        }
        if (ncells2 == 0) {
            alert(' You did not select any cells for group 2')
        }

        if (ncells1 != 0 && ncells2 != 0) {
            alert('Submitting ' + ncells1 + ' cells in group 1 and ' + ncells2 + ' in group 2')

            $.post("/submit", {
                // "contentType": "application/json",
                'data1': json1,
                'data2': json2,
                'email': email
            });



        }
        ;
    });


});

